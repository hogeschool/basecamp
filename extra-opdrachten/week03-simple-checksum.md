# Extra opdracht — Simple checksum

> Omgezet uit `Week 3 - Simple checksum assignment from Analysis (1).docx`.
> Het origineel staat in [`lesmateriaal/week03/Additional lesson material`](../lesmateriaal/week03/Additional%20lesson%20material).
> Dit is het lege format van de opleiding — invullen doe je zelf.

---
Simple checksum

formative assignment

# Problem introduction

Humans are prone to make mistakes. When dealing with numbers, especially with long sequences of numbers, we may accidentally miss a digit, duplicate another, swap the order of adjacent digits, and so on. In some cases, those mistakes could be much more costly than the others. For example, if you add 0 by mistake when paying your rent, it could alter the total from 1000 € to 10000 €). Or if you want to transfer some money from your account to another and you mistype one digit, your money could end up with a complete stranger.

Fortunately, there are fail-safes, to prevent, or at least minimize such occurrences, and those are often used in computing for error detection. One of those is checksum, which is a calculated value used to determine the validity of data.

In this assignment, you will experiment with a very simple checksum, that won’t be able to detect many mistakes, yet is easy to implement, and will be used to illustrate the concept. Let N be a number containing d digits. The first d-1 digits represent a numerical value important to us (e.g. the account number), while we reserve the last digit d as the check digit. In our case, this check digit will be the remainder of the sum of all d-1 digits, divided by 10.

For example: 1236. This number has 4 digits, such that the sum of the first d-1 digits, 1 + 2 + 3 = 6, divided by 10, gives the remainder equal to the last, check digit 6 (6 / 10 = 0 R 6).

Similarly, 9876549 would also be a valid number, as 9 + 8 + 7 + 6 + 5 + 4 = 39, divided by 10, is 3 and the remainder 9 (3 R 9), which is equal to the check digit 9.

Alternatively, 1234 would not be correct, as 1 + 2 + 3 = 6, mod 10 = 6, ≠ 4. In the same manner, 9876559 would be invalid, as 9 + 8 + 7 + 6 + 5 + 5 = 40, divided by 10, is 4 and the remainder 0 (4 R 0), which is not equal to the check digit 9.

# Problem statement

Ask the user to input a numerical value (positive integer), and using a simple checksum described above, determine if it is valid or invalid. Print “VALID” (all capitals) if the input is valid, or print “INVALID” (all capitals) otherwise.  No output other than “VALID” or “INVALID” should be given; this also applies to the input() statement.

You can assume that the input is always going to be an integer, hence, no type checking is needed.

**Example input and output:**

Input is given in BLUE. Required output is given in RED.

Case 1:

## 123456786

## VALID

Case 2:

## 123456789

## INVALID

Case 3:

## 123

## VALID

Case 4:

## 321

## INVALID

Case 5:

## 12

## INVALID
