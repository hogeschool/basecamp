# Python 06: Functions, Dictionaries and Sets.

**Introduction**: This document presents learning steps for Python 06. In Python 06, you will learn dictionaries to collect keys and coresponding values. Moreover, you will learn more features of functions. 

**Note:** Exercises of this learning path should be done using:

1. IDE: Using **BRef-01: Chapter 19, Section: Integrated Development Environment** PyCharm can be installed in your local machine.

## Materials:

The activities are designed based on these following references:

- **BRef-01**: Book, Bill Lubanovic; "Introducing Python: Modern Computing in Simple Packages"; [Available here](https://www.oreilly.com/library/view/introducing-python-2nd/9781492051374/) 
- **ORef-01**: Online Tutorial; Charles Severance; "Python for Everybody"; [Available here](https://books.trinket.io/pfe/index.html)
- **ORef-02**: Book, Brian Heinold; "A Practical Introduction to Python Programming" [Available Online, Check here](https://www.brianheinold.net/python/python_book.html)


## Path:

### Step-01: Dictionaries.

#### Goals:

```
After taking this step, you will be able to:
	1. interpret and implement Python programs with Python Dictionaries: creating, adding and modifying items,  extracting value(s), extracting key(s), deleting, pop and clear, iteration over dictionaries.
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
	- Print all the values from the distionary.
	- Print all the keys from the dictionary.
	- Print the length of the dictionary.
	- Add `"color": "Red"` and remove the pair with key = `"year"`. Print keys and values separately. 

4. Modify the code from the previous exercise so each value becomes a `tuple` containing two random numbers.

5. Provide your solutions to the exercises of **ORef-01: Dictionary**.

6. Design two exercises of your own. They should improve understanding topics of this step.

7. If you don't have PyCharm yet, install *PyCharm* on your working machine. Implement and run a simple Python program of your choice. 
	- It is important to learn how to create a new Python program, how to configure interpreter and how to run the program. Where do you see the results?

8. **Extra:** Provide your solutions to the exercises of **ORef-01: Dictionaries** 


<hr>

### Step-02: Functions (more).

#### Goals:

```
After taking this step, you will be able to:
	1. interpret and implement Python programs with Python functions: positional arguments, keyword arguments, parameters default values, docstrings.
```

#### What to Learn?

1. Using **BRef-01: Chapter 09** answer and experiment the following questions:
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


5. Design two exercises of your own. They should improve understanding topics of this step.

6. **Extra:** Provide your solutions to the exercises of **ORef-01: Functions** 


<hr>

### Step-03: Sets.

#### Goals:

```
After taking this step, you will be able to:
	1. interpret and implement Python programs with Python Sets: creating sets, difference between sets and lists and tuples, adding and removing elelemnts, membership operator, iteration over a set, basic operations between sets: intersection, union, difference and subset.
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

<hr>

## Learning Activities:

### Code Analysis
1. Analyse the given code below without executing it. What will be the result of the program?

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
2. Analyse the given code below without executing it. What will be the result of the program?

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
3. Given the following code below. Explain in your own words what happens in this code. What are the keys in the dictionary?

 ```python
import random
rdic = {}
for i in range(0,10):
	rdic[i] = random.randint(0,100)
for item in rdic.values():
	print(item)
```


### Supporting Topics
#### Debugging

##### Introduction
Debugging is an essential process in software development that involves identifying, analyzing, and resolving issues or bugs within a program's code. It is a systematic approach to troubleshooting and improving the functionality and performance of software. Debugging typically involves identifying the root cause of a problem, using techniques such as step-by-step code execution, examining variable values, and analyzing error messages. By pinpointing and resolving issues, debugging helps ensure that software operates correctly, meets user requirements, and delivers a reliable and efficient user experience. Effective debugging skills are valuable for developers in maintaining and enhancing the quality of software systems.

##### Activity

Use the following code and debugging of your IDE and find the bug(s).

[todo: extend the instructions, inject a bug]

```python
contacts = []

def add_contact(name, phone_numbers, email):
    contact = {
        'name': name,
        'phone_numbers': phone_numbers,
        'email': email
    }
    contacts.append(contact)

def search_contacts(keyword):
    return list(filter(lambda c: keyword.lower() in c['name'].lower(), contacts))

def delete_contact(name):
    global contacts
    contacts = [c for c in contacts if c['name'].lower() != name.lower()]

def update_contact(name, phone_numbers, email):
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contact['phone_numbers'] = phone_numbers
            contact['email'] = email
            break

def main():
    add_contact("John Doe", ["1234567890", "9876543210"], "john@example.com")
    add_contact("Jane Smith", ["5555555555"], "jane@example.com")
    add_contact("Bob Johnson", ["1111111111", "2222222222", "3333333333"], "bob@example.com")
    
    search_term = input("Enter a name to search: ")
    search_results = search_contacts(search_term)
    
    if search_results:
        print("Search Results:")
        for contact in search_results:
            print(f"Name: {contact['name']}")
            print("Phone Numbers:", ', '.join(contact['phone_numbers']))
            print(f"Email: {contact['email']}")
    else:
        print("No matching contacts found.")
    
    contact_name = input("Enter the name of the contact to delete: ")
    delete_contact(contact_name)
    print("Contact deleted successfully.")
    
    update_name = input("Enter the name of the contact to update: ")
    update_phone_numbers = input("Enter the new phone numbers (separated by commas): ").split(",")
    update_email = input("Enter the new email address: ")
    update_contact(update_name, update_phone_numbers, update_email)
    print("Contact updated successfully.")

main()
```