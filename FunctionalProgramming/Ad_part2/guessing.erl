-module(guessing).

-export([start/4, player/4]).

start(Name1, List1, Name2, List2) -> 
    Pl1_id = spawn(guessing, player, [Name1, undefined, List1, true]),
    Pl2_id = spawn(guessing, player, [Name2, Pl1_id, List2, false]),

    %send other pid to pl1
    Pl1_id ! {opponent, Pl2_id}.

% player(Name, Parent, OpponentPid, RemainingList, IsFirstTurn)

player(Name, Opponent, [], _) ->
    receive
        {you_lose} -> io:format("~s lost~n", [Name]);
        {guess, _} -> io:format("~s won~n", [Name])
    end,
    if
        Opponent =/= undefined -> Opponent ! {you_lose};
        true -> receive
            {opponent, NewOpponent} -> NewOpponent ! {you_lose}
        end
    end;

player(Name, undefined, List, true) ->
    [Guess | Rest] = List,
    io:format("~s guesses ~w~n", [Name, Guess]),
    receive {opponent, NewOpponent} -> 
        NewOpponent ! {guess, Guess},
        player(Name, NewOpponent, Rest, false)
    end;

player(Name, Opponent, List, false) ->
    receive
        {guess, N} ->
            case lists:member(N, List) of
                true ->
                    io:format("~s lost~n", [Name]),
                    Opponent ! {you_win};
                false ->
                    %io:format("~s got ~w~n", [Name, N]),
                    [Guess | Rest] = List,
                    io:format("~s guesses ~w~n", [Name, Guess]),
                    Opponent ! {guess, Guess},
                    player(Name, Opponent, Rest, false)
            end;
        {you_win} ->
            io:format("~s won~n", [Name]);
        {you_lose} ->
            io:format("~s lost~n", [Name])
    end.