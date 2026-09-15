# Extra oefeningen week 2 (uit Analysis 2)

> Omgezet uit `Week 2 - Exercises from Analysis 2 - fits week 2.docx`.
> Het origineel staat in [`lesmateriaal/week02/Additional lesson material`](../lesmateriaal/week02/Additional%20lesson%20material).
> Dit is het lege format van de opleiding — invullen doe je zelf.

---
Exercises 4

## Branching algorithms

Problem 4-1: division test

Problem 4-2: two digit number

Problem 4-3: division by zero

Problem 4-4: conditional sum

Problem 4-5: analysis lessons

Problem 4-6: year end bonus

Problem 4-7*: prize money

Problem 4-8: green lantern

Problem 4-9*: evaluating teacher

## Problem 4-1: division test

Read one number from the standard input. Then print “:)” if the number is divisible by 5. Otherwise, print “:(”

## Problem 4-2: two digit number

Read one number from the standard input. Check if it is a two digit number and print “TRUE” if it is, or print “FALSE” if it is not.

## Problem 4-3: division by zero

Ask the user to input two numerical values, A and B. Then find C such that C = A / B, and print it to the standard output. If the user enters 0 for B, don’t calculate C. Instead, write an error message that division by zero is not allowed.

## Problem 4-4: conditional sum

Ask the user to input three numbers A, B and C. Find out the sum of all the even numbers. (e.g. 1, 2, 3 → 2;   2, 3, 4 → 2 + 4 = 6;   2, 8, 10 → 2 + 8 + 10 = 20;   1, 3, 5 → 0)

## Problem 4-5: analysis lessons

The course of Analysis 1 consists of 12 lessons, 6 theoretical and 6 practical. During 6 teaching weeks, two lessons per week are given, always starting with the theoretical and then followed by the practical lesson. Therefore, in week 1, lessons 1 and 2 are given; in week 2, lessons 3 and 4 are given; in week 3, lessons 5 and 6 are given; and so on … where lessons 1, 3, 5, … are theoretical and lessons 2, 4, 6, … are practical.

You task it to design an algorithm that will input the lesson number (integer 1-12). If the number is not valid, you should output the appropriate message (e.g. “invalid input”). For valid lesson number, print in which week the lesson is given and is it a theoretical or a practical one.

## Problem 4-6: year end bonus

Your company wants to calculate the bonuses of employees. Bonus is related to gross annual salary of each employee. For those employees who earn below 30.000 per year bonus will be 10%, for those between 30.000 and less than 40.000 will be 12%, between 40.000 and less than 55.000 will be 14% and for all others will be 15%. For any given employee’s salary, the program should calculate the exact amount of end-year bonus.  Design the algorithm, create the flowchart, test all conditions and implement it in Python.

## Problem 4-7*: prize money

Three Informatica students are representing Hogeschool Rotterdam on an international programming competition. Each of the three students is getting a score that can be any whole number in the interval [0 - 5], and the total points the team gets is the sum of all three scores. The prize is directly dependant on the total score. If the team gets more than 10 points, then the prize is two times the product of their scores. If not, then the prize is just the product of their scores.

The students have decided to split the prize money in the following way: if the prize is divisible by 3, they all get the same share. Otherwise, they get the proportion equal to their contribution in the sum of all scores (e.g. 2 + 3 + 8 = 13; 13 is not divisible by 3; the first gets 2/13 of the prize, the second 3/13 of the prize, the third 8/13 of the prize).

Design an algorithm that will ask the user to input three scores of the students, then print out the total prize money, and how much money should each student get.

## Problem 4-8: green lantern

The Green Lantern's ring is searching the Earth for a new candidate to recruit into the Corps. When it finds a new candidate, it will check the gender (use standard input: ‘m’ for male and ‘f’ for female). If the candidate is a male, the ring will look for age and weight. If it is a female, the ring will look for age and height. To recruit the candidate into the Corps, a male must be younger than 40, and his weight must not be over 80. For female candidates, she must be over 20 years of age and taller than 160.

Design an algorithm that will check the gender of the candidate. Then, depending on the outcome, input the needed values and make the decision whether to recruit or not.

## Problem 4-9*: evaluating teacher

The students are evaluating their teacher with the grade [1 - 10]. If the teacher scores 10, then (s)he is EXCEPTIONAL. If the teacher scores [7-9], then (s)he is GOOD. For grades in interval [4-6], the teacher is AVERAGE. If the teacher scores 3 or less, then (s)he is bad.

Make an algorithm that will input the score and the salary for the teacher. Then, check if the score is valid (in range [1-10]) and if not, print that the input is wrong. Otherwise, print what kind of a teacher (s)he is, update and print the salary according to the following formula:

Exceptional teacher gets 15% raise.

Bad teachers have his / her salary reduced to 85%.

Every other type of teacher gets the raise in percentage equivalent to his / her score (e.g. grade 8 means 8% increase, grade 4 means 4% increase, …)
