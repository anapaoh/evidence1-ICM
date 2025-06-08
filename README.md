# evidence1-ICM
E1 Implementation of Lexical Analysis (Automaton and Regular Expression)


## Chakobsa language
The Chakobsa language ( šhə-k'oa-bza) is a language used by the medieval Circassians, believed to be a language that emerged after the first Assassin Wars, and in itself, “the Chakobsa language is a record that speaks of the experience and perspective of a people living on a desert planet, who value resilience and courage while awaiting a prophesied savior from another world” (Shachat, 2024). On a large scale it is a language used in the Dune movies, but upon analysis it is much more than that.

This language was not created with random letters or words, everything has a reason and a history. The Petersons, who were the linguists of these films, took care of that. The language has a complex and detailed grammatical structure, which is responsible for telling the struggle, resistance and power with which the Circassians have led their people throughout history. What happens is that it ceases to be an invented language and becomes a style of telling the stories of thousands of people who, willingly or not, had their own languages represented in this language. Being that its inspiration were languages of the “real world”, it becomes a language of all, the story of people throughout our humanity. This is how Chakobsa becomes a representation of Arabic, French, Greek, Romani and other histories.

Shachat, S. (2024, 1 marzo). IndieWire. IndieWire. https://www.indiewire.com/features/craft/dune-fremen-langauge-how-to-speak-1234958145/ 


## Key differences between DFA and NFA:

#### DFA (Deterministic Finite Automaton):

+ Only one possible state transition for each input
+ Easier to implement
+ Requires less memory
+ Always has a unique path for recognition


#### NFA (Nondeterministic Finite Automaton):


+ Multiple possible state transitions for the same input
+ Can have epsilon transitions (transitions without consuming input)
+ More flexible in pattern matching
+ Can explore multiple paths simultaneously
+ Typically requires more complex implementation

Due to theese reasons I used DFA.


MODEL:

![q0](https://github.com/user-attachments/assets/bac08fe0-3ba8-4b0f-94b7-9f9a560b46bc)

This is equivalent to the following regular expression:  _k(hala|indjal|iswa|uhar|vetch)_

## Implementation
Where: 

-khala → Valid

-kindjal → Valid

-kiswa → Valid

-kuhar → Valid

-kvetch → Valid

-Anything else → Rejected

This automaton starts at state q0. It moves through different states based on the input characters.
The state transitiones in prolog are the ones using the word "move"; ```accepting_state(f1). ```
identifies that the finishing state is "f1" and 
```
go_over_automaton(ListToCheck) :-
    automatonCheck(ListToCheck, q0).

automatonCheck([], State) :-
    accepting_state(State).

automatonCheck([Symbol | Rest], State) :-
    move(State, NextState, Symbol),
    automatonCheck(Rest, NextState).
```
is the Automaton Function for Word Recognition. 

What ocurrs here is the following:

-The function go_over_automaton/1 starts at state q0.

-It processes the input one character at a time using move/3.

-If the automaton reaches an accepting state (f1), the word is recognized.


## Test

The following tests were made in order to confirm the veracity of this work, the resuts were as it follows:

```
?- test_kalah.
Testing "khala", true
true.
```

```
?- test_hello.
hello
Testinf "hello", false
false.
```

```
?- test_kindjal.
Testing "kindjal, true
true.
```

```
?- test_kindjal2.
Testing "Kindjal", false
false.
```

```
?- test_kvilth.
Testing "kvilth", false
false.
```

## Time Complexity Analysis

The provided code uses a Deterministic Finite Automaton (DFA) to determine whether a word is valid. Below is an analysis of the primary function, go_over_automaton/1, and its computational complexity.


### Functionality of go_over_automaton/1

This function takes a list of symbols (characters of a word) and checks whether the automaton accepts or rejects the input. It relies on the recursive function automatonCheck/2, which processes each symbol in the input list sequentially.


The automatonCheck/2 function transitions between states using the move/3 predicate, which evaluates the state transitions based on the current input symbol.


### Time Complexity
Each symbol in the input list is processed exactly once. Consequently, the time complexity of this function is _O(n)_, where n represents the length of the input word.

## Comparison
When I did this evidence I decided to go with the automaton because it was easier for me to understand; however this could also be implemented with regex.

