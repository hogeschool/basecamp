# Python 06: Functions, Dictionaries and Sets.

**Introduction**: This document presents learning steps for Python 06. In Python 06, you will learn dictionaries to collect keys and coresponding values. Moreover, you will learn how anonymous functions can be helpful. 


**Note:** Exercises of this learning path should be done using:

1. IDE: Using online resources [Visual Studio Code](https://code.visualstudio.com/docs) can be installed on your local machine.


## Materials:

The activities are designed based on these following references:

- **BRef-01**: Book, Bill Lubanovic; "Introducing Python: Modern Computing in Simple Packages"; [Available here](https://www.oreilly.com/library/view/introducing-python-2nd/9781492051374/)
- **ORef-01**: Online Tutorial; Charles Severance; "Python for Everybody"; [Available here](https://books.trinket.io/pfe/index.html)
- **ORef-02**: Book, Brian Heinold; "A Practical Introduction to Python Programming" [Available Online, Check here](https://www.brianheinold.net/python/python_book.html)


## Path:

### Step-01: Dictionaries.

#### Goals:

```
After taking this step, you will be able to interpret and implement Python programs with Python Dictionaries: creating, adding and modifying items,  extracting value(s), extracting key(s), deleting, pop and clear, iteration over dictionaries.
```

#### What to Learn?

1. Using **BRef-01: Chapter 08** answer and experiment the following questions:
   1. What is a dictionary in Python and how can you create a dictionary?
   2. How can items be added/changed to/in a dictionary?
   3. How can you get the value of a given key?
   4. What are the behaviour of these functions: *keys()*, *values()*, *items()*?
   5. When can we use *del*, *pop()* and *clear()*? Experiment with some examples.
   6. How can one iterate over a dictionary?

#### Exercises:

1. Describe in your own words the difference between a `dictionary` and a `tuple`.
2. Create a new dictionary containing a key named `FirstName` with the value `Larry`, a key named `LastName` with the value `Page`. Print the last value from the dictionary.
3. Create a dictionary with the following pairs `"brand": "Ford", "model": "Mustang", "year": 1964`.
	- Print all the values from the dictionary.
	- Print all the keys from the dictionary.
	- Print the length of the dictionary.
	- Add `"color": "Red"` and remove the pair with key = `"year"`. Print keys and values separately.

4. Modify the code from the previous exercise so each value becomes a `tuple` containing two random numbers.

5. Design two exercises of your own. They should improve understanding topics of this step.

6. If you don't have VSCode yet, install *VSCode* on your working machine. Implement and run a simple Python program of your choice.
	- It is important to learn how to create a new Python program, how to configure interpreter and how to run the program. Where do you see the results?

7. **Extra:** Provide your solutions to the exercises of **ORef-01: Dictionaries**


<hr>


### Step-02: Sets.

#### Goals:

```
After taking this step, you will be able to interpret and implement Python programs with Python Sets: creating sets, difference between sets and lists and tuples, adding and removing elelemnts, membership operator, iteration over a set, basic operations between sets: intersection, union, difference and subset.
```

#### What to Learn?

1. Using **BRef-01: Chapter 08** answer and experiment the following questions:
   1. What is a set in Python and how is it defined?
   2. How can one add/remove elements to/from a set?
   3. How can one iterate over a set?
   4. Assume two sets S1 and S2. How can one specify the following operations on S1 and S2 in Python:
	   - Intersection of S1 and S2.
	   - Union of S1 and S2.
	   - Difference S1 and S2.
	   - Is S1 a subset of S2 (or vice-versa)?

#### Exercises:

1. Describe in your own words the difference between a `set` and a `tuple`.
2. Describe in your own words the difference between a `set` and a `list`.
3. Create a set with and fill it with some values you can think of yourself. Print the length and the last value from the set.
3. Create a function which takes a `dictionary` as argument and returns a `set` created from the values of the given `dictionary`. Call the function and print all values from the returned set.
4. Create a `set` containing 5 letters `x,y,q,z,u`. Ask the user the input a letter. Check with `if` statement if the given letter is inside the `set`, print `yes` or `no`.

5. Design two exercises of your own. They should improve understanding topics of this step.


### Step-03: Functions (more).

#### Goals:

```
After taking this step, you will be able to interpret and implement Python programs with anonymous functions.
```

#### What to Learn?

1. Using **BRef-01: Chapter 09** answer and experiment the following questions:
   1. "Functions are first-class citizens": What does this sentence mean?
   2. What is an anonymous function and how can you define it in Python? Experiment with some examples.

#### Exercises:


1. Complete the given code by creating a lambda that checks if a given number is even.

```python
even = #your lambda here
print(even(4))
print(even(13))
```

2. Create a code snippet that splits up a list into two new lists. Depending on if the number in the list is even or odd. Accomplish this with using a lambda and knowledge from the earlier weeks. 
- For example: Original list of integers:
`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`.
New list with only the even numbers:
`[2, 4, 6, 8, 10]`.
New list with the odd numbers:
`[1, 3, 5, 7, 9]`

3. Complete the function that checks if a given list is sorted or not, use at least one lambda within the function.

```python
def am_i_sorted(numberlist):
    #write the code
result = am_i_sorted([1,2,5,6,8,17])
print(result) #True
result = am_i_sorted([1,2,99,6,8,17])
print(result) #False
```

4. Create a lambda that takes two arguments and returns a Tuple containing those two values. 


5. Design two exercises of your own. They should improve understanding topics of this step.


<hr>


## Code Analysis
1. Analyze the given code below without executing it. What will be the result of the program?

 ```python
sfind = set('orihme')
schar = set('ichgo')
print("Step 1:")
for i in sfind:
    if i in schar:
        print(i)
#
print("Step 2:")
schar.update(sfind)
for i in schar:
    print(i)
```

2. Given the following code below. Explain in your own words what happens in this code. What are the keys in the dictionary?

 ```python
import random
rdic = {}
for i in range(0,10):
	rdic[i] = random.randint(0,100)
for item in rdic.values():
	print(item)
```

3. Analyse the given code below without executing it. What will be the result of the program?

```python
r = lambda a : a + 15
print(r(10))
r = lambda x, y : x * y
print(r(12, 4))
```
