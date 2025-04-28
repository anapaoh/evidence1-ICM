### Evidence 2 ICM
# Nahuatl 


Nahuatl is an ancient Mexican language that has been spoken since at least the 7th century A.D., playing a significant role in the cultural and historical development of the region. It was the language of the Aztecs, one of the most influential civilizations in pre-Columbian Mesoamerica.

Despite efforts by Spanish colonizers to eradicate native cultures and languages — often through violence and suppression — Nahuatl and its speakers endured. The survival of the language stands as a powerful testament to the resilience of Indigenous identity.

Today, Nahuatl is spoken by approximately 1.5 million Nahua people, primarily in central Mexico. While its number of speakers has declined, Nahuatl remains a beautiful and vital link to Mexico’s ancestral roots, reminding us of the importance of preserving Indigenous languages and honoring the diversity they represent.

“Varieties of Nahuatl are spoken by an estimated 1.5 million Nahua people, most of whom live in Central Mexico. All Nahuan languages are indigenous to Mesoamerica.”
_— College of Liberal Arts | The University of Texas at Austin_

# Models

## Nahuatl Grammar Specification

## 1. Phonological Rules

### 1.1 Phoneme Inventory
```
Vowels = {a, e, i, o, ā, ē, ī, ō} // Short and long vowels
Consonants = {p, t, k, kw, ʔ, s, ʃ, m, n, l, j, w, ts, tɬ, tʃ}
```

### 1.2 Syllable Structure
```
Syllable → (C)(C)V(C)
```
Where C = consonant, V = vowel

### 1.3 Phonological Rules
- Word-final devoicing: voiced consonants become voiceless at the end of words
- Vowel harmony: certain suffixes change vowel quality based on the root vowel
- Stress placement on penultimate syllable

## 2. Morphological Rules

### 2.1 Noun Structure
```
Noun → [Possessive-Prefix] + Root + [Number-Suffix] + [Absolutive-Suffix]

Possessive-Prefix → no- | mo- | i- | to- | amo- | in-
Number-Suffix → -tin | -meh | -h | -Ø
Absolutive-Suffix → -tl | -tli | -li | -in | -Ø
```
### 2.2 Verb Structure
```
Verb → [Tense-Prefix] + [Subject-Prefix] + [Object-Prefix] + Root + [Directional-Suffix] + [Tense-Suffix]

Tense-Prefix → o- | Ø-
Subject-Prefix → ni- | ti- | Ø- | an- 
Object-Prefix → nech- | mitz- | k(i)- | tech- | amech- | kin-
Directional-Suffix → -ki | -ka | -kui | -temo | -kiza | -kalaki
Tense-Suffix → -a | -ya | -ki | -z | -zki
```

### 2.3 Adjective Structure
```
Adjective → Root + [Intensifier-Suffix]

Intensifier-Suffix → -tzin | -tontli | -pol
```
## 3. Syntactic Rules

### 3.1 Basic Sentence Structure
```
S → VP [NP] [NP] [PP]    // VSO basic order

// Noun Phrase
NP → [Det] [Adj]* N [PP] [RC]
Det → in | ce | inon
PP → P NP
P → ipan | ika | itech | itlan | ixpan

// Verb Phrase
VP → V [Adv]
Adv → niman | zan | ok | kualli | mach

// Relative Clause
RC → in V [NP] [NP] [PP]
```

### 3.2 Question Formation
```
Question → kuen S | tleika S | kanin S | akiea S | keski S | kenamih S
```

### 3.3 Complex Sentences
```
ComplexS → S Conj S
Conj → ihuan | auh | intla | ipampa | moneki
```
## 4. Lexical Categories
### 4.1 Noun Subcategories
```
N → N_animate | N_inanimate | N_natural | N_abstract

N_animate → tlacatl | cihuatl | coyotl | mazatl | ...
N_inanimate → tetl | cuauhitl | calli | ...
N_natural → atl | tepetl | citlalli | tonatiuh | ...
N_abstract → tlazohtlaliztli | nemilyotl | ...
```

### 4.2 Verb Subcategories
```
V → V_transitive | V_intransitive | V_stative

V_transitive → nemi | cochi | choca | ...
V_intransitive → mictia | tlazotla | chihua | ...
V_stative → ca | neci | ...
```
## 5. Sample Derivations
### 5.1 Simple Sentence
```
"Nitemachtia" (I teach)
ni- + temachtia
[Subject-Prefix:1SG] + [V_root:teach]
```

### 5.2 Complex Sentence
```
"Nitlakwa ihuan nitlai" (I eat and I drink)
ni- + tlakwa + ihuan + ni- + tlai
[Subject-Prefix:1SG] + [V_root:eat] + [Conj:and] + [Subject-Prefix:1SG] + [V_root:drink]
```

### 5.3 Noun Possession
```
"Nocal" (my house)
no- + cal + -li
[Possessive-Prefix:1SG] + [N_root:house] + [Absolutive-Suffix]
```

#### Now that we understand the rules for the Na'vi grammar we need to create a tree rule for it, the word we are going to use for the grammar are:
### Verbs:
* nemi - to live, to walk
* tlacua - to eat
* cochi - to sleep
* tequiti - to work
* chihua - to make, to do
* temachtia - to teach

### Nouns :
* tlacatl - person, man
* cihuatl - woman
* piltzintli - child
* calli - house
* atl - water
* tetl - stone
* cuahuitl - tree, wood
* tlaxcalli - tortilla, bread
* xochitl - flower
* tepetl - mountain
* tlamachtilli - student
* teotl - god, deity
* tonatiuh - sun
* metztli - moon
* cuicatl - song

### Conjunctions:
* ihuan - and
* auh - but, and
* intla - if

# Unambiguous Nahuatl Grammar

## 1. Terminal Symbols

### 1.1 Verbs
```
V_ROOT → nemi | tlacua | cochi | tequiti | chihua | temachtia
```

### 1.2 Nouns
```
N_ROOT → tlaca | cihua | piltzin | cal | a | te | cuahui | tlaxcal | xochi | tepe | tlamachtil | teo | tonatiu | metz | cuica
```

### 1.3 Affixes
```
POSS_PREFIX → no | mo | i | to | amo | in
SUBJ_PREFIX → ni | ti | Ø | an
OBJ_PREFIX → nech | mitz | k | ki | tech | amech | kin
TENSE_PREFIX → o | Ø
ABS_SUFFIX → tl | tli | li | in
PLUR_SUFFIX → tin | meh | h
VERB_SUFFIX → a | ya | z | que
```

### 1.4 Function Words
```
DET → in | ce
CONJ → ihuan | auh | intla
NEG → amo
```

## 2. Non-Terminal Symbols and Production Rules

### 2.1 Sentence Structure (Eliminating Ambiguity)
```
S → VP NP_OPT NP_OPT PP_OPT             # Base sentence structure
S → NEG VP NP_OPT NP_OPT PP_OPT         # Negated sentence
S → S CONJ S                            # Compound sentence
```

### 2.2 Noun Phrases (Avoiding Left Recursion)
```
NP → DET N_FORM                         # Determinative noun phrase
NP → N_FORM                             # Simple noun phrase
NP_OPT → NP | ε                         # Optional noun phrase

N_FORM → POSS_PREFIX N_STEM             # Possessed noun
N_FORM → N_STEM                         # Unpossessed noun
N_STEM → N_ROOT ABS_SUFFIX              # Singular noun
N_STEM → N_ROOT PLUR_SUFFIX ABS_SUFFIX  # Plural noun
```

### 2.3 Verb Phrases (Eliminating Ambiguity)
```
VP → V_SIMPLE                           # Simple verb
VP → V_TRANSITIVE                       # Transitive verb with object prefix
VP → V_INCORP                           # Verb with incorporated noun

V_SIMPLE → TENSE_PREFIX SUBJ_PREFIX V_ROOT VERB_SUFFIX
V_TRANSITIVE → TENSE_PREFIX SUBJ_PREFIX OBJ_PREFIX V_ROOT VERB_SUFFIX
V_INCORP → TENSE_PREFIX SUBJ_PREFIX N_ROOT V_ROOT VERB_SUFFIX
```

### 2.4 Prepositional Phrases
```
PP → P NP                               # Prepositional phrase
PP_OPT → PP | ε                         # Optional prepositional phrase
P → ipan | ica | itech                  # Prepositions
```

### 2.5 Question Formation (Non-Ambiguous)
```
Q → Q_MARKER S                          # Question with marker
Q_MARKER → cuix | tlen | aquin | canin  # Question markers
```

## 3. Example Sentences with Syntactic Trees

### Sentence 1: "Nicochi." (I sleep.)
```
          S
          |
          VP
          |
      V_SIMPLE
      ---------
     |     |     |
TENSE_PREFIX SUBJ_PREFIX V_ROOT VERB_SUFFIX
    |         |       |       |
    Ø         ni     coch     i
```

Derivation:
- S → VP NP_OPT NP_OPT PP_OPT
- S → VP ε ε ε
- S → V_SIMPLE
- S → TENSE_PREFIX SUBJ_PREFIX V_ROOT VERB_SUFFIX
- S → Ø ni coch i

### Sentence 2: "In tlacatl cochi." (The man sleeps.)
```
            S
       /         \
      VP          NP_OPT
      |           |
  V_SIMPLE        NP
 /    |    \     /  \
Ø     Ø    cochi DET N_FORM
                 |     |
                 in  N_STEM
                    /     \
                N_ROOT  ABS_SUFFIX
                  |        |
                tlaca      tl
```

Derivation:
- S → VP NP_OPT NP_OPT PP_OPT
- S → VP NP ε ε
- S → V_SIMPLE NP
- S → Ø Ø cochi DET N_FORM
- S → Ø Ø cochi in N_STEM
- S → Ø Ø cochi in N_ROOT ABS_SUFFIX
- S → Ø Ø cochi in tlaca tl

### Sentence 3: "Nictlaxcalchihua." (I make tortillas./I tortilla-make.)
```
          S
          |
          VP
          |
      V_INCORP
    /     |      \
TENSE_PREFIX SUBJ_PREFIX N_ROOT V_ROOT VERB_SUFFIX
    |         |       |      |       |
    Ø         ni    tlaxcal chihua    a
```

Derivation:
- S → VP NP_OPT NP_OPT PP_OPT
- S → VP ε ε ε
- S → V_INCORP
- S → TENSE_PREFIX SUBJ_PREFIX N_ROOT V_ROOT VERB_SUFFIX
- S → Ø ni tlaxcal chihua a

### Sentence 4: "In cihuatl quicua in tlaxcalli." (The woman eats the tortilla.)
```
                   S
        /          |          \
       VP          NP_OPT      NP_OPT
       |           |            |
  V_TRANSITIVE     NP           NP
 /    |     \     /  \         /  \
Ø     Ø    qui  DET N_FORM    DET N_FORM
      |     |    |    |        |    |
      Ø    cua  in  N_STEM    in  N_STEM
                   /    \        /    \
                N_ROOT ABS_SUFFIX N_ROOT ABS_SUFFIX
                  |       |        |       |
                cihua     tl     tlaxcal   li
```

Derivation:
- S → VP NP_OPT NP_OPT PP_OPT
- S → VP NP NP ε
- S → V_TRANSITIVE NP NP
- S → TENSE_PREFIX SUBJ_PREFIX OBJ_PREFIX V_ROOT VERB_SUFFIX NP NP
- S → Ø Ø qui cua Ø DET N_FORM DET N_FORM
- S → Ø Ø qui cua Ø in N_STEM in N_STEM
- S → Ø Ø qui cua Ø in N_ROOT ABS_SUFFIX in N_ROOT ABS_SUFFIX
- S → Ø Ø qui cua Ø in cihua tl in tlaxcal li

### Sentence 5: "Nitequiti ipan calli." (I work in the house.)
```
                S
        /       |       \
       VP     NP_OPT    PP_OPT
       |        |         |
   V_SIMPLE     ε         PP
  /   |    \             /  \
 Ø    ni tequiti        P    NP
                        |     |
                      ipan  N_FORM
                             |
                           N_STEM
                           /    \
                       N_ROOT ABS_SUFFIX
                         |       |
                        cal      li
```

Derivation:
- S → VP NP_OPT NP_OPT PP_OPT
- S → VP ε ε PP
- S → V_SIMPLE ε ε PP
- S → TENSE_PREFIX SUBJ_PREFIX V_ROOT VERB_SUFFIX ε ε P NP
- S → Ø ni tequiti ti ε ε ipan N_FORM
- S → Ø ni tequiti ti ε ε ipan N_STEM
- S → Ø ni tequiti ti ε ε ipan N_ROOT ABS_SUFFIX
- S → Ø ni tequiti ti ε ε ipan cal li

### Sentence 6: "Cuix ticochi?" (Do you sleep?)
```
       Q
     /   \
Q_MARKER   S
   |       |
 cuix      VP
           |
       V_SIMPLE
      /   |    \
TENSE_PREFIX SUBJ_PREFIX V_ROOT VERB_SUFFIX
     |        |       |      |
     Ø        ti     coch    i
```

Derivation:
- Q → Q_MARKER S
- Q → cuix VP NP_OPT NP_OPT PP_OPT
- Q → cuix VP ε ε ε
- Q → cuix V_SIMPLE
- Q → cuix TENSE_PREFIX SUBJ_PREFIX V_ROOT VERB_SUFFIX
- Q → cuix Ø ti coch i

### Sentence 7: "Nicochi ihuan nitequiti." (I sleep and I work.)
```
            S
        /   |   \
       S   CONJ   S
       |    |     |
      VP   ihuan  VP
       |          |
   V_SIMPLE    V_SIMPLE
  /   |    \   /   |    \
 Ø   ni  cochi Ø   ni  tequiti
```

Derivation:
- S → S CONJ S
- S → VP NP_OPT NP_OPT PP_OPT CONJ VP NP_OPT NP_OPT PP_OPT
- S → VP ε ε ε CONJ VP ε ε ε
- S → V_SIMPLE ihuan V_SIMPLE
- S → TENSE_PREFIX SUBJ_PREFIX V_ROOT VERB_SUFFIX ihuan TENSE_PREFIX SUBJ_PREFIX V_ROOT VERB_SUFFIX
- S → Ø ni coch i ihuan Ø ni tequit i


  ## Analysis of Nahuatl Grammar in Chomsky's Hierarchy

## Original Grammar Level in Chomsky's Hierarchy

The Nahuatl grammar as implemented in the code is a **Context-Free Grammar (CFG)** - Level 2 in Chomsky's hierarchy. This is evidenced by:

1. The grammar is defined using NLTK's CFG class
2. Productions have a single non-terminal on the left-hand side followed by any combination of terminals and non-terminals
3. Rules like `S -> VP NP_OPT NP_OPT PP_OPT` are typical CFG productions

Key characteristics in the original grammar that make it a CFG:
- The presence of recursive rules (like compound sentences)
- The use of epsilon productions (empty/optional elements)
- Productions dependent solely on the non-terminal being expanded, not the surrounding context

The grammar contains several sources of ambiguity and left recursion:
- Optional elements (NP_OPT, PP_OPT) create multiple valid derivations
- Rules like `BASE_S -> VP NP_OPT NP_OPT PP_OPT` could lead to ambiguous parses
- Potential left recursion in complex noun phrase formations

## Grammar After Eliminating Ambiguity and Left Recursion

After eliminating ambiguity and left recursion, the grammar would still be a **Context-Free Grammar**, but it would now be in a restricted form suitable for **LL(1) parsing** - still Level 2 in Chomsky's hierarchy, but a more efficient subclass.

The transformed grammar would have:
- No left recursion (all recursion converted to right recursion)
- No ambiguity (each input has exactly one valid derivation)
- No common prefixes in production alternatives
- No epsilon productions combined with recursion

This form is a proper subset of CFGs that can be parsed deterministically in linear time.

## Time Complexity Implications

| Grammar Level | Name | Time Complexity | Parser Type |
|---------------|------|-----------------|------------|
| Type 0 | Unrestricted | Undecidable | Turing Machine |
| Type 1 | Context-Sensitive | Exponential O(2^n) | Linear Bounded Automaton |
| Type 2 (original) | Context-Free | Cubic O(n³) | Non-deterministic PDA |
| Type 2 (transformed) | LL(1) Context-Free | Linear O(n) | Deterministic PDA |
| Type 3 | Regular | Linear O(n) | Finite State Automaton |

## String Examples for Each Level

1. **Type 0 (Unrestricted):**
   - Example: Natural language with complex semantics and context
   - String: "The man who I think saw her believes she likes him"
   - Features: Cross-serial dependencies, semantic constraints

2. **Type 1 (Context-Sensitive):**
   - Example: a^n b^n c^n (equal number of a's, b's, and c's)
   - String: "aaabbbccc"
   - Features: Requires counting three different elements

3. **Type 2 (Context-Free):**
   - Example: a^n b^n (equal number of a's and b's)
   - String: "aaabbb"
   - Features: Nested structures, matching pairs
   - Nahuatl example: "in cihuatl quicua in tlaxcalli" (The woman eats the tortilla)

4. **Type 2 - LL(1) (Deterministic Context-Free):**
   - Same language capacity as CFG but with deterministic parsing
   - String: Same as Type 2, but with unambiguous parsing
   - Nahuatl example (after transformation): "in cihuatl quicua in tlaxcalli"

5. **Type 3 (Regular):**
   - Example: (ab)* (any number of "ab" repetitions)
   - String: "ababab"
   - Features: Cannot handle nested structures
   - Limited Nahuatl example: "nicochi" (just a verb with prefixes)

The transformation from a general CFG to an LL(1) grammar doesn't change the theoretical power (both Type 2), but dramatically improves parsing efficiency from O(n³) to O(n), enabling practical implementations for natural language processing applications.

# References
College of Liberal Arts | The University of Texas at Austin. (s. f.). https://liberalarts.utexas.edu/languages/nahuatl.html#:~:text=Nahuatl%2C%20known%20informally%20as%20Aztec,languages%20are%20indigenous%20to%20Mesoamerica. 

Hopcroft, J. E., Motwani, R., & Ullman, J. D. (2006). Introduction to Automata Theory, Languages, and Computation (3rd ed.). Pearson.

GeeksforGeeks. (2023). Construction of LL(1) Parsing Table. https://www.geeksforgeeks.org/construction-of-ll1-parsing-table/
