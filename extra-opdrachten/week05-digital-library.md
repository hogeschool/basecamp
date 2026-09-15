# Extra opdracht — Digital Library Management System

> Omgezet uit `Extra assignment week 5 - Digital Library Management System.docx`.
> Het origineel staat in [`lesmateriaal/week05/Lesson Material/Additional lesson material`](../lesmateriaal/week05/Lesson%20Material/Additional%20lesson%20material).
> Dit is het lege format van de opleiding — invullen doe je zelf.

---
**Assignment Description:**

In this assignment, you will be working on a Python program that simulates a digital library management system. The goal of this assignment is to apply your knowledge of lists, functions, lambdas, dictionaries, args and kwargs, and loops to create a functional library system.

**Requirements:**

1. **Library System Setup:**

Create a list to store information about books in the library. Each book should be represented as a dictionary with the following keys: `'title'`, `'author'`, `'genre'`, and `'available'`.

Initialize the list with at least 10 books.

2. **Functions:**

Create a function `display_books` that takes the list of books and displays the details of each book, including whether it's available or checked out.

Create a function `find_books_by_author` that takes the list of books and an author's name as an argument. It should return a list of books by that author.

Create a function `check_out_book` that takes the list of books and the title of the book to be checked out. Update the book's availability status to "checked out."

Create a function `return_book` that takes the list of books and the title of the book to be returned. Update the book's availability status to "available."

3. **Lambdas:**

Use a lambda function to sort the list of books by title in alphabetical order.

Use another lambda function to sort the list of books by author's name in alphabetical order.

4. **Dictionaries:**

Create a dictionary to store information about library members. Each member should have a unique ID, name, and a list of checked-out books.

5. **Args and Kwargs:**

Create a function `add_member` that accepts a member's name and other optional information (kwargs) such as address, phone number, etc. Assign a unique ID to each member and store their information in the members dictionary.

6. **Loops:**

Implement a menu-driven interface using a while loop that allows users to interact with the library system. The menu should include options to display books, find books by author, check out a book, return a book, add a new member, and exit the program.

**Submission Guidelines:**

Please submit a Python script that includes the implementation of the above requirements. Include comments and explanations to make your code clear and easy to understand. Also, provide sample usage of your library system by simulating different actions in the main part of your script.
