# Python 02: Branching Programs

**Introduction**: This document presents learning steps for Python 02. In Python 02, you will learn basics of Python structures to add decision points to your programs. A branching program is a flow of sequential instructions with branching statements. By the end this week, you will be able to implement a program where a user can enter simple input, the program can make choices based on some conditions and after calculation, results can be printed.

**Note:** Exercises of this learning path can be done using:

1. Online Python Editor **OPyEditor**: The final program should be stored on your local machine.
2. Local Python Package (see Step-01): Using **BRef-01: Appendix B** Python can be installed on your local machine.

## Materials:

The activities are designed based on these following references:

- **BRef-01**: Book, Bill Lubanovic; "Introducing Python: Modern Computing in Simple Packages"; [Available here](https://www.oreilly.com/library/view/introducing-python-2nd/9781492051374/)
- **OPyEditor**: Online Editor for Programming; "Online Python (with shell and file storing functionalities)"; [Available here](https://www.online-python.com/)

## Path:


Follow these steps:

### Step-01: Set Up
#### Goals:

```
After taking this step, you will be able to:
	1. implement and run your Python programs on your local machine.
```

#### What to Learn?

1. Using **BRef-01: Appendix B** perform the following tasks:
   1. Install Python on your machine.
   2. Open a terminal (command window) and check the version of your Python. Which command did you use?
   3. Using **OPyEditor** implement a program that prints a statement of a defined variable, like ```Hello Python!```. Save the file on your local machine within a folder created by you. Using your terminal (command line) execute your first Python program. Which command do you need to execute a Python program?

#### Exercises:

1. Create a file named ```print_input.py```. Open it using an editor of your own choice. Enter your code in it to ask the user to input a text. Print that text. Run the file using the command line.
2. Read **BRef-01: Chapter 01, Section Running Python** and runPython shell. Excute ```quit()```. What do you observe?
3. StartPython shell and execute ```num = input('Enter a number:')```. Enter a number and print the value of ```num```. There are two different ways to print the value of ```num```. Try both at shell. Which one works in **OPyEditor**? Do you recognise differences between programming using *python shell* and an *editor*? Read **BRef-01: Chapter 01, Section Running Python** including subsections.

**Note**: After this step, you can try both *python shell* and *editor* to practice. It is recommended to use *python shell* for small experiments and use programming within *editor*s (local or online) for writing a full program.

<hr>

### Step-02: Programs need to decide.
#### Goals:

```
After taking this step, you will be able to:
	1. interpret and implement boolean expressions.
	2. implement Python programs with conditional statements.
```

#### What to Learn?

1. Using **BRef-01: Chapter 04** discuss and experiment the following questions:
   1. What is a comment? How can you specify a comment in Python?
   2. What are: boolean values, boolean expressions, comparison operators?
   3. What is a conditional statement in Python? What is correct syntax for a correct *if-else* statament? What is a *body* of a *if-else* statement?

#### Exercises:

1. Create a variable with the value ```True```. Print it. Change the value to ```False```. Print it.
2. Create a variable
	- named ```a``` with the value ```True```, another
	- named ```b``` with the value ```False```. Use print to check the output of ```print(a == b)```.
	- Do the same for the other comparison operators, ```!=```, ```<```, ```>```, ```<=```, ```>=```.
4. Repeat the second exercise using an *if-statement*. Print ```yes``` or ```no```, for true false.
	- Write a comment above the *if-statement* explaining with it does.
6. Implement a program in which the user is asked for input. Save the input of the user in a variable. Print ```yes``` if the input contains the character ```e```, ```no``` if not.
7. Think of an useful situation where you need to check something with a if-statement within another if-statement (nested if-statements). Code it and write a comment to explain why it needs a nested if.
8. Finish all the exercises listed in **BRef-01-Chapter 04: Things to Do**.

<hr>

### Step-03: What is a function?

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

*Note*: In the following exercises you can decide yourself what should be the name of function in your solution. Check [PEP8 Function and Variable Names](https://peps.python.org/pep-0008/#function-and-variable-names) for guidelines.

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


## Learning Activities:

### Code Analysis

1. Given the following problem statement, one of the students has submitted a solution. The submitted solution may not work correctly.
	- Without executing the submitted code, check the implementation, analyze and find the issue(s).
	- Use the following link to run the code step by step and visualize the execution. [Python Execution Visualizer](https://cscircles.cemc.uwaterloo.ca/visualize) Note: Before pressing "Visualize Execution" you need to enter your input at "Enter optional text input for ...". 
	- This step-by-step execution should confirm the issues you have found in the code.
	- After listing the issues, propose how the code must be fixed. Fix the code and again use step-by-step execution to see that the possible issues are fixed.
	- Remember: the main goal is to learn how the program is executed step-by-step. Focus on the **goal**.

	**Problem Statement**
   > Develop a program that reads a four-digit integer from the user and displays the sum of the digits in the number.
   >
   > ###### Input example:
   > `3141`
   >
   > ###### Output example:
   > `3+1+4+1=9`

	**Incorrect Solutions** \
   Solution 1:
   ```python
   fourdigit_num = int(input("Input a four digit number: "))
   x  = fourdigit_num // 1000
   x1 = (fourdigit_num - x * 1000) // 100
   x2 = (fourdigit_num - x * 1000 - x1 * 100) // 10
   x3 = fourdigit_num - x * 1000 - x1 * 100 - x2 * 10
   print("Sum:",x+x1+x2+x3)
   ```
   Solution 2:
   ```python
   numstr = input("enter a 4 digit number")
   sum = 0
   text = ""
   for i in range(len(numstr)):
      sum += int(numstr[i])
      text = text + numstr[i]
   print(text)
   ```