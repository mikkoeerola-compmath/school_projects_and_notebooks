% Database
arc(a,c).  arc(b,a).  arc(c,b).  arc(d,c).

% Definition of path/2
path(X,Y) :- arc(X,Y).
path(X,Y) :- path(X,Z), arc(Z,Y).