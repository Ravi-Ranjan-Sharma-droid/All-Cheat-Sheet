# Sets in Python

Sets are unordered collections of unique elements in Python. They are useful for membership testing, removing duplicates, and performing mathematical set operations like unions, intersections, and differences.

## Creating Sets

There are several ways to create sets in Python:

### Using Curly Braces

```python
# Empty set (cannot use {} as that creates an empty dictionary)
empty_set = set()

# Set with elements
numbers = {1, 2, 3, 4, 5}
fruits = {"apple", "banana", "cherry"}

# Duplicates are automatically removed
with_duplicates = {1, 2, 2, 3, 3, 3, 4, 5, 5}
print(with_duplicates)  # {1, 2, 3, 4, 5}

# Mixed data types (elements must be hashable)
mixed = {1, "hello", (1, 2), True}

# This would raise an error because lists are not hashable
# invalid_set = {1, [2, 3]}  # TypeError: unhashable type: 'list'
```

### Using the `set()` Constructor

```python
# Empty set
empty_set = set()

# Convert other iterables to sets
set_from_list = set([1, 2, 3, 2, 1])       # {1, 2, 3}
set_from_tuple = set((1, 2, 3, 2, 1))     # {1, 2, 3}
set_from_string = set("hello")             # {'h', 'e', 'l', 'o'}
set_from_range = set(range(5))             # {0, 1, 2, 3, 4}
set_from_dict = set({1: 'a', 2: 'b'})      # {1, 2} (only keys are used)
```

### Using Set Comprehensions

Set comprehensions provide a concise way to create sets based on existing iterables.

```python
# Basic set comprehension
squares = {x**2 for x in range(10)}
print(squares)  # {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}

# Set comprehension with condition
even_squares = {x**2 for x in range(10) if x % 2 == 0}
print(even_squares)  # {0, 4, 16, 36, 64}
```

## Set Properties

Sets have several important properties:

### Unordered

Sets do not maintain the order of elements. The order may change when elements are added or removed.

```python
fruits = {"apple", "banana", "cherry"}
print(fruits)  # The order is not guaranteed
```

### Unique Elements

Sets automatically eliminate duplicates.

```python
numbers = {1, 2, 2, 3, 3, 3, 4, 5, 5}
print(numbers)  # {1, 2, 3, 4, 5}
```

### Mutable

Sets can be modified after creation (unlike frozensets, which are immutable).

```python
fruits = {"apple", "banana", "cherry"}
fruits.add("date")
fruits.remove("banana")
print(fruits)  # {'apple', 'cherry', 'date'}
```

### Hashable Elements

Set elements must be hashable (immutable). This means you can include numbers, strings, tuples, and frozensets, but not lists, dictionaries, or regular sets.

```python
# Valid set elements
valid_set = {1, "hello", (1, 2), frozenset([1, 2, 3])}

# Invalid set elements would raise errors
# invalid_set = {1, [2, 3]}  # TypeError: unhashable type: 'list'
# invalid_set = {1, {2: 3}}  # TypeError: unhashable type: 'dict'
# invalid_set = {1, {2, 3}}  # TypeError: unhashable type: 'set'
```

## Accessing Set Elements

Since sets are unordered, you cannot access elements by index. Instead, you can iterate through the set or check for membership.

### Iterating Through a Set

```python
fruits = {"apple", "banana", "cherry"}

# Iterate through the set
for fruit in fruits:
    print(fruit)
```

### Checking Membership

```python
fruits = {"apple", "banana", "cherry"}

# Check if an element is in the set
print("banana" in fruits)  # True
print("grape" in fruits)   # False

# Check if an element is not in the set
print("grape" not in fruits)  # True
```

## Set Methods

Python sets provide many methods for adding, removing, and manipulating elements.

### Adding Elements

```python
fruits = {"apple", "banana", "cherry"}

# add(): Add a single element
fruits.add("date")
print(fruits)  # {'apple', 'banana', 'cherry', 'date'}

# update(): Add multiple elements from another iterable
fruits.update(["elderberry", "fig"])
print(fruits)  # {'apple', 'banana', 'cherry', 'date', 'elderberry', 'fig'}

# update() can take multiple iterables
fruits.update(["grape"], ["honeydew"])
print(fruits)  # {'apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew'}
```

### Removing Elements

```python
fruits = {"apple", "banana", "cherry", "date", "elderberry"}

# remove(): Remove a specific element, raises KeyError if not found
fruits.remove("cherry")
print(fruits)  # {'apple', 'banana', 'date', 'elderberry'}

# discard(): Remove a specific element if present, does nothing if not found
fruits.discard("banana")
print(fruits)  # {'apple', 'date', 'elderberry'}
fruits.discard("fig")  # No error, even though "fig" is not in the set

# pop(): Remove and return an arbitrary element, raises KeyError if set is empty
element = fruits.pop()
print(element)  # Could be any element from the set
print(fruits)  # Set without the popped element

# clear(): Remove all elements
fruits.clear()
print(fruits)  # set()
```

### Set Operations

Sets support mathematical set operations like union, intersection, difference, and symmetric difference.

```python
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# union(): Elements in either set
union_result = set1.union(set2)
print(union_result)  # {1, 2, 3, 4, 5, 6, 7, 8}

# intersection(): Elements in both sets
intersection_result = set1.intersection(set2)
print(intersection_result)  # {4, 5}

# difference(): Elements in set1 but not in set2
difference_result = set1.difference(set2)
print(difference_result)  # {1, 2, 3}

# symmetric_difference(): Elements in either set, but not in both
symmetric_difference_result = set1.symmetric_difference(set2)
print(symmetric_difference_result)  # {1, 2, 3, 6, 7, 8}
```

### Set Operators

Set operations can also be performed using operators.

```python
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# | (Union)
union_result = set1 | set2
print(union_result)  # {1, 2, 3, 4, 5, 6, 7, 8}

# & (Intersection)
intersection_result = set1 & set2
print(intersection_result)  # {4, 5}

# - (Difference)
difference_result = set1 - set2
print(difference_result)  # {1, 2, 3}

# ^ (Symmetric Difference)
symmetric_difference_result = set1 ^ set2
print(symmetric_difference_result)  # {1, 2, 3, 6, 7, 8}
```

### Update Methods

Set operations can also be performed in-place, modifying the original set.

```python
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# update() or |=: Update set1 with elements from set1 or set2
set1.update(set2)  # or set1 |= set2
print(set1)  # {1, 2, 3, 4, 5, 6, 7, 8}

# intersection_update() or &=: Update set1 with elements common to set1 and set2
set1 = {1, 2, 3, 4, 5}
set1.intersection_update(set2)  # or set1 &= set2
print(set1)  # {4, 5}

# difference_update() or -=: Update set1 with elements in set1 but not in set2
set1 = {1, 2, 3, 4, 5}
set1.difference_update(set2)  # or set1 -= set2
print(set1)  # {1, 2, 3}

# symmetric_difference_update() or ^=: Update set1 with elements in either set1 or set2, but not both
set1 = {1, 2, 3, 4, 5}
set1.symmetric_difference_update(set2)  # or set1 ^= set2
print(set1)  # {1, 2, 3, 6, 7, 8}
```

### Other Set Methods

```python
set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3}
set3 = {6, 7, 8}

# issubset(): Check if set2 is a subset of set1
print(set2.issubset(set1))  # True
print(set2 <= set1)         # True (operator form)

# issuperset(): Check if set1 is a superset of set2
print(set1.issuperset(set2))  # True
print(set1 >= set2)           # True (operator form)

# isdisjoint(): Check if set1 and set3 have no elements in common
print(set1.isdisjoint(set3))  # True

# copy(): Create a shallow copy of the set
set_copy = set1.copy()
print(set_copy)  # {1, 2, 3, 4, 5}
```

## Frozensets

Frozensets are immutable sets. Once created, you cannot add, remove, or change elements.

```python
# Create a frozenset
frozen = frozenset([1, 2, 3, 4, 5])
print(frozen)  # frozenset({1, 2, 3, 4, 5})

# Frozensets can be elements of regular sets or dictionary keys
set_of_frozensets = {frozenset([1, 2]), frozenset([3, 4])}
dict_with_frozenset_keys = {frozenset([1, 2]): "set1", frozenset([3, 4]): "set2"}

# These would raise errors
# frozen.add(6)  # AttributeError: 'frozenset' object has no attribute 'add'
# frozen.remove(1)  # AttributeError: 'frozenset' object has no attribute 'remove'
```

Frozensets support all the non-modifying operations of regular sets, such as `union()`, `intersection()`, etc.

## Common Use Cases for Sets

### Removing Duplicates

Sets are an efficient way to remove duplicates from a sequence while preserving the remaining elements.

```python
# Remove duplicates from a list
duplicates = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique = list(set(duplicates))
print(unique)  # [1, 2, 3, 4, 5] (order may vary)

# To preserve order in Python 3.7+, use dict.fromkeys()
unique_ordered = list(dict.fromkeys(duplicates))
print(unique_ordered)  # [1, 2, 3, 4, 5] (original order preserved)
```

### Membership Testing

Sets provide O(1) average time complexity for membership testing, making them much faster than lists for this operation.

```python
# Membership testing with a list (O(n) time complexity)
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(5 in my_list)  # True, but has to check each element

# Membership testing with a set (O(1) time complexity)
my_set = set(my_list)
print(5 in my_set)  # True, much faster for large collections
```

### Finding Unique Elements

Sets can be used to find elements that are unique to specific collections.

```python
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Elements in list1 but not in list2
unique_to_list1 = set(list1) - set(list2)
print(unique_to_list1)  # {1, 2, 3}

# Elements in list2 but not in list1
unique_to_list2 = set(list2) - set(list1)
print(unique_to_list2)  # {6, 7, 8}

# Elements that appear in exactly one of the lists
symmetric_difference = set(list1) ^ set(list2)
print(symmetric_difference)  # {1, 2, 3, 6, 7, 8}
```

### Finding Common Elements

Sets can efficiently find common elements between collections.

```python
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
list3 = [5, 6, 7, 8, 9]

# Elements common to list1 and list2
common_elements = set(list1) & set(list2)
print(common_elements)  # {4, 5}

# Elements common to all three lists
common_to_all = set(list1) & set(list2) & set(list3)
print(common_to_all)  # {5}
```

### Removing Specified Items

Sets can be used to remove specific elements from a collection.

```python
original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_remove = {2, 5, 8}

# Remove elements in to_remove from original
filtered = [x for x in original if x not in to_remove]
print(filtered)  # [1, 3, 4, 6, 7, 9, 10]

# Alternative approach using sets
filtered = list(set(original) - to_remove)
print(filtered)  # [1, 3, 4, 6, 7, 9, 10] (order may vary)
```

## Performance Considerations

### Time Complexity

Set operations have the following average time complexities:

- Membership testing (`x in s`): O(1)
- Adding elements (`add()`, `update()`): O(1)
- Removing elements (`remove()`, `discard()`, `pop()`): O(1)
- Set operations (`union()`, `intersection()`, etc.): O(len(s) + len(t))

This makes sets much more efficient than lists for operations like membership testing and removing duplicates.

```python
import time

# Compare membership testing performance
large_list = list(range(1000000))
large_set = set(large_list)
target = 999999

# Time for list membership testing
start = time.time()
result = target in large_list
list_time = time.time() - start
print(f"List membership testing time: {list_time:.6f} seconds")

# Time for set membership testing
start = time.time()
result = target in large_set
set_time = time.time() - start
print(f"Set membership testing time: {set_time:.6f} seconds")

# The set is typically orders of magnitude faster
```

### Memory Usage

Sets typically use more memory than lists with the same elements due to the hash table implementation.

```python
import sys

# Compare memory usage
my_list = list(range(1000))
my_set = set(my_list)

list_size = sys.getsizeof(my_list) + sum(sys.getsizeof(i) for i in my_list)
set_size = sys.getsizeof(my_set)

print(f"List size: {list_size} bytes")
print(f"Set size: {set_size} bytes")
```

## Best Practices

### When to Use Sets

- Use sets when you need to ensure elements are unique
- Use sets for fast membership testing
- Use sets for mathematical set operations (union, intersection, etc.)
- Use sets when the order of elements doesn't matter

```python
# Good use cases for sets
unique_visitors = set()  # Track unique visitors
valid_options = {"yes", "no", "maybe"}  # Valid choices
tags = {"python", "programming", "tutorial"}  # Collection of tags
```

### When Not to Use Sets

- Don't use sets when you need to preserve order (use lists or OrderedDict)
- Don't use sets when you need duplicate elements (use lists)
- Don't use sets when elements are not hashable (use lists)

```python
# Cases where sets are not appropriate
ordered_items = ["first", "second", "third"]  # Order matters
user_inputs = [5, 5, 6, 7, 7, 7]  # Duplicates matter
complex_data = [[1, 2], [3, 4]]  # Elements are not hashable
```

### Using Set Comprehensions Effectively

Set comprehensions can make your code more concise and readable.

```python
# Instead of this
even_squares = set()
for x in range(10):
    if x % 2 == 0:
        even_squares.add(x**2)

# Use this
even_squares = {x**2 for x in range(10) if x % 2 == 0}
```

### Using Frozensets for Immutable Sets

Use frozensets when you need an immutable set, such as for dictionary keys or elements of another set.

```python
# Using frozensets as dictionary keys
user_permissions = {
    frozenset(["read", "write"]): ["editor", "admin"],
    frozenset(["read"]): ["viewer"]
}

# Check user permissions
user_role = "editor"
user_access = frozenset(["read", "write"])

for permissions, roles in user_permissions.items():
    if permissions == user_access and user_role in roles:
        print("Access granted")
        break
```

## Common Pitfalls

### Modifying a Set While Iterating

Modifying a set while iterating over it can lead to unexpected results or errors.

```python
numbers = {1, 2, 3, 4, 5, 6}

# This will raise a RuntimeError
# for num in numbers:
#     if num % 2 == 0:
#         numbers.remove(num)

# Better approach: create a new set or use a copy
to_remove = {num for num in numbers if num % 2 == 0}
numbers -= to_remove
print(numbers)  # {1, 3, 5}

# Or iterate over a copy
numbers = {1, 2, 3, 4, 5, 6}
for num in numbers.copy():
    if num % 2 == 0:
        numbers.remove(num)
print(numbers)  # {1, 3, 5}
```

### Unhashable Elements

Remember that set elements must be hashable. Trying to add unhashable elements will raise an error.

```python
# This will raise a TypeError
# my_set = {[1, 2], [3, 4]}  # TypeError: unhashable type: 'list'

# Solution: use tuples instead of lists
my_set = {(1, 2), (3, 4)}
print(my_set)  # {(1, 2), (3, 4)}

# Or use frozensets for sets of sets
my_set = {frozenset([1, 2]), frozenset([3, 4])}
print(my_set)  # {frozenset({1, 2}), frozenset({3, 4})}
```

### Set Order is Not Guaranteed

Don't rely on the order of elements in a set, as it may change.

```python
my_set = {3, 1, 4, 1, 5, 9, 2, 6, 5}
print(my_set)  # Order is not guaranteed

# If order matters, convert to a sorted list
sorted_elements = sorted(my_set)
print(sorted_elements)  # [1, 2, 3, 4, 5, 6, 9]
```

### Set Operations vs. Methods

Be aware of the difference between set operations using operators and methods.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Set operations with operators create new sets
union_result = set1 | set2
print(set1)  # {1, 2, 3} (unchanged)

# Set methods with _update suffix modify the original set
set1.update(set2)  # or set1 |= set2
print(set1)  # {1, 2, 3, 4, 5} (modified)
```

## Next Steps

Now that you understand sets in Python, you're ready to move on to [Dictionaries](../09_Dictionaries/README.md).