# Python 05: Functions, Lists and Tuples.

**Introduction**: This document presents learning steps for Python 05. In Python 05, you will learn basics of functions to organise your large programs. A function is a fragment of code with a name to be reused in different places of the program. Moreover, in this week you will learn how to build a sequence structure using basic data types.

**Note:** Exercises of this learning path can be done using:

1. IDE: Using **BRef-01: Chapter 19, Section: Integrated Development Environment** PyCharm can be installed in your local machine.

## Materials:

The activities are designed based on these following references:

- **BRef-01**: Book, Bill Lubanovic; "Introducing Python: Modern Computing in Simple Packages"; [Available here](https://www.oreilly.com/library/view/introducing-python-2nd/9781492051374/) 
- **ORef-01**: Online Tutorial; Charles Severance; "Python for Everybody"; [Available here](https://books.trinket.io/pfe/index.html)

## Path:

### Step-01: What is a function?

#### Goals:

```
After taking this step, you will be able to:
	1. interpret and implement Python programs with Python functions: function definition, calling functions, return of a function, functions with arguments.
```

#### What to Learn?

1. Using **BRef-01: Chapter 09** answer and experiment the following questions:
   1. What is a function in Python?
   2. What are the main elements of a Python function? Define a simple function that does nothing.
   3. How can a function be used (called)? 
   4. How can one return the result of a function?
   5. What are the arguments and/or parameters?

#### Exercises:

*Note*: In the following exercises you can decide yourself what should be the name of function in your solution. Check [PEP8 Function and Variable Names](https://peps.python.org/pep-0008/#function-and-variable-names).

1. Explain in your own words the difference between `arguments` and `parameters`.
2. Create a function that just prints the word `hello`. Call the function and run your program. Where the function is *defined*? Where is it *called*?
3. Create a function that takes a text as an argument. The function prints the text it receives. Call the function and run your program.
4. Create a function that takes two numbers as argument. The function adds the numbers together and returns the results. Call the function and run your program.
5. Create two functions, each takes a number as argument. The first one returns the number multiplied by 2 and returns it. The second multiplies it by 10 and returns it. Calling both functions add the two returned numbers together and print it. Run your program and check the results.
6. Create two functions. One that prints `hello`, the other prints `bye`. Ask the user to input a number, if the number is higher than 10, call the first function. If the number if lower or equal to 10, call the second function. Test your program.
7. Create two functions. One that prints `hello`, the other prints `bye`. The first functions calls the second one after printing. Call the first function.
8. Provide your solutions to the exercises of Python 05: Step-01. **ORef-01: Functions** can be used as extra learning reference.
9. Design two exercises of your own. They should improve understanding topics of this step.
10. Install *PyCharm* on your working machine. Implement and run a simple Python program of your choice. 
	- It is important to learn how to create a new Python program, how to configure interpreter and how to run the program. Where do you see the results?


<hr>

### Step-02: Tuples.

#### Goals:

```
After taking this step, you will be able to:
	1. interpret and implement Python programs using tuples.
```

#### What to Learn?

1. Using **BRef-01: Chapter 07** answer and experiment the following questions:
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

### Step-03: Lists.

#### Goals:

```
After taking this step, you will be able to:
	1. interpret and implement Python programs using lists: defining, offset, slicing, adding new element, modifying an element.
```

#### What to Learn?


1. Using **BRef-01: Chapter 07** answer and experiment the following questions:
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

## Learning Activities:

### Code Analysis
1. Analyze the two given codes below without executing them. What will be the result of the programs?

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

### Supporting Topics

## Testing: Input/Output

Implementing a *correct* program is not easy. Programs always tend to have bugs. **Input/Output Test** is one of the common techniques to test the correctness of a program. The main idea is to *design* certain inputs, run the program with the inputs and check if the *produced* output satisfies *expected* output.

1. Make a brief research about input/output testing with some examples. Make a summary of the techniques with the examples.
2. Choose one of the problems you have solved for this week.
	- Certainly there are some normal inputs that your program is supposed to provide a correct output. Think about three different *expected* inputs and see if the output is correct.
	- There are some inputs that are not expected. For example, if your program is supposed to receive an integer between 0 and 10, then a negative integer is not expected. Choose three different unexpected inputs and test your program. If your program crashes, then fix your program such that provides a proper message instead of crashing.
	- Usually, users unexpectedly make mistakes when trying to give an input. For example, if they try to enter a digit between 0 and 10, mistakenly they press `6;` . Check if your program is resilient for such errors.
