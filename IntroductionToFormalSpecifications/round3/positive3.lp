% Testing database
% arc(a,b).  arc(b,c).  arc(c,d).  arc(d,a). arc(c,a).

% Project nodes from arcs
node(X) :- arc(X,Y).
node(Y) :- arc(X,Y).

connected(X,Y) :- arc(X,Y).
connected(X,Y) :- arc(Y,X).
path(X,Y) :- arc(X,Y)
path(X,Y) :- arc(X,Z), path(Z,Y).
inloop(X) :- arc(X,X).
inloop(X) :- arc(X,Y), path(Y,X).