% render solutions nicely.
:- use_rendering(chess).

% given two queens, which differ of R rows, and are on column M and N, when do they threaten each other?
% 1) if they are on the same column: M=N
% 2) if they differ of exactly R: abs(M-N) = R

queens(Qs, N):-
    length(Qs, N),
    listnum(N, L), % generate list L of N numbers [N, N-1, ..., 1]
    permutation(L, Qs), % generate permutation Qs of L.
    safe_queens(Qs). % check if Qs is safe.

% listnum(A, B) generates a list B, with numbers from A to 1, in decreasing order.
listnum(1, [1]) :- !.
listnum(N, [N|L]) :- M is N-1, listnum(M, L).

% permutation(A,B) generates a permutation B of the list A.
permutation([], []).
permutation([H|T], PL) :-
    permutation(T, PT), % find all possible permutation of T
	select(H, PL, PT). % The element H is removed from the list PL obtaining the final list PT => put H in PT to obtain PL. 

% check if the solution is safe
safe_queens([]) :- !.
safe_queens([Q|Qs]) :-
	safe_queens(Qs), % the rest of the board is safe
    noattack(Qs,Q, 1). % check that queen Q does not threaten Qs

% check if 
noattack([],_,_) :- !.
noattack([Q|Qs], Q0,D) :-
	Q0-Q=\=D,
	Q-Q0=\=D,
	D1 is D +1,
	noattack(Qs, Q0,D1).



/** <examples>

?- queens(Qs, 8).

*/
