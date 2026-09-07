# A1W3A2 — Mountain climbing time trail

| | |
|---|---|
| **Code** | `A1W3A2` |
| **CodeGrade** | https://app.codegra.de/courses/21582/assignments/455958 |
| **Available** | 2026-08-31 |
| **Deadline** | 2027-01-08 23:59 (CET) |

---

**Note: make a flow chart or pseudo code for A1W3A1 before starting this assignment!**

A mountain sports organization is conducting a speed climbing event where participants can begin their ascent at any time they choose. Your task is to develop a Python program that tracks participant information, calculates climbing durations, and reports competition results.

Your program must:

- Prompt for each participant’s **first name** and **last name**.
- Request their **start time** and **end time** in `HH:MM` format.
- Compute the **total climbing time** in minutes.
- Validate all user input using dedicated functions.
- After each participant, show a **live summary**:
  - Their total climb time in `HH:MM`
  - Whether they were **faster or slower than the average** up to that point
- Continue collecting entries until the user indicates there are no more participants.
- At the end, display:
  - The **fastest climber**
  - The **total number of participants**
  - The **average climbing time** in `HH:MM` format

---

### Program Requirements:

- **First name**:

  - Must consist solely of alphabetic characters
  - Must be between 2 and 10 characters in length
  - Must begin with an uppercase letter
  - Validate using the function: `is_first_name_valid(name: str) -> bool`

- **Last name**:

  - Must consist solely of alphabetic characters
  - Must be between 2 and 20 characters in length
  - Is allowed to have spaces, and the following chars `',', '-', '/'`
  - Validate using the function: `is_last_name_valid(name: str) -> bool`

- **Time entries** (`HH:MM` format):

  - Must follow the `HH:MM` format **with leading zeros** (e.g. `09:05`, not `9:5`)
  - Hours must be in the range 00–23
  - Minutes must be in the range 00–59
  - Validate using the function: `is_time_valid(time_str: str) -> bool`

- The climbing **duration must be between 10 minutes and 3 hours**.

  - Use a function `is_duration_valid(start: int, end: int) -> bool` to check this.

- The start time must chronologically precede the end time, same day only.

- If any input is invalid, display `Input error` and prompt again.

- After each participant input, show:

  - Their climbing duration in `HH:MM`
  - A message indicating if this was faster or slower than the current average

- After all data is collected, output a summary report as shown below.

### Implementation Notes:

- Use a `while` loop to process entries for multiple participants.
- Define helper functions to perform input validation.
- Convert start and finish times to total minutes using: total minutes = number of hours * 60 + number of minutes For example: Start time = 08:30, start_minutes = 8 * 60 + 30
- Calculate duration using: `duration = finish_minutes - start_minutes`
- Duration must be between 10 and 180 minutes (3 hours).
- Keep track of total time and fastest time using basic variables (no lists).
- If you know the total number of climbers and the total time, you can calculate the average climbing time by dividing the total time by the number of climbers.
- After each participant, update and compare the average to show a dynamic report.

---

### Sample Scenario:

#### Input:
```
> First name? Anna
> Last name? Keller
> Start time? 09:15
> Finish time? 10:05
```
#### Intermediate output:
```
Anne Keller did it in 00:50
This participant is currently faster than the average.
```

#### Input:
```
> New participant? (Yes or No): Yes
> First name? Liam
> Last name? Brooks
> Start time? 08:00
> Finish time? 08:45
```
#### Intermediate output:
```
Liam Brooks did it in 00:45
This participant is currently faster than the average.
```
#### Input:
```
> New participant? (Yes or No): No
```

### Final Output:

```
Fastest participant: Liam Brooks (00:45)
Total participants: 2
Average time: 00:47
```

---

### Sample Input With Errors:

#### Input:
```
> First name? jo
```
#### Intermediate output:
```
Input error
````

#### Input:
```
> First name? Jo
> Last name? van der Meer3
```

#### Intermediate output:
```
Input error
```

#### Input:
```
> Last name? van der Meer
> Start time? 8:30
```
#### Intermediate output:
```
Input error
```

#### Input:
```
> Start time? 08:30
> Finish time? 08:15
```
#### Intermediate output:
```
Input error
```
#### Input:
```
> Start time? 08:30
> Finish time? 09:05
```
#### Intermediate output:
```
Duration: 00:35
This participant is currently faster than the average.
```

#### Input:
```
> New participant? (Yes or No): No
```

### Sample Output With Errors:

```
Fastest participant: Jo van der Meer (00:35)
Total participants: 1
Average time: 00:35
```
