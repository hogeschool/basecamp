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

### Step-03: Strings are essential.
#### Goals:

```
After taking this step, you will be able to:
	1. interpret and implement basic operations of strings: concatenation (combining), duplicating, scanning and slicing.
```

#### What to Learn?

1. Using **BRef-01: Chapter 05** discuss and experiment the following questions:
   1. How can you combine several strings? Implement an example.
   2. Can you multiply a number with a string? What is the result? Implement an example.
   3. How can you get character 5 of a given string? How can you get the first character?
   4. How can you get a substring from a given string?

#### Exercises:

1. We can use a ```+``` or a ```,``` to combine two strings within a print. What's the difference?
2. Using a program, ask the user for input. Print the first and last character from the input.
3. Student numbers start with 0. Implement a program where the user enters a student number and your program must check if it starts with 0.
4. Ask the user to input a number. If it is lower than ```10``` print it, otherwise only print the first character.
5. Write down the complete alphabet in a variable. Split it halfway over two different variables. Join them back together in the wrong order and print it.
6. Explain in your own words with a ```f``` style string is?
7. Look up the Spanish alphabet and put it in a variable. Put the Dutch alphabet in a variable. Print ```yes``` if the letter ```k``` is at the same position at both, print ```no``` if not. Use an ```if``` statement.
8. Ask the user for a text input. Change both the first and last characters to uppercase and print it.
9. Practice the exercises listed in **BRef-01-Chapter 05: Things to Do**.

 <hr>


## Learning Activities:

### Code Analysis

1. Given the following problem statement, one of the students has submitted a solution. The submitted solution is not working correctly.
	- Without executing the submitted code, check the implementation, analyze and find the issue(s).
	- Use the following link to run the code step by step and visualize the execution. [Python Execution Visualizer](https://cscircles.cemc.uwaterloo.ca/visualize)
	- This step-by-step execution should confirm the issues you have found in the code.
	- After listing the issues, propose how the code must be fixed. Fix the code and again use step-by-step execution to see that the issues are fixed.

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

<br>

### Supporting Topics

1. Perform a free (re-)search and explore answers for the following questions:
   1. What is an Operating System and why do we need it?
   2. Consider your own computer and OS (Operating System). How do you interact with the OS: Graphical User Interface (GUI) or commands?

2. Perform a free (re-)search and carry on the following tasks:
	1. Open a terminal / a command prompt. What is the current folder?
	2. How can you make a list of the contents of the current folder?
	3. Using the command line, create a folder and name it `workspace`.
	4. Use command prompts and change your current folder such that you are in the folder `workspace`.
	5. Create a folder `basecamp` and within `basecamp` create `week01`.
	6. You have used an online editor to implement your solutions for the given problems of this week. Save one of the solutions within `../basecamp/week01/`. Name the file properly. Make sure that the extension of the file is `.py`.
	7. Is it possible to execute the downloaded Python program using command line? Try it. *Note: You may receive an error because Python is not installed on your machine. In this case, you can try this next week.*
	8. Use the command line to create an empty Python file with a proper name.
	9. Use the command line to create another folder named `week02` within `./basecamp/`. Copy (using the command line) your empty Python file within `week02`.
	10. Within the folder of `week01` use the command line and create a file named `summary.txt`. Open the file (using commands), write down a summary of commands you have learned and used so far and save the file.
