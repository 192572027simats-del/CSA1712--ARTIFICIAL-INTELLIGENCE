bird(sparrow).
bird(parrot).
bird(ostrich).
bird(penguin).

can_fly(sparrow).
can_fly(parrot).

cannot_fly(ostrich).
cannot_fly(penguin).

check(Bird) :-
    can_fly(Bird),
    write(Bird), write(' can fly.').

check(Bird) :-
    cannot_fly(Bird),
    write(Bird), write(' cannot fly.').