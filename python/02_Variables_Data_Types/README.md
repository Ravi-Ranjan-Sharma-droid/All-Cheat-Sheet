# Variables and Data Types

## Variables in Python

Variables are containers for storing data values. In Python, variables are created when you assign a value to them.

```python
# Variable assignment
name = "John"
age = 30
height = 5.9
is_student = True
```

Unlike some other programming languages, Python has no command for declaring a variable. A variable is created the moment you first assign a value to it.

## Variable Naming Rules

- Variable names must start with a letter or underscore
- The rest of the name can contain letters, numbers, and underscores
- Names are case-sensitive (`name` and `Name` are different variables)
- Cannot use Python keywords (like `if`, `for`, `while`, etc.)

```python
# Valid variable names
name = "John"
_name = "John"
name_1 = "John"
NAME = "John"  # Different from 'name'

# Invalid variable names
1name = "John"  # Cannot start with a number
name-1 = "John"  # Cannot use hyphen
if = "John"  # Cannot use Python keywords
```

## Python Naming Conventions

- Use snake_case for variable and function names (words separated by underscores)
- Use CamelCase for class names
- Use UPPERCASE for constants

```python
user_name = "john_doe"  # Variable (snake_case)

def calculate_area():  # Function (snake_case)
    pass

class UserProfile:  # Class (CamelCase)
    pass

MAX_SIZE = 100  # Constant (UPPERCASE)
```

## Basic Data Types

Python has several built-in data types:

### Numeric Types

#### Integers (`int`)

Whole numbers without a decimal point.

```python
age = 30
count = -5
big_number = 1_000_000  # Underscores for readability (Python 3.6+)
```

#### Floating-Point Numbers (`float`)

Numbers with a decimal point.

```python
height = 5.9
pi = 3.14159
scientific = 1.23e4  # Scientific notation (12300.0)
```

#### Complex Numbers (`complex`)

Numbers with a real and imaginary part.

```python
z = 2 + 3j  # j represents the imaginary part
```

### Text Type

#### Strings (`str`)

Sequences of characters enclosed in quotes (single, double, or triple).

```python
name = "John"
single_quotes = 'Python'
multi_line = """This is a
multi-line string"""
```

### Boolean Type

#### Boolean (`bool`)

Represents one of two values: `True` or `False`.

```python
is_active = True
is_completed = False
```

### Sequence Types

#### Lists (`list`)

Ordered, mutable collections of items.

```python
fruits = ["apple", "banana", "cherry"]
mixed_list = [1, "hello", True, 3.14]
```

#### Tuples (`tuple`)

Ordered, immutable collections of items.

```python
coordinates = (10, 20)
person = ("John", 30, "New York")
```

#### Range (`range`)

Represents a sequence of numbers.

```python
numbers = range(5)  # 0, 1, 2, 3, 4
even_numbers = range(2, 10, 2)  # 2, 4, 6, 8
```

### Mapping Type

#### Dictionaries (`dict`)

Unordered collections of key-value pairs.

```python
person = {"name": "John", "age": 30, "city": "New York"}
```

### Set Types

#### Sets (`set`)

Unordered collections of unique items.

```python
unique_numbers = {1, 2, 3, 4, 5}
fruits = {"apple", "banana", "cherry"}
```

#### Frozen Sets (`frozenset`)

Immutable sets.

```python
immutable_set = frozenset([1, 2, 3, 4, 5])
```

### None Type

#### None (`NoneType`)

Represents the absence of a value or a null value.

```python
result = None
```

## Checking Data Types

You can check the type of a variable using the `type()` function.

```python
name = "John"
age = 30
height = 5.9

print(type(name))    # <class 'str'>
print(type(age))     # <class 'int'>
print(type(height))  # <class 'float'>
```

## Type Conversion

Python allows you to convert between different data types.

### Implicit Type Conversion (Coercion)

Python automatically converts one data type to another when needed.

```python
x = 10      # int
y = 3.14    # float
z = x + y   # z becomes a float (13.14)
```

### Explicit Type Conversion (Casting)

You can explicitly convert from one type to another using built-in functions.

```python
# Convert to integer
int_from_float = int(3.14)       # 3 (truncates decimal part)
int_from_string = int("10")      # 10

# Convert to float
float_from_int = float(5)        # 5.0
float_from_string = float("3.14") # 3.14

# Convert to string
string_from_int = str(42)        # "42"
string_from_float = str(3.14)    # "3.14"

# Convert to boolean
bool_from_int = bool(1)          # True (0 is False, any other number is True)
bool_from_string = bool("Hello") # True (empty string is False, non-empty is True)
```

## Memory Management

Python handles memory management automatically. When you create a variable, Python allocates memory and when the variable is no longer in use, Python's garbage collector reclaims the memory.

```python
# Variables point to objects in memory
x = 10
y = x  # Both x and y point to the same object

# Modifying y doesn't affect x for immutable types like integers
y = 20
print(x)  # Still 10
print(y)  # 20
```

## Variable Scope

The scope of a variable determines where in your code the variable is accessible.

### Local Scope

Variables defined inside a function are only accessible within that function.

```python
def my_function():
    local_var = 10  # Local variable
    print(local_var)

my_function()  # Outputs: 10
# print(local_var)  # This would cause an error
```

### Global Scope

Variables defined outside of any function are accessible throughout the file.

```python
global_var = 20  # Global variable

def my_function():
    print(global_var)  # Can access global variable

my_function()  # Outputs: 20
print(global_var)  # Outputs: 20
```

### Modifying Global Variables

To modify a global variable inside a function, use the `global` keyword.

```python
counter = 0

def increment():
    global counter  # Declare counter as global
    counter += 1

increment()
print(counter)  # Outputs: 1
```

## Constants

Python doesn't have built-in constant types, but by convention, variables with names in ALL_CAPS are treated as constants.

```python
PI = 3.14159
MAX_USERS = 100

# These shouldn't be changed, but Python won't prevent it
```

## Multiple Assignment

Python allows you to assign values to multiple variables in one line.

```python
# Assign the same value to multiple variables
x = y = z = 0

# Assign different values to multiple variables
a, b, c = 1, 2, 3

# Unpack a list or tuple
coordinates = (10, 20, 30)
x, y, z = coordinates
```

## Common Pitfalls

### Mutable Default Arguments

Be careful with mutable default arguments in functions.

```python
# Problematic
def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item("apple"))  # ["apple"]
print(add_item("banana"))  # ["apple", "banana"] - Not a new empty list!

# Better approach
def add_item_fixed(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

### Variable References vs. Copies

Be aware of the difference between creating a reference and a copy.

```python
# For mutable objects like lists
original = [1, 2, 3]
reference = original  # Creates a reference to the same list
copy = original[:]    # Creates a copy of the list

reference.append(4)
print(original)   # [1, 2, 3, 4] - Modified because reference points to the same object
print(reference)  # [1, 2, 3, 4]

copy.append(5)
print(original)   # [1, 2, 3, 4] - Not modified because copy is a different object
print(copy)       # [1, 2, 3, 4, 5]
```

## Next Steps

Now that you understand variables and data types in Python, you're ready to move on to [Operators](../03_Operators/README.md).