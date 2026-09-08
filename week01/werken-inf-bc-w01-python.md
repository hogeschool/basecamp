# Python 01: Linear Programs — werkblad

> Vragen uit [inf-bc-w01-python.md](./inf-bc-w01-python.md). Vul je antwoord onder elke vraag in.

---

## Step-01: What is a Program?

### What to Learn

*Use **BRef-01: Chapter 01** and **BRef-02: Chapter 02** as a reference and discuss the following questions*

#### 1. What is a general definition of a program? Provide some (non-computer) examples.

Iets met een input en output, volgens bepaalde regels. Het voert een actie uit. Of een volgorde; bijvoorbeeld een boekrecept.


#### 2. What are the main elements of a (Python) program?

1. **Waarden / objecten** — `42`, `3.14`, `"hallo"`, `True`. Alle data in Python is een object.
2. **Variabelen (namen)** — labels die naar een object verwijzen: `leeftijd = 21`.
3. **Expressies** — stukjes code die een waarde opleveren: `2 + 3 * 4`, `input("naam: ")`.
4. **Statements** — opdrachten die iets _doen_: toekenning (`x = 5`), `print(...)`, `if`, `while`, `import`.
5. **Functies** — herbruikbare blokken code, ingebouwd (`print`, `input`, `int`, `len`) of zelfgeschreven.
6. **Modules / packages** — bestanden met code die je met `import` binnenhaalt (`import random`).
7. **Programma** — één of meer modules die samen worden uitgevoerd.


#### 3. How Python runs programs?

Broncode > compile > btecode > antwoorden via Python Virtual Machine


#### 4. **First Taste of Python**: Read section *Little Programs* and analyze the provided examples.

Als ik er naar kijk zie ik dat het werkt met data, en vervolgens aan de hand van die data iets uitprit


#### 5. Consider the following Python programs and guess what each program does. Analyze and discuss inputs, behaviour and expected outputs.

Takeaway: offset, begint bij tellen met 0, wij bij 1

- *Note*: Certainly there are lines that you won't understand. The goal is to evaluate your first taste of Python programs and check how intuitive they are. You will be learning all details in later stages.

```python
#Code 01:
words = []
num_str = input("How many words would you like to enter?")
num = int(num_str)
for _ in range(0, num):
	word = input("Next word: ")
  	words.append(word)
print("This is your list of words:", words)
```


### Exercises

#### Oefening 1. Make a small research to understand the meaning of *syntax in programming*. Give three examples of the programs you have read in **BRef-01: Chapter 01**.

Meaning of syntax according to the book: Rules about what can be said, and where—syntax

1. Wanneer je bijvoorbeeld een komma gebruikt en waar.
2. for, in print, de woorden die je gebruikt
3. Het gebruiken van bijvoorbeeld haakjes []


#### Oefening 2. Take each of the given following Python programs and carry out these steps

- Write down syntactical elements that are understandable for you.
  - Specify statements that you know (or you can guess) the results of the their execution.
  - Share your lists within your learning group.
  - Discuss what will be the result / output of the program (without execution).

*Note*: It is not expected that students understand all the elements of these programs. The main goal is to get a taste of Python programs and discuss about them. *Trust your intuition*.

```python
#Code 02f
a = 16
b = 12
b = a
a = 22
print(a)
print(b)
# what will be printed here?
```

```python
#Code 03
num = int(input("Enter a number: "))
if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   while num > 0:
       sum += num
       num -= 1
   print("Result is", sum)
```

```python
#Code 04
import random
print(random.randint(0, 9))
```

```python
#Code 05
my_str = input("Enter a string: ")
words = [word.lower() for word in my_str.split()]
words.sort()
print("The sorted words are:")
for word in words:
	print(word)
```

##### Code 02F

Variabelen zijn a en b, statement; print.

##### Code 03

num = word tot een functie gemaakt.


#### Oefening 3. Using **OPyEditor** try to execute the given programs. Does the output of the programs match your expectations?


---

## Step-02: Everything starts with Data

### What to Learn

*Using **BRef-01: Chapter 02** and **BRef-02: Chapter 04, Chapter 05** explore the answers for the following questions*

#### 1. What is a value? What is a variable?


#### 2. What is a *type*? Provide five examples.


#### 3. How can you define a variable in Python?


#### 4. Define some variables in Python that are not permitted in Python. Experiment with breaking various rules in defining variables. Analyse the error message.


#### 5. How can you assign a value to a variable? How can we express that two items are equal?


#### 6. How can you identify the type of a value / variable?


*Using **BRef-01: Chapter 05** and **BRef-02: Chapter 07** discuss and experiment the following questions*

#### 7. What are the character and text string types in Python? Make examples.


#### 8. How can you combine several strings? Implement an example.


#### 9. Can you multiply a number with a string? What is the result? Implement an example.


#### 10. How can you get the 5th character of a given string? How can you get the first character?


#### 11. How can you get a substring from a given string? For example, the zipcodes (postcodes) in The Netherlands consist of 4 digits followed by 2 letters. How can you extract the letters from a given zipcode?


#### 12. You have learned how to print something as an output of your program. How can you read something as input? What is the *function*? What is the type?


### Exercises

#### Oefening 1. Check the following program and write down what will be the result of the prints

```python
x = 12
y = 15
z = 1
y = z
z = 12
y = 13
x = y
y = x
z = 7
print(x)
print(y)
print(z)
```


#### Oefening 2. A phone number is a number. Yet we would want to save it as a text. Can you think of a reason why?


#### Oefening 3. The number in the address of your house, for example Kerkweg **8**, is a number. Yet we would want to save it as a text. Can you think of a reason why?


#### Oefening 4. What is an example from a number we use in the real world that we want to save as a number in Python, not as a text.


#### Oefening 5. User input in Python is always considered a text, even if we just enter numbers, why would it act like this?


#### Oefening 6. Define a variable called zipcode (postcode) and give it the value of your own zipcode. Print it using print().


#### Oefening 7. Define a variable called favorite_food, give it the value "Pizza". Print it. Change the value to "Roti". Print it.


#### Oefening 8. Define a variable that stores your school email address. Extract your student number from this email address.


#### Oefening 9. Write down the complete alphabet in a variable. Split it halfway over two different variables. Join them back together in the wrong order and print it.


#### Oefening 10. Explain in your own words with an `f` string is?


#### Oefening 11. Finish all the exercises listed in **BRef-01-Chapter 02: Things to Do** and Practice the exercises listed in **BRef-01-Chapter 05: Things to Do**.


---

## Step-03: How to Calculate?

### What to Learn

*Using **BRef-01: Chapter 03** and **BRef-02: Chapter 05**answer the following questions*

#### 1. Name basic built-in data types in Python. Use examples.


#### 2. What are the basic arithmetic operations? Make a list with the meaning (semantics) of each operation.


#### 3. Why is *precedence* an important concept? Make examples.


#### 4. How can you convert one data type to another? Name basic built-in functions.


### Exercises

#### Oefening 1. Create two variables with a number in it, you can decide which numbers, add them together and print the result.


#### Oefening 2. Do the same for subtraction, division and multiplication.


#### Oefening 3. Get input from the user. Save it as a number. Print it.


#### Oefening 4. Try to divide something by zero. Describe the error you get.


#### Oefening 5. Create two variables with text in them. Print them togeter at once, using only 1 print statement.


#### Oefening 6. Python uses PEMDAS. What is that and is it different from the way you learned it?


#### Oefening 7. Create one calculation using at least four parentheses, three multiplications and four subtractions. Print the result.


#### Oefening 8. Finish all the exercises listed in **BRef-01-Chapter 03: Things to Do**.



