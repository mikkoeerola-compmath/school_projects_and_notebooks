% Code owner: Mikko Eerola 151184192, mikko.eerol@tuni.fi
%
% Test client process (test fail and recover). new_client initiates a client, other functions perform actions
% towards servers. 
%
% Requests to Servers follow the structure from material: {{ClientPid,Ref},Request}

-module(client3).
-export([new_client/1, client2_test/0, subscribe/2, write/3, read/2]).

% Init client with name
new_client(Name) ->
    PID = spawn(?MODULE, client2_test, []),
    register(Name, PID),
    io:format("Starting client: ~p on ~p~n", [Name, PID]).

% Client sends test data
client2_test() ->
    Server3 = whereis(server3),
    read(Server3, key2),
    timer:sleep(1000),
    read(Server3, key3),

    rpc_loop().

% Client waits for responses and prints them
rpc_loop() ->
    receive
        {_Ref,{crash,Reason}} ->
            exit(Reason);
        {Ref, Response} ->
            io:format("Client ~p (ref: ~p) received:~n~p~n", [self(),Ref,Response]),
            rpc_loop()
    after
        2000 ->
            io:format("Client ~p timed out waiting for messages.~n", [self()]),
            exit(timeout)
    end.

subscribe(Server, Key) ->
    Ref = make_ref(),
    Server ! {{self(), Ref}, {sub,{Key, self()}}}.

write(Server, Key, Value) ->
    Ref = make_ref(),
    Server ! {{self(), Ref}, {write,{Key,Value}}}.

read(Server, Key) ->
    Ref = make_ref(),
    Server ! {{self(), Ref}, {read,{Key}}}.