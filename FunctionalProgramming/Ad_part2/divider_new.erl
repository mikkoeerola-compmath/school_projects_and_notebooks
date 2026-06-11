-module(divider_new).
-export([new_server/2, server/1, on_exit/2, keep_alive/1]).

on_exit(Pid,Fun) ->
 spawn(fun() -> process_flag(trap_exit,true),
                link(Pid),
                receive
                    {'EXIT',Pid,Why} -> Fun(Why)
                end
        end).

keep_alive(Fun) ->
    Pid = spawn(Fun),
    on_exit(Pid,fun(_) -> keep_alive(Fun) end).

server(Mod) ->
    receive
        {Client, {Val1, Oper, Val2}} ->
            case catch Mod:handle(Oper, Val1, Val2) of
                {Reason} -> 
                    reply(Client,{crash, Reason}),
                    io:format("EXIT: ~s~n", [Reason]),
                    server(Mod);
                N -> 
                    reply(Client,N),
                    server(Mod)
            end;
        {Client, {code_change,NewMod}} ->
            reply(Client,{ok,ok}),
            server(NewMod)
    end.

new_server(Name,Mod) ->
    keep_alive(fun() -> register(Name,self()),
                                server(Mod) end).

reply({ClientPid,Ref},Response) ->
    ClientPid ! {Ref,Response}.
