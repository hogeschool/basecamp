# Python 09: Everything is an Object.

**Introduction**: This document presents learning steps for Python 09. In Python 09, you will get introduced with classes and objects in Python. This will be the first step in Object Oriented Programming in Python.

**Note**: In this phase, it is expected the learner can divide the program into smaller learning steps. The goal and direction of the topics will be provided. The learning must take smaller steps towards the goals such that can implement solutions to the given problems and product(s).

## Materials:

The activities are designed based on these following references:

- **BRef-01**: Book, Bill Lubanovic; "Introducing Python: Modern Computing in Simple Packages"; [Available here](https://www.oreilly.com/library/view/introducing-python-2nd/9781492051374/)
- **ORef-01**: Online Tutorial; Charles Severance; "Python for Everybody"; [Available here](https://books.trinket.io/pfe/index.html)


## Path:

### Step: Class and Object.

#### Goals:

```
After taking this step, you will be able to:
	1. interpret and implement Python programs with Python objects and classes: defining a class, instantiating an object, attributes and methods, initializing and object.
	2. understand the concepts of namespace and scope in Python programs.
```

#### What to Learn?


1. Using **BRef-01: Chapter 10** answer and experiment the following questions:
   1. What is an Object in Python?
   2. What is a class and how can you define a class in Python? Make an example.
   3. How can you create and use an object from a class? Experiment with examples.
   4. What are attributes? How they help programmers to encapsulate their data values?
   5. What is a method? Focus only on *instance methods*.
   5. How can you initialize an instance (object)? Implement a class with **__init__** method.


#### Exercises:

1. Design at least ten different exercises of your own. They should improve understanding topics of this step. Share your exercises with your learning community and practice.

<hr>

## Learning Activities:

### Code Analysis

**Problem**: In a programming assignment, students are asked to implement a simple Python program where libraries can store books. Below, you can find a sample solution provided by one of the students.
- Without executing the code, read the code and try to predict what will be printed at the end.
- Run the code in your IDE. Does it print what you had predicted? If not, why?
- Debug the code carefully and fix the bug, if you find any. 


```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __repr__(self) -> str:
        return f'Title: {self.title} , Author: {self.author}'

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
    def add_books(self, books):
        self.books = books
    def display_books(self):
        print(f"Books in {self.name} Library:")
        for book in self.books:
            print(book)

def main():
    # Create Books
    book1 = Book('Introducing Python','Bill Lubanovic')
    book2 = Book('The Python Workbook','Ben Stephenson')
    book3 = Book('Learn Python Programming','Fabrizio Romano')
    book4 = Book('Fleunt Python','Luciano Ramalho')
    # Create libraries
    univ_lib = Library('University')
    city_lib = Library('City')
    # Add books to the libraries
    univ_lib.add_books([book1,book4])
    city_lib.add_books([book1,book3])
    univ_lib.add_books([book1,book2])
    city_lib.add_books([book3,book4])  
    # Display books in libraries
    univ_lib.display_books()
    city_lib.display_books()

main()
```

### Supporting Topics

**Introduction**: In this week, you have been introduced to objects and classes in Python. This is the very first step in Object-Oriented Programming. In general, the four pillars of Object-Oriented Programming are: Encapsulation, Inheritance, Polymorphism, and Abstraction. In this activity, you will carry out a small research about **Encapsulation**.

- Conduct a small research about Encapsulation and try to discuss the concept within your learning team.
- Implement a Python program where basic information of cars (model, price, year, mileage) can be processed by some car agencies. Keep the functionalities simple.
- Try to explain encapsulation within your own implementation. If you don't see encapsulation within your solution, refactor your code.
- Share your findings and pros and cons of each solution with your teacher / classmates.



### Extra topics (Optional)
The follwoing concepts are not part of the main learning path, but can be considered as *optional* learning steps for those who seek more challenges:

- Inheritance
- Polymorphysm
- Abstraction
- Class methods
- Static methods
- Dataclasses
