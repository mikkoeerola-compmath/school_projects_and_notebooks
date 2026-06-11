-module(divider_org).
-export([genserver/0, keep_alive/1, on_exit/2]).

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
                keep_alive(fun() -> genserver() end);
            _ -> keep_alive(Fun)
        end
    end).  
 
genserver() ->
    keep_alive(fun() -> register(divider,self()),
    receive
        {Val1, Oper, Val2} ->  io:format("~n~p~n",[func(Oper, Val1, Val2)])
        end
    end).

func(Op, X, Y) ->
    case Op of
        "+" -> X + Y;
        "-" -> X - Y;
        "*" -> X * Y;
        "/" -> X / Y;
        _ -> Op ++ " is not a valid operator"
    end.