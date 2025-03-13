# Python 05: Functions, Lists and Tuples.

**Introduction**: This document presents learning steps for Python 05. In Python 05, you will learn how to build a sequence structure using basic data types. Moreover, you will learn more features of functions.

**Note:** Exercises of this learning path can be done using:

1. IDE: Using online resources [Visual Studio Code](https://code.visualstudio.com/docs) can be installed on your local machine.

## Materials:

The activities are designed based on these following references:

- BaseCamp Tutorial - Week 05 [Available here](./bc-w05-python-tutorial.md)
- **BRef-01**: Book, Bill Lubanovic; "Introducing Python: Modern Computing in Simple Packages"; [Available here](https://www.oreilly.com/library/view/introducing-python-2nd/9781492051374/)
- **ORef-01**: Online Tutorial; Charles Severance; "Python for Everybody"; [Available here](https://books.trinket.io/pfe/index.html)

## Path:

### Step-01: Tuples.

#### Goals:

```
After taking this step, you will be able to:
	1. interpret and implement Python programs using tuples: creating, unpacking, modifying, combining two tuples, iterating over a tuple.
```

#### What to Learn?

1. Using BaseCamp Tutorial [Available here](./bc-w05-python-tutorial.md) and **BRef-01: Chapter 07** answer and experiment the following questions:
   1. What is a tuple in Python and how is it defined?
   2. How can one combine and compare two (or more) tuples?
   3. How can one iterate over the elements of a tuple?
   4. How is a tuple modified?

#### Exercises:
1. You can create a tuple with mixed types in it, for example texts and numbers. Can you think of a advantage and a disadvantage of doing this? Implement your example.
2. Create a tuple with three numbers in it. Unpack the tuple into three different variables. Print the last one.
3. Create a tuple with two numbers in it, create a second tuple with two texts in it. Add them together into a new tuple. Print the new tuple.
4. Create a tuple with three numbers in it. Use a for loop to iterate over each value. Multiply each value by 2 and print each result.
5. Create a function that returns a tuple containing three texts. Call the function. Unpack the tuple into variables. Print the variables.
6. Design two exercises of your own. They should improve understanding topics of this step.

<hr>

### Step-02: Lists.

#### Goals:

```
After taking this step, you will be able to:
	1. interpret and implement Python programs using lists: defining, offset, slicing, adding new element, modifying an element.
```

#### What to Learn?


1. Using BaseCamp Tutorial [Available here](./bc-w05-python-tutorial.md) and **BRef-01: Chapter 07** answer and experiment the following questions:
   1. What is a list in Python and how is it defined?
   2. What is the result of *split()* on a string?
   3. There are two ways to get items from a list: offset and slice. What are the pros / cons of each? Experiment with some examples.
   4. How can you add new elements to a list?
   5. How can you modify elements of a list?
   6. How can one iterate over the elements of a list?
   7. *Mutability* is one of the main differences between a tuple and a list. Elaborate this with some example.

#### Exercises:

1. Define a list of integers representing scores of a game. Write a program that prints out maximum and minimum of the ```scores```.
2. Extend your program from the previous exercise such that it prints two largest and two smallest elements of the ```scores```.
3. Write a program that asks the user to enter a list of integers. Do the following:
	- Print the total number of items in the list.
	- Print the last item in the list.
	- Print the list in reverse order.
	- Print Yes if the list contains a 5 and No otherwise.
	- Print the number of fives in the list.
	- Remove the first and last items from the list, sort the remaining items, and print the result.
	- Print how many integers in the list are less than 5.
4. Write a program that generates a list of 20 random numbers between 1 and 100.
 	- Print the list.
	- Print the average of the elements in the list.
	- Print the largest and smallest values in the list.
	- Print the second largest and second smallest entries in the list
	- Print how many even numbers are in the list.
5. Start with the list ```[8,9,10]```. Do the following:
	- Set the second entry (index 1) to 17
	- Add 4,5, and 6 to the end of the list
	- Remove the first entry from the list
	- Sort the list
	- Double the list
	- Insert 25 at index 3
	- The final list should equal ```[4,5,6,25,10,17,4,5,6,10,17]```
6. Create the following lists using a loop.
	- A list consisting of the integers 0 through 49
	- A list containing the squares of the integers 1 through 50.
	- The list ```['a','bb','ccc','dddd', . . . ]``` that ends with 26 copies of the letter z.
7. Write a program that takes any two lists L and M of the same size and adds their elements together to form a new list N whose elements are sums of the corresponding elements in L and M. For instance, if ```L=[3,1,4]``` and ```M=[1,5,9]```, then N should equal ```[4,6,13]```.
8. Design two exercises of your own. They should improve understanding topics of this step.


<hr>

### Step-03: Functions (more).

#### Goals:

```
After taking this step, you will be able to:
	1. interpret and implement Python programs with Python functions: positional arguments, keyword arguments, parameters default values, docstrings.
```

#### What to Learn?

1. Using BaseCamp Tutorial [Available here](./bc-w05-python-tutorial.md) and **BRef-01: Chapter 09** answer and experiment the following questions:
   1. What are the positional arguments in Python? What about keyword arguments?
   2. How can one define default values for function parameters?
   3. What are Docstrings? How can they be helpful?

#### Exercises:

1. Describe in your own words what `*args` and `**kwargs` do.
2. Create a function that takes an `*args` of numbers as argument, which calculates the sum of all numbers and returns the result. Call the function and print the returned value.
3. Complete the given code below.

 ```python
def count_passes(**kwargs):
    count = 0
    #Complete this function to count the number of passes

    return count
#
result = count_passes(math="Fail", science="Fail", history="Pass", english="Pass")
print(result)
```


4. Design two exercises of your own. They should improve understanding topics of this step.

5. **Extra:** Provide your solutions to the exercises of **ORef-01: Functions**


<hr>



## Code Analysis

1. Analyze the given codes below without executing them. What will be the result of the programs?

```python
a_tuple = ('Never', 'gonna', 'give', 'you', 'up')
counter = 0
for x in a_tuple:
    if x[0] ==  'g':
        counter = counter + 1
    else:
        counter = counter + 2
print(counter)
```

```python
def do_something(x):
    rtuple = x,
    for i in range(2,11):
        rtuple = rtuple + ((x*i),)
    return rtuple
print(do_something(6))
```

```python
def do_something(*args, **kwargs):
    for i in args:
        for key, value in kwargs.items():
            if i == key:
                print(value)
#
#
do_something("a", "z", "d", "b", a=1, b=2, c=3, d=4)
```

```python
def process_strings(strings):
    processed_strings = []
    for string in strings:
        processed_string = ""
        for char in reversed(string):
            processed_string += char
        processed_strings.append(processed_string)
    return processed_strings

def main():
    names = ["Alice", "Bob", "Charlie", "Dave"]
    processed_names = process_strings(names)
    for name in processed_names:
        print(name)

main()
```