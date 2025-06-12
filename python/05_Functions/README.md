# Functions in Python

Functions are reusable blocks of code that perform a specific task. They help organize code, make it more readable, and reduce duplication.

## Defining Functions

In Python, you define a function using the `def` keyword, followed by the function name, parentheses, and a colon. The function body is indented.

```python
def greet():
    print("Hello, World!")

# Call the function
greet()  # Output: Hello, World!
```

## Function Parameters

Functions can accept parameters (also called arguments), which are values passed to the function.

```python
def greet(name):
    print(f"Hello, {name}!")

# Call the function with an argument
greet("Alice")  # Output: Hello, Alice!
```

### Default Parameters

You can specify default values for parameters, which are used when the function is called without the corresponding argument.

```python
def greet(name="World"):
    print(f"Hello, {name}!")

# Call the function without an argument
greet()  # Output: Hello, World!

# Call the function with an argument
greet("Alice")  # Output: Hello, Alice!
```

### Positional Arguments

Positional arguments are matched with parameters based on their position.

```python
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")

# Call the function with positional arguments
describe_pet("dog", "Rex")  # Output: I have a dog named Rex.
```

### Keyword Arguments

Keyword arguments are matched with parameters based on their name, regardless of their position.

```python
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")

# Call the function with keyword arguments
describe_pet(pet_name="Rex", animal_type="dog")  # Output: I have a dog named Rex.
```

### Mixing Positional and Keyword Arguments

You can mix positional and keyword arguments, but positional arguments must come before keyword arguments.

```python
def describe_pet(animal_type, pet_name, age):
    print(f"I have a {age}-year-old {animal_type} named {pet_name}.")

# Mixing positional and keyword arguments
describe_pet("dog", pet_name="Rex", age=3)  # Output: I have a 3-year-old dog named Rex.

# This would cause an error: positional argument after keyword argument
# describe_pet(animal_type="dog", "Rex", age=3)
```

### Variable-Length Arguments (`*args`)

You can use `*args` to allow a function to accept any number of positional arguments.

```python
def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

# Call the function with different numbers of arguments
print(sum_numbers(1, 2))  # Output: 3
print(sum_numbers(1, 2, 3, 4, 5))  # Output: 15
```

### Variable-Length Keyword Arguments (`**kwargs`)

You can use `**kwargs` to allow a function to accept any number of keyword arguments.

```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Call the function with different keyword arguments
print_info(name="Alice", age=30)  # Output: name: Alice\nage: 30
print_info(name="Bob", age=25, city="New York")  # Output: name: Bob\nage: 25\ncity: New York
```

### Combining `*args` and `**kwargs`

You can use both `*args` and `**kwargs` in the same function.

```python
def print_everything(*args, **kwargs):
    print("Positional arguments:")
    for arg in args:
        print(arg)
    print("\nKeyword arguments:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Call the function with both types of arguments
print_everything(1, 2, 3, name="Alice", age=30)
```

### Parameter Order

When defining a function with different types of parameters, they must be in the following order:
1. Positional parameters
2. Parameters with default values
3. `*args` (variable-length positional arguments)
4. `**kwargs` (variable-length keyword arguments)

```python
def example_function(pos1, pos2, default1="default", default2="default", *args, **kwargs):
    pass
```

## Return Values

Functions can return values using the `return` statement.

```python
def add(a, b):
    return a + b

# Call the function and store the result
result = add(3, 5)
print(result)  # Output: 8
```

### Returning Multiple Values

Functions can return multiple values as a tuple.

```python
def get_dimensions():
    return 500, 300

# Unpack the returned tuple
width, height = get_dimensions()
print(f"Width: {width}, Height: {height}")  # Output: Width: 500, Height: 300

# Or store the tuple directly
dimensions = get_dimensions()
print(dimensions)  # Output: (500, 300)
```

### Early Returns

You can use `return` to exit a function early.

```python
def absolute_value(number):
    if number >= 0:
        return number
    return -number

print(absolute_value(5))   # Output: 5
print(absolute_value(-5))  # Output: 5
```

## Function Scope

Variables defined inside a function are only accessible within that function, unless they are explicitly returned or are global variables.

### Local Scope

Variables defined inside a function have local scope.

```python
def my_function():
    local_var = 10  # Local variable
    print(local_var)

my_function()  # Output: 10

# This would cause an error: local_var is not defined outside the function
# print(local_var)
```

### Global Scope

Variables defined outside of any function have global scope.

```python
global_var = 20  # Global variable

def my_function():
    print(global_var)  # Can access global variable

my_function()  # Output: 20
print(global_var)  # Output: 20
```

### Modifying Global Variables

To modify a global variable inside a function, use the `global` keyword.

```python
counter = 0

def increment():
    global counter  # Declare counter as global
    counter += 1

increment()
print(counter)  # Output: 1
```

### Nonlocal Variables

The `nonlocal` keyword is used to work with variables in the nearest enclosing scope that is not global.

```python
def outer_function():
    outer_var = 10
    
    def inner_function():
        nonlocal outer_var  # Declare outer_var as nonlocal
        outer_var += 5
    
    inner_function()
    print(outer_var)  # Output: 15

outer_function()
```

## Docstrings

Docstrings are string literals that appear right after the definition of a function, class, or module. They are used to document what the function does.

```python
def calculate_area(radius):
    """Calculate the area of a circle given its radius.
    
    Args:
        radius (float): The radius of the circle.
        
    Returns:
        float: The area of the circle.
    """
    import math
    return math.pi * radius ** 2

# Access the docstring
print(calculate_area.__doc__)

# Or use the help function
help(calculate_area)
```

## Lambda Functions

Lambda functions are small, anonymous functions defined using the `lambda` keyword. They can have any number of arguments but only one expression.

```python
# Regular function
def add(a, b):
    return a + b

# Equivalent lambda function
add_lambda = lambda a, b: a + b

print(add(3, 5))        # Output: 8
print(add_lambda(3, 5))  # Output: 8
```

Lambda functions are often used with functions like `map()`, `filter()`, and `sorted()`.

```python
# Using lambda with map()
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(squares)  # Output: [1, 4, 9, 16, 25]

# Using lambda with filter()
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]

# Using lambda with sorted()
people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
sorted_by_age = sorted(people, key=lambda person: person[1])
print(sorted_by_age)  # Output: [("Bob", 25), ("Alice", 30), ("Charlie", 35)]
```

## Function Annotations

Function annotations provide a way to attach metadata to function parameters and return values.

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!

# Access the annotations
print(greet.__annotations__)  # Output: {'name': <class 'str'>, 'return': <class 'str'>}
```

Annotations don't affect how the function works; they're just metadata. However, they can be used by tools like type checkers, IDEs, and documentation generators.

## Recursive Functions

A recursive function is a function that calls itself.

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120 (5 * 4 * 3 * 2 * 1)
```

Recursive functions need a base case to prevent infinite recursion.

## Higher-Order Functions

Higher-order functions are functions that take other functions as arguments or return functions.

```python
# Function that takes another function as an argument
def apply_function(func, value):
    return func(value)

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

print(apply_function(square, 3))  # Output: 9
print(apply_function(cube, 3))    # Output: 27

# Function that returns another function
def create_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

double = create_multiplier(2)
triple = create_multiplier(3)

print(double(5))  # Output: 10
print(triple(5))  # Output: 15
```

## Function Decorators

Decorators are a way to modify or enhance functions without changing their code. They are higher-order functions that take a function as an argument and return a new function.

```python
# Simple decorator
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

# Apply the decorator
@my_decorator
def say_hello():
    print("Hello!")

# Call the decorated function
say_hello()
# Output:
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.
```

Decorators can also take arguments.

```python
# Decorator with arguments
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

# Apply the decorator with an argument
@repeat(3)
def say_hello(name):
    print(f"Hello, {name}!")

# Call the decorated function
say_hello("Alice")
# Output:
# Hello, Alice!
# Hello, Alice!
# Hello, Alice!
```

## Function Caching

Function caching is a technique to store the results of expensive function calls and return the cached result when the same inputs occur again.

```python
from functools import lru_cache

# Apply the lru_cache decorator
@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Call the function
print(fibonacci(30))  # This would be slow without caching
```

## Partial Functions

Partial functions allow you to fix a certain number of arguments of a function and generate a new function.

```python
from functools import partial

def power(base, exponent):
    return base ** exponent

# Create a new function with base=2
square = partial(power, 2)

# Create a new function with exponent=2
square_number = partial(power, exponent=2)

print(square(3))        # Output: 8 (2^3)
print(square_number(3))  # Output: 9 (3^2)
```

## Best Practices

### Keep Functions Small and Focused

Functions should do one thing and do it well. If a function is doing too many things, consider breaking it into smaller functions.

```python
# Too many responsibilities
def process_data(data):
    # Validate data
    if not data:
        return None
    
    # Transform data
    transformed = [x * 2 for x in data]
    
    # Calculate statistics
    total = sum(transformed)
    average = total / len(transformed)
    
    return total, average

# Better: separate functions
def validate_data(data):
    return data is not None and len(data) > 0

def transform_data(data):
    return [x * 2 for x in data]

def calculate_statistics(data):
    total = sum(data)
    average = total / len(data)
    return total, average

def process_data(data):
    if not validate_data(data):
        return None
    transformed = transform_data(data)
    return calculate_statistics(transformed)
```

### Use Descriptive Names

Function names should be descriptive and follow the snake_case convention in Python.

```python
# Less descriptive
def calc(a, b):
    return a + b

# More descriptive
def calculate_sum(a, b):
    return a + b
```

### Use Default Arguments Carefully

Be careful with mutable default arguments, as they are created only once when the function is defined.

```python
# Problematic
def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item("apple"))   # Output: ["apple"]
print(add_item("banana"))  # Output: ["apple", "banana"] - Not a new empty list!

# Better approach
def add_item_fixed(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(add_item_fixed("apple"))   # Output: ["apple"]
print(add_item_fixed("banana"))  # Output: ["banana"]
```

### Return Early

Return early from functions to avoid deep nesting and make the code more readable.

```python
# Deep nesting
def process_data(data):
    if data:
        if isinstance(data, list):
            if len(data) > 0:
                # Process data
                return result
            else:
                return None
        else:
            return None
    else:
        return None

# Early returns
def process_data(data):
    if not data:
        return None
    if not isinstance(data, list):
        return None
    if len(data) == 0:
        return None
    
    # Process data
    return result
```

### Document Your Functions

Use docstrings to document what your functions do, what parameters they take, and what they return.

```python
def calculate_area(radius):
    """Calculate the area of a circle given its radius.
    
    Args:
        radius (float): The radius of the circle.
        
    Returns:
        float: The area of the circle.
    """
    import math
    return math.pi * radius ** 2
```

## Next Steps

Now that you understand functions in Python, you're ready to move on to [Lists](../06_Lists/README.md).