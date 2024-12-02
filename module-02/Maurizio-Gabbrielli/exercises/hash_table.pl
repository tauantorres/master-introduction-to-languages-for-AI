% hash_lookup(Key, Table, Value)
% Succeeds if Value is associated with Key in Table.
% Fails if Key is not found.

% Clause 1: Key matches the head of the list.
hash_lookup(Key, [key(Key, Value)|_], Value).

% Clause 2: Key does not match; recurse on the tail.
hash_lookup(Key, [_|Tail], Value) :-
    hash_lookup(Key, Tail, Value).
