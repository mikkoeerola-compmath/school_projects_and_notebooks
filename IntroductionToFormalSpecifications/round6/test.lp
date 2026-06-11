a :- not b, not c.
b :- not a, not c.
c :- not a, not c.

d :- a', not a.	d :- a, not a'.
d :- b', not b.	d :- b, not b'.
d :- c', not c.	d :- c, not c'.

:- not d.

h' :- not b, not c.
1 <= #count{b';c'} <= 1 :- not a.