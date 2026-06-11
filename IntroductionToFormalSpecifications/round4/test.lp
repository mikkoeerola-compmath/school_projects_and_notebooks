#const n=50. person(1..n).
voted_yes(X) :- not voted_no(X), person(X).
voted_no(X) :- not voted_yes(X), person(X).