# Python 07: Functions and Collective Structures.

**Introduction**: This document presents learning steps for Python 07. In Python 07, you will learn more in depth about tuples, lists, dictionaris and functions.

**Note:** Exercises of this learning path must be done using:

1. IDE: Using **BRef-01: Chapter 19, Section: Integrated Development Environment** PyCharm can be installed on your local machine.


## Materials:

The activities are designed based on these following references:
Python
- **BRef-01**: Book, Bill Lubanovic; "Introducing Python: Modern Computing in Simple Packages"; [Available here](https://www.oreilly.com/library/view/introducing-python-2nd/9781492051374/)
- **ORef-01**: Online Tutorial; Charles Severance; "Python for Everybody"; [Available here](https://books.trinket.io/pfe/index.html)


## Path:

### Step-01: Functions (more).

#### Goals:

```
After taking this step, you will be able to:
	1. interpret and implement Python programs with Python functions: anonymous functions.
	2. understand the concepts of namespace and scope in Python programs.
```

#### What to Learn?

1. Using **BRef-01: Chapter 09** answer and experiment the following questions:
   1. "Functions are first-class citizens": What does this sentence mean?
   2. What is an anonymous function and how can you define it in Python? Experiment with some examples.
   3. What are *namespace* and *scope*? What is the scope of a function? Use examples to justify your answers.

#### Exercises:


2. Complete the given code by creating a lambda that checks if a given number is even.

```python
even = #your lambda here
print(even(4))
print(even(13))
```

3. Create a code snippet that splits up a list into two new lists. Depending on if the number in the list is even or odd. Accomplish this with using a lambda and knowledge from the earlier weeks.
- For example: Original list of integers:
`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`.
New list with only the even numbers:
`[2, 4, 6, 8, 10]`.
New list with the odd numbers:
`[1, 3, 5, 7, 9]`

4. Complete the function that checks if a given list is sorted or not, use at least one lambda within the function.

```python
def am_i_sorted(numberlist):
    #write the code
result = am_i_sorted([1,2,5,6,8,17])
print(result) #True
result = am_i_sorted([1,2,99,6,8,17])
print(result) #False
```

5. Create a lambda that takes two arguments and returns a Tuple containing those two values.

6. Complete the function that checks if the items in a given list are `True` for the given lambda. Return a list containing all `True` values.

```python
def check_with_lambda(lam, l):
    #write the code

x = lambda a : a < 10
y = [1,6,19,22,7]
print(check_with_lambda(x, y)) #[1,6,7]
x = lambda a : a[1] == 'b'
y = ["abc", "bcd", "ube", "cur"]
print(check_with_lambda(x, y)) #["abc","ube"]
```

7. Often implementing your solutions you may need to use some important built-in functions: ```map(...)``` and ```filter(...)```. Study them first [here](https://www.brianheinold.net/python/python_book.html#section_map_filter_reduce) and practice a few small examples to understand how they work and when you might need them.

8. Design two exercises of your own. They should improve understanding topics of this step.

<hr>

### Step-02: Tuples and Lists (more).

#### Goals:

```
After taking this step, you will be able to:
	1. interpret and implement Python programs with Python Tuples and Lists: join(), list(), copy(), deepcopy(), slicing and list comprehension.
```

#### What to Learn?

1. Using **BRef-01: Chapter 07** answer and experiment the following questions:
   1. We have learned *join()* on a string. How does *join()* work in a list?
   2. How can we sort items of a list? Is this possible on a tuple?
   3. There are several ways to copy a list: *list(), slicing, copy()* and *deepcopy()*. Experiment different expamples for each technique.
   4. How can one build a list using *list comprehension*? Do we have *tuple comprehension*?

#### Exercises:

1. The method `list.sort()` sorts a list ascending. Look up how to sort descending and try it.

2. Create a list containing at least three `tuples` containing some numbers. Print the last item of each tuple by looping through the list.

3. Complete the function that returns a list containing all the values from all tuples in the given list.

```python
def create_list_from_tuples(a):
    #write the code

l = [(1,5,4),(1,2),(8,5,19,0)]
print(create_list_from_tuples(l))
#[1,5,4,1,2,8,5,19,0]
```

4. Take the list of tuples from the previous exercise. Sort the list ascending on the last item of each tuple.

5. Create a loop that creates a list containing tuples with the numbers 1 to 10 in pairs of 2. The result should be `[(1,2),(3,4),(5,6),(7,8),(9,10)]`.

6. Take the list from the previous exercise. Remove the tuples in which the first item is an odd number. Use a lambda to determine this.

7. Design two exercises of your own. They should improve understanding topics of this step.

<hr>

### Step-03: Dictionaries and Sets (more).

#### Goals:

```
After taking this step, you will be able to:
	1. interpret and implement Python programs with Python Dictionaries and Sets: copy(), deepcopy(), dictionary comprehension, nested structures.
```

#### What to Learn?

1. Using **BRef-01: Chapter 08** answer and experiment the following questions:
   1. How do *copy()* and *deepcopy()* behave on dictionaries? What about sets?
   2. How does *dictionary comprehension* work? What about sets?
   3. Try to build the following nested structures:
	   - List of lists.
	   - Tuple of lists.
	   - Tuple of tuples.
	   - List of tuples

#### Exercises:

1. Complete the function to merge two lists into one dictionary.

```python
def merge_lists_into_dictionary(l1, l2):
    #write the code

keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']
result = merge_lists_into_dictionary(keys, values)
print(result) #{'red': '#FF0000', 'green': '#008000', 'blue': '#0000FF'}
```

2. Given is a list of dictionaries. Sadly the values are the wrong way around. The first value should be at the last key, second value at the second from last key, and so on. Create a function that switches these values for each list you could give it.

```python
def swith_the_values(l):
    #Write the code

x = [{'Math':81}, {'Physics':83}, {'Chemistry':87}, {'English': 42}]
print(swith_the_values(x))
#[{'Math':42}, {'Physics':87}, {'Chemistry':83}, {'English': 81}]
x = [{'a':'b'}, {'c':'d'}]
print(swith_the_values(x))
#[{'a':'d'}, {'c':'b'}]
```

3. Given is a dictionary with tuples. Complete to code to add all keys, at which the second Tuple value is Pass, to a list and return that list

```python
def create_pass_list(l):
    #Write the code

x = {'Math':(81,"Pass"), 'Physics':(50,"Fail"), 'Chemistry':(90,"Pass"), 'English': (42,"Fail")}
print(create_pass_list(x))
#["Math", "Chemistry"]
```

4. Based on the previous exercise. Write a new function that creates a list with failed subjects. Merge the two lists into a new dictionary with the correct keys. Result should be: `{'Pass':["Math", "Chemistry"], 'Fail':["Physics","English"]}`.

5. Write a function that takes the dictionary from the previous exercise and turns each value into his own key:value pair. Sort the dictionary by the key. The result should be: `{'Chemistry': 'Pass', 'English': 'Fail', 'Math': 'Pass', 'Physics': 'Fail'}`;

6. Test all the functions from the last few exercises if they still work given a different starting dictionary. If not, try to explain what went wrond and fix it.
A different dictionary could be:
`{'Soccer':(9, "Pass"), 'Snowboarding':(3, "Fail"), 'Tennis':(7, "Pass")}`.

7. Design two exercises of your own. They should improve understanding topics of this step.

<hr>

## Learning Activities:

### Code Analysis
1. Analyze the given code below without executing it. What will be the result of the program?

```python
r = lambda a : a + 15
print(r(10))
r = lambda x, y : x * y
print(r(12, 4))
```

2. One of the students has implemented the following code.
	- Apply Input/Output testing and see if the program works correctly.
	- Analyze the code (without execution) and see if you can detect the bug.
	- Debug the code and validate your finding.

```python
students = []

def add_student(name, age, grade):
    student = {
        'name': name,
        'age': age,
        'grade': grade
    }
    students.append(student)

def get_student(name):
    return list(filter(lambda s: s['name'] != name, students))

def get_students_by_grade(grade):
    return list(filter(lambda s: s['grade'] != grade, students))

def main():
    while True:
        print("Student Management System")
        print("1. Add Student")
        print("2. Search Student by Name")
        print("3. List Students by Grade")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            grade = input("Enter student grade: ")
            add_student(name, age, grade)
            print("Student added successfully!")

        elif choice == '2':
            name = input("Enter student name: ")
            student = get_student(name)
            if student:
                print("Student found:")
                print(f"Name: {student[0]['name']}")
                print(f"Age: {student[0]['age']}")
                print(f"Grade: {student[0]['grade']}")
            else:
                print("Student not found.")

        elif choice == '3':
            grade = input("Enter grade to filter students: ")
            students_by_grade = get_students_by_grade(grade)
            if students_by_grade:
                print(f"Students in grade {grade}:")
                for student in students_by_grade:
                    print(f"Name: {student['name']}, Age: {student['age']}")
            else:
                print("No students found in the given grade.")

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

main()
```