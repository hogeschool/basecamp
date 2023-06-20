# Python 15: Recursive Functions.

**Introduction**: This document presents learning steps for Python 15. In Python 15, you will learn and practice recursive functions in Python. Recursive functions are the functions that call themselves. In majority of cases, you may implement a solution, non-recursively. There are cases that the definition is naturally recursive. In these cases, recursive functions can be easier to implement.

**Note**: In this phase, it is expected the learner can plan and run required learning process towards the goals of the week: making solutions to the given problems and product(s).

## Materials:

The activities are designed based on these following references:

- **BRef-01**: Book, Bill Lubanovic; "Introducing Python: Modern Computing in Simple Packages"; [Available here](https://www.oreilly.com/library/view/introducing-python-2nd/9781492051374/) 

- Free research.


## Path:

#### Goals:

```
After taking this step, you will be able to:
	1. understand recursive functions.
```
#### What to learn?

**Note:** If this is the first time that you try recursion, it is very cruccial to start with small steps, small examples, seeing more samples and trying yourself. It will take time to feel confident in writing a solution recursively. Be patient.

1. Using **BRef-01, Chapter 9 (Section: Recursion)** make a plan for the week to learn basics of recursive functions in Python.
	- Make an overview of the provided problems and final product.
	- Plan what you need to learn in order to provide your solutions.
	- Read proposed book chapter and practice basic provided examples.
	- Read [this resource](https://www.pythontutorial.net/python-basics/python-recursive-functions/) and run provided examples.
	- Watch [this video](https://www.youtube.com/watch?v=m1Fjdnj_Mds). 

<hr>

## Exercises:

1. Play [Tower of Hanoi](https://webgamesonline.com/towers-of-hanoi/).
2. From elementary school we know $5^3=5 \times 5 \times 5$. But, we can also define it recursively: $5^3 = 5 \times 5^2$. Or in general we can define the concept of $m^n$ recursively: $m^n=m \times m^{(n-1)}$. Check the implementation below. Try the code. There is something missing which makes it incorrect. Fix the implementation.

```python
    def rec_power(m:int,n:int)->int:
        '''
        The function implements m to the power of n, recursively.
        '''
        return m*rec_power(m,n-1)
```  

<hr>

## Learning Activities:

### Code Analysis
[todo]

### Supporting Topics
[todo]