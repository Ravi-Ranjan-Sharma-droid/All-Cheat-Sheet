# Tuples in Python

Tuples are ordered, immutable collections of elements in Python. They are similar to lists but with a key difference: once created, tuples cannot be modified. This immutability makes tuples useful for representing fixed collections of items.

## Creating Tuples

There are several ways to create tuples in Python:

### Using Parentheses

```python
# Empty tuple
empty_tuple = ()

# Tuple with one element (note the comma)
single_element = (1,)

# Tuple with multiple elements
numbers = (1, 2, 3, 4, 5)
fruits = ("apple", "banana", "cherry")

# Mixed data types
mixed = (1, "hello", 3.14, True)

# Nested tuples
nested = ((1, 2), (3, 4), (5, 6))
```

### Using the `tuple()` Constructor

```python
# Empty tuple
empty_tuple = tuple()

# Convert other iterables to tuples
tuple_from_list = tuple([1, 2, 3])       # (1, 2, 3)
tuple_from_string = tuple("hello")       # ('h', 'e', 'l', 'l', 'o')
tuple_from_range = tuple(range(5))       # (0, 1, 2, 3, 4)
tuple_from_dict = tuple({1: 'a', 2: 'b'})  # (1, 2) (only keys are used)
```

### Using Tuple Packing

Tuple packing is when Python automatically creates a tuple from a sequence of values.

```python
# Tuple packing
coordinates = 10, 20, 30  # Creates the tuple (10, 20, 30)

# Tuple unpacking
x, y, z = coordinates  # x = 10, y = 20, z = 30
```

## Accessing Tuple Elements

### Indexing

Tuple elements are accessed using zero-based indexing, just like lists.

```python
fruits = ("apple", "banana", "cherry", "date")

# Positive indexing (from the beginning)
print(fruits[0])  # "apple"
print(fruits[2])  # "cherry"

# Negative indexing (from the end)
print(fruits[-1])  # "date"
print(fruits[-3])  # "banana"

# Attempting to modify a tuple element will raise an error
# fruits[0] = "apricot"  # TypeError: 'tuple' object does not support item assignment
```

### Slicing

Slicing works the same way as with lists, allowing you to extract portions of a tuple.

```python
fruits = ("apple", "banana", "cherry", "date", "elderberry")

# Basic slicing: tuple[start:stop]
print(fruits[1:4])    # ("banana", "cherry", "date")

# Omitting start (defaults to 0)
print(fruits[:3])     # ("apple", "banana", "cherry")

# Omitting stop (defaults to len(tuple))
print(fruits[2:])     # ("cherry", "date", "elderberry")

# Negative indices in slicing
print(fruits[1:-1])   # ("banana", "cherry", "date")

# Step parameter: tuple[start:stop:step]
print(fruits[::2])    # ("apple", "cherry", "elderberry")
print(fruits[1:5:2])  # ("banana", "date")

# Reversing a tuple
print(fruits[::-1])   # ("elderberry", "date", "cherry", "banana", "apple")
```

## Tuple Methods

Tuples have only two built-in methods, reflecting their immutable nature:

### `count()`

Returns the number of occurrences of a specified value.

```python
numbers = (1, 2, 3, 2, 4, 2, 5)
count = numbers.count(2)
print(count)  # 3
```

### `index()`

Returns the index of the first occurrence of a specified value.

```python
fruits = ("apple", "banana", "cherry", "banana", "date")

# Find the index of "banana"
index = fruits.index("banana")
print(index)  # 1

# Find the index of "banana" starting from index 2
index = fruits.index("banana", 2)
print(index)  # 3

# Find the index of "banana" between indices 2 and 4
index = fruits.index("banana", 2, 4)
print(index)  # 3

# Attempting to find a non-existent value will raise a ValueError
# index = fruits.index("grape")  # ValueError: tuple.index(x): x not in tuple
```

## Tuple Operations

### Concatenation

You can concatenate tuples using the `+` operator to create a new tuple.

```python
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Using the + operator
combined = tuple1 + tuple2
print(combined)  # (1, 2, 3, 4, 5, 6)
```

### Repetition

You can repeat a tuple using the `*` operator.

```python
tuple1 = (1, 2, 3)

# Using the * operator
repeated = tuple1 * 3
print(repeated)  # (1, 2, 3, 1, 2, 3, 1, 2, 3)
```

### Membership Testing

You can check if an element exists in a tuple using the `in` operator.

```python
fruits = ("apple", "banana", "cherry")

# Using the in operator
print("banana" in fruits)  # True
print("grape" in fruits)   # False

# Using the not in operator
print("grape" not in fruits)  # True
```

### Tuple Unpacking

Tuple unpacking allows you to assign the elements of a tuple to multiple variables at once.

```python
# Basic unpacking
coordinates = (10, 20, 30)
x, y, z = coordinates
print(x, y, z)  # 10 20 30

# Unpacking with * to collect remaining elements
fruits = ("apple", "banana", "cherry", "date", "elderberry")
first, second, *rest = fruits
print(first)   # "apple"
print(second)  # "banana"
print(rest)    # ["cherry", "date", "elderberry"] (note: this is a list, not a tuple)

# Unpacking with * in the middle
first, *middle, last = fruits
print(first)   # "apple"
print(middle)  # ["banana", "cherry", "date"]
print(last)    # "elderberry"

# Ignoring values with _
a, _, c = (1, 2, 3)  # _ is a convention for values you don't need
print(a, c)  # 1 3
```

## Immutability and Its Implications

Tuples are immutable, which means once created, their elements cannot be changed, added, or removed. This has several implications:

### Advantages of Immutability

1. **Hashability**: Tuples can be used as dictionary keys or elements in a set, unlike lists.
2. **Safety**: Immutability prevents accidental modification of data.
3. **Performance**: In some cases, tuples can be more memory-efficient and faster than lists.

```python
# Tuples as dictionary keys
coordinates = {(0, 0): "origin", (1, 0): "right", (0, 1): "up"}
print(coordinates[(0, 0)])  # "origin"

# This would raise an error
# coordinates[[0, 0]] = "origin"  # TypeError: unhashable type: 'list'
```

### Working with Immutable Tuples

While you can't modify a tuple directly, you can create a new tuple based on an existing one.

```python
fruits = ("apple", "banana", "cherry")

# Create a new tuple with an additional element
fruits_extended = fruits + ("date",)
print(fruits_extended)  # ("apple", "banana", "cherry", "date")

# Create a new tuple with a replaced element
index = 1  # index of the element to replace
fruits_modified = fruits[:index] + ("blueberry",) + fruits[index+1:]
print(fruits_modified)  # ("apple", "blueberry", "cherry")
```

### Nested Tuples with Mutable Elements

While tuples themselves are immutable, they can contain mutable objects like lists, which can be modified.

```python
# Tuple containing a list
tuple_with_list = (1, 2, [3, 4])

# Cannot modify the tuple itself
# tuple_with_list[0] = 5  # TypeError: 'tuple' object does not support item assignment

# But can modify the mutable object inside the tuple
tuple_with_list[2][0] = 5
print(tuple_with_list)  # (1, 2, [5, 4])
```

## Named Tuples

Named tuples are a subclass of tuples that allow you to access elements by name as well as by index. They are defined in the `collections` module.

```python
from collections import namedtuple

# Define a named tuple class
Person = namedtuple('Person', ['name', 'age', 'city'])

# Create an instance of the named tuple
alice = Person(name="Alice", age=30, city="New York")

# Access elements by name
print(alice.name)  # "Alice"
print(alice.age)   # 30
print(alice.city)  # "New York"

# Access elements by index
print(alice[0])    # "Alice"
print(alice[1])    # 30
print(alice[2])    # "New York"

# Unpack the named tuple
name, age, city = alice
print(name, age, city)  # "Alice" 30 "New York"

# Convert to dictionary
alice_dict = alice._asdict()
print(alice_dict)  # {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Create a new instance with one field replaced
bob = alice._replace(name="Bob")
print(bob)  # Person(name='Bob', age=30, city='New York')
```

## Common Use Cases for Tuples

### Returning Multiple Values from Functions

Tuples are commonly used to return multiple values from a function.

```python
def get_dimensions():
    return 500, 300  # Returns a tuple (500, 300)

# Unpack the returned tuple
width, height = get_dimensions()
print(f"Width: {width}, Height: {height}")  # Width: 500, Height: 300

# Or store the tuple directly
dimensions = get_dimensions()
print(dimensions)  # (500, 300)
```

### Function Arguments Unpacking

Tuples can be unpacked to pass multiple arguments to a function.

```python
def add(a, b, c):
    return a + b + c

numbers = (1, 2, 3)
result = add(*numbers)  # Unpacks the tuple to pass as separate arguments
print(result)  # 6
```

### Representing Fixed Data Structures

Tuples are ideal for representing fixed collections of data where each position has a specific meaning.

```python
# Representing a point in 2D space
point = (10, 20)
x, y = point

# Representing RGB colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Representing a record
employee = ("John Doe", 30, "Software Engineer")
name, age, position = employee
```

### Swapping Variables

Tuples can be used to swap variables without using a temporary variable.

```python
a = 5
b = 10

# Swap values using tuple packing and unpacking
a, b = b, a

print(a, b)  # 10 5
```

## Performance Considerations

### Tuples vs. Lists

Tuples are generally more memory-efficient and slightly faster than lists for similar operations due to their immutability.

```python
import sys

# Compare memory usage
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)

print(sys.getsizeof(my_list))   # Typically larger
print(sys.getsizeof(my_tuple))  # Typically smaller

# Compare creation time
import timeit

list_time = timeit.timeit(stmt="[1, 2, 3, 4, 5]", number=1000000)
tuple_time = timeit.timeit(stmt="(1, 2, 3, 4, 5)", number=1000000)

print(f"List creation time: {list_time}")
print(f"Tuple creation time: {tuple_time}")
```

## Best Practices

### When to Use Tuples vs. Lists

- Use tuples for heterogeneous data (different types) that belongs together
- Use tuples for data that shouldn't change
- Use tuples when you need a hashable sequence (for dict keys or set elements)
- Use lists when you need a homogeneous sequence that might change

```python
# Good tuple use cases
point = (10, 20)  # x, y coordinates
person = ("John", 30, "New York")  # name, age, city
rgb_color = (255, 0, 0)  # red, green, blue values

# Good list use cases
scores = [85, 90, 78, 92, 88]  # collection of similar items that might change
commands = ["start", "stop", "restart"]  # collection of options that might be extended
```

### Using Named Tuples for Clarity

When a tuple represents a specific entity with multiple attributes, consider using named tuples for better readability.

```python
from collections import namedtuple

# Instead of this
person = ("John", 30, "New York")
name, age, city = person

# Use this
Person = namedtuple('Person', ['name', 'age', 'city'])
person = Person("John", 30, "New York")
print(person.name, person.age, person.city)
```

### Tuple Unpacking for Multiple Assignments

Use tuple unpacking to make multiple assignments more readable.

```python
# Instead of this
user_info = get_user_info()
username = user_info[0]
email = user_info[1]
role = user_info[2]

# Use this
username, email, role = get_user_info()
```

## Common Pitfalls

### Single-Element Tuple Syntax

Remember to include a trailing comma when creating a single-element tuple.

```python
# This is not a tuple, it's just a value in parentheses
not_a_tuple = (42)
print(type(not_a_tuple))  # <class 'int'>

# This is a tuple with one element
single_element_tuple = (42,)
print(type(single_element_tuple))  # <class 'tuple'>
```

### Modifying Mutable Elements in Tuples

Be careful with tuples containing mutable objects, as these objects can still be modified.

```python
# Tuple with a mutable list
data = (1, 2, [3, 4])

# This modifies the list inside the tuple
data[2].append(5)
print(data)  # (1, 2, [3, 4, 5])

# If you need true immutability, consider freezing all nested structures
import copy
frozen_data = copy.deepcopy(data)
# And possibly convert any lists to tuples
frozen_data = tuple(tuple(x) if isinstance(x, list) else x for x in frozen_data)
```

## Next Steps

Now that you understand tuples in Python, you're ready to move on to [Sets](../08_Sets/README.md).