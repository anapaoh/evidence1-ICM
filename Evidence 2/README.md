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
## 5. Incorporation Rules
### 5.1 Noun Incorporation
```
V_incorporated → [Subject-Prefix] + N_root + V_root + [Tense-Suffix]
```

### 5.2 Applicative Form
```
V_applicative → V_root + -lia | -ia | -huia
```

### 5.3 Causative Form
```
V_causative → V_root + -ltia | -tia
```
## 6. Semantic Features
### 6.1 Difrasismo (Paired Metaphorical Expressions)
```
Difrasismo → NP Conj NP
```
Examples: in xochitl in cuicatl (flower and song = poetry)

### 6.2 Reverential and Diminutive Forms
```
N_reverential → N_root + -tzin | -tzintli
N_diminutive → N_root + -tontli | -ton
N_augmentative → N_root + -pol
```
## 7. Sample Derivations
### 7.1 Simple Sentence
```
"Nitemachtia" (I teach)
ni- + temachtia
[Subject-Prefix:1SG] + [V_root:teach]
```

### 7.2 Complex Sentence
```
"Nitlakwa ihuan nitlai" (I eat and I drink)
ni- + tlakwa + ihuan + ni- + tlai
[Subject-Prefix:1SG] + [V_root:eat] + [Conj:and] + [Subject-Prefix:1SG] + [V_root:drink]
```

### 7.3 Noun Possession
```
"Nocal" (my house)
no- + cal + -li
[Possessive-Prefix:1SG] + [N_root:house] + [Absolutive-Suffix]
```

## Now that we understand the rules for the Na'vi grammar we need to create a tree rule for it, the word we are going to use for the grammar are:
Verbs:
* nemi - to live, to walk
* tlacua - to eat
* cochi - to sleep
* tequiti - to work
* chihua - to make, to do
* temachtia - to teach

Nouns :
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

Conjunctions:
* ihuan - and
* auh - but, and
* intla - if

# References
College of Liberal Arts | The University of Texas at Austin. (s. f.). https://liberalarts.utexas.edu/languages/nahuatl.html#:~:text=Nahuatl%2C%20known%20informally%20as%20Aztec,languages%20are%20indigenous%20to%20Mesoamerica. 
