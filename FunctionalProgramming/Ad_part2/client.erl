-module(client).
-export([rpc/2]).

rpc(ServerName,RequestList) ->
    lists:foreach(fun(Request) ->
        Ref = make_ref(),
        ServerName ! {{self(),Ref},Request},
        receive
            {Ref,{crash, Reason}} -> 
                io:format("~n~p: ~s~n", [Ref, Reason]);
            {Ref,Response} ->
                io:format("~n~p: ~p~n", [Ref, Response])
        after
            100 -> 
                io:format("~nTimed out: ~p~n", [Request])
        end
    end, RequestList).

