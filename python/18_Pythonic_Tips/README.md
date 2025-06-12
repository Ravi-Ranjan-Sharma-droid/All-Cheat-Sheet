# Pythonic Tips

Writing "Pythonic" code means following the conventions, idioms, and best practices that are widely accepted in the Python community. This section covers various Pythonic tips and techniques that will help you write cleaner, more readable, and more efficient Python code.

## The Zen of Python

The Zen of Python, by Tim Peters, is a collection of 19 guiding principles for writing computer programs in Python. You can view it by running `import this` in a Python interpreter:

```python
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

These principles guide the design of Python and should influence how you write Python code.

## Code Style and PEP 8

PEP 8 is the official style guide for Python code. Following PEP 8 makes your code more readable and consistent with other Python code.

### Indentation

Use 4 spaces per indentation level (not tabs).

```python
# Good
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# Bad (using tabs)
def long_function_name(
		var_one, var_two, var_three,
		var_four):
	print(var_one)
```

### Maximum Line Length

Limit lines to 79 characters for code and 72 for comments and docstrings.

```python
# Good
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# Bad
foo = long_function_name(var_one, var_two, var_three, var_four)
```

### Imports

Imports should be on separate lines and grouped in the following order:
1. Standard library imports
2. Related third-party imports
3. Local application/library specific imports

Each group should be separated by a blank line.

```python
# Good
import os
import sys

import numpy as np
import pandas as pd

from mymodule import MyClass
from mypackage.mymodule import function

# Bad
import sys, os
import numpy as np, pandas as pd
from mymodule import MyClass, function
```

### Whitespace

Use whitespace consistently:

```python
# Good
x = 1
y = 2
long_variable = 3

# Bad
x=1
y = 2
long_variable=3

# Good
if x == 4: print(x, y)

# Bad
if x == 4 : print( x , y )
```

### Naming Conventions

- `snake_case` for functions, variables, and methods
- `PascalCase` for classes
- `UPPER_CASE` for constants
- `_single_leading_underscore` for private attributes
- `__double_leading_underscore` for strongly private attributes
- `__double_leading_and_trailing_underscore__` for special methods

```python
# Good
class MyClass:
    CONSTANT = 42
    
    def __init__(self):
        self._private_attribute = 10
        self.__very_private = 20
    
    def my_method(self):
        local_variable = 30
        return local_variable

# Bad
class myclass:
    Constant = 42
    
    def __init__(self):
        self.PrivateAttribute = 10
        self.very_private = 20
    
    def MyMethod(self):
        LocalVariable = 30
        return LocalVariable
```

### Comments

Comments should be complete sentences and should be used sparingly.

```python
# Good
# Calculate the average of the list
average = sum(values) / len(values)

# Bad
# avg
average = sum(values) / len(values)
```

### Docstrings

Use docstrings for modules, functions, classes, and methods. Follow the conventions in PEP 257.

```python
def calculate_average(values):
    """Calculate the average of a list of numbers.
    
    Args:
        values (list): A list of numbers.
        
    Returns:
        float: The average of the numbers.
        
    Raises:
        ValueError: If the list is empty.
    """
    if not values:
        raise ValueError("Cannot calculate average of empty list")
    return sum(values) / len(values)
```

## Pythonic Idioms

### List Comprehensions

Use list comprehensions instead of `map()` or `filter()` when appropriate.

```python
# Good
squares = [x**2 for x in range(10)]

# Less Pythonic
squares = list(map(lambda x: x**2, range(10)))

# Good
even_squares = [x**2 for x in range(10) if x % 2 == 0]

# Less Pythonic
even_squares = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, range(10))))
```

### Dictionary Comprehensions

Use dictionary comprehensions for creating dictionaries.

```python
# Good
square_dict = {x: x**2 for x in range(5)}

# Less Pythonic
square_dict = {}
for x in range(5):
    square_dict[x] = x**2
```

### Set Comprehensions

Use set comprehensions for creating sets.

```python
# Good
square_set = {x**2 for x in range(5)}

# Less Pythonic
square_set = set()
for x in range(5):
    square_set.add(x**2)
```

### Generator Expressions

Use generator expressions for memory efficiency.

```python
# Good (memory efficient)
sum_of_squares = sum(x**2 for x in range(1000000))

# Bad (creates a large list in memory)
sum_of_squares = sum([x**2 for x in range(1000000)])
```

### Unpacking

Use unpacking for multiple assignments and swapping variables.

```python
# Good (unpacking)
a, b = 1, 2

# Good (swapping variables)
a, b = b, a

# Good (unpacking in a for loop)
points = [(1, 2), (3, 4), (5, 6)]
for x, y in points:
    print(x, y)

# Good (unpacking with *)
first, *middle, last = [1, 2, 3, 4, 5]
print(first)   # 1
print(middle)  # [2, 3, 4]
print(last)    # 5
```

### Enumerate

Use `enumerate()` instead of manually tracking indices.

```python
# Good
fruits = ['apple', 'banana', 'cherry']
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# Bad
fruits = ['apple', 'banana', 'cherry']
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")
```

### Zip

Use `zip()` to iterate over multiple sequences in parallel.

```python
# Good
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# Bad
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
for i in range(len(names)):
    print(f"{names[i]} is {ages[i]} years old")
```

### Context Managers

Use context managers (`with` statement) for resource management.

```python
# Good
with open('file.txt', 'r') as file:
    content = file.read()

# Bad
file = open('file.txt', 'r')
try:
    content = file.read()
finally:
    file.close()
```

### Default Dictionaries

Use `defaultdict` for dictionaries with default values.

```python
from collections import defaultdict

# Good
word_count = defaultdict(int)
for word in text.split():
    word_count[word] += 1

# Less Pythonic
word_count = {}
for word in text.split():
    if word not in word_count:
        word_count[word] = 0
    word_count[word] += 1
```

### Named Tuples

Use `namedtuple` for simple data classes.

```python
from collections import namedtuple

# Good
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)  # 1 2

# Less Pythonic
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(1, 2)
print(p.x, p.y)  # 1 2
```

### Get Dictionary Item with Default

Use `dict.get()` with a default value instead of checking if a key exists.

```python
# Good
value = my_dict.get('key', 'default')

# Less Pythonic
if 'key' in my_dict:
    value = my_dict['key']
else:
    value = 'default'
```

### Join Strings

Use `str.join()` to concatenate strings.

```python
# Good
words = ['Hello', 'World']
sentence = ' '.join(words)

# Bad
words = ['Hello', 'World']
sentence = ''
for word in words:
    sentence += word + ' '
sentence = sentence.strip()
```

### Truth Value Testing

Use implicit truth value testing.

```python
# Good
if value:
    print("Value is truthy")

if not value:
    print("Value is falsy")

# Bad
if value != 0 and value != '' and value != [] and value is not None:
    print("Value is truthy")

if value == 0 or value == '' or value == [] or value is None:
    print("Value is falsy")
```

### Checking for None

Use `is` and `is not` for checking against `None`.

```python
# Good
if value is None:
    print("Value is None")

if value is not None:
    print("Value is not None")

# Bad
if value == None:
    print("Value is None")

if value != None:
    print("Value is not None")
```

### Using `in` for Membership Tests

Use `in` to check if an item is in a sequence.

```python
# Good
if item in my_list:
    print("Item is in the list")

# Bad
found = False
for i in my_list:
    if i == item:
        found = True
        break
if found:
    print("Item is in the list")
```

### Using `all()` and `any()`

Use `all()` and `any()` for checking conditions on iterables.

```python
# Good
if all(x > 0 for x in values):
    print("All values are positive")

if any(x < 0 for x in values):
    print("At least one value is negative")

# Bad
all_positive = True
for x in values:
    if x <= 0:
        all_positive = False
        break
if all_positive:
    print("All values are positive")

any_negative = False
for x in values:
    if x < 0:
        any_negative = True
        break
if any_negative:
    print("At least one value is negative")
```

### Using `sorted()` with Key

Use the `key` parameter of `sorted()` for custom sorting.

```python
# Good
sorted_names = sorted(names, key=len)

# Good (sorting by last name)
names = ["John Smith", "Jane Doe", "Bob Johnson"]
sorted_names = sorted(names, key=lambda name: name.split()[-1])

# Good (sorting a list of dictionaries)
people = [{'name': 'John', 'age': 30}, {'name': 'Jane', 'age': 25}]
sorted_people = sorted(people, key=lambda person: person['age'])
```

### Using `reversed()`

Use `reversed()` to iterate over a sequence in reverse order.

```python
# Good
for item in reversed(my_list):
    print(item)

# Bad
for i in range(len(my_list) - 1, -1, -1):
    print(my_list[i])
```

## Performance Tips

### Use Built-in Functions and Libraries

Python's built-in functions and standard library are optimized and should be preferred over custom implementations.

```python
# Good (using built-in sum)
total = sum(values)

# Bad (manual implementation)
total = 0
for value in values:
    total += value
```

### Avoid Global Variables

Global variables can lead to unexpected behavior and make code harder to understand and maintain.

```python
# Good
def process_data(data):
    result = []
    for item in data:
        result.append(item * 2)
    return result

# Bad
result = []

def process_data(data):
    global result
    for item in data:
        result.append(item * 2)
```

### Use List Comprehensions for Simple Loops

List comprehensions are often faster than equivalent `for` loops.

```python
# Good (faster)
squares = [x**2 for x in range(1000)]

# Bad (slower)
squares = []
for x in range(1000):
    squares.append(x**2)
```

### Use Generator Expressions for Large Datasets

Generator expressions are memory-efficient for large datasets.

```python
# Good (memory-efficient)
sum_of_squares = sum(x**2 for x in range(1000000))

# Bad (memory-intensive)
sum_of_squares = sum([x**2 for x in range(1000000)])
```

### Use `collections` Module

The `collections` module provides specialized container datatypes that can be more efficient than the built-in types.

```python
from collections import Counter, defaultdict, deque

# Counter for counting occurrences
word_count = Counter(text.split())

# defaultdict for dictionaries with default values
graph = defaultdict(list)

# deque for efficient queue operations
queue = deque([1, 2, 3])
queue.append(4)       # Add to right
queue.appendleft(0)   # Add to left
queue.pop()           # Remove from right
queue.popleft()       # Remove from left
```

### Use `set` for Membership Testing

Membership testing in sets is much faster than in lists for large collections.

```python
# Good (fast for large collections)
my_set = set(large_list)
if item in my_set:
    print("Item found")

# Bad (slow for large collections)
if item in large_list:
    print("Item found")
```

### String Concatenation

Use `str.join()` for concatenating many strings.

```python
# Good (efficient)
parts = ['a', 'b', 'c', 'd']
result = ''.join(parts)

# Bad (inefficient)
result = ''
for part in parts:
    result += part
```

### Local Variables

Local variables are faster to access than global variables, attributes, or nested functions.

```python
# Good
def process_data(data):
    # Local reference to len
    length = len
    result = [length(item) for item in data]
    return result

# Less efficient
def process_data(data):
    result = [len(item) for item in data]
    return result
```

### Use `__slots__`

For classes with many instances, using `__slots__` can reduce memory usage.

```python
# Good (memory-efficient for many instances)
class Point:
    __slots__ = ('x', 'y')
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Regular class (more memory usage)
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

## Debugging Tips

### Using `print()` for Quick Debugging

The simplest way to debug is to add `print()` statements.

```python
def calculate(a, b):
    print(f"calculate called with a={a}, b={b}")
    result = a * b
    print(f"result = {result}")
    return result
```

### Using `assert` Statements

Use `assert` statements to check assumptions during development.

```python
def divide(a, b):
    assert b != 0, "Division by zero"
    return a / b
```

### Using the `logging` Module

For more sophisticated debugging, use the `logging` module.

```python
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate(a, b):
    logging.debug(f"calculate called with a={a}, b={b}")
    result = a * b
    logging.debug(f"result = {result}")
    return result
```

### Using the `pdb` Module

For interactive debugging, use the `pdb` module.

```python
import pdb

def complex_function(a, b):
    result = a * b
    pdb.set_trace()  # Debugger will start here
    return result + 42
```

In Python 3.7+, you can use the built-in `breakpoint()` function instead of `pdb.set_trace()`.

```python
def complex_function(a, b):
    result = a * b
    breakpoint()  # Debugger will start here
    return result + 42
```

### Using `try-except` for Debugging

Use `try-except` blocks to catch and print exceptions during debugging.

```python
try:
    result = complex_calculation(a, b)
except Exception as e:
    print(f"Error: {e}")
    # Re-raise the exception if needed
    raise
```

## Code Organization Tips

### Keep Functions Small and Focused

Functions should do one thing and do it well.

```python
# Good (small, focused functions)
def read_data(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def parse_data(data):
    return data.split('\n')

def process_data(lines):
    return [line.strip().upper() for line in lines]

# Bad (one large function doing multiple things)
def process_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    lines = data.split('\n')
    return [line.strip().upper() for line in lines]
```

### Use Classes to Group Related Functionality

Classes can help organize related functions and data.

```python
# Good (using a class to group related functionality)
class DataProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
    
    def read_data(self):
        with open(self.file_path, 'r') as file:
            return file.read()
    
    def parse_data(self, data):
        return data.split('\n')
    
    def process_data(self, lines):
        return [line.strip().upper() for line in lines]
    
    def run(self):
        data = self.read_data()
        lines = self.parse_data(data)
        return self.process_data(lines)

# Usage
processor = DataProcessor('data.txt')
result = processor.run()
```

### Use Modules to Group Related Classes and Functions

Modules can help organize related classes and functions.

```python
# data_processor.py
class DataReader:
    def __init__(self, file_path):
        self.file_path = file_path
    
    def read(self):
        with open(self.file_path, 'r') as file:
            return file.read()

class DataParser:
    def parse(self, data):
        return data.split('\n')

class DataProcessor:
    def process(self, lines):
        return [line.strip().upper() for line in lines]

# main.py
from data_processor import DataReader, DataParser, DataProcessor

reader = DataReader('data.txt')
parser = DataParser()
processor = DataProcessor()

data = reader.read()
lines = parser.parse(data)
result = processor.process(lines)
```

### Use Packages to Group Related Modules

Packages can help organize related modules.

```
my_package/
    __init__.py
    data/
        __init__.py
        reader.py
        parser.py
    processing/
        __init__.py
        processor.py
    utils/
        __init__.py
        helpers.py
```

## Documentation Tips

### Write Clear Docstrings

Docstrings should explain what a function or class does, its parameters, return values, and any exceptions it might raise.

```python
def calculate_average(values):
    """Calculate the average of a list of numbers.
    
    Args:
        values (list): A list of numbers.
        
    Returns:
        float: The average of the numbers.
        
    Raises:
        ValueError: If the list is empty.
    """
    if not values:
        raise ValueError("Cannot calculate average of empty list")
    return sum(values) / len(values)
```

### Use Type Hints

Type hints can make your code more readable and help catch type-related errors.

```python
from typing import List, Dict, Tuple, Optional, Union

def process_data(data: List[int]) -> List[int]:
    return [x * 2 for x in data]

def get_user(user_id: int) -> Optional[Dict[str, Union[str, int]]]:
    if user_id in users:
        return users[user_id]
    return None

def parse_point(point_str: str) -> Tuple[float, float]:
    x, y = point_str.split(',')
    return float(x), float(y)
```

### Add Comments for Complex Logic

Add comments to explain complex or non-obvious logic.

```python
def calculate_distance(point1, point2):
    # Using the Euclidean distance formula: sqrt((x2 - x1)^2 + (y2 - y1)^2)
    return ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5
```

## Testing Tips

### Write Unit Tests

Unit tests help ensure your code works as expected and continues to work as you make changes.

```python
import unittest

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
    
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
    
    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
    
    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        with self.assertRaises(ValueError):
            divide(6, 0)

if __name__ == '__main__':
    unittest.main()
```

### Use `pytest` for More Readable Tests

`pytest` provides a more concise way to write tests.

```python
import pytest

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2

def test_multiply():
    assert multiply(2, 3) == 6

def test_divide():
    assert divide(6, 3) == 2
    with pytest.raises(ValueError):
        divide(6, 0)
```

### Use Parameterized Tests

Parameterized tests allow you to run the same test with different inputs.

```python
import pytest

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (5, 3, 8),
    (0, 0, 0),
    (-1, 1, 0),
])
def test_add(a, b, expected):
    assert add(a, b) == expected
```

## Common Pythonic Patterns

### Context Managers for Resource Management

Use context managers to ensure resources are properly managed.

```python
class File:
    def __init__(self, file_path, mode):
        self.file_path = file_path
        self.mode = mode
    
    def __enter__(self):
        self.file = open(self.file_path, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

# Usage
with File('data.txt', 'r') as file:
    content = file.read()
```

### Decorators for Cross-Cutting Concerns

Use decorators to handle cross-cutting concerns like logging, timing, or authentication.

```python
import functools
import time

def timing_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.6f} seconds to run")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(1)
    return "Function completed"
```

### Descriptors for Attribute Management

Use descriptors to manage attribute access.

```python
class Positive:
    def __init__(self, name):
        self.name = name
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError(f"{self.name} must be positive")
        instance.__dict__[self.name] = value

class Circle:
    radius = Positive('radius')
    
    def __init__(self, radius):
        self.radius = radius
    
    @property
    def area(self):
        import math
        return math.pi * self.radius ** 2

# Usage
circle = Circle(5)
print(circle.area)  # 78.53981633974483

try:
    circle.radius = -1  # Raises ValueError
except ValueError as e:
    print(e)  # radius must be positive
```

### Properties for Computed Attributes

Use properties for computed attributes.

```python
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be positive")
        self._width = value
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be positive")
        self._height = value
    
    @property
    def area(self):
        return self.width * self.height
    
    @property
    def perimeter(self):
        return 2 * (self.width + self.height)

# Usage
rect = Rectangle(5, 3)
print(rect.area)       # 15
print(rect.perimeter)  # 16

rect.width = 10
print(rect.area)       # 30
```

### Mixins for Reusable Functionality

Use mixins to add reusable functionality to classes.

```python
class JSONSerializableMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)

class Person(JSONSerializableMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Usage
person = Person("Alice", 30)
print(person.to_json())  # {"name": "Alice", "age": 30}
```

### Factory Pattern

Use factory functions or classes to create objects.

```python
def create_shape(shape_type, **kwargs):
    if shape_type == 'circle':
        return Circle(kwargs['radius'])
    elif shape_type == 'rectangle':
        return Rectangle(kwargs['width'], kwargs['height'])
    else:
        raise ValueError(f"Unknown shape type: {shape_type}")

# Usage
circle = create_shape('circle', radius=5)
rectangle = create_shape('rectangle', width=10, height=5)
```

### Strategy Pattern

Use the strategy pattern to select an algorithm at runtime.

```python
class SortStrategy:
    def sort(self, data):
        pass

class BubbleSort(SortStrategy):
    def sort(self, data):
        print("Sorting using bubble sort")
        return sorted(data)  # Simplified implementation

class QuickSort(SortStrategy):
    def sort(self, data):
        print("Sorting using quick sort")
        return sorted(data)  # Simplified implementation

class Sorter:
    def __init__(self, strategy):
        self.strategy = strategy
    
    def sort(self, data):
        return self.strategy.sort(data)

# Usage
data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

sorter = Sorter(BubbleSort())
print(sorter.sort(data))  # Sorting using bubble sort\n[1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

sorter = Sorter(QuickSort())
print(sorter.sort(data))  # Sorting using quick sort\n[1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
```

## Next Steps

Now that you understand Pythonic tips and best practices, you're ready to move on to [Advanced Topics](../19_Advanced_Topics/README.md).