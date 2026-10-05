# GenAI Prompting for Learning Programming

## Introduction

Generative AI (GenAI) tools can be useful while learning programming. They can explain concepts, provide examples, help you understand error messages, ask you questions, and give feedback on your reasoning.

However, using GenAI effectively for learning is different from simply asking it to produce an answer.

Consider these two prompts:

> Write a Python program that checks whether a string contains a character.

and:

> Act as my programming tutor. I am learning Python and currently studying loops and conditional statements. Help me understand how I could determine whether a given string contains a specific character. Guide me step by step and ask me questions before showing a complete solution.

Both prompts concern the same programming problem, but they give GenAI very different roles.

In the first case, GenAI is mainly being used as an **answer generator**.

In the second case, GenAI is being used as a **learning assistant**.

In this tutorial, we focus on the second approach.

---

## Learning Objective

After completing this tutorial, you should be able to write prompts that use GenAI as a **learning assistant or tutor** rather than simply as an answer generator.

You will learn how to:

1. explicitly define the role of GenAI;
2. provide relevant context about what you are learning;
3. clearly describe your learning goal;
4. specify how GenAI should help you;
5. improve a prompt through follow-up questions;
6. critically evaluate GenAI responses;
7. verify important information using textbooks, course materials, documentation, and other reliable sources.

The most important principle is:

> **GenAI can support your learning, but it should not replace your own thinking or reliable learning resources.**

---

# 1. What Is a Prompt?

A **prompt** is the instruction or question that you give to a GenAI system.

A prompt can be very simple:

> What is a Python list?

Or it can provide much more information:

> Act as my programming tutor. I have just started learning Python and I understand variables, but I am new to lists. Explain Python lists using a simple example. Then give me a small exercise to check whether I understood the concept. Do not give me the solution until I attempt the exercise.

The second prompt gives GenAI much more information about:

- its **role**;
- your **current knowledge**;
- your **learning goal**;
- how you want to learn;
- what kind of response you expect.

This usually produces a response that is more useful for learning.

---

# 2. Start by Giving GenAI a Role

When using GenAI for studying, explicitly tell it that its role is to support your learning.

For example:

> Act as my programming tutor.

Or:

> Act as a learning assistant helping me understand introductory Python programming.

This simple instruction is important because it establishes the purpose of the conversation.

You are not asking GenAI to **do your work for you**. You are asking it to **help you learn how to do the work yourself**.

You can make the role even more specific:

> Act as my programming tutor. Help me reason about problems instead of immediately giving me the final answer.

Or:

> Act as my Python tutor. When I make a mistake, explain what is wrong and help me discover the correction myself.

---

# 3. Give Relevant Context

GenAI does not automatically know what you have already learned in your course.

Providing some context helps it adjust its explanation to your level.

Compare:

> Explain functions.

with:

> Act as my programming tutor. I am learning Python. I already understand variables, `if` statements, and loops, but functions are new to me. Explain why we need functions before explaining how to define one.

The second prompt tells GenAI what knowledge it can build upon.

Useful context might include:

- the programming language you are studying;
- the topic you are currently learning;
- concepts you already understand;
- concepts you have not learned yet;
- the difficulty you are experiencing.

For example:

> Act as my programming tutor. I am learning Python and currently studying `for` loops. I understand variables and `if` statements, but I still find nested loops confusing.

Now GenAI has a much better idea of where to start.

---

# 4. State Your Learning Goal

Tell GenAI what you want to **learn**, not only what task you want to complete.

Instead of:

> Solve this Python exercise.

try:

> Act as my programming tutor. I want to learn how to solve this type of problem myself. Help me identify the important parts of the problem and decide which Python concepts I might need.

The difference is subtle but important.

Your objective is not:

**"How can GenAI finish this task?"**

Your objective should be:

**"How can GenAI help me become able to finish this task myself?"**

For example:

> I want to understand how a loop can be used to find the largest value in a list. Guide me through the reasoning before discussing the code.

This makes your **learning goal** explicit.

---

# 5. Tell GenAI How You Want It to Help

You can control how much assistance GenAI provides.

For example, you might ask it to:

- explain something step by step;
- use a simple example;
- give you a hint;
- ask you questions;
- create a practice exercise;
- review your reasoning;
- explain an error;
- compare two approaches;
- wait for your attempt before showing a solution.

For example:

> Act as my programming tutor. I am learning Python loops. Give me a small exercise involving a `while` loop. Let me attempt it first. Do not provide the solution unless I ask for it.

Another useful approach is asking GenAI to use questions:

> Act as my programming tutor. Help me solve this problem by asking me one question at a time. Do not immediately give me the solution.

This turns the interaction into a learning conversation rather than a simple question-and-answer session.

---

# 6. Build a Good Learning Prompt

A useful starting structure is:

**Role + Context + Learning Goal + Instructions**

For example:

> **Role:** Act as my programming tutor.
>
> **Context:** I am learning introductory Python. I understand variables and conditional statements, and I am now learning loops.
>
> **Learning goal:** I want to understand when and why a `while` loop should be used.
>
> **Instructions:** Explain it using a simple example. Ask me a question afterward to check my understanding. Do not immediately give me the answer if I make a mistake; first give me a hint.

You do not always need to write these headings. A normal prompt can contain the same information:

> Act as my programming tutor. I am learning introductory Python. I understand variables and conditional statements, and I am now learning loops. Help me understand when and why a `while` loop should be used. Use a simple example and then ask me a question to check my understanding. If I make a mistake, first give me a hint instead of immediately giving me the answer.

---

# 7. Prompting Is a Conversation

You do not need to create a perfect prompt in one attempt.

A powerful way to use GenAI is to **refine the conversation**.

Imagine that GenAI explains Python functions, but you still do not understand the explanation.

You can continue with:

> I don't understand why we need parameters. Explain that part again with a simpler example.

Then:

> Show me what happens when the same function is called with two different arguments.

Then:

> Give me a small exercise where I have to define the parameter myself.

Then:

> Here is my solution. Review it as my tutor. Do not rewrite the whole program. Tell me what I should investigate first.

Each prompt builds on the previous interaction.

This process is sometimes called **iterative prompting**: improving and refining the interaction step by step.

---

# 8. Use GenAI to Understand Errors

Programming errors are valuable learning opportunities.

Suppose your program contains:

```python
numbers = [2, 4, 6, 8]

for i in range(len(numbers)):
    print(numbers[i + 1])
```

Instead of asking:

> Fix my code.

you could ask:

> Act as my programming tutor. The code above produces an error. Help me understand why the error occurs. Do not immediately provide corrected code. First explain what Python is doing during each iteration and ask me to identify where the problem occurs.

This encourages you to understand the cause of the error rather than simply copying a correction.

After attempting the problem yourself, you can ask:

> I think the problem happens during the last iteration because `i + 1` refers to an index that does not exist. Is my reasoning correct?

Now GenAI can provide feedback on **your reasoning**.

---

# 9. Ask GenAI to Challenge You

GenAI does not always have to explain something to you. It can also help you **practise and test your understanding**.

For example:

> Act as my Python tutor. I have just studied lists and loops. Give me three small questions, one at a time, that gradually become more difficult. Do not give me the answer until I submit my attempt.

You can also ask GenAI to evaluate your own explanation:

> I will explain how a `for` loop works in my own words. Act as my programming tutor and identify anything that is incorrect or incomplete.

Explaining a concept yourself can be an effective way to discover gaps in your understanding.

---

# 10. GenAI Can Be Wrong

There is an important limitation you must always remember:

> **A confident GenAI answer is not necessarily a correct answer.**

GenAI can:

- make factual mistakes;
- generate code that does not work;
- misunderstand your question;
- use functions or libraries incorrectly;
- provide outdated information;
- invent references or details;
- give explanations that sound convincing but are inaccurate.

Therefore:

> **Do not treat GenAI as an authoritative source.**

This is especially important when you are learning something new because you may not yet have enough knowledge to recognize an incorrect answer.

---

# 11. Verify Important Information

An important part of working with GenAI is **verification**.

Suppose GenAI tells you:

> Python lists are immutable.

**You should not accept the statement simply because GenAI generated it.
Check it against a reliable source.**

For programming courses, useful verification sources include:

1. the textbook used in your course;
2. lecture slides and course materials;
3. official programming-language documentation;
4. official documentation of the library or framework being used;
5. reliable sources recommended by your teacher.

You can also test programming claims yourself.

For example:

```python
numbers = [10, 20, 30]
numbers[0] = 100

print(numbers)
```

Run the program and observe what happens.

The result provides evidence that helps you evaluate the claim about Python lists.

Verification is therefore not something separate from learning programming. **Testing claims with code can itself be part of the learning process.**

---

# 12. Ask GenAI What Should Be Verified

GenAI itself can help you identify claims that deserve checking.

For example:

> Act as my programming tutor. Explain Python dictionaries. At the end, identify the important technical claims in your explanation that I should verify using my textbook or the official Python documentation.

However, there is an important rule:

> **Asking GenAI to verify its own answer is not independent verification.**

For example:

> Are you sure?

may cause GenAI to reconsider its answer, but it does not prove that the answer is correct.

Real verification requires comparison with **independent and reliable sources**.

---

# 13. A Practical Prompting Pattern

When studying programming, you can use the following pattern as a starting point:

> **ROLE**  
> Act as my programming tutor and learning assistant.
>
> **CONTEXT**  
> I am studying [topic].  
> I already understand [previous knowledge].  
> I am having difficulty with [specific difficulty].
>
> **LEARNING GOAL**  
> I want to understand [concept or skill].
>
> **HOW TO HELP ME**  
> Explain the concept step by step.  
> Use simple programming examples.  
> Ask me questions to check my understanding.  
> Give hints before giving complete solutions.
>
> **VERIFICATION**  
> Clearly identify important technical claims that I should verify. I will compare important information with my textbook, course materials, official documentation, or other reliable sources.

You can adapt this structure depending on what you are studying.

---

# 14. Example: From a Weak Prompt to a Learning Prompt

Suppose you receive the following programming exercise:

> Write a program that finds the largest number in a list.

A weak prompt would be:

> Solve this.

GenAI will probably produce some code. You may finish the exercise quickly, but you may learn very little.

A better prompt would be:

> Act as my programming tutor. I am learning Python loops and lists. I need to write a program that finds the largest number in a list, but I want to develop the solution myself.
>
> Do not give me the complete code yet. Help me break the problem into smaller steps. Ask me one question at a time and give me hints if I get stuck.

After developing your solution, you could continue:

> Now review my solution. Identify any mistakes and explain why they are mistakes. Do not replace my solution unless necessary.

Finally:

> Identify the Python concepts in your feedback that I should verify in my textbook or the official Python documentation.

This interaction uses GenAI to support the **learning process**, rather than replacing it.

---

# 15. Think, Ask, Evaluate, Verify, Learn

A useful workflow for studying with GenAI is:

### 1. THINK

First think about the problem yourself.

- What do you already know?
- What exactly is confusing?
- What have you already tried?


### 2. ASK

Give GenAI a clear:

- **role**;
- **context**;
- **learning goal**;
- **instruction for how it should help you**.


### 3. INTERACT

Use the conversation actively.

- Ask questions.
- Request examples.
- Attempt exercises.
- Explain your own reasoning.
- Ask for hints when needed.


### 4. EVALUATE

Do not automatically accept the response.

Ask yourself:

- Does the explanation make sense?
- Does the code actually run?
- Does it agree with what I have learned?
- Are there claims that I am unsure about?


### 5. VERIFY

Check important information using:

- your textbook;
- course materials;
- official documentation;
- other reliable sources;
- experiments with your own code.


### 6. LEARN

Use what you discovered to improve your own understanding.

---

# Final Message

GenAI is most useful for education when it helps you **think**, rather than when it thinks *instead of you*.

A good learning prompt therefore does more than ask a question. It establishes a learning relationship:

> **"Act as my tutor. Here is what I know. Here is what I want to learn. Help me reason about it."**

And every GenAI interaction should be accompanied by a second habit:

> **"Do I have good evidence that this answer is correct?"**

Use GenAI to:

- explore;
- explain;
- practise;
- ask questions;
- receive feedback.

But use **textbooks, course materials, official documentation, reliable sources, and your own experiments** to verify what you learn.