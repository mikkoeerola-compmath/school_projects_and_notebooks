% Code owner: Mikko Eerola 151184192, mikko.eerol@tuni.fi
%
% Controlling process to test out servers and clients. After tests time out (>10s) 
% you can ask the state of the server by server# ! show_state. This will show
% said servers state.

-module(control_test).
-export([main/0]).

main() ->
    % Single server and client tests
    server:new_server(server1,statemanager),
    timer:sleep(100),
    client1:new_client(client1),
    timer:sleep(100),

    % Multiple servers and clients tests
    server:new_server(server2, statemanager),
    timer:sleep(100),
    client2:new_client(client2),
    timer:sleep(100),

    % Server fail and recovering tests
    server:new_server(server3,statemanager),
    timer:sleep(100),
    whereis(server3) ! fail,
    client3:new_client(client3),
    timer:sleep(500),
    whereis(server3) ! recover,

    % wait for processes to finish and then timeout
    io:format("Control waiting for processes~n"),
    timer:sleep(10000).
