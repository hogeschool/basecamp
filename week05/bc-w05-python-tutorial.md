# Python 05: Tutorial


## Introduction

So far, we have learned the fundamental structure of a Python program. We have practiced how to interact with the user using the `input()` and `print()` functions, employed conditional statements (`if`, `elif`, `else`) to make decisions in code execution, and experimented with loops (`for` and `while`) to iterate through sequences of instructions. We have also studied how to define and manipulate primitive data types, such as numbers and strings, and finally, we explored how functions can be used to break down long pieces of code into smaller, manageable components.

However, in many real-world scenarios, solving problems requires handling multiple values simultaneously, rather than working with just a few individual variables. To efficiently manage and organize data, Python provides collection structures that allow us to store, modify, and process multiple values within a single entity. Each of these structures serves a specific purpose and is optimized for different types of operations, making it easier for programmers to handle complex data efficiently.

In this tutorial, we will introduce the basics of two fundamental data structures in Python and explore how they can be utilized effectively. Additionally, we will further expand our understanding of functions and their features to enhance the modularity and efficiency of Python programs.


## Step 01: Tuples

A tuple in Python is a way to store multiple values together in one variable. Imagine you want to keep a set of related items, like the names of the days in a week, the RGB values of a color, or the coordinates of a point in space. Instead of creating separate variables for each value, you can put them inside a tuple. A tuple keeps the order of the values exactly as you define them, and once you create it, you cannot change its contents. When we say that a tuple cannot be changed after creation, it means that it is **immutable**. This is an important property of tuples in Python. Once a tuple is created, you cannot add, remove, or modify its elements. The values inside the tuple will always remain the same throughout the program.

To define a tuple in Python, you write the values inside parentheses `()`, separated by commas. For example, a tuple that stores the names of three colors can be written as `colors = ("red", "green", "blue")`. You can also create a tuple without parentheses by simply writing the values with commas, like `numbers = 10, 20, 30`. If a tuple has only one value, you must add a comma after it, like `single = (5,)`, otherwise Python will not recognize it as a tuple.

```python
# Defining a tuple using parentheses
colors = ("red", "green", "blue")
print("Colors tuple:", colors)

# Defining a tuple without parentheses
numbers = 10, 20, 30
print("Numbers tuple:", numbers)

# Defining a single-element tuple (note the comma)
single = (5,)
print("Single-element tuple:", single)

# Without a comma, Python does not recognize it as a tuple
not_a_tuple = (5)
print("Not a tuple, just an integer:", not_a_tuple)
```

Once a tuple is created, you can access its values by using their positions, which are called **indexes**. Indexes in Python start from `0`, meaning the first item is at position `0`, the second at position `1`, and so on. For example, if you have `fruits = ("apple", "banana", "cherry")`, you can get the first fruit by writing `fruits[0]`, which will return `"apple"`. 

Sometimes, you may want to take a part of a tuple instead of a single item. This is called **slicing**. You can do this by writing the starting and ending positions inside square brackets. If you have `numbers = (1, 2, 3, 4, 5)`, then `numbers[1:4]` will give you `(2, 3, 4)`. The first number in the brackets tells Python where to start, and the second number tells Python where to stop (but it does not include that position).

```python
# Defining a tuple
fruits = ("apple", "banana", "cherry")

# Accessing elements using indexes
print("First fruit:", fruits[0])  # Output: apple
print("Second fruit:", fruits[1]) # Output: banana
print("Third fruit:", fruits[2])  # Output: cherry

# Defining another tuple for slicing
numbers = (1, 2, 3, 4, 5)

# Slicing the tuple (from index 1 to 4, but excluding 4)
sliced_numbers = numbers[1:4]  # This will include elements at indexes 1, 2, and 3
print("Sliced tuple:", sliced_numbers)  # Output: (2, 3, 4)
```

Another useful thing about tuples is that you can store different types of values together. A tuple can contain numbers, text, or even a mix of both. For example, `person = ("Alice", 25, "Engineer")` keeps a name, an age, and a profession in one place.

You can also unpack a tuple, which means taking its values and assigning them to separate variables in one step. If you have `point = (3, 7)`, you can write `x, y = point`, and now `x` will be `3` and `y` will be `7`.

```python
# Defining a tuple with different types of values
person = ("Alice", 25, "Engineer")

# Accessing elements in the tuple
print("Name:", person[0])       # Output: Alice
print("Age:", person[1])        # Output: 25
print("Profession:", person[2]) # Output: Engineer

# Tuple unpacking
point = (3, 7)

# Assigning tuple values to separate variables
x, y = point

print("X coordinate:", x)  # Output: 3
print("Y coordinate:", y)  # Output: 7
```

Tuples are powerful tools that allow you to organize data efficiently while keeping it safe from accidental changes. They provide a structured way to store values, combine different pieces of data, compare elements, and iterate through them in an easy and efficient manner. 

### Problem Solving

You have two subgroups of delivery drones, each represented as a tuple of `(ID, location (x, y), battery level)`. Your tasks:
	1.	Use a function to combine the two subgroups into one tuple containing all drones.
	2.	Iterate through all drones and display their details.
	3.	Find the drone with the lowest battery (so it can be recharged).
	4.	Find the drone closest to a given target location for delivery using a manual distance formula.

#### Strategy

When solving a problem like coordinating drones using tuples, a structured approach helps break the problem into manageable steps. Here’s a simple problem-solving strategy you can use:

1.	Understand the Problem Clearly
	- Identify what information is given (e.g., drone ID, location, battery level).
	- Determine the required tasks (e.g., finding the lowest battery, nearest drone).
2.	Decide on a Data Structure
	- Since each drone has multiple attributes, a tuple is a good choice because it keeps related data together.
	- Use a tuple of tuples to store multiple drones.
3.	Break the Problem into Subtasks
	- Storing Data: Define tuples to represent individual drones and groups of drones.
	- Combining Data: Use functions to merge two drone groups.
	- Iterating Over Data: Use loops to go through each drone and analyze its attributes.
	- Knowing How to Calculate the Closest Distance Between Two Points: The distance between two points $(x_1, y_1)$ and $(x_2, y_2)$ can be found using the Euclidean distance formula: $d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$
	- Comparing Values: Find the drone with the lowest battery and the closest drone.
4.	Write Modular Code
	- Use functions to keep code organized (e.g., a function for combining tuples, another for calculating distance).
	- This makes the solution reusable and easy to modify.
5.	Test with Sample Data
	- Run the program with different drone locations and battery levels to verify results.

#### Solution

```python
# Function to combine two tuples of drones
def combine_drones(group1, group2):
    """Combines two groups of drones into a single tuple."""
    return group1 + group2  # Uses the + operator to merge the tuples

# Function to calculate Euclidean distance manually
def calculate_distance(loc1, loc2):
    """Calculates the Euclidean distance between two points (x1, y1) and (x2, y2)."""
    x1, y1 = loc1
    x2, y2 = loc2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5  # Square root of sum of squared differences

# Function to print all drones
def display_drones(drones):
    """Displays all drones with their location and battery level."""
    print("Drone Fleet:")
    for drone in drones:
        print(f"Drone {drone[0]} - Location: {drone[1]}, Battery: {drone[2]}%")

# Function to find the drone with the lowest battery
def find_lowest_battery_drone(drones):
    """Finds and returns the drone with the lowest battery."""
    lowest_battery_drone = drones[0]  # Assume the first drone has the lowest battery
    for drone in drones:
        if drone[2] < lowest_battery_drone[2]:  # Compare battery levels
            lowest_battery_drone = drone  # Update if a lower battery is found
    return lowest_battery_drone

# Function to find the closest drone to a given target location
def find_closest_drone(drones, target_location):
    """Finds and returns the drone closest to the target location."""
    closest_drone = drones[0]  # Assume the first drone is the closest
    closest_distance = calculate_distance(drones[0][1], target_location)

    for drone in drones:
        distance = calculate_distance(drone[1], target_location)
        if distance < closest_distance:  # If a drone is closer, update the best choice
            closest_drone = drone
            closest_distance = distance

    return closest_drone, closest_distance

# Main function to run the program
def main():
    """Main function to coordinate drones, find the lowest battery drone, and find the closest drone."""
    # Defining two groups of drones (each tuple contains: ID, location (x, y), battery level)
    drones_group1 = (
        ("D1", (10, 20), 80),
        ("D2", (5, 15), 60),
        ("D3", (12, 8), 90)
    )

    drones_group2 = (
        ("D4", (3, 5), 50),
        ("D5", (20, 10), 75),
        ("D6", (7, 7), 40)
    )

    # Combining the two drone groups using the function
    drones = combine_drones(drones_group1, drones_group2)

    # Display all drones
    display_drones(drones)

    # Find the drone with the lowest battery
    lowest_battery_drone = find_lowest_battery_drone(drones)
    print(f"\nDrone with the lowest battery: {lowest_battery_drone[0]} - Battery: {lowest_battery_drone[2]}%")

    # Define target location for delivery
    target_location = (10, 10)

    # Find the closest drone to the target location
    closest_drone, closest_distance = find_closest_drone(drones, target_location)
    print(f"\nBest drone for delivery to {target_location}: {closest_drone[0]} (Distance: {closest_distance:.2f})")

# Run the program
if __name__ == "__main__":
    main()
```

## Step 02: Lists

A list in Python is a collection of items stored in a specific order. It is similar to a tuple, but the key difference is that lists are **mutable**, meaning their contents can be changed after creation. This makes lists useful when you need a collection of values that may change over time, such as a list of names, numbers, or even a mix of different types.

A list is defined using square brackets `[ ]`, with elements separated by commas. For example, `numbers = [10, 20, 30, 40]` creates a list of four numbers, and `person = ["Alice", 25, "Engineer"]` creates a list containing a mix of text and numbers. Lists can also be empty, like `empty_list = []`. In contrast, a tuple is defined using parentheses `()`, such as `numbers_tuple = (10, 20, 30, 40)`. While both lists and tuples store multiple values, lists allow modifications, whereas tuples do not.


```python
# A list of numbers
numbers = [10, 20, 30, 40]

# A list of mixed data types
person = ["Alice", 25, "Engineer"]

# An empty list
empty_list = []
```

Like tuples, lists support indexing and slicing to access elements. For example, in `fruits = ["apple", "banana", "cherry", "date"]`, `fruits[0]` gives `"apple"`, while `fruits[2]` gives `"cherry"`. Slicing allows extracting part of a list, such as `fruits[1:3]`, which results in `["banana", "cherry"]`.
Negative indexing is supported both in lists and tuples. If `"apple"` has the index `0` then `fruits[-1]` returns `"date"` and `fruits[-2]` will result in `"cherry"`.

```python
fruits = ["apple", "banana", "cherry", "date"]

# Accessing elements using indexes
print(fruits[0])  # Output: apple
print(fruits[2])  # Output: cherry

# Negative indexing (counting from the end)
print(fruits[-1])  # Output: date

# Slicing (extracting a portion of the list)
print(fruits[1:3])  # Output: ['banana', 'cherry']

# Full slice (returns a copy of the entire list)
print(fruits[:])  # Output: ['apple', 'banana', 'cherry', 'date']

# Slice from the beginning up to index 3 (excluding index 3)
print(fruits[:3])  # Output: ['apple', 'banana', 'cherry']

# Slice from the beginning up to index 2 (excluding index 2)
print(fruits[:2])  # Output: ['apple', 'banana']
```


Since lists are mutable, you can modify their contents in various ways. Unlike tuples, lists allow direct modifications using indexing, and they can also be combined or repeated using mathematical operators.

One way to manipulate a list is by updating a value using an index (offset). Since each element in a list has a specific position, you can replace an existing value by assigning a new one to a particular index. For example, if you have `fruits = ["apple", "banana", "cherry", "date"]` and you want to change `"banana"` to `"blueberry"`, you can do so by writing `fruits[1] = "blueberry"`, which updates the second element of the list. This operation is not allowed in tuples, as they are immutable.


```python

fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"  # Replacing 'banana' with 'blueberry'
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']

fruits_tuple = ("apple", "banana", "cherry")
# TUPLES ARE IMMUTABLE
fruits_tuple[1] = "blueberry"  # TypeError: 'tuple' object does not support item assignment
```

Another way to manipulate lists is by extending them using the `+` operator, which joins two lists together to form a new list. If `list1 = [1, 2, 3]` and `list2 = [4, 5, 6]`, writing `combined_list = list1 + list2` results in `[1, 2, 3, 4, 5, 6]`. This operation does not modify the original lists but instead creates a new one containing elements from both.

Lists can also be multiplied using the `*` operator, which repeats their elements multiple times. If `numbers = [1, 2, 3]`, then `numbers * 3` produces `[1, 2, 3, 1, 2, 3, 1, 2, 3]`, where the original list is repeated three times in the new list.

```python
# Extending lists using the + operator
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Creating a new combined list
combined_list = list1 + list2

print("Original list1:", list1)  # Output: [1, 2, 3]
print("Original list2:", list2)  # Output: [4, 5, 6]
print("Combined list:", combined_list)  # Output: [1, 2, 3, 4, 5, 6]

# Multiplying a list using the * operator
numbers = [1, 2, 3]

# Creating a new repeated list
repeated_list = numbers * 3

print("Original numbers list:", numbers)  # Output: [1, 2, 3]
print("Repeated list:", repeated_list)  # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]
```

### Problem Solving

In a city, there are 20 ambulances stationed at different locations, each represented by its coordinates (x, y). Some ambulances are available, while others are occupied attending to other emergencies.

An incident has just occurred at a specific location, and we need to find the closest available ambulance to dispatch to the scene.

You are given:
	- A list of ambulance locations represented as tuples (x, y).
	- A corresponding list indicating availability, where True means the ambulance is available, and False means it is currently in use.
	- The incident location as a tuple (x, y).

Your task is to identify the closest available ambulance using the Euclidean distance formula and dispatch it to the incident. If no ambulances are available, print a message indicating that all are occupied.

#### Strategy

When solving a problem like finding the closest available ambulance using lists, it is important to follow a structured approach. Here’s a step-by-step strategy to tackle the problem efficiently:


1. Understand the Problem Clearly
	- Identify the inputs:
		- A list of ambulance coordinates representing their locations in the city.
		- A list of availability statuses indicating whether each ambulance is available or occupied.
		- A coordinate for the incident location where help is needed.
	- Determine the required output:
		- Find the closest available ambulance based on Euclidean distance.
		- If no ambulances are available, return a message saying all are occupied.


2. Choose the Right Data Structures
	- Use a list of tuples for ambulance locations, where each tuple represents an (x, y) coordinate.
	- Use a list of booleans for ambulance availability, where True means available, and False means occupied.
	- Store the incident location as a tuple (x, y).

3. Break the Problem into Subtasks: 
	- To make the solution modular and manageable, break it down into smaller subtasks:
		- Calculate the Distance: Use the Euclidean distance formula to measure how far an ambulance is from the incident location:
$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$
		- Implement a function that takes two coordinates and returns the computed distance.
	-	Find the Closest Available Ambulance
		- Iterate over the ambulance list while checking availability.
		- Compare the distances and keep track of the ambulance with the shortest distance.
	-	Return and Display the Result
		- If a closest available ambulance is found, print its location and distance.
		- If no ambulances are available, display an appropriate message.

4. Write Modular and Readable Code
	- Use functions for: Calculating distance, Finding the closest ambulance, Displaying the dispatch details, Wrap the logic inside a `main()` function for better organization.

5. Test with Sample Data
	- Try different incident locations and availability scenarios:
	- Cases where multiple ambulances are available.
	- Cases where only one ambulance is available.
	- Cases where all ambulances are occupied.


#### Solution

```python
import math

# Function to calculate Euclidean distance between two points
def calculate_distance(loc1, loc2):
    """Calculates the Euclidean distance between two coordinates (x, y)."""
    x1, y1 = loc1
    x2, y2 = loc2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Function to find the closest available ambulance
def find_closest_ambulance(ambulance_locations, ambulance_availability, incident_location):
    """Finds the closest available ambulance to the given incident location."""
    closest_ambulance = None
    closest_distance = float("inf")  # Initialize with a large value

    for i in range(len(ambulance_locations)):
        if ambulance_availability[i]:  # Check if the ambulance is available
            distance = calculate_distance(ambulance_locations[i], incident_location)
            if distance < closest_distance:
                closest_distance = distance
                closest_ambulance = ambulance_locations[i]

    return closest_ambulance, closest_distance

# Function to display the dispatch result
def dispatch_ambulance(closest_ambulance, distance, incident_location):
    """Prints the details of the closest available ambulance being dispatched."""
    if closest_ambulance:
        print(f"Dispatching ambulance at {closest_ambulance} (Distance: {distance:.2f}) to the incident at {incident_location}.")
    else:
        print("No available ambulances at the moment.")

# Main function to run the program
def main():
    """Main function to manage the ambulance dispatch process."""
    # Define a list of ambulance locations (x, y)
    ambulance_locations = [
        (2, 3), (5, 8), (12, 15), (7, 9), (20, 5), (3, 10), (18, 2), (8, 6),
        (10, 14), (14, 4), (6, 7), (15, 3), (11, 9), (9, 5), (4, 12), (13, 6),
        (17, 10), (1, 2), (16, 8), (19, 7)
    ]

    # Define availability status (True = available, False = occupied)
    ambulance_availability = [
        True, False, True, True, False, True, False, True,
        False, True, True, False, True, False, True, True,
        False, True, True, False
    ]

    # Define the incident location (x, y)
    incident_location = (10, 10)

    # Find the closest available ambulance
    closest_ambulance, distance = find_closest_ambulance(ambulance_locations, ambulance_availability, incident_location)

    # Display the dispatch result
    dispatch_ambulance(closest_ambulance, distance, incident_location)

# Run the program
if __name__ == "__main__":
    main()
```

## Step 03: Functions (more)?

Functions in Python allow us to pass inputs (arguments) to perform specific operations. These arguments provide flexibility by letting functions work with different values without modifying the function itself.

There are three main types of arguments in Python:

1. Positional Arguments: Values are assigned based on the order in which they are passed.
2.	Keyword Arguments: Values are assigned using parameter names, allowing arguments to be passed in any order.
3.	Default Values for Arguments: Parameters can have a default value, which is used if no argument is provided.

Using these types of arguments can make functions more readable, flexible, and easier to use. Let’s explore them with different examples.

```python
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

# Using positional arguments (order matters)
greet("Alice", 25)  
# Output: Hello, Alice! You are 25 years old.

# Using keyword arguments (order does not matter)
greet(age=30, name="Bob")  
# Output: Hello, Bob! You are 30 years old.
```

Sometimes one may need to assigne a default value for an argument of a function. A default value is a value assigned to a function parameter in case no argument is provided by the caller for it. This makes some parameters optional when calling the function. In the example provided below, since `age=18` is set as a default value, the function works even if age is not provided. This makes `age` an optional parameter, improving flexibility.

```python
def greet(name, age=18):
    print(f"Hello, {name}! You are {age} years old.")

# Calling the function with both arguments
greet("Alice", 25)  
# Output: Hello, Alice! You are 25 years old.

# Calling the function with only one argument (uses the default value for age)
greet("Bob")  
# Output: Hello, Bob! You are 18 years old.
```

Our next example presents mixing positional arguments, keyword arguments and default arguments to provide a flexible solution for ordering a pizza with default and custom toppings.

```python
def order_pizza(size, crust, topping="cheese"):
    print(f"Ordered a {size} pizza with {crust} crust and {topping} topping.")

# Using only positional arguments
order_pizza("large", "thin")  
# Output: Ordered a large pizza with thin crust and cheese topping.

# Using a mix of positional and keyword arguments
order_pizza("medium", "stuffed", topping="pepperoni")  
# Output: Ordered a medium pizza with stuffed crust and pepperoni topping.

# Using all keyword arguments
order_pizza(size="small", crust="thick", topping="mushrooms")  
# Output: Ordered a small pizza with thick crust and mushrooms topping.
``` 


### Problem Solving

A school wants to develop a student grade management system that:
	- Stores student information (name, subject, grades).
	- Keeps track of multiple students.
	- Process student data.
	- Provides an option for default values when retrieving student details.
	- Allows teachers to input multiple grades at once.
	- Includes docstrings to describe each function.

#### Strategy

To solve this problem efficiently and modularly, we need a clear plan that ensures the program is organized, flexible, and easy to maintain. 
The following strategy breaks down the problem into manageable steps:

1. Understand the Problem Clearly
- We need to store student details, including: Name (string), Subject (string), Grades (multiple values, unknown count).
- We should be able to: Add students dynamically, Handle multiple grades for each student, Calculate the average grade for a student, Display student details in a structured format, Allow optional parameters, such as choosing whether to display the subject.

2. Choose the Right Data Structures
- Tuples: Use for storing individual student records as (name, subject, grades).
- Lists: Use to store multiple student records.
- Functions: Use to modularize operations like adding students, calculating averages, and displaying details.
- *args: Use to allow flexible grade input.
- Default Values: Use to provide optional display customization.

3. Break the Problem into Subtasks: To keep the code clean and maintainable, we break it down into four key functions:
- `add_student(student_list, name, subject, *grades)`
	- Takes a student `name`, `subject`, and `grades` as input.
	- Stores the data in a tuple and adds it to the student list.
- `calculate_average(grades)`
	- Computes the average grade from a tuple of grades.
	- Returns `0` if no grades are provided (to avoid division errors).
- `display_student_info(student, include_subject=True)`
	- Displays a formatted student profile.
	- Uses default values to allow optional subject display.
- `main()`
	- Handles program execution, adding students, and displaying their information.


4. Implement the Solution in a Modular Way: Encapsulate logic into functions to avoid repetitive code, Use `main()` to control program flow, Use docstrings to explain each function.

5. Test with Sample Data: Add multiple students with different numbers of grades, Check edge cases, such as a student with no grades, Verify output formatting for clarity.



#### Solution

```python
def add_student(student_list, name, subject, *grades):
    """Adds a student to the list with their subject and grades.

    Args:
        student_list (list): The list that stores student records.
        name (str): The name of the student.
        subject (str): The subject the student is enrolled in.
        *grades (float): Variable number of grades for the student.

    Returns:
        None
    """
    student_list.append((name, subject, grades))


def calculate_average(grades):
    """Calculates and returns the average of a given set of grades.

    Args:
        grades (tuple): A tuple containing numeric grades.

    Returns:
        float: The average grade, rounded to 2 decimal places.
    """
    if not grades:  # Check if grades is empty
        return 0
    
    return round(sum(grades) / len(grades), 2)

def display_student_info(student, include_subject=True):
    """Displays a student's information, including their average grade.

    Args:
        student (tuple): A tuple containing (name, subject, grades).
        include_subject (bool, optional): Whether to display the subject. Defaults to True.

    Returns:
        None
    """
    name, subject, grades = student
    avg_grade = calculate_average(grades)

    print(f"Student: {name}")
    if include_subject:
        print(f"Subject: {subject}")
    print(f"Grades: {grades}")
    print(f"Average Grade: {avg_grade}\n")


def main():
    """Main function to manage student grades and display student details."""
    students = []

    # Adding students using *args to input multiple grades
    add_student(students, "Alice", "Math", 85, 90, 88)
    add_student(students, "Bob", "Science", 78, 82, 80, 79)
    add_student(students, "Charlie", "History", 92, 88)

    # Display all student records
    print("\nStudent Records:")
    for student in students:
        display_student_info(student)

    # Display student details without showing subject (using default value)
    print("\nDisplaying a student without subject info:")
    display_student_info(students[0], include_subject=False)


# Run the program
if __name__ == "__main__":
    main()

```

## Summary

This tutorial provided an introduction to fundamental data structures and key programming concepts in Python. It began by highlighting the importance of efficiently managing multiple values using Python’s collection structures, particularly lists and tuples. Tuples were covered first, emphasizing their immutability and suitability for storing fixed collections of items where data integrity was important. The tutorial then introduced lists as ordered, mutable collections that allowed duplicate elements.

The tutorial also explored functions. Various techniques for passing parameters were introduced. These concepts helped in writing reusable and scalable Python functions, making the code more efficient and readable.

