move(q0, q1, 'k').
move(q1, q2, 'h').
move(q1, q5, 'i').
move(q1, q12, 'u').
move(q1, q15, 'v').
move(q2, q3, 'a').
move(q3, q4, 'l').
move(q4, f1, 'a').
move(q5, q6, 'n').
move(q6, q7, 'd').
move(q7, q8, 'j').
move(q8, q9, 'a').
move(q9, f1, 'l').
move(q5, q10, 's').
move(q10, q11, 'w').
move(q11, f1, 'a').
move(q12, q13, 'h').
move(q13, q14, 'a').
move(q14, f1, 'r').
move(q15, q16, 'e').
move(q16, q17, 't').
move(q17, q18, 'c').
move(q18, f1, 'h').

/*Define the accepting state*/
accepting_state(f1).

/* Function to check if a word is recognized by the automaton*/
go_over_automaton(ListToCheck) :-
    automatonCheck(ListToCheck, q0).

automatonCheck([], State) :-
    accepting_state(State).

automatonCheck([Symbol | Rest], State) :-
    move(State, NextState, Symbol),
    automatonCheck(Rest, NextState).

/*Test cases*/
test_kalah:-
    write('Testing "khala", true'), nl,
    go_over_automaton(['k', 'h', 'a', 'l', 'a']).

test_hello:-
    write('hello'), nl,
    write('Testinf "hello", false'), nl,
    go_over_automaton([h, e, l, l, o]).

test_kindjal:-
    write('Testing "kindjal, true"'), nl,
    go_over_automaton(['k', 'i', 'n', 'd', 'j', 'a', 'l']).

test_kindjal2:-
    write('Testing "Kindjal", false'), nl,
    go_over_automaton(['K', 'i', 'n', 'd', 'j', 'a', 'l']).

test_kiswa:-
    write('Testing "kiswa", true'), nl,
    go_over_automaton(['k', 'i', 's', 'w', 'a']).

test_kvilth:-
    write('Testing "kvilth", false'), nl,
    go_over_automaton(['K', 'v', 'i', 'l', 't', 'h']).

test_kuhar:-
    write('Testing "kuhar", true'), nl,
    go_over_automaton(['k', 'u', 'h', 'a', 'r']).

test_kvetch:-
    write('Testing "kvetch"'), nl,
    go_over_automaton(['k', 'v', 'e', 't', 'c', 'h']).

test_kvotch:-
    write('Testing "kvotch", false'), nl,
    go_over_automaton(['K', 'v', 'o', 't', 'c', 'h']).