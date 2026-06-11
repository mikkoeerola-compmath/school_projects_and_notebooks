-module(divtest).
-export([start/0]).

%Diveder testing

start() ->
    Pid = spawn(devider)