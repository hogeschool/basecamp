# Basecamp INFBSC02 — 2026-2027

> **Wegwijzer.** Onder deze kop staat de originele Engelstalige introductie van de
> opleiding op het Python-leerpad. Wat je in de praktijk het vaakst nodig hebt:

| Wat zoek je? | Waar |
|---|---|
| Rooster, alle deadlines, opdrachtenlijst | [`programma.md`](./programma.md) |
| Leeruitkomsten, beoordeling, aanwezigheidsplicht | [`cursushandleiding.md`](./cursushandleiding.md) |
| Doelen en programma van een week, dag voor dag | `weekNN/lesweek-NN.md` |
| Het leerpad van die week | `weekNN/week N voorbereiding.md` |
| Jouw antwoorden op de weekvragen | `weekNN/week N werkblad.md` |
| Een opdracht om aan te werken | `weekNN/<CODE>-<naam>/` |
| De originele docx, pptx en pdf van HR | `lesmateriaal/weekNN/` — of klik ze aan in het weekoverzicht |
| Extra oefenmateriaal | [`extra-opdrachten/`](./extra-opdrachten) |
| Invulformats (dossier, PvA, evaluaties, challenge) | [`formats/`](./formats) |

### Hoe een weekmap eruitziet

```
week06/
  lesweek-06.md                  doelen, deadlines, dag voor dag, links naar het materiaal
  week 6 voorbereiding.md        het leerpad van de opleiding
  week 6 werkblad.md             jouw antwoorden op de weekvragen
  A2W6A1-social-network/         werkmap per opdracht
    README.md                    de opdracht + jouw aanpak
    A2W6A1.py                    hier schrijf je je code
  A2W6P1-unique-characters/
  ...

lesmateriaal/week06/             de originele docx en pptx van HR  (buiten git)
  INDEX.md                       wat erin zit, met de slidetitels per deck
```

De weekmap bevat alleen tekst en je eigen werk. De docx en pptx staan gebundeld in
`lesmateriaal/`; klik ze aan vanuit `lesweek-NN.md` en ze openen in Word of PowerPoint.

### De weken

| Arch | Weken |
|---|---|
| Arch 0 — introductie | [00](./week00/lesweek-00.md) |
| Arch 1 — programmeerbasis | [01](./week01/lesweek-01.md) · [02](./week02/lesweek-02.md) · [03](./week03/lesweek-03.md) · [04](./week04/lesweek-04.md) *(challenge)* |
| Arch 2 — collecties, testen | [05](./week05/lesweek-05.md) · [06](./week06/lesweek-06.md) · [07](./week07/lesweek-07.md) · [08](./week08/lesweek-08.md) *(challenge + mid-term)* |
| Arch 3 — objecten, bestanden | [09](./week09/lesweek-09.md) · [10](./week10/lesweek-10.md) · [11](./week11/lesweek-11.md) · [12](./week12/lesweek-12.md) *(challenge)* |
| Arch 4 — databases, afronding | [13](./week13/lesweek-13.md) · [14](./week14/lesweek-14.md) · [15](./week15/lesweek-15.md) · [16](./week16/lesweek-16.md) *(meesterproef)* · [17](./week17/lesweek-17.md) · [18](./week18/lesweek-18.md) *(assessments)* · [19](./week19/lesweek-19.md) *(afsluiting)* |

Week 4, 8 en 12 zijn challengeweken zonder gewoon programmeerritme; daar staat geen
`week N voorbereiding.md`. Hetzelfde geldt voor week 0 en 17 t/m 19.

`lesmateriaal/` staat buiten git — 715 MB, en het materiaal is van de opleiding terwijl
deze repo publiek is. De inhoud is wel omgezet: de lesplannen naar `lesweek-NN.md`, de
formats naar `formats/`, de handleiding naar `cursushandleiding.md`, en elke
`lesmateriaal/weekNN/INDEX.md` somt per PowerPoint de slidetitels op zodat je erop kunt
zoeken zonder de binary te openen.

---

# Introduction

This collection covers a learning path for Basics of Programming. It covers acitivities around topics that are essential to learn basics of programming in Python.

**Note**: The content is designed based on Facilitated Learning method. Facilitated learning is an educational method where the students are encouraged to take more control of their learning process. The role of the coach (teacher) is more a learning facilitator, i.e. organising and providing resources to learners.

## Arch One:
**Programming Elements**: In **Arch One** the following programming elements are covered:

	- primitive data types: character, string, integer, float and boolean.
	- basic numerical operations: + , - , * , / , %
	- simple user inputs and print formats.
	- boolean expressions and conditional statements: if-else statements
	- loops: while and for.
	- string processing: length, split, join, replace, join.
	- basic of functions: defining and calling functions, return of a function, functions with arguments.

As a result of participating in **BaseCamp:Arch One**, students will be able to:

1. Read, Understand and Analyze the behaviour of a Python program implementing the programming elements covered in Arch One.
2. Implement their solutions for a given problem statement using the programming elements covered in Arch One.
3. Implementing their Python programs in Python Shell and an IDE.
4. Execute Python programs using a terminal and an IDE.

This Arch is constructed in the following weeks:

- [**Week01: Linear Programs**](./week01/week%201%20voorbereiding.md) 
- [**Week02: Branching Programs, Functions**](./week02/week%202%20voorbereiding.md) 
- [**Week03: Iterative Programs**](./week03/week%203%20voorbereiding.md) 
- **Week04: Review and Challenge**


<br><br>

## Arch Two:

**Programming Elements**: In **Arch Two** the following programming elements are covered:

	- functions (more): positional arguments, keyword arguments, parameters default values, docstrings, anonymous functions.
	- collective structures: lists with basic operations (defining, offset, slicing, adding new element, modifying an element, list comprehension), tuples with basic operations (creating, unpacking, modifying, combining two tuples, iterating over a tuple), dictionaries with basic operations (creating, adding and modifying items,  extracting value(s), extracting key(s), deleting, pop and clear, iteration over dictionaries), sets with basic operations (creating sets, adding and removing elelemnts, membership operator, iteration over a set, basic operations between sets, i.e. intersection, union, difference and subset),  copy(), deepcopy(), nested structures.

As a result of participating in **BaseCamp: Arch Two**, students will be able to:

1. Read, Understand and Analyze the behaviour of a Python program implementing the programming elements covered in Arch Two.
2. Implement their solutions for a given problem statement using functions, list, tuple, set, and ditionaries.
3. Debug and apply basics of testing (input / output and acceptance testing) on a given Python program.


This Arch is constructed in the following weeks:

- [**Week05: Functions, Lists and Tuples**](./week05/week%205%20voorbereiding.md) 
- [**Week06: Functions, Dictionaries and Sets**](./week06/week%206%20voorbereiding.md) 
- [**Week07: Functions and Nested Structures**](./week07/week%207%20voorbereiding.md) 
- **Week08: Review and Challenge**

<br><br>

## Arch Three:

**Programming Elements**: In **Arch Three** the following programming elements are covered:

	- objects and classes: defining a class, instantiating an object, attributes and methods, initializing an object.
	- plain data files: encoding / decoding, ascii and utf-8 encodings, binary vs text files, reading / modifying / wrting binary / text data files, searching content.
	- structured data files: reading / writing content from / to CSV / JSON files, processing / modifying content of CSV / JSON files.

As a result of participating in **BaseCamp: Arch Three**, students will be able to:

1. Read, Understand and Analyze the behaviour of a Python program implementing the programming elements covered in Arch Three.
2. Implement their solutions for a given problem statement employing Python class.
3. Implement Python solutions to process and manipulate data provided as files (plain text, JSON and csv). 
4. Apply basics of unit testing on a given Python program.


This Arch is constructed in the following weeks:

- [**Week09: Everything is an Object**](./week09/week%209%20voorbereiding.md) 
- [**Week10: (Plain) Data Files**](./week10/week%2010%20voorbereiding.md) 
- [**Week11: Structured Data Files**](./week11/week%2011%20voorbereiding.md) 
- **Week12: Review and Challenge**

<br><br>

## Arch Four:

**Programming Elements**: In **Arch Four** the following programming elements are covered:

	- (basics of) databases using SQLite and simple queries: CREATE, INSERT, DELETE, UPDATE, SELECT x,y,z FROM t WHERE c.
	- functions as parameters, generators and decorators.
	- recursive functions.

As a result of participating in **BaseCamp: Arch Four**, students will be able to:

1. Read, Understand and Analyze the behaviour of a Python program implementing the programming elements covered in Arch Four.
2. Implement Python solutions to process and manipulate data provided in a simple database (SQLite). 

This Arch is constructed in the following weeks:

- [**Week13: Database - basics**](./week13/week%2013%20voorbereiding.md) 
- [**Week14: Database - extended**](./week14/week%2014%20voorbereiding.md) 
- [**Week15: Functions: Higher Order & Recursion**](./week15/week%2015%20voorbereiding.md) 
- **Week16: Review and Challenge**

<br><br>


## References:
### Programming:
1. Bill Lubanovic; **"Introducing Python: Modern Computing in Simple Packages"**; [Check here](https://www.oreilly.com/library/view/introducing-python-2nd/9781492051374/) 
2. Mark Lutz; **"Learning Python: Powerful Object-Oriented Programming"**; [Check here](https://www.oreilly.com/library/view/learning-python-6th/9781098171292/) 
3. Brian Heinold; **"A Practical Introduction to Python Programming"** [Available Online, Check here](https://www.brianheinold.net/python/python_book.html).
	- Solutions to the exercises are [available here](https://github.com/henrytirla/Practical-Introduction-to-python).
4. Ben Stephenson; **"The Python Workbook: A Brief Introduction with Exercises and Solutions"**; [Check here](https://link.springer.com/book/10.1007/978-3-319-14240-1)
5. Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers; **"How to Think Like a Computer Scientist"**;[Check here](https://openbookproject.net/thinkcs/python/english3e/)
6. **"CS Principles: Big Ideas in Programming"**; [Check here](https://www.openbookproject.net/books/StudentCSP/)


### Skills:

1. Fernando Doglio; **"Skills of a Successful Software Engineer"** [Check here](https://www.manning.com/books/skills-of-a-successful-software-engineer?query=skills%20software%20engineers)

### Teaching:
1. Felienne Hermans; **"The Programmer's Brain: What Every Programmer Needs to Know about Cognition"** [Check here](https://www.amazon.com/Programmers-Brain-every-programmer-cognition/dp/1617298670)
2. David Allen, Tina Blythe; **"Facilitating for Learning: Tools for Teacher Groups of All Kinds"**. [Check here](https://www.amazon.com/Facilitating-Learning-Tools-Teacher-Groups/dp/0807757381)
3. Margaret Crockett, Janet Foster; **"Training the Trainer Resource Pack"** [Check here](http://www.ica-sae.org/trainer/english/index.htmArch)

