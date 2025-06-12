# Decorators and Generators in Python

Decorators and generators are powerful features in Python that enable elegant solutions to common programming problems. This section explores these concepts in depth, providing practical examples and best practices.

## Decorators

Decorators are a design pattern in Python that allows you to extend or modify the behavior of callable objects (functions, methods, or classes) without permanently modifying the callable itself.

### Basic Decorator Syntax

A decorator is applied to a function using the `@decorator_name` syntax, which is equivalent to `function = decorator_name(function)`.

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# This is equivalent to:
# say_hello = my_decorator(say_hello)

say_hello()
# Output:
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.
```

### Decorators with Arguments

To create a decorator that accepts arguments, you need to add another level of nesting.

```python
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hello(name):
    print(f"Hello, {name}!")
    return f"Hello, {name}!"

say_hello("Alice")
# Output:
# Hello, Alice!
# Hello, Alice!
# Hello, Alice!
```

### Preserving Function Metadata

When you use decorators, the original function's metadata (like name, docstring, etc.) is lost. The `functools.wraps` decorator helps preserve this metadata.

```python
import functools

def my_decorator(func):
    @functools.wraps(func)  # Preserves func's metadata
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    """A function that says hello to someone."""
    print(f"Hello, {name}!")
    return f"Hello, {name}!"

print(say_hello.__name__)  # Output: say_hello (not wrapper)
print(say_hello.__doc__)   # Output: A function that says hello to someone.
```

### Class-Based Decorators

Decorators can also be implemented as classes.

```python
class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Call {self.count} of {self.func.__name__}")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")  # Output: Call 1 of say_hello\nHello, Alice!
say_hello("Bob")    # Output: Call 2 of say_hello\nHello, Bob!
```

### Method Decorators

Decorators can be applied to methods in classes.

```python
def log_method_call(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        print(f"Calling method {func.__name__} of {self.__class__.__name__}")
        return func(self, *args, **kwargs)
    return wrapper

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @log_method_call
    def greet(self, greeting="Hello"):
        return f"{greeting}, I'm {self.name} and I'm {self.age} years old."

person = Person("Alice", 30)
print(person.greet())
# Output:
# Calling method greet of Person
# Hello, I'm Alice and I'm 30 years old.
```

### Class Decorators

Decorators can also be applied to classes.

```python
def add_greeting(cls):
    cls.greet = lambda self: f"Hello, I'm {self.name}"
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

person = Person("Alice")
print(person.greet())  # Output: Hello, I'm Alice
```

### Multiple Decorators

You can apply multiple decorators to a function. They are applied from bottom to top (the decorator closest to the function is applied first).

```python
def bold(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper

def italic(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return f"<i>{func(*args, **kwargs)}</i>"
    return wrapper

@bold
@italic
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: <b><i>Hello, Alice!</i></b>
```

### Stateful Decorators

Decorators can maintain state between function calls.

```python
def counter(func):
    count = 0
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Function {func.__name__} has been called {count} times")
        return func(*args, **kwargs)
    return wrapper

@counter
def say_hello(name):
    return f"Hello, {name}!"

print(say_hello("Alice"))  # Output: Function say_hello has been called 1 times\nHello, Alice!
print(say_hello("Bob"))    # Output: Function say_hello has been called 2 times\nHello, Bob!
```

### Decorator Factories

Decorator factories are functions that create and return decorators.

```python
def log_with_level(level):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"{level}: Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
            result = func(*args, **kwargs)
            print(f"{level}: {func.__name__} returned {result}")
            return result
        return wrapper
    return decorator

@log_with_level("INFO")
def add(a, b):
    return a + b

print(add(5, 3))
# Output:
# INFO: Calling add with args: (5, 3), kwargs: {}
# INFO: add returned 8
# 8
```

### Common Built-in Decorators

Python provides several built-in decorators:

#### `@property`

Converts a method into a read-only attribute.

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @property
    def diameter(self):
        return 2 * self._radius
    
    @property
    def area(self):
        import math
        return math.pi * self._radius ** 2

circle = Circle(5)
print(circle.radius)    # Output: 5
print(circle.diameter)  # Output: 10
print(circle.area)      # Output: 78.53981633974483

# This will raise an AttributeError
try:
    circle.radius = 10
except AttributeError as e:
    print(f"Error: {e}")  # Output: Error: can't set attribute
```

#### `@classmethod`

Converts a method into a class method that receives the class as the first argument.

```python
class Person:
    count = 0
    
    def __init__(self, name):
        self.name = name
        Person.count += 1
    
    @classmethod
    def number_of_people(cls):
        return cls.count
    
    @classmethod
    def from_birth_year(cls, name, birth_year):
        import datetime
        age = datetime.datetime.now().year - birth_year
        return cls(name, age)

print(Person.number_of_people())  # Output: 0

person1 = Person("Alice")
person2 = Person("Bob")

print(Person.number_of_people())  # Output: 2
```

#### `@staticmethod`

Converts a method into a static method that doesn't receive any special first argument.

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def multiply(a, b):
        return a * b

print(MathUtils.add(5, 3))       # Output: 8
print(MathUtils.multiply(5, 3))  # Output: 15

# You can also call static methods on instances
math = MathUtils()
print(math.add(5, 3))       # Output: 8
print(math.multiply(5, 3))  # Output: 15
```

#### `@abstractmethod`

Marks a method as abstract, requiring subclasses to implement it.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

# This will work
rectangle = Rectangle(5, 3)
print(rectangle.area())       # Output: 15
print(rectangle.perimeter())  # Output: 16

# This will raise TypeError because Shape is abstract
try:
    shape = Shape()
except TypeError as e:
    print(f"Error: {e}")  # Output: Error: Can't instantiate abstract class Shape with abstract methods area, perimeter
```

### Practical Decorator Examples

#### Timing Decorator

```python
import time
import functools

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

print(slow_function())  
# Output:
# slow_function took 1.001234 seconds to run
# Function completed
```

#### Retry Decorator

```python
import functools
import time

def retry(max_attempts, delay=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts == max_attempts:
                        raise
                    print(f"Attempt {attempts} failed with error: {e}. Retrying in {delay} seconds...")
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(max_attempts=3, delay=0.5)
def unreliable_function():
    import random
    if random.random() < 0.7:  # 70% chance of failure
        raise ValueError("Random failure")
    return "Success!"

try:
    print(unreliable_function())
except ValueError:
    print("Function failed after all retry attempts")
```

#### Memoization Decorator

```python
import functools

def memoize(func):
    cache = {}
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Convert kwargs to a frozenset of items for hashing
        kwargs_key = frozenset(kwargs.items())
        # Create a composite key from args and kwargs_key
        key = (args, kwargs_key)
        
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    
    return wrapper

@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Without memoization, this would be very slow
print(fibonacci(35))  # Output: 9227465
```

#### Validation Decorator

```python
import functools

def validate_args(*types):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if len(args) != len(types):
                raise ValueError(f"Expected {len(types)} arguments, got {len(args)}")
            
            for arg, expected_type in zip(args, types):
                if not isinstance(arg, expected_type):
                    raise TypeError(f"Expected {expected_type}, got {type(arg)}")
            
            return func(*args, **kwargs)
        return wrapper
    return decorator

@validate_args(int, int)
def add(a, b):
    return a + b

print(add(5, 3))  # Output: 8

try:
    print(add(5, "3"))
except TypeError as e:
    print(f"Error: {e}")  # Output: Error: Expected <class 'int'>, got <class 'str'>
```

#### Singleton Decorator

```python
def singleton(cls):
    instances = {}
    
    @functools.wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return get_instance

@singleton
class DatabaseConnection:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        print(f"Connecting to database at {host}:{port}")
    
    def query(self, sql):
        print(f"Executing SQL: {sql}")
        return ["result1", "result2"]

# Only one connection will be created
db1 = DatabaseConnection("localhost", 5432)
db2 = DatabaseConnection("localhost", 5432)

print(db1 is db2)  # Output: True
```

#### Permission Decorator

```python
import functools

def require_permission(permission):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(user, *args, **kwargs):
            if permission in user.permissions:
                return func(user, *args, **kwargs)
            else:
                raise PermissionError(f"User {user.name} does not have permission {permission}")
        return wrapper
    return decorator

class User:
    def __init__(self, name, permissions):
        self.name = name
        self.permissions = permissions

class AdminPanel:
    @require_permission("admin")
    def delete_user(self, user, user_id):
        print(f"{user.name} deleted user {user_id}")
    
    @require_permission("view")
    def view_users(self, user):
        print(f"{user.name} viewed all users")

admin = User("Admin", ["admin", "view"])
viewer = User("Viewer", ["view"])

panel = AdminPanel()
panel.view_users(admin)    # Output: Admin viewed all users
panel.view_users(viewer)   # Output: Viewer viewed all users
panel.delete_user(admin, 123)  # Output: Admin deleted user 123

try:
    panel.delete_user(viewer, 123)
except PermissionError as e:
    print(f"Error: {e}")  # Output: Error: User Viewer does not have permission admin
```

## Generators

Generators are a special type of iterator that allow you to iterate over a potentially infinite sequence of values without storing the entire sequence in memory.

### Basic Generator Syntax

Generators are created using functions with the `yield` statement.

```python
def count_up_to(n):
    i = 0
    while i < n:
        yield i
        i += 1

# Using the generator
for num in count_up_to(5):
    print(num, end=" ")  # Output: 0 1 2 3 4

# Creating a list from a generator
numbers = list(count_up_to(5))
print(numbers)  # Output: [0, 1, 2, 3, 4]
```

### Generator Expressions

Generator expressions are similar to list comprehensions but create generators instead of lists.

```python
# List comprehension (creates the entire list in memory)
squares_list = [x**2 for x in range(10)]
print(squares_list)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Generator expression (creates values on-the-fly)
squares_gen = (x**2 for x in range(10))
print(squares_gen)  # Output: <generator object <genexpr> at 0x...>

# Consuming the generator
for square in squares_gen:
    print(square, end=" ")  # Output: 0 1 4 9 16 25 36 49 64 81
```

### Generator Methods

Generators have methods like `send()`, `throw()`, and `close()`.

```python
def echo_generator():
    value = yield "Ready"
    while True:
        value = yield f"Echo: {value}"

# Create the generator
gen = echo_generator()

# Start the generator (moves to the first yield)
print(next(gen))  # Output: Ready

# Send values to the generator
print(gen.send("Hello"))  # Output: Echo: Hello
print(gen.send("World"))  # Output: Echo: World

# Close the generator
gen.close()

# This will raise StopIteration
try:
    print(next(gen))
except StopIteration:
    print("Generator is closed")
```

### Yielding from Another Generator

The `yield from` statement allows you to yield values from another generator.

```python
def gen1():
    yield "A"
    yield "B"

def gen2():
    yield "C"
    yield "D"

def combined():
    yield from gen1()
    yield from gen2()
    yield "E"

for item in combined():
    print(item, end=" ")  # Output: A B C D E
```

### Infinite Generators

Generators can produce an infinite sequence of values.

```python
def infinite_counter(start=0):
    i = start
    while True:
        yield i
        i += 1

# Create an infinite generator
counter = infinite_counter()

# Take only what you need
for _ in range(5):
    print(next(counter), end=" ")  # Output: 0 1 2 3 4

# Using itertools to limit an infinite generator
import itertools
limited = itertools.islice(infinite_counter(10), 5)
print(list(limited))  # Output: [10, 11, 12, 13, 14]
```

### Generator Pipelines

Generators can be chained together to create data processing pipelines.

```python
def read_data():
    # Simulate reading data from a file or database
    data = ["1,John,25", "2,Jane,30", "3,Bob,22", "4,Alice,35"]
    for line in data:
        yield line

def parse_csv(lines):
    for line in lines:
        yield line.split(",")

def filter_by_age(records, min_age):
    for record in records:
        if int(record[2]) >= min_age:
            yield record

def format_output(records):
    for id, name, age in records:
        yield f"{name} (ID: {id}) is {age} years old"

# Create the pipeline
data = read_data()
parsed_data = parse_csv(data)
filtered_data = filter_by_age(parsed_data, 30)
formatted_data = format_output(filtered_data)

# Process the data
for item in formatted_data:
    print(item)
# Output:
# Jane (ID: 2) is 30 years old
# Alice (ID: 4) is 35 years old
```

### Coroutines with Generators

Generators can be used to implement coroutines for cooperative multitasking.

```python
def coroutine_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)  # Advance to the first yield
        return gen
    return wrapper

@coroutine_decorator
def receiver():
    while True:
        value = yield
        print(f"Received: {value}")

# Create and use the coroutine
receiver_coro = receiver()
receiver_coro.send("Hello")
receiver_coro.send("World")
# Output:
# Received: Hello
# Received: World

# Close the coroutine
receiver_coro.close()
```

### Exception Handling in Generators

Generators can handle exceptions using try-except blocks.

```python
def generator_with_exception_handling():
    try:
        yield 1
        yield 2
        yield 3
    except ValueError:
        yield "ValueError was caught"
    finally:
        print("Generator is being closed")

# Create the generator
gen = generator_with_exception_handling()

print(next(gen))  # Output: 1
print(next(gen))  # Output: 2

# Throw an exception into the generator
print(gen.throw(ValueError))  # Output: ValueError was caught

# Close the generator
gen.close()  # Output: Generator is being closed
```

### Practical Generator Examples

#### Reading Large Files

```python
def read_large_file(file_path, chunk_size=1024):
    with open(file_path, 'r') as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            yield chunk

# Usage (assuming 'large_file.txt' exists)
try:
    for chunk in read_large_file('large_file.txt'):
        print(f"Processing chunk of size {len(chunk)}")
except FileNotFoundError:
    print("File not found. This is just an example.")
```

#### Generating Fibonacci Numbers

```python
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Get the first 10 Fibonacci numbers
fib_gen = fibonacci_generator()
fib_numbers = [next(fib_gen) for _ in range(10)]
print(fib_numbers)  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

#### Data Transformation Pipeline

```python
def read_data():
    # Simulate reading data
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for item in data:
        yield item

def square(numbers):
    for number in numbers:
        yield number ** 2

def filter_even(numbers):
    for number in numbers:
        if number % 2 == 0:
            yield number

# Create the pipeline
data = read_data()
squared_data = square(data)
even_squares = filter_even(squared_data)

# Process the data
print(list(even_squares))  # Output: [4, 16, 36, 64, 100]
```

#### Pagination

```python
def paginate(items, page_size):
    """Yield items in chunks of page_size."""
    for i in range(0, len(items), page_size):
        yield items[i:i + page_size]

# Sample data
items = list(range(1, 21))  # 1 to 20

# Paginate the data
for i, page in enumerate(paginate(items, 5), 1):
    print(f"Page {i}: {page}")
# Output:
# Page 1: [1, 2, 3, 4, 5]
# Page 2: [6, 7, 8, 9, 10]
# Page 3: [11, 12, 13, 14, 15]
# Page 4: [16, 17, 18, 19, 20]
```

#### Generating Permutations

```python
def permutations(items):
    if len(items) <= 1:
        yield items
    else:
        for i in range(len(items)):
            # Get current item
            current = items[i]
            # Get remaining items
            remaining = items[:i] + items[i+1:]
            # For each permutation of remaining items
            for p in permutations(remaining):
                # Yield current item followed by the permutation
                yield [current] + p

# Generate all permutations of [1, 2, 3]
for p in permutations([1, 2, 3]):
    print(p)
# Output:
# [1, 2, 3]
# [1, 3, 2]
# [2, 1, 3]
# [2, 3, 1]
# [3, 1, 2]
# [3, 2, 1]
```

## Combining Decorators and Generators

### Generator Decorator

```python
import functools

def debug_generator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        gen = func(*args, **kwargs)
        for value in gen:
            print(f"Generator {func.__name__} yielded: {value}")
            yield value
    return wrapper

@debug_generator
def count_up_to(n):
    for i in range(n):
        yield i

# Use the decorated generator
for num in count_up_to(3):
    pass
# Output:
# Generator count_up_to yielded: 0
# Generator count_up_to yielded: 1
# Generator count_up_to yielded: 2
```

### Memoized Generator

```python
import functools

def memoize_generator(func):
    cache = {}
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key not in cache:
            cache[key] = list(func(*args, **kwargs))
        return iter(cache[key])
    
    return wrapper

@memoize_generator
def expensive_generator(n):
    print(f"Generating {n} items...")
    for i in range(n):
        print(f"Generating item {i}...")
        yield i

# First call (generates and caches values)
print("First call:")
for item in expensive_generator(3):
    print(f"Got item: {item}")

# Second call (uses cached values)
print("\nSecond call:")
for item in expensive_generator(3):
    print(f"Got item: {item}")
# Output:
# First call:
# Generating 3 items...
# Generating item 0...
# Got item: 0
# Generating item 1...
# Got item: 1
# Generating item 2...
# Got item: 2
#
# Second call:
# Got item: 0
# Got item: 1
# Got item: 2
```

### Timed Generator

```python
import time
import functools

def timed_generator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        yield from func(*args, **kwargs)
        end_time = time.time()
        print(f"Generator {func.__name__} took {end_time - start_time:.6f} seconds")
    return wrapper

@timed_generator
def slow_generator(n):
    for i in range(n):
        time.sleep(0.1)  # Simulate slow operation
        yield i

# Use the timed generator
list(slow_generator(3))
# Output: Generator slow_generator took 0.301234 seconds
```

## Best Practices

### Decorator Best Practices

1. **Use `functools.wraps`**: Always use `functools.wraps` to preserve the metadata of the decorated function.

2. **Keep decorators simple**: Decorators should have a single responsibility.

3. **Document decorators**: Clearly document what your decorator does and how it modifies the behavior of the decorated function.

4. **Handle exceptions**: Properly handle exceptions in decorators to avoid obscuring the source of errors.

5. **Avoid stateful decorators**: Be cautious with decorators that maintain state, as they can lead to unexpected behavior.

6. **Use class-based decorators for complex cases**: For decorators with complex behavior or state, consider using class-based decorators.

7. **Compose decorators**: Create small, focused decorators and compose them rather than creating large, monolithic decorators.

### Generator Best Practices

1. **Use generators for large data sets**: Generators are memory-efficient for processing large data sets.

2. **Close generators properly**: Always close generators when you're done with them, especially if they hold resources.

3. **Use generator expressions for simple cases**: For simple transformations, use generator expressions instead of generator functions.

4. **Build generator pipelines**: Chain generators together to create data processing pipelines.

5. **Handle exceptions in generators**: Properly handle exceptions in generators to ensure resources are cleaned up.

6. **Use `yield from` for delegation**: Use `yield from` to delegate to sub-generators.

7. **Avoid mixing `yield` and `return` with values**: In Python 3.3+, `return value` in a generator is equivalent to `raise StopIteration(value)`, which can be confusing.

## Common Pitfalls

### Decorator Pitfalls

1. **Forgetting `functools.wraps`**: Without `functools.wraps`, the decorated function loses its metadata.

```python
# Bad
def my_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

# Good
import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

2. **Decorating methods incorrectly**: When decorating methods, remember that the first argument is `self`.

```python
# Bad
def method_decorator(func):
    def wrapper(*args, **kwargs):
        # Missing self
        return func(*args, **kwargs)
    return wrapper

# Good
def method_decorator(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        # self is explicitly handled
        return func(self, *args, **kwargs)
    return wrapper
```

3. **Mutable default arguments**: Be careful with mutable default arguments in decorators.

```python
# Bad
def cache_decorator(func, cache={}):
    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

# Good
def cache_decorator(func):
    cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper
```

4. **Excessive nesting**: Too many levels of nesting in decorators can make them hard to understand.

```python
# Bad (too many levels of nesting)
def decorator_with_args(arg1, arg2):
    def real_decorator(func):
        def wrapper(*args, **kwargs):
            # Complex logic here
            return func(*args, **kwargs)
        return wrapper
    return real_decorator

# Better (use classes to reduce nesting)
class DecoratorWithArgs:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
    
    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Complex logic here
            return func(*args, **kwargs)
        return wrapper
```

### Generator Pitfalls

1. **Not closing generators**: Generators that hold resources should be closed when no longer needed.

```python
# Bad
def read_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line

# Usage (file remains open until garbage collection)
gen = read_file('file.txt')
for line in gen:
    if 'error' in line:
        break  # File remains open

# Good
def read_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line
    # File is closed when generator is exhausted or closed

# Usage
gen = read_file('file.txt')
try:
    for line in gen:
        if 'error' in line:
            break
finally:
    gen.close()  # Explicitly close the generator
```

2. **Consuming generators multiple times**: Generators can only be consumed once.

```python
# Bad
def count_up_to(n):
    for i in range(n):
        yield i

gen = count_up_to(5)
print(list(gen))  # Output: [0, 1, 2, 3, 4]
print(list(gen))  # Output: [] (generator is already exhausted)

# Good
def count_up_to(n):
    for i in range(n):
        yield i

# Create a new generator each time
print(list(count_up_to(5)))  # Output: [0, 1, 2, 3, 4]
print(list(count_up_to(5)))  # Output: [0, 1, 2, 3, 4]
```

3. **Memory leaks in infinite generators**: Infinite generators can cause memory leaks if not used carefully.

```python
# Bad (potential memory leak)
def infinite_generator():
    cache = []
    i = 0
    while True:
        cache.append(i)  # Cache grows indefinitely
        yield i
        i += 1

# Good
def infinite_generator():
    i = 0
    while True:
        yield i
        i += 1
```

4. **Mixing `yield` and `return` incorrectly**: In Python 3.3+, `return value` in a generator is equivalent to `raise StopIteration(value)`, which can be confusing.

```python
# Confusing
def generator_with_return():
    yield 1
    yield 2
    return 3  # This value is not yielded

# Usage
gen = generator_with_return()
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
try:
    print(next(gen))  # Raises StopIteration(3)
except StopIteration as e:
    print(f"Return value: {e.value}")  # Output: Return value: 3

# Clearer
def generator_with_final_yield():
    yield 1
    yield 2
    yield 3  # This value is yielded
```

## Next Steps

Now that you understand decorators and generators in Python, you're ready to move on to [Virtual Environments](../17_Virtual_Environments/README.md).