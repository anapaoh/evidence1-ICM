# evidence1-ICM
E1 Implementation of Lexical Analysis (Automaton and Regular Expression)


## Chakobsa language
El idioma chakobsa ( šhə-k'oa-bza) es un lenguaje que usaban los circasianos medievales, se cree que es un lenguaje que surgió después de las primeras Guerras de Asesinos, y en sí, " el idioma chakobsa es un registro que habla de la experiencia y la perspectiva de un pueblo que vive en un planeta desértico, que valora la resiliencia y el coraje mientras espera a un salvador profetizado de otro mundo" (Shachat, 2024). A grande escala es un lenguaje usado en las películad de _**Dune**_, pero analizándolo es mucho más que eso.

Este idioma no fue creado con letras o palabras al azar, todo tiene un motivo y una historia. Los Peterson, que fueron los linguistas de estas películas se encargaron de ello. El lenguaje cuenta con una estructura gramatical compleja y detallada, que se encarga de contar la lucha, resistencia y poder con el que los circasianos han llevado a su pueblo a lo largo de la historia. Lo que pasa es que deja de ser un lenguaje inventado y se vuelve en un estilo de contar las historias de miles de personas que, queriendo o no, tuvieron sus propios idiomas representados en este lenguaje. Siendo que su inspiración fueron idiomas del "mundo real", este se vuelve un lenguaje de todos, el relato de personas a lo largo de nuestra humanidad. Es así como el Chakobsa se vuelve una representación de la historia árabe, francesa, griega, romaní y otras.



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

Due to thiese reasons I used FDA.
