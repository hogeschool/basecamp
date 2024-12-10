# Python 14: Databases - part 2.

**Introduction**: This document presents learning steps for Python 13. In Python 13, you will learn the basics of implementing Python programs that can interact with databases.

**Note**: In this phase, it is expected the learner can plan and run the required learning process towards the goals of the week: making solutions to the given problems and product(s).

## Materials:

The activities are designed based on these following references:

- **BRef-01**: Book, Bill Lubanovic; "Introducing Python: Modern Computing in Simple Packages"; [Available here](https://www.oreilly.com/library/view/introducing-python-2nd/9781492051374/)
- Free research.

## Path:

### Step: Databases.

#### Goals:

```
After taking this step, you will be able to:
	1. understand the concept of databases.
	2. understand and implement Python programs making basic queries in SQLite: SELECT x,y,z FROM t WHERE c GROUP BY x ORDER BY y, INSERT, UPDATE, DELETE, SUM, COUNT.
```
#### What to learn?

1. Using **BRef-01, Chapter 16: Relational Databases** make a plan for the week to learn basics of Python programs interacting with relational databases.
	- Make an overview of the provided problems and final product.
	- Plan what you need to learn in order to provide your solutions.
	- Read proposed book chapter and practice basic steps.

<hr>

#### What is a database

A **database** is an organized collection of data, generally stored and accessed electronically from a computer system. Databases are essential for managing large amounts of data efficiently. Here's an overview of key concepts:

**Data** refers to the raw facts and figures that are processed to obtain information. For example, a person's name, age, and address are pieces of data.

##### Tables
Databases organize data into tables, which are collections of related data entries. Each table consists of rows and columns.

- **Row**: A single, horizontal entity in a table (also known as a record).
- **Column**: A vertical attribute in a table (also known as a field).
- **Primary Key**: A primary key is a unique identifier for a record in a table. \
	No two rows can have the same primary key value. It ensures that each record can be uniquely identified.
- **Foreign Key**: A foreign key is a field (or a collection of fields) in one table that uniquely identifies a row of another table.
- **Indexes**: Indexes are used to speed up the retrieval of data from a database table by creating a separate data structure that can be searched efficiently.

##### SQL (Structured Query Language)
SQL is the standard language used to communicate with a database. It includes commands to create tables, insert data, query data, and more.

##### Creating tables
Let's assume we have a table for `students`, this table has 5 rows (`id`, `first_name`, `last_name`, `date_of_birth`, `city` and `points`).

| id   | first_name | last_name | date_of_birth | city      | points |
| :--- | :--------- | :-------- | :------------ | :-------- | :----- |
| 1    | Alice      | Smith     | 2000-01-15    | Amsterdam | 50     |
| 2    | Bob        | Johnson   | 1999-05-22    | Utrecht   | 43     |
| 3    | Charlie    | Brown     | 2001-11-03    | The Hague | 19     |

If we want to store this information in a database, we need to create this table first.\
This would reflect in the following SQL command:

```sql
CREATE TABLE students (
	id INTEGER PRIMARY KEY AUTOINCREMENT
	first_name VARCHAR(50), 
	last_name VARCHAR(100),
	date_of_birth DATE, 
	city VARCHAR(50),
	points INT
);
```


###### CRUD Operations
CRUD stands for the four basic operations you can perform on data:

<br>

**Create**: Add new records.
```sql
INSERT INTO students (first_name, last_name, date_of_birth, city) 
VALUES ('John', 'Doe', '1998-04-18', 'Rotterdam');
```

<br>

**Read**: Retrieve and read existing records.
```sql
SELECT * FROM students;
```

The `*` in the above example is a wildcard, and will retrieve all fields from the table `students`.\
For our database this will mean we will get back records containing the fields:\
- `id`
- `first_name`
- `last_name`
- `date_of_birth`
- `city`
- `points`

You could also specify which fields you want (subset of fields):
```sql
SELECT first_name, last_name, city FROM students
```
This will retrieve all records from `students`, but will only return the `first_name, last_name, city` in each record.

<br>

To retrieve only specific students matching something `Rotterdam` as city for example, we can use the `WHERE` keyword in the `SELECT` statement:
```sql
SELECT first_name, last_name, city FROM students WHERE city = 'Rotterdam';
```
This will return only records that have a match on `city = 'Rotterdam'`, in our database this will reflect to:
| id   | first_name | last_name | date_of_birth | city      | points |
| :--- | :--------- | :-------- | :------------ | :-------- | :----- |
| 4    | John       | Doe       | 1998-04-18    | Rotterdam | 0      |


<br>

**Update**: Modify existing records.

Alice moved from Amsterdam to Rotterdam, so we need to `UPDATE` her record.

```sql
UPDATE students SET city = 'Rotterdam' WHERE id = 1;
```

*notice the `WHERE` condition here, if you leave it out it will update **ALL** records!* 


You can also update multiple fields at the same time, just seperate them by a `,` *(comma)*:\
For example, Alice moved to Rotterdam because she married John. We update her `city` but also her `last_name`:
```sql
UPDATE students SET last_name = 'Doe', city = 'Rotterdam' WHERE id = 1;
```

<br>

**Delete**: Remove records.

Sometimes a student leaves and we need to remove it's record from the database, we use `DELETE` for that.
```sql
DELETE FROM students WHERE id = 2;
```
*notice the `WHERE` condition here, if you leave it out it will delete **ALL** records!* 


###### Extra SQL Functions

**GROUP BY**

The `GROUP BY` clause groups rows that have the same values in specified columns into aggregated data.\
It’s often used with aggregate functions (like `COUNT`, `SUM`, `AVG`, `MAX`, `MIN`) to perform operations on each group of rows.

```sql
SELECT city, COUNT(*) as student_count FROM students GROUP BY city;
```
This query will count the number of students in each city.


<br>

**ORDER BY**

The `ORDER BY` clause is used to sort the result set by one or more columns.\
By default, it sorts in ascending order, but you can specify `DESC` for descending order.
```sql
SELECT first_name, last_name, city FROM students ORDER BY last_name ASC, first_name DESC;
```
This query will sort students by last name in ascending order and by first name in descending order.

<br>

**SUM**

The `SUM` function returns the total sum of a numeric column.\
It’s often used with the `GROUP BY` clause to sum values for groups.

```sql
SELECT city, SUM(points) as total_points FROM students GROUP BY city;
```

This query will sum the points of students in each city.

<br>

**COUNT**

The `COUNT` function returns the number of rows that match a specified condition.\
It’s commonly used to count the number of records in a table.

```sql
SELECT COUNT(*) as total_students FROM students;
```
This query will count the total number of students in the students table.


<br>

**AVG, MAX, MIN**
Beside `SUM` and `COUNT` there are more functions you could use: `AVG`, `MAX` and `MIN`.\
Do some research in what each functions does and how you could use them in your benefit.
