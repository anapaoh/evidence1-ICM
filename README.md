# evidence1-ICM
E1 Implementation of Lexical Analysis (Automaton and Regular Expression)


## Chakobsa language
The Chakobsa language ( šhə-k'oa-bza) is a language used by the medieval Circassians, believed to be a language that emerged after the first Assassin Wars, and in itself, “the Chakobsa language is a record that speaks of the experience and perspective of a people living on a desert planet, who value resilience and courage while awaiting a prophesied savior from another world” (Shachat, 2024). On a large scale it is a language used in the Dune movies, but upon analysis it is much more than that.

This language was not created with random letters or words, everything has a reason and a history. The Petersons, who were the linguists of these films, took care of that. The language has a complex and detailed grammatical structure, which is responsible for telling the struggle, resistance and power with which the Circassians have led their people throughout history. What happens is that it ceases to be an invented language and becomes a style of telling the stories of thousands of people who, willingly or not, had their own languages represented in this language. Being that its inspiration were languages of the “real world”, it becomes a language of all, the story of people throughout our humanity. This is how Chakobsa becomes a representation of Arabic, French, Greek, Romani and other histories.

Translated with DeepL.com (free version)


Shachat, S. (2024, 1 marzo). IndieWire. IndieWire. https://www.indiewire.com/features/craft/dune-fremen-langauge-how-to-speak-1234958145/ 


Key differences between DFA and NFA:

DFA (Deterministic Finite Automaton):

Only one possible state transition for each input
Easier to implement
Requires less memory
Always has a unique path for recognition


NFA (Nondeterministic Finite Automaton):

Multiple possible state transitions for the same input
Can have epsilon transitions (transitions without consuming input)
More flexible in pattern matching
Can explore multiple paths simultaneously
Typically requires more complex implementation

Due to thEese reasons I used FDA.


MODEL:

![q0](https://github.com/user-attachments/assets/bac08fe0-3ba8-4b0f-94b7-9f9a560b46bc)

this is equivalent to the following regular expression: k(hala|indjal|iswa|uhar|vetch)

## Implementation
Where: 

-khala → Valid
-kindjal → Valid
-kiswa → Valid
-kuhar → Valid
-kvetch → Valid
-Anything else → Rejected

This automaton starts at state q0. It moves through different states based on the input characters.
The state transitiones in prolog are the ones using the word "move"; ''' accepting_state(f1). '''

