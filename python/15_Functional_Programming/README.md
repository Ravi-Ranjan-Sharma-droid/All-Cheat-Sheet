# Functional Programming in Python

Functional programming is a programming paradigm that treats computation as the evaluation of mathematical functions and avoids changing state and mutable data. Python is not a pure functional programming language, but it supports many functional programming concepts. This section covers functional programming principles and techniques in Python.

## First-Class Functions

In Python, functions are first-class citizens, which means they can be:
- Assigned to variables
- Passed as arguments to other functions
- Returned from other functions
- Stored in data structures

### Assigning Functions to Variables

```python
def greet(name):
    return f"Hello, {name}!"

# Assign the function to a variable
say_hello = greet

# Call the function through the variable
print(say_hello("Alice"))  # Output: Hello, Alice!
```

### Passing Functions as Arguments

```python
def apply_function(func, value):
    return func(value)

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

# Pass functions as arguments
print(apply_function(square, 5))  # Output: 25
print(apply_function(cube, 5))    # Output: 125
```

### Returning Functions from Functions

```python
def create_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

# Create specific multiplier functions
double = create_multiplier(2)
triple = create_multiplier(3)

# Use the created functions
print(double(5))  # Output: 10
print(triple(5))  # Output: 15
```

### Storing Functions in Data Structures

```python
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# Store functions in a dictionary
operations = {
    'add': add,
    'subtract': subtract,
    'multiply': multiply,
    'divide': divide
}

# Use functions from the dictionary
print(operations['add'](5, 3))      # Output: 8
print(operations['multiply'](5, 3))  # Output: 15
```

## Pure Functions

A pure function is a function that:
1. Given the same input, always returns the same output
2. Has no side effects (doesn't modify external state)

### Pure Function Example

```python
# Pure function
def add(x, y):
    return x + y

# Always returns the same output for the same input
print(add(5, 3))  # Output: 8
print(add(5, 3))  # Output: 8
```

### Impure Function Example

```python
# Impure function (has side effects)
total = 0

def add_to_total(x):
    global total
    total += x
    return total

# Returns different outputs for the same input
print(add_to_total(5))  # Output: 5
print(add_to_total(5))  # Output: 10
```

### Benefits of Pure Functions

1. **Predictability**: Pure functions always produce the same output for the same input.
2. **Testability**: Pure functions are easier to test because they don't depend on external state.
3. **Concurrency**: Pure functions can be executed in parallel without race conditions.
4. **Caching**: Results of pure functions can be cached (memoized) for performance.

## Higher-Order Functions

Higher-order functions are functions that take other functions as arguments or return functions as results.

### Built-in Higher-Order Functions

#### `map()`

The `map()` function applies a function to each item in an iterable and returns an iterator of the results.

```python
# Using map() with a built-in function
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x ** 2, numbers)
print(list(squared))  # Output: [1, 4, 9, 16, 25]

# Using map() with a custom function
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

temperatures_c = [0, 10, 20, 30, 40]
temperatures_f = map(celsius_to_fahrenheit, temperatures_c)
print(list(temperatures_f))  # Output: [32.0, 50.0, 68.0, 86.0, 104.0]

# Using map() with multiple iterables
list1 = [1, 2, 3]
list2 = [4, 5, 6]
sums = map(lambda x, y: x + y, list1, list2)
print(list(sums))  # Output: [5, 7, 9]
```

#### `filter()`

The `filter()` function constructs an iterator from elements of an iterable for which a function returns true.

```python
# Using filter() with a lambda function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4, 6, 8, 10]

# Using filter() with a custom function
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

numbers = range(1, 20)
prime_numbers = filter(is_prime, numbers)
print(list(prime_numbers))  # Output: [2, 3, 5, 7, 11, 13, 17, 19]
```

#### `reduce()`

The `reduce()` function applies a function of two arguments cumulatively to the items of an iterable, reducing the iterable to a single value.

```python
from functools import reduce

# Using reduce() to compute the sum of a list
numbers = [1, 2, 3, 4, 5]
sum_result = reduce(lambda x, y: x + y, numbers)
print(sum_result)  # Output: 15

# Using reduce() to find the maximum value
numbers = [5, 8, 3, 1, 7]
max_value = reduce(lambda x, y: x if x > y else y, numbers)
print(max_value)  # Output: 8

# Using reduce() with an initial value
numbers = [1, 2, 3, 4, 5]
sum_with_initial = reduce(lambda x, y: x + y, numbers, 10)
print(sum_with_initial)  # Output: 25 (10 + 1 + 2 + 3 + 4 + 5)
```

### Custom Higher-Order Functions

```python
def compose(f, g):
    """Compose two functions: compose(f, g)(x) = f(g(x))"""
    return lambda x: f(g(x))

def repeat(f, n):
    """Repeat a function n times: repeat(f, n)(x) = f(f(...f(x)...))"""
    def repeated(x):
        result = x
        for _ in range(n):
            result = f(result)
        return result
    return repeated

# Use the compose function
square = lambda x: x ** 2
double = lambda x: x * 2
square_then_double = compose(double, square)
double_then_square = compose(square, double)

print(square_then_double(3))  # Output: 18 (double(square(3)) = double(9) = 18)
print(double_then_square(3))  # Output: 36 (square(double(3)) = square(6) = 36)

# Use the repeat function
increment = lambda x: x + 1
increment_thrice = repeat(increment, 3)

print(increment_thrice(5))  # Output: 8 (5 + 1 + 1 + 1 = 8)
```

## Immutability

Immutability is a core principle of functional programming. An immutable object cannot be changed after it is created.

### Immutable Data Types in Python

Python has several built-in immutable data types:
- Numbers (int, float, complex)
- Strings
- Tuples
- Frozen sets

```python
# Strings are immutable
s = "hello"
try:
    s[0] = "H"  # This will raise a TypeError
except TypeError as e:
    print(f"Error: {e}")  # Output: Error: 'str' object does not support item assignment

# Creating a new string instead
s = "H" + s[1:]
print(s)  # Output: Hello

# Tuples are immutable
t = (1, 2, 3)
try:
    t[0] = 10  # This will raise a TypeError
except TypeError as e:
    print(f"Error: {e}")  # Output: Error: 'tuple' object does not support item assignment

# Creating a new tuple instead
t = (10,) + t[1:]
print(t)  # Output: (10, 2, 3)
```

### Working with Immutable Data

When working with immutable data, you create new objects instead of modifying existing ones.

```python
# Function that creates a new list with an element replaced
def replace_at_index(lst, index, value):
    return lst[:index] + [value] + lst[index+1:]

# Original list
numbers = [1, 2, 3, 4, 5]

# Create a new list with the element at index 2 replaced
new_numbers = replace_at_index(numbers, 2, 30)

print(numbers)     # Output: [1, 2, 3, 4, 5] (unchanged)
print(new_numbers)  # Output: [1, 2, 30, 4, 5]
```

### Namedtuples for Immutable Objects

Namedtuples are a convenient way to create simple immutable objects.

```python
from collections import namedtuple

# Define a namedtuple class
Person = namedtuple('Person', ['name', 'age', 'city'])

# Create a Person object
alice = Person('Alice', 30, 'New York')

print(alice.name)  # Output: Alice
print(alice.age)   # Output: 30
print(alice.city)  # Output: New York

# Namedtuples are immutable
try:
    alice.age = 31  # This will raise an AttributeError
except AttributeError as e:
    print(f"Error: {e}")  # Output: Error: can't set attribute

# Create a new Person object with updated age
bob = alice._replace(name='Bob', age=25)
print(bob)  # Output: Person(name='Bob', age=25, city='New York')
```

## Recursion

Recursion is a technique where a function calls itself to solve a problem. It's a common approach in functional programming.

### Basic Recursion

```python
# Factorial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120

# Fibonacci sequence using recursion
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(10):
    print(fibonacci(i), end=" ")  # Output: 0 1 1 2 3 5 8 13 21 34
```

### Tail Recursion

Tail recursion is a special case of recursion where the recursive call is the last operation in the function. Python doesn't optimize tail recursion, but it's still a useful concept.

```python
# Factorial using tail recursion
def factorial_tail(n, accumulator=1):
    if n == 0 or n == 1:
        return accumulator
    else:
        return factorial_tail(n - 1, n * accumulator)

print(factorial_tail(5))  # Output: 120

# Fibonacci sequence using tail recursion
def fibonacci_tail(n, a=0, b=1):
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return fibonacci_tail(n - 1, b, a + b)

for i in range(10):
    print(fibonacci_tail(i), end=" ")  # Output: 0 1 1 2 3 5 8 13 21 34
```

### Recursive Data Structures

Recursive data structures are data structures that contain themselves as sub-structures.

```python
# Binary tree using recursion
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Create a binary tree
tree = TreeNode(1,
                TreeNode(2,
                         TreeNode(4),
                         TreeNode(5)),
                TreeNode(3,
                         TreeNode(6),
                         TreeNode(7)))

# Traverse the tree using recursion (in-order traversal)
def in_order_traversal(node):
    if node is None:
        return []
    return in_order_traversal(node.left) + [node.value] + in_order_traversal(node.right)

print(in_order_traversal(tree))  # Output: [4, 2, 5, 1, 6, 3, 7]
```

## Closures

A closure is a function that remembers the values from the enclosing lexical scope even when the program flow is no longer in that scope.

```python
def create_counter():
    count = 0
    
    def increment():
        nonlocal count
        count += 1
        return count
    
    return increment

# Create counter functions
counter1 = create_counter()
counter2 = create_counter()

print(counter1())  # Output: 1
print(counter1())  # Output: 2
print(counter1())  # Output: 3

print(counter2())  # Output: 1 (separate counter)
print(counter2())  # Output: 2
```

### Closures for Data Hiding

```python
def create_bank_account(initial_balance):
    balance = initial_balance
    
    def deposit(amount):
        nonlocal balance
        balance += amount
        return balance
    
    def withdraw(amount):
        nonlocal balance
        if amount <= balance:
            balance -= amount
            return balance
        else:
            return "Insufficient funds"
    
    def get_balance():
        return balance
    
    # Return a dictionary of functions
    return {
        'deposit': deposit,
        'withdraw': withdraw,
        'get_balance': get_balance
    }

# Create a bank account
account = create_bank_account(1000)

print(account['get_balance']())  # Output: 1000
print(account['deposit'](500))   # Output: 1500
print(account['withdraw'](200))  # Output: 1300
print(account['withdraw'](2000))  # Output: Insufficient funds
```

## Partial Application and Currying

### Partial Application

Partial application is the process of fixing a number of arguments to a function, producing another function of smaller arity.

```python
from functools import partial

# Original function
def power(base, exponent):
    return base ** exponent

# Create a new function with partial application
square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(square(5))  # Output: 25
print(cube(5))    # Output: 125

# Another example
def greet(greeting, name):
    return f"{greeting}, {name}!"

say_hello = partial(greet, "Hello")
say_hi = partial(greet, "Hi")

print(say_hello("Alice"))  # Output: Hello, Alice!
print(say_hi("Bob"))      # Output: Hi, Bob!
```

### Currying

Currying is the technique of transforming a function that takes multiple arguments into a sequence of functions that each take a single argument.

```python
# Manual currying
def curry_power(base):
    def with_exponent(exponent):
        return base ** exponent
    return with_exponent

# Use the curried function
square_of = curry_power(2)
cube_of = curry_power(3)

print(square_of(5))  # Output: 32 (2^5)
print(cube_of(5))    # Output: 243 (3^5)

# Another example
def curry_add(x):
    def add_y(y):
        return x + y
    return add_y

add_5 = curry_add(5)
add_10 = curry_add(10)

print(add_5(3))   # Output: 8
print(add_10(3))  # Output: 13
```

### Implementing a General Curry Function

```python
def curry(func, arity):
    """Curry a function of given arity."""
    def curried(*args):
        if len(args) >= arity:
            return func(*args)
        return lambda *more_args: curried(*(args + more_args))
    return curried

# Original function
def add3(a, b, c):
    return a + b + c

# Curry the function
curried_add3 = curry(add3, 3)

# Use the curried function in different ways
print(curried_add3(1, 2, 3))    # Output: 6
print(curried_add3(1)(2)(3))    # Output: 6
print(curried_add3(1, 2)(3))    # Output: 6
print(curried_add3(1)(2, 3))    # Output: 6
```

## Lazy Evaluation

Lazy evaluation is a strategy that delays the evaluation of an expression until its value is needed.

### Generators

Generators provide a way to implement lazy evaluation in Python.

```python
# A generator function that yields an infinite sequence
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

# Create a generator
gen = infinite_sequence()

# Get the first 5 numbers
for _ in range(5):
    print(next(gen), end=" ")  # Output: 0 1 2 3 4

# Generator expression
even_numbers = (x for x in range(10) if x % 2 == 0)
print(list(even_numbers))  # Output: [0, 2, 4, 6, 8]
```

### Lazy Evaluation with `itertools`

```python
import itertools

# Generate an infinite sequence of numbers
counter = itertools.count(start=1)

# Take the first 5 numbers
first_five = list(itertools.islice(counter, 5))
print(first_five)  # Output: [1, 2, 3, 4, 5]

# Generate an infinite cycle
cycle = itertools.cycle(['A', 'B', 'C'])

# Take the first 7 elements
first_seven = list(itertools.islice(cycle, 7))
print(first_seven)  # Output: ['A', 'B', 'C', 'A', 'B', 'C', 'A']

# Repeat an element infinitely
repeater = itertools.repeat('X')

# Take the first 3 elements
first_three = list(itertools.islice(repeater, 3))
print(first_three)  # Output: ['X', 'X', 'X']
```

### Custom Lazy Evaluation

```python
class LazyProperty:
    def __init__(self, function):
        self.function = function
        self.name = function.__name__

    def __get__(self, instance, owner):
        if instance is None:
            return self
        value = self.function(instance)
        setattr(instance, self.name, value)
        return value

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @LazyProperty
    def expensive_calculation(self):
        print("Performing expensive calculation...")
        # Simulate an expensive operation
        import time
        time.sleep(1)
        return f"{self.name}'s expensive result"

# Create a Person object
person = Person("Alice", 30)

# The expensive_calculation is not computed yet
print("Before accessing the property")

# Access the property (triggers the calculation)
print(person.expensive_calculation)

# Access the property again (uses the cached value)
print(person.expensive_calculation)
```

## Functional Programming Libraries

### `functools`

The `functools` module provides higher-order functions and operations on callable objects.

```python
import functools

# partial: Create a new function with some arguments fixed
add = lambda x, y: x + y
add_5 = functools.partial(add, 5)
print(add_5(10))  # Output: 15

# reduce: Apply a function cumulatively to the items of an iterable
numbers = [1, 2, 3, 4, 5]
sum_result = functools.reduce(lambda x, y: x + y, numbers)
print(sum_result)  # Output: 15

# lru_cache: Memoize a function's results
@functools.lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(30))  # Output: 832040 (computed efficiently with memoization)

# singledispatch: Create a generic function with different implementations based on the type of the first argument
@functools.singledispatch
def process(obj):
    return f"Default: {obj}"

@process.register
def _(obj: int):
    return f"Integer: {obj}"

@process.register
def _(obj: str):
    return f"String: {obj}"

@process.register
def _(obj: list):
    return f"List with {len(obj)} items"

print(process(10))        # Output: Integer: 10
print(process("hello"))   # Output: String: hello
print(process([1, 2, 3]))  # Output: List with 3 items
print(process(1.5))       # Output: Default: 1.5
```

### `itertools`

The `itertools` module provides functions for creating iterators for efficient looping.

```python
import itertools

# count: Create an iterator that counts from a starting value
counter = itertools.count(start=10, step=2)
for i in itertools.islice(counter, 5):
    print(i, end=" ")  # Output: 10 12 14 16 18
print()

# cycle: Create an iterator that cycles through an iterable
cycle = itertools.cycle(['A', 'B', 'C'])
for i in itertools.islice(cycle, 7):
    print(i, end=" ")  # Output: A B C A B C A
print()

# repeat: Create an iterator that repeats an object
repeater = itertools.repeat('X', 3)
for i in repeater:
    print(i, end=" ")  # Output: X X X
print()

# chain: Chain multiple iterables together
chained = itertools.chain([1, 2, 3], ['A', 'B', 'C'])
print(list(chained))  # Output: [1, 2, 3, 'A', 'B', 'C']

# combinations: Generate all combinations of r elements from an iterable
combos = itertools.combinations([1, 2, 3, 4], 2)
print(list(combos))  # Output: [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

# permutations: Generate all permutations of r elements from an iterable
perms = itertools.permutations([1, 2, 3], 2)
print(list(perms))  # Output: [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

# product: Generate the Cartesian product of input iterables
prod = itertools.product(['A', 'B'], [1, 2])
print(list(prod))  # Output: [('A', 1), ('A', 2), ('B', 1), ('B', 2)]

# groupby: Group consecutive items by a key function
data = [('A', 1), ('A', 2), ('B', 1), ('B', 2)]
grouped = itertools.groupby(data, lambda x: x[0])
for key, group in grouped:
    print(key, list(group))
# Output:
# A [('A', 1), ('A', 2)]
# B [('B', 1), ('B', 2)]
```

### `operator`

The `operator` module provides functions corresponding to the intrinsic operators of Python.

```python
import operator
from functools import reduce

# Arithmetic operators
print(operator.add(5, 3))       # Output: 8
print(operator.sub(5, 3))       # Output: 2
print(operator.mul(5, 3))       # Output: 15
print(operator.truediv(5, 3))   # Output: 1.6666666666666667
print(operator.floordiv(5, 3))  # Output: 1
print(operator.mod(5, 3))       # Output: 2
print(operator.pow(5, 3))       # Output: 125

# Comparison operators
print(operator.eq(5, 5))   # Output: True
print(operator.ne(5, 3))   # Output: True
print(operator.lt(3, 5))   # Output: True
print(operator.le(5, 5))   # Output: True
print(operator.gt(5, 3))   # Output: True
print(operator.ge(5, 5))   # Output: True

# Logical operators
print(operator.and_(True, False))  # Output: False
print(operator.or_(True, False))   # Output: True
print(operator.not_(True))         # Output: False

# Item and attribute access
my_list = [1, 2, 3, 4, 5]
print(operator.getitem(my_list, 2))  # Output: 3

class Person:
    def __init__(self, name):
        self.name = name

person = Person("Alice")
print(operator.attrgetter("name")(person))  # Output: Alice

# Using operators with higher-order functions
numbers = [1, 2, 3, 4, 5]

# Sum using reduce and operator.add
sum_result = reduce(operator.add, numbers)
print(sum_result)  # Output: 15

# Sort a list of tuples by the second element
data = [("Alice", 25), ("Bob", 20), ("Charlie", 30)]
sorted_data = sorted(data, key=operator.itemgetter(1))
print(sorted_data)  # Output: [('Bob', 20), ('Alice', 25), ('Charlie', 30)]

# Sort a list of objects by an attribute
people = [Person("Alice"), Person("Bob"), Person("Charlie")]
sorted_people = sorted(people, key=operator.attrgetter("name"))
for person in sorted_people:
    print(person.name, end=" ")  # Output: Alice Bob Charlie
```

### `toolz`

The `toolz` library provides a set of utility functions for functional programming.

```python
# Install toolz: pip install toolz
import toolz

# Compose functions
square = lambda x: x ** 2
double = lambda x: x * 2
square_then_double = toolz.compose(double, square)
double_then_square = toolz.compose(square, double)

print(square_then_double(3))  # Output: 18 (double(square(3)) = double(9) = 18)
print(double_then_square(3))  # Output: 36 (square(double(3)) = square(6) = 36)

# Curry functions
def add3(a, b, c):
    return a + b + c

curried_add3 = toolz.curry(add3)
print(curried_add3(1)(2)(3))  # Output: 6
print(curried_add3(1, 2)(3))  # Output: 6

# Pipe data through a sequence of functions
result = toolz.pipe(3, square, double, str)
print(result)  # Output: '18'

# Group data by a key function
data = [('A', 1), ('B', 2), ('A', 3), ('B', 4), ('C', 5)]
grouped = toolz.groupby(lambda x: x[0], data)
print(grouped)  # Output: {'A': [('A', 1), ('A', 3)], 'B': [('B', 2), ('B', 4)], 'C': [('C', 5)]}

# Partition data into chunks
chunks = list(toolz.partition(2, [1, 2, 3, 4, 5]))
print(chunks)  # Output: [(1, 2), (3, 4)]

# Partition all data, including leftovers
chunks_all = list(toolz.partition_all(2, [1, 2, 3, 4, 5]))
print(chunks_all)  # Output: [(1, 2), (3, 4), (5,)]

# Filter a dictionary by its keys
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
filtered = toolz.keyfilter(lambda k: k in ['a', 'c'], my_dict)
print(filtered)  # Output: {'a': 1, 'c': 3}

# Filter a dictionary by its values
filtered = toolz.valfilter(lambda v: v % 2 == 0, my_dict)
print(filtered)  # Output: {'b': 2, 'd': 4}

# Map a function over a dictionary's values
mapped = toolz.valmap(lambda v: v * 2, my_dict)
print(mapped)  # Output: {'a': 2, 'b': 4, 'c': 6, 'd': 8}
```

## Functional Programming Patterns

### Function Composition

```python
def compose(*functions):
    """Compose functions from right to left."""
    def composed(x):
        result = x
        for f in reversed(functions):
            result = f(result)
        return result
    return composed

# Define some functions
def add_one(x):
    return x + 1

def double(x):
    return x * 2

def square(x):
    return x ** 2

# Compose functions
f = compose(square, double, add_one)

# Use the composed function
print(f(5))  # Output: 144 (square(double(add_one(5))) = square(double(6)) = square(12) = 144)
```

### Pipeline Pattern

```python
def pipeline(*functions):
    """Create a pipeline of functions from left to right."""
    def piped(x):
        result = x
        for f in functions:
            result = f(result)
        return result
    return piped

# Define some functions
def add_one(x):
    return x + 1

def double(x):
    return x * 2

def square(x):
    return x ** 2

# Create a pipeline
pipe = pipeline(add_one, double, square)

# Use the pipeline
print(pipe(5))  # Output: 144 (square(double(add_one(5))) = square(double(6)) = square(12) = 144)
```

### Monads

Monads are a design pattern that allows for sequential composition of functions that can handle side effects.

```python
class Maybe:
    """A simple Maybe monad implementation."""
    def __init__(self, value):
        self.value = value
    
    @staticmethod
    def unit(value):
        return Maybe(value)
    
    def bind(self, func):
        if self.value is None:
            return Maybe(None)
        return func(self.value)
    
    def __str__(self):
        return f"Maybe({self.value})"

# Functions that return Maybe values
def safe_divide(x, y):
    if y == 0:
        return Maybe(None)
    return Maybe(x / y)

def safe_sqrt(x):
    if x < 0:
        return Maybe(None)
    import math
    return Maybe(math.sqrt(x))

# Use the Maybe monad
def compute(x, y):
    return Maybe(x).bind(lambda a: 
                 Maybe(y).bind(lambda b: 
                 safe_divide(a, b).bind(lambda c: 
                 safe_sqrt(c))))

print(compute(16, 4))    # Output: Maybe(2.0)
print(compute(16, 0))    # Output: Maybe(None)
print(compute(-16, 4))   # Output: Maybe(None)
```

## Best Practices

### Prefer Pure Functions

```python
# Impure function
total = 0

def add_to_total(x):
    global total
    total += x
    return total

# Pure function
def add(x, y):
    return x + y

# Use pure functions with reduce for accumulation
from functools import reduce

numbers = [1, 2, 3, 4, 5]
total = reduce(add, numbers, 0)
print(total)  # Output: 15
```

### Use List Comprehensions

```python
# Imperative style
squares = []
for i in range(10):
    if i % 2 == 0:
        squares.append(i ** 2)

# Functional style with list comprehension
squares = [i ** 2 for i in range(10) if i % 2 == 0]
print(squares)  # Output: [0, 4, 16, 36, 64]
```

### Use Generator Expressions

```python
# List comprehension (eager evaluation)
squares = [i ** 2 for i in range(1000000)]

# Generator expression (lazy evaluation)
squares_gen = (i ** 2 for i in range(1000000))

# Process only the first 5 elements
for i, square in enumerate(squares_gen):
    if i >= 5:
        break
    print(square, end=" ")  # Output: 0 1 4 9 16
```

### Use Higher-Order Functions

```python
# Imperative style
result = []
for x in range(10):
    if x % 2 == 0:
        result.append(x ** 2)

# Functional style with higher-order functions
result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, range(10))))
print(result)  # Output: [0, 4, 16, 36, 64]
```

### Avoid Mutable State

```python
# Function with mutable state (bad practice)
def append_to(element, to=[]):
    to.append(element)
    return to

print(append_to(1))  # Output: [1]
print(append_to(2))  # Output: [1, 2] (unexpected!)

# Function without mutable state (good practice)
def append_to(element, to=None):
    if to is None:
        to = []
    return to + [element]

print(append_to(1))  # Output: [1]
print(append_to(2))  # Output: [2]
```

### Use Immutable Data Structures

```python
from collections import namedtuple

# Immutable Point class using namedtuple
Point = namedtuple('Point', ['x', 'y'])

# Create a point
p1 = Point(1, 2)

# Create a new point with modified coordinates
p2 = p1._replace(x=3)

print(p1)  # Output: Point(x=1, y=2)
print(p2)  # Output: Point(x=3, y=2)
```

### Use Function Composition

```python
from functools import reduce

def compose(*functions):
    """Compose functions from right to left."""
    return reduce(lambda f, g: lambda x: f(g(x)), functions)

# Define some functions
add_one = lambda x: x + 1
double = lambda x: x * 2
square = lambda x: x ** 2

# Compose functions
f = compose(square, double, add_one)

# Use the composed function
print(f(5))  # Output: 144 (square(double(add_one(5))) = square(double(6)) = square(12) = 144)
```

## Common Pitfalls

### Mutable Default Arguments

```python
# Bad practice
def append_to(element, to=[]):
    to.append(element)
    return to

print(append_to(1))  # Output: [1]
print(append_to(2))  # Output: [1, 2] (unexpected!)

# Good practice
def append_to(element, to=None):
    if to is None:
        to = []
    to.append(element)
    return to

print(append_to(1))  # Output: [1]
print(append_to(2))  # Output: [2]
```

### Recursion Depth Limit

```python
# This will raise RecursionError for large n
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

try:
    print(factorial(1000))  # This will raise RecursionError
except RecursionError as e:
    print(f"Error: {e}")  # Output: Error: maximum recursion depth exceeded

# Use tail recursion with a wrapper function
def factorial(n):
    def factorial_tail(n, accumulator=1):
        if n == 0 or n == 1:
            return accumulator
        else:
            return factorial_tail(n - 1, n * accumulator)
    
    return factorial_tail(n)

# Or use a loop
def factorial_loop(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(factorial_loop(1000))  # This will work for large n
```

### Performance Considerations

```python
import time

# Measure the time taken by a function
def time_it(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.6f} seconds")
    return result

# Recursive Fibonacci (inefficient)
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Memoized Fibonacci (efficient)
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_memoized(n):
    if n <= 1:
        return n
    return fibonacci_memoized(n-1) + fibonacci_memoized(n-2)

# Iterative Fibonacci (efficient)
def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Compare performance
n = 30
print("Recursive:")
time_it(fibonacci_recursive, n)

print("\nMemoized:")
time_it(fibonacci_memoized, n)

print("\nIterative:")
time_it(fibonacci_iterative, n)
```

### Overusing Lambda Functions

```python
# Hard to read
result = list(filter(lambda x: x % 2 == 0, map(lambda x: x ** 2, range(10))))

# More readable
def is_even(x):
    return x % 2 == 0

def square(x):
    return x ** 2

result = list(filter(is_even, map(square, range(10))))

# Even more readable with list comprehension
result = [x ** 2 for x in range(10) if (x ** 2) % 2 == 0]

print(result)  # Output: [0, 4, 16, 36, 64]
```

## Next Steps

Now that you understand functional programming in Python, you're ready to move on to [Decorators & Generators](../16_Decorators_Generators/README.md).