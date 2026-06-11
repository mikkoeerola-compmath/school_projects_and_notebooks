-module(divider).
-export([genserver/1, keep_alive/1, on_exit/2]).

on_exit(Pid,Fun) ->
 spawn(fun() -> process_flag(trap_exit,true),
                link(Pid),
                receive
                    {'EXIT',Pid,Why} -> Fun(Why)
                end
        end).

keep_alive(Fun) ->
    Pid = spawn(Fun),
    on_exit(Pid,fun(Why) -> 
        case Why of 
            {swap, NewMod} ->
                keep_alive(fun() -> genserver(NewMod)end);
            _ -> keep_alive(Fun)
        end
    end). 
 
genserver(Mod) ->
    keep_alive(fun() -> register(server,self()),
    receive
        {Val1, Op, Val2} ->
            io:format("Received ~p~n", [Op]),
            Result = Mod:calc(Op, Val1, Val2),
            io:format("~n~p~n", [Result]),
            genserver(Mod);
        {code_swap, NewMod} -> 
            io:format("swapping"),
            exit({swap, NewMod})
        end
    end).


