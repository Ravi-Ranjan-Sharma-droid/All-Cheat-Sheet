# Operators in Python

Operators are special symbols that perform operations on variables and values. Python provides a variety of operators grouped into several categories.

## Arithmetic Operators

Arithmetic operators are used to perform mathematical operations.

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraction | `5 - 3` | `2` |
| `*` | Multiplication | `5 * 3` | `15` |
| `/` | Division | `5 / 3` | `1.6666...` |
| `//` | Floor Division | `5 // 3` | `1` |
| `%` | Modulus | `5 % 3` | `2` |
| `**` | Exponentiation | `5 ** 3` | `125` |

```python
# Examples of arithmetic operators
a = 10
b = 3

addition = a + b        # 13
subtraction = a - b     # 7
multiplication = a * b  # 30
division = a / b        # 3.3333...
floor_division = a // b # 3
modulus = a % b         # 1
exponentiation = a ** b # 1000
```

### Division in Python 3

In Python 3, the division operator (`/`) always returns a float, even if the result is a whole number.

```python
result = 10 / 5  # 2.0, not 2
```

If you want integer division (discarding the remainder), use the floor division operator (`//`).

```python
result = 10 // 3  # 3, not 3.3333...
```

## Comparison Operators

Comparison operators are used to compare values and return a boolean result (`True` or `False`).

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `==` | Equal | `5 == 3` | `False` |
| `!=` | Not Equal | `5 != 3` | `True` |
| `>` | Greater Than | `5 > 3` | `True` |
| `<` | Less Than | `5 < 3` | `False` |
| `>=` | Greater Than or Equal | `5 >= 5` | `True` |
| `<=` | Less Than or Equal | `5 <= 3` | `False` |

```python
# Examples of comparison operators
a = 10
b = 3
c = 10

equal = a == b              # False
not_equal = a != b          # True
greater_than = a > b        # True
less_than = a < b           # False
greater_or_equal = a >= c   # True
less_or_equal = b <= c      # True
```

### Chaining Comparison Operators

Python allows you to chain comparison operators.

```python
# Check if a number is between 1 and 10
x = 5
result = 1 < x < 10  # True

# Equivalent to
result = 1 < x and x < 10  # True
```

## Logical Operators

Logical operators are used to combine conditional statements.

| Operator | Description | Example |
|----------|-------------|--------|
| `and` | Returns `True` if both statements are true | `x > 5 and x < 10` |
| `or` | Returns `True` if one of the statements is true | `x < 5 or x > 10` |
| `not` | Reverses the result, returns `False` if the result is true | `not(x > 5 and x < 10)` |

```python
# Examples of logical operators
x = 7

result1 = x > 5 and x < 10   # True (both conditions are true)
result2 = x < 5 or x > 10    # False (neither condition is true)
result3 = not(x > 5)         # False (reverses True to False)
```

### Short-Circuit Evaluation

Python uses short-circuit evaluation for logical operators:
- For `and`, if the first operand is `False`, the second operand is not evaluated
- For `or`, if the first operand is `True`, the second operand is not evaluated

```python
# Short-circuit with 'and'
result = False and print("This won't be printed")  # The print function is not called

# Short-circuit with 'or'
result = True or print("This won't be printed")    # The print function is not called
```

## Assignment Operators

Assignment operators are used to assign values to variables.

| Operator | Example | Equivalent To |
|----------|---------|---------------|
| `=` | `x = 5` | `x = 5` |
| `+=` | `x += 3` | `x = x + 3` |
| `-=` | `x -= 3` | `x = x - 3` |
| `*=` | `x *= 3` | `x = x * 3` |
| `/=` | `x /= 3` | `x = x / 3` |
| `//=` | `x //= 3` | `x = x // 3` |
| `%=` | `x %= 3` | `x = x % 3` |
| `**=` | `x **= 3` | `x = x ** 3` |
| `&=` | `x &= 3` | `x = x & 3` |
| `|=` | `x |= 3` | `x = x | 3` |
| `^=` | `x ^= 3` | `x = x ^ 3` |
| `>>=` | `x >>= 3` | `x = x >> 3` |
| `<<=` | `x <<= 3` | `x = x << 3` |

```python
# Examples of assignment operators
x = 10

x += 5   # x = 15 (10 + 5)
x -= 3   # x = 12 (15 - 3)
x *= 2   # x = 24 (12 * 2)
x /= 4   # x = 6.0 (24 / 4)
x //= 2  # x = 3.0 (6.0 // 2, result is float because x was float)
x %= 2   # x = 1.0 (3.0 % 2)
```

## Bitwise Operators

Bitwise operators act on operands as if they were strings of binary digits.

| Operator | Name | Description |
|----------|------|-------------|
| `&` | AND | Sets each bit to 1 if both bits are 1 |
| `\|` | OR | Sets each bit to 1 if one of the bits is 1 |
| `^` | XOR | Sets each bit to 1 if only one of the bits is 1 |
| `~` | NOT | Inverts all the bits |
| `<<` | Left Shift | Shifts left by pushing zeros in from the right |
| `>>` | Right Shift | Shifts right by pushing copies of the leftmost bit in from the left |

```python
# Examples of bitwise operators
a = 60  # 0011 1100 in binary
b = 13  # 0000 1101 in binary

bitwise_and = a & b        # 12 (0000 1100)
bitwise_or = a | b         # 61 (0011 1101)
bitwise_xor = a ^ b        # 49 (0011 0001)
bitwise_not = ~a           # -61 (1100 0011, in 2's complement form)
left_shift = a << 2        # 240 (1111 0000)
right_shift = a >> 2       # 15 (0000 1111)
```

## Identity Operators

Identity operators are used to compare the memory locations of two objects.

| Operator | Description | Example |
|----------|-------------|--------|
| `is` | Returns `True` if both variables are the same object | `x is y` |
| `is not` | Returns `True` if both variables are not the same object | `x is not y` |

```python
# Examples of identity operators
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a is b)      # False (different objects with the same content)
print(a is c)      # True (same object)
print(a is not b)  # True (different objects)
```

### `is` vs `==`

- `is` checks if two variables refer to the same object in memory
- `==` checks if the values of two variables are equal

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True (same values)
print(a is b)  # False (different objects)

# For some built-in types like small integers, Python may reuse objects
x = 5
y = 5
print(x is y)  # True (Python may reuse small integer objects)
```

## Membership Operators

Membership operators are used to test if a sequence contains a specific value.

| Operator | Description | Example |
|----------|-------------|--------|
| `in` | Returns `True` if a value is found in the sequence | `x in y` |
| `not in` | Returns `True` if a value is not found in the sequence | `x not in y` |

```python
# Examples of membership operators
fruits = ["apple", "banana", "cherry"]

print("apple" in fruits)       # True
print("orange" in fruits)      # False
print("orange" not in fruits)  # True

# Works with strings too
name = "Python"
print("P" in name)            # True
print("x" in name)            # False
```

## Operator Precedence

Operator precedence determines the order in which operations are performed. Operations with higher precedence are performed before operations with lower precedence.

Here's the precedence of operators in Python, from highest to lowest:

| Operators | Description |
|-----------|-------------|
| `()` | Parentheses |
| `**` | Exponentiation |
| `+x`, `-x`, `~x` | Unary plus, minus, and bitwise NOT |
| `*`, `/`, `//`, `%` | Multiplication, division, floor division, modulus |
| `+`, `-` | Addition, subtraction |
| `<<`, `>>` | Bitwise shifts |
| `&` | Bitwise AND |
| `^` | Bitwise XOR |
| `\|` | Bitwise OR |
| `==`, `!=`, `>`, `>=`, `<`, `<=`, `is`, `is not`, `in`, `not in` | Comparisons, identity, membership |
| `not` | Logical NOT |
| `and` | Logical AND |
| `or` | Logical OR |

```python
# Examples of operator precedence
result = 2 + 3 * 4       # 14 (multiplication before addition)
result = (2 + 3) * 4     # 20 (parentheses have highest precedence)
result = 4 ** 2 + 3      # 19 (exponentiation before addition)
result = 10 / 2 + 3      # 8.0 (division before addition)
```

## Walrus Operator (`:=`) - Python 3.8+

The walrus operator (`:=`) allows you to assign values to variables as part of an expression.

```python
# Without walrus operator
data = get_data()
if data:
    process(data)

# With walrus operator
if data := get_data():
    process(data)
```

This is particularly useful in loops and conditional statements:

```python
# Example: Processing lines from a file until an empty line
while (line := input()) != "":
    process(line)

# Example: Filtering a list
filtered = [x for x in data if (x_processed := process(x)) is not None]
```

## Common Pitfalls

### Mutable Objects and Assignment

Be careful when using assignment operators with mutable objects like lists.

```python
# This doesn't create a copy, it creates a reference
original = [1, 2, 3]
reference = original
reference += [4]  # Modifies both reference and original
print(original)   # [1, 2, 3, 4]

# To create a copy, use slicing or copy methods
copy = original[:]
copy += [5]       # Only modifies copy
print(original)   # [1, 2, 3, 4]
print(copy)       # [1, 2, 3, 4, 5]
```

### Chained Assignments

Chained assignments can lead to unexpected behavior with mutable objects.

```python
# This creates three references to the same list
x = y = z = []
x.append(1)
print(y)  # [1] (y is modified too)

# To create separate lists
x, y, z = [], [], []
x.append(1)
print(y)  # [] (y is not modified)
```

### Floating-Point Precision

Be aware of floating-point precision issues when using arithmetic operators.

```python
result = 0.1 + 0.2
print(result)  # 0.30000000000000004, not exactly 0.3

# For equality comparisons, use a small epsilon
epsilon = 1e-10
print(abs(result - 0.3) < epsilon)  # True

# Or use the decimal module for precise decimal arithmetic
from decimal import Decimal
result = Decimal('0.1') + Decimal('0.2')
print(result)  # 0.3
```

## Next Steps

Now that you understand operators in Python, you're ready to move on to [Control Flow](../04_Control_Flow/README.md).