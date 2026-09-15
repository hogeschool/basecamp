# Python 07: Functions and Collective Structures — werkblad

> Vragen uit [week 7 voorbereiding.md](./week%207%20voorbereiding.md). Vul je antwoord onder elke vraag in.

---

## Step-01: Functions (more)

### What to Learn

*Using **BRef-01: Chapter 09** answer and experiment the following questions*

#### 1. What are *namespace* and *scope*? What is the scope of a function? Use examples to justify your answers.


#### 2. What is a `global` variable? What is a `local` variable?


#### 3. Often implementing your solutions you may need to use some important built-in functions: `map(...)` and `filter(...)`. Study them first [here](https://www.brianheinold.net/python/python_book.html#section_map_filter_reduce) and practice a few small examples to understand how they work and when you might need them.


### Exercises

#### Oefening 1. Check the following code. Identify global variables and local variables. What do you expect to be printed? Modify the function to make it use the global x instead of the local x.

```python
x = 10 

def my_function():
    x = 5  
    print("Inside the function, x =", x)

my_function()
print("Outside the function, x =", x)
```


#### Oefening 2. Complete the function that checks if the items in a given list are `True` for the given lambda. Return a list containing all `True` values.

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


#### Oefening 3. There is a list of names given below.

1. Using `filter(...)`, write a program that provides a list containing the name(s) with more than 5 characters. 
  2. Using map(...), implement a program that converts all the names in the list to uppercase.

```python
names = ["Mia", "Alex", "Sarah", "Benjamin", "Eve", "Christopher", "Leo", "Isabella", "Max", "Jonathan"]
```


#### Oefening 4. Design two exercises of your own. They should improve understanding topics of this step.


---

## Step-02: Tuples and Lists (more)

### What to Learn

*Using **BRef-01: Chapter 07** answer and experiment the following questions*

#### 1. We have learned *join()* on a string. How does *join()* work in a list?


#### 2. How can we sort items of a list? Is this possible on a tuple?


#### 3. There are several ways to copy a list: *list(), slicing, copy()* and *deepcopy()*. Experiment different expamples for each technique.


#### 4. How can one build a list using *list comprehension* (for more check [here](https://www.brianheinold.net/python/python_book.html#section_list_comp))? Do we have *tuple comprehension*?


### Exercises

#### Oefening 1. The method `list.sort()` sorts a list ascending. Look up how to sort descending and try it.


#### Oefening 2. Create a list containing at least three `tuples` containing some numbers. Print the last item of each tuple by looping through the list.


#### Oefening 3. Complete the function that returns a list containing all the values from all tuples in the given list.

```python
def create_list_from_tuples(a):
    #write the code

l = [(1,5,4),(1,2),(8,5,19,0)]
print(create_list_from_tuples(l))
#[1,5,4,1,2,8,5,19,0]
```


#### Oefening 4. Take the list of tuples from the previous exercise. Sort the list ascending on the last item of each tuple.


#### Oefening 5. Create a loop that creates a list containing tuples with the numbers 1 to 10 in pairs of 2. The result should be `[(1,2),(3,4),(5,6),(7,8),(9,10)]`.


#### Oefening 6. Take the list from the previous exercise. Remove the tuples in which the first item is an odd number. Use a lambda to determine this.


#### Oefening 7. Design two exercises of your own. They should improve understanding topics of this step.


---

## Step-03: Dictionaries and Sets (more)

### What to Learn

*Using **BRef-01: Chapter 08** answer and experiment the following questions*

#### 1. How do *copy()* and *deepcopy()* behave on dictionaries? What about sets?


#### 2. How does *dictionary comprehension* work? What about sets?


#### 3. Try to build the following nested structures

- List of lists.
- Tuple of lists.
- Tuple of tuples.
- List of tuples


### Exercises

#### Oefening 1. Complete the function to merge two lists into one dictionary.

```python
def merge_lists_into_dictionary(l1, l2):
    #write the code

keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']
result = merge_lists_into_dictionary(keys, values)
print(result) #{'red': '#FF0000', 'green': '#008000', 'blue': '#0000FF'}
```


#### Oefening 2. Given is a list of dictionaries. Sadly the values are the wrong way around. The first value should be at the last key, second value at the second from last key, and so on. Create a function that switches these values for each list you could give it.

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


#### Oefening 3. Given is a dictionary with tuples. Complete to code to add all keys, at which the second Tuple value is Pass, to a list and return that list

```python
def create_pass_list(l):
    #Write the code

x = {'Math':(81,"Pass"), 'Physics':(50,"Fail"), 'Chemistry':(90,"Pass"), 'English': (42,"Fail")}
print(create_pass_list(x))
#["Math", "Chemistry"]
```


#### Oefening 4. Based on the previous exercise. Write a new function that creates a list with failed subjects. Merge the two lists into a new dictionary with the correct keys. Result should be: `{'Pass':["Math", "Chemistry"], 'Fail':["Physics","English"]}`.


#### Oefening 5. Write a function that takes the dictionary from the previous exercise and turns each value into his own key:value pair. Sort the dictionary by the key. The result should be: `{'Chemistry': 'Pass', 'English': 'Fail', 'Math': 'Pass', 'Physics': 'Fail'}`;


#### Oefening 6. Test all the functions from the last few exercises if they still work given a different starting dictionary. If not, try to explain what went wrond and fix it.

A different dictionary could be:
`{'Soccer':(9, "Pass"), 'Snowboarding':(3, "Fail"), 'Tennis':(7, "Pass")}`.


#### Oefening 7. Design two exercises of your own. They should improve understanding topics of this step.



