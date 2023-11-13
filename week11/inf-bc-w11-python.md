# Python 11: Structured Data Files

**Introduction**: This document presents learning steps for Python 11. In Python 10, you have learned how to manipulate plain text files, i.e. files containing unstructured contents. But, often in software projects we face data values with a specific structure, like csv file. In Python 11, you will get introduced with files that contains more structured data values.

**Note**: In this phase, it is expected the learner can divide the program into smaller learning steps. The goal and direction of the topics will be provided. The student must take smaller steps towards the goals such that can implement solutions to the given problems and product(s).


## Materials:

The activities are designed based on these following references:

- **BRef-01**: Book, Bill Lubanovic; "Introducing Python: Modern Computing in Simple Packages"; [Available here](https://www.oreilly.com/library/view/introducing-python-2nd/9781492051374/)
- **ORef-02**: Online Tutorial; Lucas Lofaro; "Working With JSON Data in Python"; [Available here](https://realpython.com/python-json/)
- **ORef-03**: Online Tutorial; Jon Fincher; "Reading and Writing CSV Files in Python"; [Available here](https://realpython.com/python-csv/)


## Path:

### Step: Tabular Text Files.

#### Goals:

```
After taking this step, you will be able to:
	1. interpret and implement Python programs using structured data files: reading / writing content from / to CSV / JSON files, processing / modifying content of CSV / JSON files.
```
#### What ro learn?

1. Using **BRef-01: Chapter 16**, **ORef-02** and **ORef-03** answer and experiment the following questions:
   1. What is a csv file? How can one read the content of a csv file?
   2. What is a JSON file? How can one read the content of a JSON file?
   3. Given a csv file, how can we process the records? Experiment with an example where:
	   - a specific term is being searched
	   - the values of specific attributes for some records are extracted.
	   - the values of specific attributes for some records are modified.
   4. Given a JSON file, how can we process the objects? Experiment with an example where:
	   - the values of specific attributes for some objects are extracted.
	   - the values of specific attributes for some objects are modified.

#### Exercises:

1. Design at least ten different exercises of your own. They should improve understanding topics of this step. Share your exercises with your learning group and practice.


<hr>

## Learning Activities:

### Code Analysis

There is a json file containing menu items of a resturant. An example of the content is given below.

```python
{
    "menu": {
      "breakfast": {
        "items": [
          {"name": "Pancakes", "price": 8.99},
          {"name": "Omelette", "price": 9.99},
          {"name": "French Toast", "price": 7.49}
        ]
      },
      "lunch": {
        "items": [
          {"name": "Caesar Salad", "price": 10.99},
          {"name": "Chicken Wrap", "price": 12.49},
          {"name": "Vegetarian Pizza", "price": 14.99}
        ]
      },
      "dinner": {
        "items": [
          {"name": "Grilled Salmon", "price": 18.99},
          {"name": "Steak with Potatoes", "price": 22.99},
          {"name": "Pasta Alfredo", "price": 15.99}
        ]
      }
    }
}
```

Students are asked to implement a program that inquires about the mealtime and prints items from the menu corresponding to the provided input. One of the solutions is provided below. The program raises an exception. Read the program, analyze the structure of the JSON file and help the student to solve the issue.

```python
import json

class MenuManager:
    def __init__(self, file_path):
        self.menu_data = self.load_menu(file_path)

    def load_menu(self, file_path):
        with open(file_path, 'r') as file:
            menu_data = json.load(file)
        return menu_data

    def display_meal_items(self, meal_time):
        try:
            items = self.menu_data["menu"]["items"]
            print(f"\n{meal_time.capitalize()} Menu:")
            for item in items:
                print(f"{item['name']}: ${item['price']:.2f}")
        except KeyError:
            print(f"\nNo menu found for {meal_time.capitalize()}.")

if __name__ == "__main__":
    file_path = "menu_data.json" 
    menu_manager = MenuManager(file_path)

    user_input = input("Enter the meal time (breakfast, lunch, or dinner): ")
    menu_manager.display_meal_items(user_input)
```

### Supporting Topics

**Introduction**: Relational Databases:

In general, a database is a structured and organized collection of data that is easily accessible, manageable, and updateable. Databases are designed to store and retrieve information efficiently. They provide a systematic way to organize and manage data, allowing users to interact with and manipulate information. A relational database is a type of database that stores and organizes data in tables. In a relational databases, data is structured in tables, where each table represents a specific entity or concept, and relationships between tables are defined to establish connections between different pieces of data.
 
Example: A simple **Students** table:

| StudentID | FirstName | LastName | Age | Grade |
|-----------|-----------|----------|-----|-------|
| 1         | John      | Doe      | 20  | A     |
| 2         | Jane      | Smith    | 22  | C     |
| 3         | Mike      | Johnson  | 21  | B     |

**Activity**:
- Provide a JSON file that contains the information provided in the example table above.
- As can be seen, a JSON file can also provide the same structure and data content as a table in a relational database. Conduct a small research and justify the benefits of (relational) databases over (structured) files.

**Note**: This is just a short prepatory activity about databases. More in-depth learning activity will be provided in the coming weeks.
