% Einstein riddle, CLP implementation
% author: Andrea Galssi

:- use_module(library(clpfd)).

% structure: 25 variables, divided in a 5x5 matrix: 5 aspects, 5 options.
% the value of each variable indicates the corresponding house.
houses(VARIABLES) :-
    length(VARIABLES, 5),
    length(NATIONALITY, 5),
    length(PET, 5),
    length(SMOKE, 5),
    length(DRINK, 5),
    length(COLOUR, 5),
    NATIONALITY ins 1..5,
    PET ins 1..5,
    SMOKE ins 1..5,
    DRINK ins 1..5,
    COLOUR ins 1..5,
    VARIABLES = [NATIONALITY, PET, SMOKE, DRINK, COLOUR],
    NATIONALITY = [ ENGLISH, SPANIARD, JAPANESE, ITALIAN, NORWEGIAN],
    PET = [DOG, SNAILS, FOX, HORSE, _],
    SMOKE = [PARLIAMENTS, OLD, KOOLS, LUCKY, CHESTERFIELDS],
    DRINK = [TEA, COFFEE, MILK, JUICE, _],
    COLOUR = [ RED, GREEN, WHITE, YELLOW, BLUE],
	RED #= ENGLISH ,
    DOG #= SPANIARD ,
    GREEN #= COFFEE ,
    ITALIAN #= TEA ,
    KOOLS  #= YELLOW ,
    OLD #= SNAILS ,
    MILK #= 3,
    NORWEGIAN #= 1 ,
    LUCKY #= JUICE ,
    JAPANESE #= PARLIAMENTS ,
    GREEN #= (WHITE + 1),
    abs(FOX - CHESTERFIELDS ) #= 1,
    abs(HORSE - KOOLS) #= 1,
    abs(NORWEGIAN - BLUE) #= 1,
    all_distinct(NATIONALITY),
    all_distinct(PET),
    all_distinct(SMOKE),
    all_distinct(DRINK),
    all_distinct(COLOUR).

% flatten(VARIABLES, V), labeling([],V) is necessary to force the program to assign all the variables, and therefore to propagate all the constraints
% nth1(INDEX, L, EL) returns the element EL in position INDEX in the list L
zebra_owner(X) :-
	houses([NATIONALITY, PET, SMOKE, DRINK, COLOUR]),
    flatten([NATIONALITY, PET, SMOKE, DRINK, COLOUR], V), labeling([],V), 
    PET = [_, _, _, _, ZEBRA],
    ZEBRA = Y, % Y is the number of the house where there is a zebra
    INDEX in 1..5, 
	nth1(INDEX, NATIONALITY, Y), % find the index of the nationality of the person living with a zebra
	nth1(INDEX, ["ENGLISH", "SPANIARD", "JAPANESE", "ITALIAN", "NORWEGIAN"], X). % associate the index to the string
       
water_drinker(X) :-
	houses([NATIONALITY, PET, SMOKE, DRINK, COLOUR]),
    flatten([NATIONALITY, PET, SMOKE, DRINK, COLOUR], V), labeling([],V),
    DRINK = [_, _, _, _, WATER],
    INDEX in 1..5, 
    WATER = Y,
	nth1(INDEX, NATIONALITY, Y),
	nth1(INDEX, ["ENGLISH", "SPANIARD", "JAPANESE", "ITALIAN", "NORWEGIAN"], X).

line_house([H1,H2,H3,H4,H5]) :-
    house(1,H1),
    house(2,H2),
    house(3,H3),
    house(4,H4),
    house(5,H5).

house(N, [E1,E2,E3,E4,E5]) :-
	houses([NATIONALITY, PET, SMOKE, DRINK, COLOUR]),
    flatten([NATIONALITY, PET, SMOKE, DRINK, COLOUR], V), labeling([],V),
    INDEXN in 1..5,
    nth1(INDEXN, NATIONALITY, N),
	nth1(INDEXN, ["ENGLISH", "SPANIARD", "JAPANESE", "ITALIAN", "NORWEGIAN"], E1),
    INDEXP in 1..5,
    nth1(INDEXP, PET, N),
	nth1(INDEXP, ["DOG", "SNAILS", "FOX", "HORSE", "ZEBRA"], E2),
    INDEXS in 1..5,
    nth1(INDEXS, SMOKE, N),
	nth1(INDEXS, ["PARLIAMENTS", "OLD", "KOOLS", "LUCKY", "CHESTERFIELDS"], E3),
    INDEXD in 1..5,
    nth1(INDEXD, DRINK, N),
	nth1(INDEXD, ["TEA", "COFFEE", "MILK", "JUICE", "WATER"], E4),
    INDEXC in 1..5,
    nth1(INDEXC, COLOUR, N),
	nth1(INDEXC, [ "RED", "GREEN", "WHITE", "YELLOW", "BLUE"], E5).
    
/** <examples>

* to debug relationships between variables.
?- houses(VARIABLES), flatten(VARIABLES, V), labeling([],V),
    VARIABLES = [NATIONALITY, PET, SMOKE, DRINK, COLOUR],
    NATIONALITY = [ ENGLISH, SPANIARD, JAPANESE, ITALIAN, NORWEGIAN],
    PET = [DOG, SNAILS, FOX, HORSE, ZEBRA],
    SMOKE = [PARLIAMENTS, OLD, KOOLS, LUCKY, CHESTERFIELDS],
    DRINK = [TEA, COFFEE, MILK, JUICE, WATER],
    COLOUR = [ RED, GREEN, WHITE, YELLOW, BLUE].

* details on a single house
?- house(1, [NATIONALITY, PET, SMOKE, DRINK, COLOUR]).

* details on all the houses
?- line_house([H1,H2,H3,H4,H5]).

* who owns a zebra?
?- zebra_owner(X).

* who drinks water?
?- water_drinker(X).
*/