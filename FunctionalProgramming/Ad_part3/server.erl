% Code owner: Mikko Eerola 151184192, mikko.eerol@tuni.fi

-module(server).
-export([new_server/2]).

% Generic server
%
% State is a tuple: {[{key, value}], [{key, subscriber}], [other_server PID]}
% This contains all the data the server reads and writes
%
% Replies to clients follow the structure from the material: {Ref,Response}

server(Mod,State) ->
    receive
        % switches to fail_loop
        fail ->
            io:format("Received fail command: Server ~p stopping~n", [self()]),
            fail_loop(Mod, State);
        % no_reply protocol for server communication
        {no_reply, Msg} ->
            io:format("Server ~p got no reply request: ~p~n",[self(), Msg]),
            NewState = Mod:handle(Msg, State),
            server(Mod, NewState);
        % normal server behaviour
        {Client,Msg} ->
            io:format("Server ~p Got message: ~p | from Client: ~p~n",[self(),Msg, Client]),
            % Crash the client if there is a handling exception
            case Mod:handle(Msg, State) of
                {'EXIT', Reason} ->
                    reply(Client, {crash,Reason}),
                    server(Mod, State);
                {Reply,NewState} -> 
                    reply(Client,Reply),
                    server(Mod,NewState)
            end
    after
        5000 ->
            io:format("Server ~p timed out waiting for requests.~n", [self()]),
            fail_loop(Mod, State)
    end.

fail_loop(Mod, State) ->
    receive
        % recovers the newest state from other servers and returns to server loop
        recover -> 
            {_Map, _Subs, Servers} = State,
            if 
                Servers == [] -> RecoverServer = [];
                true -> [RecoverServer | _ ] = Servers
            end,
            RecoverServer ! {no_reply,{get_data, {self()}}},
            server(Mod, State);
        % able to show state when timed out if asked in command line
        show_state ->
            io:format("Server ~p has state: ~p~n", [self(), State]),
            fail_loop(Mod, State);
        % otherwise just ignore messages but keep loop alive
        _Any -> 
            fail_loop(Mod, State)
    end.

% Initate a new server with a name and module
new_server(Name,Mod) ->
    keep_alive(fun() -> register(Name,self()),
    server(Mod,Mod:init(Name)) end),
    io:format("Server: ~p running~n",[Name]).

% Simple supervisor
keep_alive(Fun) ->
    Pid = spawn(Fun),
    on_exit(Pid,fun(_) -> keep_alive(Fun) end).

% Catch exists
on_exit(Pid,Fun) ->
    timer:sleep(1000),
    spawn(fun() -> process_flag(trap_exit,true),
                   link(Pid),
                   receive
                       {'EXIT',Pid,Why} -> Fun(Why)
                   end
            end).

% Reply to client
reply({ClientPid,Ref},Response) ->
    ClientPid ! {Ref,Response}.
