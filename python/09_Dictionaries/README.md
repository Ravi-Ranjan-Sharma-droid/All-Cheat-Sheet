# Dictionaries in Python

Dictionaries are unordered collections of key-value pairs in Python. They are optimized for retrieving data when the key is known and provide a flexible way to map keys to values.

## Creating Dictionaries

There are several ways to create dictionaries in Python:

### Using Curly Braces

```python
# Empty dictionary
empty_dict = {}

# Dictionary with string keys
person = {"name": "John", "age": 30, "city": "New York"}

# Dictionary with various key types
mixed_keys = {"name": "John", 42: "answer", (1, 2): "tuple key"}

# Nested dictionaries
employee = {
    "name": "John",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "zip": "10001"
    }
}
```

### Using the `dict()` Constructor

```python
# Empty dictionary
empty_dict = dict()

# From keyword arguments (keys must be valid Python identifiers)
person = dict(name="John", age=30, city="New York")

# From a list of tuples
person = dict([("name", "John"), ("age", 30), ("city", "New York")])

# From two lists using zip()
keys = ["name", "age", "city"]
values = ["John", 30, "New York"]
person = dict(zip(keys, values))
```

### Using Dictionary Comprehensions

Dictionary comprehensions provide a concise way to create dictionaries.

```python
# Basic dictionary comprehension
squares = {x: x**2 for x in range(6)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Dictionary comprehension with condition
even_squares = {x: x**2 for x in range(6) if x % 2 == 0}
print(even_squares)  # {0: 0, 2: 4, 4: 16}

# Creating a dictionary from two lists
keys = ["apple", "banana", "cherry"]
values = [0.5, 0.3, 0.7]
fruit_prices = {k: v for k, v in zip(keys, values)}
print(fruit_prices)  # {'apple': 0.5, 'banana': 0.3, 'cherry': 0.7}
```

## Dictionary Properties

Dictionaries have several important properties:

### Keys Must Be Hashable

Dictionary keys must be hashable (immutable). This means you can use strings, numbers, tuples (if they contain only hashable types), and frozensets as keys, but not lists, dictionaries, or regular sets.

```python
# Valid dictionary keys
valid_dict = {
    "string": 1,
    42: 2,
    (1, 2): 3,
    frozenset([1, 2, 3]): 4
}

# Invalid dictionary keys would raise errors
# invalid_dict = {[1, 2]: "value"}  # TypeError: unhashable type: 'list'
# invalid_dict = {{1: 2}: "value"}  # TypeError: unhashable type: 'dict'
# invalid_dict = {{1, 2}: "value"}  # TypeError: unhashable type: 'set'
```

### Unique Keys

Dictionaries cannot have duplicate keys. If you try to add a key that already exists, it will overwrite the existing value.

```python
person = {"name": "John", "age": 30, "name": "Jane"}
print(person)  # {"name": "Jane", "age": 30}
```

### Mutable

Dictionaries are mutable, which means you can add, modify, or remove key-value pairs after creation.

```python
person = {"name": "John", "age": 30}

# Add a new key-value pair
person["city"] = "New York"

# Modify an existing value
person["age"] = 31

# Remove a key-value pair
del person["age"]

print(person)  # {"name": "John", "city": "New York"}
```

### Ordered (Python 3.7+)

As of Python 3.7, dictionaries maintain insertion order. This means that when you iterate through a dictionary, the keys will be returned in the same order they were inserted.

```python
# In Python 3.7 and later, order is preserved
person = {"name": "John", "age": 30, "city": "New York"}
for key in person:
    print(key)  # Outputs: name, age, city (in that order)
```

## Accessing Dictionary Elements

### Using Keys

You can access dictionary values using their keys.

```python
person = {"name": "John", "age": 30, "city": "New York"}

# Access a value using its key
print(person["name"])  # "John"

# This would raise a KeyError if the key doesn't exist
# print(person["country"])  # KeyError: 'country'
```

### Using `get()` Method

The `get()` method allows you to access a value by its key with a default value if the key doesn't exist.

```python
person = {"name": "John", "age": 30, "city": "New York"}

# Access a value with get()
print(person.get("name"))  # "John"

# Access a non-existent key with get()
print(person.get("country"))  # None (default)

# Specify a default value
print(person.get("country", "USA"))  # "USA"
```

### Nested Dictionaries

You can access values in nested dictionaries by chaining keys.

```python
employee = {
    "name": "John",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "zip": "10001"
    }
}

# Access a nested value
print(employee["address"]["city"])  # "New York"

# Using get() for nested dictionaries
street = employee.get("address", {}).get("street")
print(street)  # "123 Main St"

# This won't raise an error if "address" doesn't exist
country = employee.get("address", {}).get("country")
print(country)  # None
```

## Modifying Dictionaries

### Adding or Updating Elements

```python
person = {"name": "John", "age": 30}

# Add a new key-value pair
person["city"] = "New York"

# Update an existing value
person["age"] = 31

print(person)  # {"name": "John", "age": 31, "city": "New York"}

# Add or update multiple key-value pairs using update()
person.update({"age": 32, "country": "USA", "email": "john@example.com"})
print(person)  # {"name": "John", "age": 32, "city": "New York", "country": "USA", "email": "john@example.com"}
```

### Removing Elements

```python
person = {"name": "John", "age": 30, "city": "New York", "email": "john@example.com"}

# Remove a key-value pair using del
del person["age"]
print(person)  # {"name": "John", "city": "New York", "email": "john@example.com"}

# Remove and return a value using pop()
email = person.pop("email")
print(email)  # "john@example.com"
print(person)  # {"name": "John", "city": "New York"}

# Remove and return the last inserted key-value pair using popitem() (Python 3.7+)
last_item = person.popitem()  # Returns ("city", "New York")
print(last_item)  # ("city", "New York")
print(person)  # {"name": "John"}

# Remove all elements
person.clear()
print(person)  # {}
```

## Dictionary Methods

Python dictionaries provide many useful methods for working with key-value pairs.

### Accessing Methods

```python
person = {"name": "John", "age": 30, "city": "New York"}

# keys(): Return a view of all keys
keys = person.keys()
print(keys)  # dict_keys(['name', 'age', 'city'])

# values(): Return a view of all values
values = person.values()
print(values)  # dict_values(['John', 30, 'New York'])

# items(): Return a view of all key-value pairs as tuples
items = person.items()
print(items)  # dict_items([('name', 'John'), ('age', 30), ('city', 'New York')])

# Note: These views are dynamic and reflect changes to the dictionary
person["country"] = "USA"
print(keys)  # dict_keys(['name', 'age', 'city', 'country'])
```

### Copying Dictionaries

```python
person = {"name": "John", "age": 30, "address": {"city": "New York"}}

# Shallow copy using copy()
person_copy = person.copy()
person_copy["name"] = "Jane"
print(person)       # {"name": "John", "age": 30, "address": {"city": "New York"}}
print(person_copy)  # {"name": "Jane", "age": 30, "address": {"city": "New York"}}

# Nested objects are shared in a shallow copy
person_copy["address"]["city"] = "Boston"
print(person)       # {"name": "John", "age": 30, "address": {"city": "Boston"}}
print(person_copy)  # {"name": "Jane", "age": 30, "address": {"city": "Boston"}}

# Deep copy
import copy
person = {"name": "John", "age": 30, "address": {"city": "New York"}}
person_deep_copy = copy.deepcopy(person)
person_deep_copy["address"]["city"] = "Boston"
print(person)           # {"name": "John", "age": 30, "address": {"city": "New York"}}
print(person_deep_copy) # {"name": "John", "age": 30, "address": {"city": "Boston"}}
```

### Other Methods

```python
# setdefault(): Get a value or set a default if the key doesn't exist
person = {"name": "John", "age": 30}
email = person.setdefault("email", "john@example.com")
print(email)   # "john@example.com"
print(person)  # {"name": "John", "age": 30, "email": "john@example.com"}

# fromkeys(): Create a dictionary with specified keys and a default value
keys = ["name", "age", "city"]
default_dict = dict.fromkeys(keys, "unknown")
print(default_dict)  # {"name": "unknown", "age": "unknown", "city": "unknown"}

# Without a default value, None is used
default_dict = dict.fromkeys(keys)
print(default_dict)  # {"name": None, "age": None, "city": None}
```

## Iterating Through Dictionaries

### Iterating Over Keys

```python
person = {"name": "John", "age": 30, "city": "New York"}

# Iterate over keys (default)
for key in person:
    print(key)  # Outputs: name, age, city

# Explicitly iterate over keys
for key in person.keys():
    print(key)  # Outputs: name, age, city
```

### Iterating Over Values

```python
person = {"name": "John", "age": 30, "city": "New York"}

# Iterate over values
for value in person.values():
    print(value)  # Outputs: John, 30, New York
```

### Iterating Over Key-Value Pairs

```python
person = {"name": "John", "age": 30, "city": "New York"}

# Iterate over key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")  # Outputs: name: John, age: 30, city: New York
```

## Dictionary Comprehensions

Dictionary comprehensions provide a concise way to create dictionaries based on existing iterables.

```python
# Create a dictionary of squares
squares = {x: x**2 for x in range(6)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Create a dictionary with a condition
even_squares = {x: x**2 for x in range(6) if x % 2 == 0}
print(even_squares)  # {0: 0, 2: 4, 4: 16}

# Create a dictionary from two lists
keys = ["apple", "banana", "cherry"]
values = [0.5, 0.3, 0.7]
fruit_prices = {k: v for k, v in zip(keys, values)}
print(fruit_prices)  # {"apple": 0.5, "banana": 0.3, "cherry": 0.7}

# Swap keys and values (assuming values are unique)
original = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original.items()}
print(swapped)  # {1: "a", 2: "b", 3: "c"}

# Filtering and transforming
data = {"a": 1, "b": 2, "c": 3, "d": 4}
filtered = {k: v**2 for k, v in data.items() if v % 2 == 0}
print(filtered)  # {"b": 4, "d": 16}
```

## Common Use Cases for Dictionaries

### Counting Elements

Dictionaries are excellent for counting occurrences of elements.

```python
# Count occurrences of words in a text
text = "the quick brown fox jumps over the lazy dog"
words = text.split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)  # {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}

# More concise approach using get()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

# Even more concise using Counter
from collections import Counter
word_count = Counter(words)
print(word_count)  # Counter({'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1})
```

### Grouping Data

Dictionaries are useful for grouping related data.

```python
# Group people by city
people = [
    {"name": "John", "city": "New York"},
    {"name": "Jane", "city": "Boston"},
    {"name": "Bob", "city": "New York"},
    {"name": "Alice", "city": "Chicago"},
    {"name": "Mike", "city": "Boston"}
]

# Group by city
by_city = {}
for person in people:
    city = person["city"]
    if city not in by_city:
        by_city[city] = []
    by_city[city].append(person["name"])

print(by_city)  # {'New York': ['John', 'Bob'], 'Boston': ['Jane', 'Mike'], 'Chicago': ['Alice']}

# Using setdefault
by_city = {}
for person in people:
    by_city.setdefault(person["city"], []).append(person["name"])

# Using defaultdict
from collections import defaultdict
by_city = defaultdict(list)
for person in people:
    by_city[person["city"]].append(person["name"])
```

### Caching/Memoization

Dictionaries are perfect for caching results of expensive operations.

```python
# Without caching
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# With caching using a dictionary
def fibonacci_cached(n, cache={}):
    if n in cache:
        return cache[n]
    if n <= 1:
        result = n
    else:
        result = fibonacci_cached(n-1, cache) + fibonacci_cached(n-2, cache)
    cache[n] = result
    return result

# Using functools.lru_cache (Python 3.2+)
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_lru(n):
    if n <= 1:
        return n
    return fibonacci_lru(n-1) + fibonacci_lru(n-2)
```

### Representing Objects

Dictionaries can represent objects with attributes.

```python
# Represent a person as a dictionary
person = {
    "name": "John",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "zip": "10001"
    },
    "phone_numbers": ["555-1234", "555-5678"]
}

# Access attributes
print(person["name"])  # "John"
print(person["address"]["city"])  # "New York"
print(person["phone_numbers"][0])  # "555-1234"
```

## Specialized Dictionary Types

Python's `collections` module provides specialized dictionary types for specific use cases.

### `defaultdict`

A `defaultdict` automatically provides a default value for keys that don't exist.

```python
from collections import defaultdict

# defaultdict with int as default factory
word_count = defaultdict(int)
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]

for word in words:
    word_count[word] += 1  # No need to check if key exists

print(word_count)  # defaultdict(<class 'int'>, {'apple': 3, 'banana': 2, 'cherry': 1})

# defaultdict with list as default factory
by_category = defaultdict(list)
items = [("fruit", "apple"), ("vegetable", "carrot"), ("fruit", "banana")]

for category, item in items:
    by_category[category].append(item)  # No need to check if key exists

print(by_category)  # defaultdict(<class 'list'>, {'fruit': ['apple', 'banana'], 'vegetable': ['carrot']})
```

### `OrderedDict`

An `OrderedDict` remembers the order in which keys were inserted. Note that as of Python 3.7, regular dictionaries also maintain insertion order, but `OrderedDict` provides additional functionality.

```python
from collections import OrderedDict

# Create an OrderedDict
ordered = OrderedDict()
ordered["first"] = 1
ordered["second"] = 2
ordered["third"] = 3

print(ordered)  # OrderedDict([('first', 1), ('second', 2), ('third', 3)])

# Regular dict in Python 3.7+ also maintains order
regular = {}
regular["first"] = 1
regular["second"] = 2
regular["third"] = 3

print(regular)  # {'first': 1, 'second': 2, 'third': 3}

# But OrderedDict has additional functionality
ordered.move_to_end("first")
print(ordered)  # OrderedDict([('second', 2), ('third', 3), ('first', 1)])

# And it considers order when comparing for equality
dict1 = OrderedDict([('a', 1), ('b', 2)])
dict2 = OrderedDict([('b', 2), ('a', 1)])
print(dict1 == dict2)  # False (different order)

regular1 = {'a': 1, 'b': 2}
regular2 = {'b': 2, 'a': 1}
print(regular1 == regular2)  # True (order doesn't matter for regular dicts)
```

### `Counter`

A `Counter` is a dictionary subclass for counting hashable objects.

```python
from collections import Counter

# Count occurrences of elements
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
word_count = Counter(words)

print(word_count)  # Counter({'apple': 3, 'banana': 2, 'cherry': 1})

# Most common elements
print(word_count.most_common(2))  # [('apple', 3), ('banana', 2)]

# Update counts
more_words = ["apple", "date", "elderberry"]
word_count.update(more_words)
print(word_count)  # Counter({'apple': 4, 'banana': 2, 'cherry': 1, 'date': 1, 'elderberry': 1})

# Arithmetic operations
c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)
print(c1 + c2)  # Counter({'a': 4, 'b': 3})
print(c1 - c2)  # Counter({'a': 2})
```

## Performance Considerations

### Time Complexity

Dictionary operations have the following average time complexities:

- Access by key (`d[key]`): O(1)
- Insertion (`d[key] = value`): O(1)
- Deletion (`del d[key]`): O(1)
- Membership testing (`key in d`): O(1)

This makes dictionaries much more efficient than lists for lookups by key.

```python
import time

# Compare lookup performance
large_list = [(i, f"value_{i}") for i in range(1000000)]
large_dict = {i: f"value_{i}" for i in range(1000000)}
target = 999999

# Time for list lookup
start = time.time()
for item in large_list:
    if item[0] == target:
        result = item[1]
        break
list_time = time.time() - start
print(f"List lookup time: {list_time:.6f} seconds")

# Time for dictionary lookup
start = time.time()
result = large_dict[target]
dict_time = time.time() - start
print(f"Dictionary lookup time: {dict_time:.6f} seconds")

# The dictionary is typically orders of magnitude faster
```

### Memory Usage

Dictionaries typically use more memory than lists with the same number of elements due to the hash table implementation.

```python
import sys

# Compare memory usage
my_list = [(i, f"value_{i}") for i in range(1000)]
my_dict = {i: f"value_{i}" for i in range(1000)}

list_size = sys.getsizeof(my_list) + sum(sys.getsizeof(i) + sys.getsizeof(f"value_{i}") for i in range(1000))
dict_size = sys.getsizeof(my_dict)

print(f"List size: {list_size} bytes")
print(f"Dictionary size: {dict_size} bytes")
```

## Best Practices

### When to Use Dictionaries

- Use dictionaries when you need to associate values with keys
- Use dictionaries for fast lookups by key
- Use dictionaries for counting and grouping data
- Use dictionaries for representing objects with named attributes

```python
# Good use cases for dictionaries
user_settings = {"theme": "dark", "notifications": True}  # Settings with names
phone_book = {"John": "555-1234", "Jane": "555-5678"}  # Lookup by name
word_count = {"apple": 3, "banana": 2, "cherry": 1}  # Counting occurrences
```

### When Not to Use Dictionaries

- Don't use dictionaries when you need a sequence with a specific order (use lists)
- Don't use dictionaries when you need duplicate keys (use a list of tuples)
- Don't use dictionaries when you need to perform numerical operations on the data (use NumPy arrays)

```python
# Cases where dictionaries are not appropriate
ordered_items = [(1, "first"), (2, "second"), (3, "third")]  # Order matters
duplicates = [("fruit", "apple"), ("fruit", "banana")]  # Duplicate keys
numerical_data = [1, 2, 3, 4, 5]  # For numerical operations
```

### Using Dictionary Comprehensions Effectively

Dictionary comprehensions can make your code more concise and readable.

```python
# Instead of this
squares = {}
for x in range(6):
    squares[x] = x**2

# Use this
squares = {x: x**2 for x in range(6)}
```

### Handling Missing Keys

Use `get()` or `setdefault()` to handle missing keys gracefully.

```python
# Instead of this
if key in my_dict:
    value = my_dict[key]
else:
    value = default_value

# Use this
value = my_dict.get(key, default_value)

# Or if you want to update the dictionary
value = my_dict.setdefault(key, default_value)
```

### Using `defaultdict` for Grouping

Use `defaultdict` when you need to group data by a key.

```python
# Instead of this
groups = {}
for item in data:
    key = item["category"]
    if key not in groups:
        groups[key] = []
    groups[key].append(item)

# Use this
from collections import defaultdict
groups = defaultdict(list)
for item in data:
    groups[item["category"]].append(item)
```

## Common Pitfalls

### Modifying a Dictionary While Iterating

Modifying a dictionary while iterating over it can lead to unexpected results or errors.

```python
my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}

# This will raise a RuntimeError
# for key in my_dict:
#     if key == "a":
#         del my_dict[key]  # Modifying during iteration

# Better approach: create a copy to iterate over
for key in list(my_dict.keys()):
    if key == "a":
        del my_dict[key]

print(my_dict)  # {'b': 2, 'c': 3, 'd': 4}
```

### Mutable Keys

Remember that dictionary keys must be hashable. Using mutable objects as keys will raise an error.

```python
# This will raise a TypeError
# my_dict = {[1, 2]: "value"}  # TypeError: unhashable type: 'list'

# Solution: use tuples instead of lists
my_dict = {(1, 2): "value"}
print(my_dict)  # {(1, 2): 'value'}
```

### Nested Dictionary Modifications

Be careful when modifying nested dictionaries, especially when using shallow copies.

```python
original = {"name": "John", "data": {"age": 30, "city": "New York"}}
copy = original.copy()  # Shallow copy

# This modifies both dictionaries
copy["data"]["age"] = 31
print(original)  # {"name": "John", "data": {"age": 31, "city": "New York"}}
print(copy)      # {"name": "John", "data": {"age": 31, "city": "New York"}}

# Use deepcopy for independent copies
import copy
original = {"name": "John", "data": {"age": 30, "city": "New York"}}
deep_copy = copy.deepcopy(original)
deep_copy["data"]["age"] = 31
print(original)  # {"name": "John", "data": {"age": 30, "city": "New York"}}
print(deep_copy) # {"name": "John", "data": {"age": 31, "city": "New York"}}
```

### Key Errors

Accessing a non-existent key with square brackets raises a `KeyError`. Use `get()` to avoid this.

```python
my_dict = {"a": 1, "b": 2}

# This will raise a KeyError
# value = my_dict["c"]  # KeyError: 'c'

# Use get() to avoid KeyError
value = my_dict.get("c")  # None
value = my_dict.get("c", 0)  # 0 (custom default)
```

## Next Steps

Now that you understand dictionaries in Python, you're ready to move on to [String Manipulation](../10_String_Manipulation/README.md).