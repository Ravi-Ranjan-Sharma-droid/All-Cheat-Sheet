# Lists in Python

Lists are one of the most versatile and commonly used data structures in Python. They are ordered, mutable collections that can contain elements of different types.

## Creating Lists

There are several ways to create lists in Python:

### Using Square Brackets

```python
# Empty list
empty_list = []

# List of numbers
numbers = [1, 2, 3, 4, 5]

# List of strings
fruits = ["apple", "banana", "cherry"]

# Mixed data types
mixed = [1, "hello", 3.14, True]

# Nested lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

### Using the `list()` Constructor

```python
# Empty list
empty_list = list()

# Convert other iterables to lists
list_from_tuple = list((1, 2, 3))  # [1, 2, 3]
list_from_string = list("hello")   # ['h', 'e', 'l', 'l', 'o']
list_from_range = list(range(5))   # [0, 1, 2, 3, 4]
```

### Using List Comprehensions

```python
# Create a list of squares
squares = [x**2 for x in range(10)]  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Create a list with a condition
even_numbers = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

# Create a list with complex expressions
coordinates = [(x, y) for x in range(3) for y in range(2)]  # [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]
```

## Accessing List Elements

### Indexing

List elements are accessed using zero-based indexing.

```python
fruits = ["apple", "banana", "cherry", "date"]

# Positive indexing (from the beginning)
print(fruits[0])  # "apple"
print(fruits[2])  # "cherry"

# Negative indexing (from the end)
print(fruits[-1])  # "date"
print(fruits[-3])  # "banana"
```

### Slicing

Slicing allows you to extract a portion of a list.

```python
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Basic slicing: list[start:stop]
# Returns elements from index 'start' to 'stop-1'
print(fruits[1:4])    # ["banana", "cherry", "date"]

# Omitting start (defaults to 0)
print(fruits[:3])     # ["apple", "banana", "cherry"]

# Omitting stop (defaults to len(list))
print(fruits[2:])     # ["cherry", "date", "elderberry"]

# Negative indices in slicing
print(fruits[1:-1])   # ["banana", "cherry", "date"]

# Step parameter: list[start:stop:step]
print(fruits[::2])    # ["apple", "cherry", "elderberry"]
print(fruits[1:5:2])  # ["banana", "date"]

# Reversing a list
print(fruits[::-1])   # ["elderberry", "date", "cherry", "banana", "apple"]
```

## Modifying Lists

Lists are mutable, which means you can change their content without creating a new list.

### Changing Elements

```python
fruits = ["apple", "banana", "cherry"]

# Change a single element
fruits[1] = "blueberry"
print(fruits)  # ["apple", "blueberry", "cherry"]

# Change multiple elements using slicing
fruits[0:2] = ["apricot", "blackberry"]
print(fruits)  # ["apricot", "blackberry", "cherry"]

# Replace with a different number of elements
fruits[1:2] = ["boysenberry", "blackcurrant"]
print(fruits)  # ["apricot", "boysenberry", "blackcurrant", "cherry"]
```

### Adding Elements

```python
fruits = ["apple", "banana", "cherry"]

# Append: add to the end of the list
fruits.append("date")
print(fruits)  # ["apple", "banana", "cherry", "date"]

# Insert: add at a specific position
fruits.insert(1, "blueberry")
print(fruits)  # ["apple", "blueberry", "banana", "cherry", "date"]

# Extend: add multiple elements from another iterable
fruits.extend(["elderberry", "fig"])
print(fruits)  # ["apple", "blueberry", "banana", "cherry", "date", "elderberry", "fig"]

# Concatenation: create a new list by combining lists
more_fruits = fruits + ["grape", "honeydew"]
print(more_fruits)  # ["apple", "blueberry", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]
```

### Removing Elements

```python
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Remove by value (removes only the first occurrence)
fruits.remove("cherry")
print(fruits)  # ["apple", "banana", "date", "elderberry"]

# Remove by index and get the value
removed_fruit = fruits.pop(1)  # removes and returns "banana"
print(removed_fruit)  # "banana"
print(fruits)  # ["apple", "date", "elderberry"]

# Remove the last element
last_fruit = fruits.pop()  # removes and returns "elderberry"
print(last_fruit)  # "elderberry"
print(fruits)  # ["apple", "date"]

# Delete by index
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
del fruits[2]  # deletes "cherry"
print(fruits)  # ["apple", "banana", "date", "elderberry"]

# Delete a slice
del fruits[1:3]  # deletes "banana" and "date"
print(fruits)  # ["apple", "elderberry"]

# Clear the entire list
fruits.clear()
print(fruits)  # []
```

## List Methods

Python lists come with many built-in methods to perform common operations.

### Adding Elements

```python
fruits = ["apple", "banana"]

# append(): Add an element to the end
fruits.append("cherry")
print(fruits)  # ["apple", "banana", "cherry"]

# insert(): Add an element at a specific position
fruits.insert(1, "blueberry")
print(fruits)  # ["apple", "blueberry", "banana", "cherry"]

# extend(): Add multiple elements from another iterable
fruits.extend(["date", "elderberry"])
print(fruits)  # ["apple", "blueberry", "banana", "cherry", "date", "elderberry"]
```

### Removing Elements

```python
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# remove(): Remove by value (first occurrence)
fruits.remove("cherry")
print(fruits)  # ["apple", "banana", "date", "elderberry"]

# pop(): Remove by index and return the value
removed = fruits.pop(1)  # removes and returns "banana"
print(removed)  # "banana"
print(fruits)  # ["apple", "date", "elderberry"]

# pop(): Remove the last element if no index is specified
last = fruits.pop()  # removes and returns "elderberry"
print(last)  # "elderberry"
print(fruits)  # ["apple", "date"]

# clear(): Remove all elements
fruits.clear()
print(fruits)  # []
```

### Finding Elements

```python
fruits = ["apple", "banana", "cherry", "banana", "date"]

# index(): Find the index of an element (first occurrence)
index = fruits.index("banana")
print(index)  # 1

# index() with start and end parameters
index = fruits.index("banana", 2)  # start searching from index 2
print(index)  # 3

# count(): Count occurrences of an element
count = fruits.count("banana")
print(count)  # 2

# in operator: Check if an element exists
print("cherry" in fruits)  # True
print("grape" in fruits)   # False
```

### Ordering Elements

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]

# sort(): Sort the list in-place
numbers.sort()
print(numbers)  # [1, 1, 2, 3, 4, 5, 5, 6, 9]

# sort() with reverse parameter
numbers.sort(reverse=True)
print(numbers)  # [9, 6, 5, 5, 4, 3, 2, 1, 1]

# sort() with key parameter
words = ["apple", "Banana", "cherry"]
words.sort()  # Case-sensitive sort
print(words)  # ["Banana", "apple", "cherry"]

words.sort(key=str.lower)  # Case-insensitive sort
print(words)  # ["apple", "Banana", "cherry"]

# reverse(): Reverse the list in-place
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)  # [5, 4, 3, 2, 1]
```

### Other Methods

```python
# copy(): Create a shallow copy of the list
original = [1, 2, 3]
copy = original.copy()
print(copy)  # [1, 2, 3]

# Another way to create a shallow copy
copy = original[:]
print(copy)  # [1, 2, 3]
```

## List Operations

### Concatenation

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Using the + operator
combined = list1 + list2
print(combined)  # [1, 2, 3, 4, 5, 6]

# Using the extend() method
list1.extend(list2)
print(list1)  # [1, 2, 3, 4, 5, 6]
```

### Repetition

```python
list1 = [1, 2, 3]

# Using the * operator
repeated = list1 * 3
print(repeated)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]
```

### Membership Testing

```python
fruits = ["apple", "banana", "cherry"]

# Using the in operator
print("banana" in fruits)  # True
print("grape" in fruits)   # False

# Using the not in operator
print("grape" not in fruits)  # True
```

### List Comprehensions

List comprehensions provide a concise way to create lists based on existing lists.

```python
# Basic list comprehension
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares)  # [1, 4, 9, 16, 25]

# List comprehension with condition
even_squares = [x**2 for x in numbers if x % 2 == 0]
print(even_squares)  # [4, 16]

# Nested list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [x for row in matrix for x in row]
print(flattened)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# List comprehension with multiple conditions
filtered = [x for x in numbers if x > 2 and x < 5]
print(filtered)  # [3, 4]

# List comprehension with if-else
classified = ["even" if x % 2 == 0 else "odd" for x in numbers]
print(classified)  # ["odd", "even", "odd", "even", "odd"]
```

## Common List Patterns

### Finding the Maximum and Minimum

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]

# Using built-in functions
maximum = max(numbers)
print(maximum)  # 9

minimum = min(numbers)
print(minimum)  # 1
```

### Summing and Averaging

```python
numbers = [1, 2, 3, 4, 5]

# Sum
total = sum(numbers)
print(total)  # 15

# Average
average = sum(numbers) / len(numbers)
print(average)  # 3.0
```

### Filtering

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using list comprehension
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)  # [2, 4, 6, 8, 10]

# Using filter() function
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4, 6, 8, 10]
```

### Mapping

```python
numbers = [1, 2, 3, 4, 5]

# Using list comprehension
squares = [x**2 for x in numbers]
print(squares)  # [1, 4, 9, 16, 25]

# Using map() function
squares = list(map(lambda x: x**2, numbers))
print(squares)  # [1, 4, 9, 16, 25]
```

### Removing Duplicates

```python
numbers = [1, 2, 2, 3, 3, 3, 4, 5, 5]

# Using a set
unique_numbers = list(set(numbers))
print(unique_numbers)  # [1, 2, 3, 4, 5] (order may vary)

# Using a list comprehension to preserve order
seen = set()
unique_ordered = [x for x in numbers if not (x in seen or seen.add(x))]
print(unique_ordered)  # [1, 2, 3, 4, 5]
```

### Counting Elements

```python
fruits = ["apple", "banana", "cherry", "apple", "banana", "apple"]

# Using the count() method
apple_count = fruits.count("apple")
print(apple_count)  # 3

# Using a dictionary to count all elements
from collections import Counter
counts = Counter(fruits)
print(counts)  # Counter({'apple': 3, 'banana': 2, 'cherry': 1})
```

### Flattening Nested Lists

```python
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Using a list comprehension
flattened = [item for sublist in nested_list for item in sublist]
print(flattened)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Using itertools.chain
import itertools
flattened = list(itertools.chain(*nested_list))
print(flattened)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## Memory and Performance Considerations

### List vs. Array

Python lists can contain elements of different types and are dynamically resizable, but this flexibility comes with some overhead. For numerical computations, consider using arrays from the `array` module or NumPy arrays, which are more memory-efficient and faster for numerical operations.

```python
# Standard Python list
my_list = [1, 2, 3, 4, 5]

# Array from the array module
import array
my_array = array.array('i', [1, 2, 3, 4, 5])  # 'i' for signed integers

# NumPy array
import numpy as np
my_numpy_array = np.array([1, 2, 3, 4, 5])
```

### Copying Lists

Understand the difference between shallow and deep copying.

```python
original = [[1, 2, 3], [4, 5, 6]]

# Shallow copy (copies the list but not the nested objects)
shallow_copy = original.copy()  # or original[:]
shallow_copy[0][0] = 99
print(original)      # [[99, 2, 3], [4, 5, 6]] (nested list is modified)
print(shallow_copy)  # [[99, 2, 3], [4, 5, 6]]

# Deep copy (copies the list and all nested objects)
import copy
deep_copy = copy.deepcopy(original)
deep_copy[0][1] = 88
print(original)   # [[99, 2, 3], [4, 5, 6]] (nested list is not modified)
print(deep_copy)  # [[99, 88, 3], [4, 5, 6]]
```

### List Comprehensions vs. Loops

List comprehensions are generally more concise and often faster than equivalent for loops for creating lists.

```python
# Using a for loop
squares = []
for x in range(10):
    squares.append(x**2)

# Using a list comprehension
squares = [x**2 for x in range(10)]
```

## Common Pitfalls

### Modifying a List While Iterating

Modifying a list while iterating over it can lead to unexpected results.

```python
# Problematic: removing items while iterating
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    if number % 2 == 0:
        numbers.remove(number)  # This can cause items to be skipped
print(numbers)  # [1, 3, 5] (works in this case, but not reliable)

# Better approach: create a new list or iterate over a copy
numbers = [1, 2, 3, 4, 5]
numbers = [x for x in numbers if x % 2 != 0]  # Using list comprehension
print(numbers)  # [1, 3, 5]

# Or iterate over a copy
numbers = [1, 2, 3, 4, 5]
for number in numbers[:]:
    if number % 2 == 0:
        numbers.remove(number)
print(numbers)  # [1, 3, 5]
```

### Mutable Default Arguments

Be careful with mutable default arguments in functions.

```python
# Problematic
def add_to_list(item, my_list=[]):
    my_list.append(item)
    return my_list

print(add_to_list(1))  # [1]
print(add_to_list(2))  # [1, 2] (not a new empty list!)

# Better approach
def add_to_list_fixed(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list

print(add_to_list_fixed(1))  # [1]
print(add_to_list_fixed(2))  # [2]
```

### List Multiplication with Nested Lists

Be careful when using the `*` operator with lists containing mutable objects.

```python
# Problematic
row = [0] * 3  # [0, 0, 0]
grid = [row] * 3  # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
grid[0][0] = 1
print(grid)  # [[1, 0, 0], [1, 0, 0], [1, 0, 0]] (all rows are modified)

# Better approach
grid = [[0 for _ in range(3)] for _ in range(3)]
grid[0][0] = 1
print(grid)  # [[1, 0, 0], [0, 0, 0], [0, 0, 0]] (only the first row is modified)
```

## Next Steps

Now that you understand lists in Python, you're ready to move on to [Tuples](../07_Tuples/README.md).