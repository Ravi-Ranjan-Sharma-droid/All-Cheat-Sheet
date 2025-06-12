# Control Flow in Python

Control flow refers to the order in which statements are executed in a program. Python provides several structures to control the flow of execution, including conditional statements, loops, and other control flow tools.

## Conditional Statements

Conditional statements allow you to execute different blocks of code based on certain conditions.

### `if` Statement

The `if` statement executes a block of code if a specified condition is true.

```python
age = 18

if age >= 18:
    print("You are an adult.")
```

### `if-else` Statement

The `if-else` statement executes one block of code if a condition is true and another block if the condition is false.

```python
age = 16

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```

### `if-elif-else` Statement

The `if-elif-else` statement allows you to check multiple conditions.

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is {grade}")
```

### Nested `if` Statements

You can nest `if` statements inside other `if` statements.

```python
age = 25
income = 50000

if age >= 18:
    if income >= 30000:
        print("You qualify for a loan.")
    else:
        print("Your income is too low for a loan.")
else:
    print("You must be at least 18 years old for a loan.")
```

### Conditional Expressions (Ternary Operator)

Python provides a concise way to write simple if-else statements using conditional expressions.

```python
age = 20
status = "adult" if age >= 18 else "minor"
print(status)  # "adult"
```

## Loops

Loops allow you to execute a block of code multiple times.

### `for` Loop

The `for` loop iterates over a sequence (like a list, tuple, dictionary, set, or string).

```python
# Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Iterating over a string
for char in "Python":
    print(char)

# Iterating over a range
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)

# Iterating over a range with start and stop
for i in range(2, 6):  # 2, 3, 4, 5
    print(i)

# Iterating over a range with start, stop, and step
for i in range(1, 10, 2):  # 1, 3, 5, 7, 9
    print(i)
```

### `while` Loop

The `while` loop executes a block of code as long as a condition is true.

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

### Infinite Loops

An infinite loop continues indefinitely unless interrupted. Be careful with these!

```python
# An infinite loop (use Ctrl+C to stop)
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input.lower() == "quit":
        break
```

### Loop Control Statements

Python provides several statements to control the flow of loops.

#### `break` Statement

The `break` statement terminates the loop and transfers execution to the statement immediately following the loop.

```python
for i in range(10):
    if i == 5:
        break  # Exit the loop when i equals 5
    print(i)
# Output: 0, 1, 2, 3, 4
```

#### `continue` Statement

The `continue` statement skips the rest of the current iteration and moves to the next iteration of the loop.

```python
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)
# Output: 1, 3, 5, 7, 9
```

#### `else` Clause in Loops

Both `for` and `while` loops can have an optional `else` clause that executes when the loop completes normally (i.e., not terminated by a `break` statement).

```python
# else clause with for loop
for i in range(5):
    print(i)
else:
    print("Loop completed successfully")

# else clause with while loop
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("Loop completed successfully")

# else clause is not executed if the loop is terminated by break
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("This won't be printed because the loop was terminated by break")
```

### Nested Loops

You can nest one loop inside another loop.

```python
# Nested for loops
for i in range(3):
    for j in range(2):
        print(f"({i}, {j})")

# Output:
# (0, 0)
# (0, 1)
# (1, 0)
# (1, 1)
# (2, 0)
# (2, 1)
```

## Loop Techniques

Python provides several useful techniques for working with loops.

### `enumerate()`

The `enumerate()` function adds a counter to an iterable, returning both the index and the value.

```python
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Output:
# 0: apple
# 1: banana
# 2: cherry

# You can also specify the starting index
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")

# Output:
# 1: apple
# 2: banana
# 3: cherry
```

### `zip()`

The `zip()` function combines multiple iterables into a single iterable of tuples.

```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# Output:
# Alice is 25 years old
# Bob is 30 years old
# Charlie is 35 years old
```

### List Comprehensions

List comprehensions provide a concise way to create lists based on existing lists.

```python
# Create a list of squares
squares = [x**2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Create a list with a condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)  # [0, 4, 16, 36, 64]

# Nested list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = [[row[i] for row in matrix] for i in range(3)]
print(transposed)  # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
```

### Dictionary Comprehensions

Similar to list comprehensions, dictionary comprehensions provide a concise way to create dictionaries.

```python
# Create a dictionary of squares
squares = {x: x**2 for x in range(6)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Create a dictionary with a condition
even_squares = {x: x**2 for x in range(6) if x % 2 == 0}
print(even_squares)  # {0: 0, 2: 4, 4: 16}

# Convert two lists into a dictionary
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
name_to_age = {name: age for name, age in zip(names, ages)}
print(name_to_age)  # {"Alice": 25, "Bob": 30, "Charlie": 35}
```

### Set Comprehensions

Set comprehensions are similar to list comprehensions but create sets instead of lists.

```python
# Create a set of squares
squares = {x**2 for x in range(10)}
print(squares)  # {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}

# Create a set with a condition
even_squares = {x**2 for x in range(10) if x % 2 == 0}
print(even_squares)  # {0, 4, 16, 36, 64}
```

## Other Control Flow Tools

### `pass` Statement

The `pass` statement is a null operation; it does nothing. It's used as a placeholder when a statement is required syntactically but you don't want any code to execute.

```python
# Using pass in an if statement
if condition:
    pass  # Do nothing

# Using pass in a function
def my_function():
    pass  # Function will be implemented later

# Using pass in a class
class MyClass:
    pass  # Class will be implemented later
```

### `assert` Statement

The `assert` statement is used for debugging purposes. It tests a condition and raises an `AssertionError` if the condition is false.

```python
def calculate_average(numbers):
    assert len(numbers) > 0, "Cannot calculate average of empty list"
    return sum(numbers) / len(numbers)

# This will work
print(calculate_average([1, 2, 3]))  # 2.0

# This will raise an AssertionError
# print(calculate_average([]))
```

### `with` Statement (Context Managers)

The `with` statement is used to wrap the execution of a block of code with methods defined by a context manager. It ensures proper acquisition and release of resources.

```python
# Using with to open a file
with open("example.txt", "w") as file:
    file.write("Hello, World!")
# File is automatically closed after the with block

# Multiple context managers
with open("input.txt", "r") as infile, open("output.txt", "w") as outfile:
    outfile.write(infile.read())
```

## Exception Handling

Exception handling allows you to handle errors gracefully.

### `try-except` Statement

The `try-except` statement is used to catch and handle exceptions.

```python
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero")
```

### `try-except-else` Statement

The `else` clause in a `try-except` statement executes if no exceptions are raised in the `try` block.

```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print(f"Result: {result}")  # This will be executed
```

### `try-except-finally` Statement

The `finally` clause in a `try-except` statement executes regardless of whether an exception was raised or not.

```python
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This will always execute")  # This will be executed
```

### `try-except-else-finally` Statement

You can combine `else` and `finally` clauses in a `try-except` statement.

```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print(f"Result: {result}")  # This will be executed
finally:
    print("This will always execute")  # This will be executed
```

## Best Practices

### Avoid Deep Nesting

Deep nesting of control structures can make code hard to read and maintain. Consider refactoring deeply nested code into separate functions or using early returns.

```python
# Deeply nested code (hard to read)
def process_data(data):
    if data:
        if isinstance(data, list):
            if len(data) > 0:
                for item in data:
                    if item > 0:
                        # Process item
                        pass

# Refactored code (easier to read)
def process_data(data):
    if not data:
        return
    if not isinstance(data, list):
        return
    if len(data) == 0:
        return
    for item in data:
        if item <= 0:
            continue
        # Process item
        pass
```

### Use Meaningful Variable Names

Use meaningful variable names in loops and conditional statements to make your code more readable.

```python
# Less readable
for i in items:
    if i > 0:
        # Process i
        pass

# More readable
for item in items:
    if item > 0:
        # Process item
        pass
```

### Prefer Positive Conditions

Positive conditions are generally easier to understand than negative ones.

```python
# Less readable
if not is_invalid(data):
    process(data)

# More readable
if is_valid(data):
    process(data)
```

### Use `in` for Membership Tests

Use the `in` operator for membership tests instead of multiple `or` conditions.

```python
# Less readable
if fruit == "apple" or fruit == "banana" or fruit == "cherry":
    print("This is a common fruit")

# More readable
if fruit in ["apple", "banana", "cherry"]:
    print("This is a common fruit")
```

### Use Comprehensions Judiciously

While comprehensions are powerful, they can become unreadable if too complex. Use them for simple cases and switch to regular loops for more complex logic.

```python
# Simple case (good for comprehension)
squares = [x**2 for x in range(10)]

# Complex case (better as a regular loop)
result = []
for x in range(10):
    if x % 2 == 0:
        if x > 5:
            result.append(x**2)
        else:
            result.append(x)
    else:
        result.append(0)
```

## Next Steps

Now that you understand control flow in Python, you're ready to move on to [Functions](../05_Functions/README.md).