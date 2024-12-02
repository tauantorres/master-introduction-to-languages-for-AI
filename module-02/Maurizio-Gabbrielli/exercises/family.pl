% family.pl

% Facts
parent(john, mary).
parent(mary, susan).
parent(mary, tom).
parent(tom, alice).
parent(susan, brian).
parent(tom, emily).

% Define a list of family members
family_members([john, mary, susan, tom, alice]).


% Rules
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).

% Define ancestor relationship
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).

% - X is an ancestor of Y if X is a parent of Y.
% - Or, X is an ancestor of Y if X is a parent of Z and Z is an ancestor of Y.

% Define sibling relationship
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.

% - X \= Y ensures that a person is not considered their own sibling.


