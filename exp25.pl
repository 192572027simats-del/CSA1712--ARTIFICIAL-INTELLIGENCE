% Monkey can get banana
move(at_door, middle, on_floor).
move(middle, middle, on_box).
move(middle, middle, has_banana).

% Rules
can_get_banana :-
    move(at_door, middle, on_floor),
    write('Monkey moves to the middle.'), nl,
    write('Monkey pushes the box to the middle.'), nl,
    write('Monkey climbs onto the box.'), nl,
    write('Monkey gets the banana.'), nl.