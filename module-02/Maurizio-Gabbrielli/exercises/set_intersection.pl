% set_intersection(Set1, Set2, Intersection)

% Base case
set_intersection([], _, []).

% Recursive case: H is in Set2
set_intersection([H|T], Set2, [H|Result]) :-
    member(H, Set2),
    set_intersection(T, Set2, Result).

% Recursive case: H is not in Set2
set_intersection([H|T], Set2, Result) :-
    \+ member(H, Set2),
    set_intersection(T, Set2, Result).
