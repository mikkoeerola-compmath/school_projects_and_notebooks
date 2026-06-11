-module(divider2).
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
        timer:sleep(1000),
        case Why of 
            {swap, NewMod} ->
                keep_alive(fun() -> genserver(NewMod) end);
            _ -> keep_alive(Fun)
        end
    end).  

genserver(Mod) ->
    keep_alive(fun() -> 
        case whereis(divider) of
            undefined -> register(divider, self());
            _ -> 
                unregister(divider),
                register(divider, self())
        end,
    receive
        {Val1, Oper, Val2} ->  io:format("~n~p~n",[Mod:calc(Oper, Val1, Val2)]);
        {swap, NewMod} -> exit({swap, NewMod})
        end
    end).