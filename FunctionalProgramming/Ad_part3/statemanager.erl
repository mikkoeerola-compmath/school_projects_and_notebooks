% Code owner: Mikko Eerola 151184192, mikko.eerol@tuni.fi

-module(statemanager).
-export([init/1, handle/2]).

% State is a tuple: {[{key, value}], [{key, subscriber}], [other_server PID]}
% This contains all the data the server reads and writes

% init server with exsiting servers and notify them about the new server with no_reply
init(Name) -> 
    Processes = registered(),
    % Filter for server processes
    Filter = fun(A) ->
                    Str = atom_to_list(A),
                    StrName = atom_to_list(Name),
                    (lists:prefix("server", Str)) and (Str /= StrName) end,
    Servers = lists:filter(Filter, Processes),
    % tell other servers about a new server
    lists:foreach(fun(Server) -> Server ! {no_reply,{add_server, {Name}}} end, Servers),
    % init server key value data from existing servers if there are any
    if 
        Servers /= [] ->
            [InitServer | _ ] = Servers,
            InitServer ! {no_reply, {get_data, {self()}}},
            {[],[],Servers};
        true -> {[],[],Servers}
    end.


handle(Msg, State) ->
    {Operation, Rest} = Msg,
    case Operation of
        write -> 
            {Key, Value} = Rest,
            write(State, Key, Value);
        write_copy ->
            {Key, Value} = Rest,
            write_copy(State, Key, Value);
        sub ->
            {Key, PID} = Rest,
            sub(State, Key, PID);
        read ->
            {Key} = Rest,
            read(State, Key);
        get_data -> 
            {PID} = Rest,
            get_data(State, PID);
        recover_data ->
            {Map} = Rest,
            % recover_data(State, Map);
            recover(State, Map);
        add_server ->
            {Name} = Rest,
            add_server(State, Name)
    end.

% Store the subscribe informaiton into a list.
% This means that a client PID wants to get all the updates for that key from that server
sub(State, Key, PID) ->
    {Map,Subs,Servers} = State,
    {subscription_done, {Map, [{Key, PID} | Subs], Servers}}.

% Store the new value for key.  Also send a {write_copy , key, value}  to all other servers,
% and send the new value to all client processes who have subscribed to that
% key from that server.
write(State, Key, Value) -> 
    {Map, Subs, Servers} = State,
    % notify subs
    lists:foreach(fun({SubsKey, PID}) -> if SubsKey == Key -> 
                                            PID ! {no_ref,{subs_value_change, {Key, Value}}}
                                        end
                                    end, Subs),
    % send change to other servers using write_copy with no_rpely
    lists:foreach(fun(PID) -> PID ! {no_reply,{write_copy, {Key, Value}}} end, Servers),
    % store new value
    {{wrote_key_value_pair, {Key, Value}},{lists:keystore(Key, 1, Map, {Key, Value}), Subs, Servers}}.

% Only store a new value to the State
write_copy(State, Key, Value) ->
    {Map, Subs, Servers} = State,
    {lists:keystore(Key, 1, Map, {Key, Value}), Subs, Servers}.

% send the value associated to key to client process PID
read(State, Key) ->
    {Map, _Subs, _Servers} = State,
    Tuple = lists:keyfind(Key, 1, Map),
    if not Tuple ->
        {{key_did_not_match, {}}, State};
    true ->
        {{answer, Tuple}, State}
    end.

% returns all the key-value pairs the State has with no_reply
get_data(State, PID) ->
    {Map, _Subs, _Servers} = State,
    PID ! {no_reply, {recover_data, {Map}}},
    State.

% Recovers data.
%recover_data(State, Map) ->
%    {_OldMap, Subs, Servers} = State,
%    {Map, Subs, Servers}.

% add a new server name to server's state's server list
add_server(State, ServerName) ->
    {Map,Subs,Servers} = State,
    {Map, Subs, [ServerName | Servers]}.

% Returns the recovered key value list with old state (subs and server info)
% notifys subs
recover(State, Map) ->
    {_OldMap,Subs,Servers} = State,
    lists:foreach(
        fun({SubsKey, PID}) -> 
            Tuple = lists:keyfind(SubsKey,1,Map),
            if 
                not Tuple -> ok;
                true -> PID ! {no_ref,{subs_value_change, {element(2, Tuple)}}}
            end
        end, Subs),
    {Map,Subs,Servers}.