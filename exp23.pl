% Facts
male(ram).
male(raj).
male(kumar).

female(sita).
female(gita).

parent(ram, raj).
parent(sita, raj).
parent(raj, kumar).
parent(gita, kumar).

% Rules
father(X, Y) :-
    male(X),
    parent(X, Y).

mother(X, Y) :-
    female(X),
    parent(X, Y).

sibling(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    X \= Y.