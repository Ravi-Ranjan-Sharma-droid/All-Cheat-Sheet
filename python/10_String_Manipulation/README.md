# String Manipulation in Python

Strings are one of the most commonly used data types in Python. They represent sequences of characters and are used for storing and manipulating text. Python provides a rich set of operations and methods for string manipulation.

## String Basics

### Creating Strings

In Python, strings can be created using single quotes (`'`), double quotes (`"`), or triple quotes (`'''` or `"""`).

```python
# Single quotes
single_quoted = 'Hello, World!'

# Double quotes
double_quoted = "Hello, World!"

# Triple quotes (can span multiple lines)
triple_quoted = '''This is a multi-line
string using triple quotes.'''

# Triple double quotes
triple_double = """Another multi-line
string using triple double quotes."""

# Empty string
empty_string = ""
```

### String Properties

- **Immutable**: Strings in Python are immutable, meaning they cannot be changed after creation.
- **Ordered**: Strings maintain the order of characters.
- **Indexed**: Each character in a string has an index, starting from 0.
- **Iterable**: You can iterate through each character in a string.

## Accessing Characters in Strings

### Indexing

You can access individual characters in a string using indexing.

```python
text = "Python"

# Positive indexing (from left to right, starting at 0)
print(text[0])  # 'P'
print(text[1])  # 'y'
print(text[5])  # 'n'

# Negative indexing (from right to left, starting at -1)
print(text[-1])  # 'n'
print(text[-2])  # 'o'
print(text[-6])  # 'P'

# Attempting to access an index out of range raises an IndexError
# print(text[6])  # IndexError: string index out of range
```

### Slicing

Slicing allows you to extract a substring from a string.

```python
text = "Python Programming"

# Basic slicing: string[start:end] (end is exclusive)
print(text[0:6])    # 'Python'
print(text[7:18])   # 'Programming'

# Omitting start or end
print(text[:6])     # 'Python' (from beginning to index 5)
print(text[7:])     # 'Programming' (from index 7 to end)

# Negative indices in slicing
print(text[-11:])   # 'Programming' (last 11 characters)
print(text[:-12])   # 'Python' (all except last 12 characters)

# Step parameter: string[start:end:step]
print(text[0:18:2])  # 'Pto rgamn' (every second character)
print(text[::2])     # 'Pto rgamn' (same as above)

# Negative step (reverses the string)
print(text[::-1])    # 'gnimmargorP nohtyP' (entire string reversed)
print(text[5:0:-1])  # 'nohty' (from index 5 to 1, reversed)
```

## String Operations

### Concatenation

You can combine strings using the `+` operator.

```python
first_name = "John"
last_name = "Doe"

# Concatenation using +
full_name = first_name + " " + last_name
print(full_name)  # 'John Doe'

# Concatenation with non-string types requires conversion
age = 30
# message = "Age: " + age  # TypeError: can only concatenate str (not "int") to str
message = "Age: " + str(age)  # 'Age: 30'
```

### Repetition

You can repeat a string using the `*` operator.

```python
word = "Python"

# Repeat a string
repeated = word * 3
print(repeated)  # 'PythonPythonPython'

# Useful for creating separators
separator = "-" * 20
print(separator)  # '--------------------'
```

### Membership Testing

You can check if a substring exists in a string using the `in` and `not in` operators.

```python
sentence = "Python is a powerful programming language"

# Check if a substring exists
print("Python" in sentence)  # True
print("Java" in sentence)    # False
print("Java" not in sentence)  # True
```

## String Methods

Python provides numerous built-in methods for string manipulation.

### Case Conversion

```python
text = "Python Programming"

# Convert to uppercase
print(text.upper())  # 'PYTHON PROGRAMMING'

# Convert to lowercase
print(text.lower())  # 'python programming'

# Capitalize (first character uppercase, rest lowercase)
print(text.capitalize())  # 'Python programming'

# Title case (first character of each word uppercase)
print(text.title())  # 'Python Programming'

# Swap case (swap uppercase to lowercase and vice versa)
print(text.swapcase())  # 'pYTHON pROGRAMMING'

# Check case properties
print("PYTHON".isupper())  # True
print("python".islower())  # True
print("Python".istitle())  # True
```

### Searching and Replacing

```python
text = "Python is amazing and Python is powerful"

# Find the first occurrence of a substring (returns index or -1 if not found)
print(text.find("Python"))  # 0
print(text.find("Python", 1))  # 21 (start searching from index 1)
print(text.find("Java"))  # -1 (not found)

# Index works like find but raises ValueError if not found
print(text.index("Python"))  # 0
# print(text.index("Java"))  # ValueError: substring not found

# Count occurrences of a substring
print(text.count("Python"))  # 2

# Replace occurrences of a substring
print(text.replace("Python", "Java"))  # 'Java is amazing and Java is powerful'
print(text.replace("Python", "Java", 1))  # 'Java is amazing and Python is powerful' (replace only first occurrence)
```

### Stripping Whitespace

```python
text = "   Python Programming   "

# Remove whitespace from both ends
print(text.strip())  # 'Python Programming'

# Remove whitespace from left end
print(text.lstrip())  # 'Python Programming   '

# Remove whitespace from right end
print(text.rstrip())  # '   Python Programming'

# Strip specific characters
text = "###Python###"
print(text.strip("#"))  # 'Python'
print(text.lstrip("#"))  # 'Python###'
print(text.rstrip("#"))  # '###Python'
```

### Splitting and Joining

```python
# Split a string into a list of substrings
sentence = "Python is a powerful programming language"
words = sentence.split()
print(words)  # ['Python', 'is', 'a', 'powerful', 'programming', 'language']

# Split with a specific delimiter
data = "apple,banana,cherry,date"
fruits = data.split(",")
print(fruits)  # ['apple', 'banana', 'cherry', 'date']

# Split with a maximum number of splits
print(data.split(",", 2))  # ['apple', 'banana', 'cherry,date']

# Split by lines
text = "Line 1\nLine 2\nLine 3"
lines = text.splitlines()
print(lines)  # ['Line 1', 'Line 2', 'Line 3']

# Join a list of strings into a single string
words = ["Python", "is", "awesome"]
sentence = " ".join(words)
print(sentence)  # 'Python is awesome'

# Join with different delimiters
print(", ".join(fruits))  # 'apple, banana, cherry, date'
print("-".join("Python"))  # 'P-y-t-h-o-n'
```

### Checking String Content

```python
# Check if string consists of alphanumeric characters
print("Python3".isalnum())  # True
print("Python 3".isalnum())  # False (space is not alphanumeric)

# Check if string consists of alphabetic characters
print("Python".isalpha())  # True
print("Python3".isalpha())  # False (3 is not alphabetic)

# Check if string consists of digits
print("123".isdigit())  # True
print("123a".isdigit())  # False

# Check if string consists of decimal characters
print("123".isdecimal())  # True
print("123.45".isdecimal())  # False (. is not a decimal character)

# Check if string is a valid identifier
print("variable_name".isidentifier())  # True
print("123variable".isidentifier())  # False (cannot start with a digit)

# Check if string consists of printable characters
print("Hello\n".isprintable())  # False (\n is not printable)

# Check if string consists of whitespace
print("   \t\n".isspace())  # True
print(" a ".isspace())  # False
```

### Alignment and Padding

```python
text = "Python"

# Center align with padding
print(text.center(20))  # '       Python       '
print(text.center(20, "*"))  # '*******Python*******'

# Left align with padding
print(text.ljust(20))  # 'Python              '
print(text.ljust(20, "-"))  # 'Python--------------'

# Right align with padding
print(text.rjust(20))  # '              Python'
print(text.rjust(20, "="))  # '==============Python'

# Zero padding for numbers
num = "42"
print(num.zfill(5))  # '00042'
```

### Other Useful Methods

```python
# Check if string starts or ends with a substring
text = "Python Programming"
print(text.startswith("Py"))  # True
print(text.endswith("ing"))  # True

# Check with start and end indices
print(text.startswith("Pro", 7))  # True
print(text.endswith("Python", 0, 6))  # True

# Partition a string (returns a 3-tuple: before, separator, after)
print("Python is fun".partition("is"))  # ('Python ', 'is', ' fun')

# If separator not found, returns string and two empty strings
print("Python is fun".partition("not"))  # ('Python is fun', '', '')

# Replace tabs with spaces
print("Python\tProgramming".expandtabs(4))  # 'Python  Programming'

# Translate characters using a mapping table
trans_table = str.maketrans("aeiou", "12345")
print("Python".translate(trans_table))  # 'Pyth4n'

# Remove characters
trans_table = str.maketrans("", "", "aeiou")
print("Python".translate(trans_table))  # 'Pythn'
```

## String Formatting

Python offers several ways to format strings.

### Old-style Formatting (% operator)

This is the oldest method, similar to C's `printf()`.

```python
name = "John"
age = 30

# Basic formatting
print("Name: %s, Age: %d" % (name, age))  # 'Name: John, Age: 30'

# Width and precision
pi = 3.14159
print("Pi: %10.2f" % pi)  # 'Pi:       3.14' (width 10, 2 decimal places)

# Left-aligned with width
print("Name: %-10s" % name)  # 'Name: John      ' (left-aligned, width 10)

# Zero padding for numbers
print("Number: %05d" % 42)  # 'Number: 00042' (zero-padded to width 5)
```

### `str.format()` Method

This is a more modern and flexible method.

```python
name = "John"
age = 30

# Basic formatting
print("Name: {}, Age: {}".format(name, age))  # 'Name: John, Age: 30'

# Positional arguments
print("Name: {0}, Age: {1}".format(name, age))  # 'Name: John, Age: 30'
print("Age: {1}, Name: {0}".format(name, age))  # 'Age: 30, Name: John'

# Keyword arguments
print("Name: {name}, Age: {age}".format(name=name, age=age))  # 'Name: John, Age: 30'

# Accessing object attributes and dictionary items
person = {"name": "John", "age": 30}
print("Name: {p[name]}, Age: {p[age]}".format(p=person))  # 'Name: John, Age: 30'

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("John", 30)
print("Name: {p.name}, Age: {p.age}".format(p=person))  # 'Name: John, Age: 30'

# Width, alignment, and padding
print("{:10}".format("Python"))  # 'Python    ' (right-aligned, width 10)
print("{:<10}".format("Python"))  # 'Python    ' (left-aligned, width 10)
print("{:>10}".format("Python"))  # '    Python' (right-aligned, width 10)
print("{:^10}".format("Python"))  # '  Python  ' (center-aligned, width 10)
print("{:*^10}".format("Python"))  # '**Python**' (center-aligned, width 10, * padding)

# Number formatting
pi = 3.14159
print("{:.2f}".format(pi))  # '3.14' (2 decimal places)
print("{:10.2f}".format(pi))  # '      3.14' (width 10, 2 decimal places)
print("{:010.2f}".format(pi))  # '0000003.14' (zero-padded, width 10, 2 decimal places)

# Thousands separator
print("{:,}".format(1000000))  # '1,000,000'

# Percentage
print("{:.2%}".format(0.25))  # '25.00%'

# Binary, octal, hexadecimal
print("{:b}".format(42))  # '101010' (binary)
print("{:o}".format(42))  # '52' (octal)
print("{:x}".format(42))  # '2a' (hexadecimal lowercase)
print("{:X}".format(42))  # '2A' (hexadecimal uppercase)
print("{:#x}".format(42))  # '0x2a' (with prefix)
```

### f-Strings (Python 3.6+)

f-Strings (formatted string literals) are the newest and most concise way to format strings in Python.

```python
name = "John"
age = 30

# Basic formatting
print(f"Name: {name}, Age: {age}")  # 'Name: John, Age: 30'

# Expressions inside braces are evaluated
print(f"Age next year: {age + 1}")  # 'Age next year: 31'
print(f"Name uppercase: {name.upper()}")  # 'Name uppercase: JOHN'

# Width, alignment, and padding (same as str.format())
print(f"{name:10}")  # 'John      ' (right-aligned, width 10)
print(f"{name:<10}")  # 'John      ' (left-aligned, width 10)
print(f"{name:>10}")  # '      John' (right-aligned, width 10)
print(f"{name:^10}")  # '   John   ' (center-aligned, width 10)
print(f"{name:*^10}")  # '***John***' (center-aligned, width 10, * padding)

# Number formatting
pi = 3.14159
print(f"{pi:.2f}")  # '3.14' (2 decimal places)
print(f"{pi:10.2f}")  # '      3.14' (width 10, 2 decimal places)

# Thousands separator
print(f"{1000000:,}")  # '1,000,000'

# Percentage
print(f"{0.25:.2%}")  # '25.00%'

# Binary, octal, hexadecimal
print(f"{42:b}")  # '101010' (binary)
print(f"{42:o}")  # '52' (octal)
print(f"{42:x}")  # '2a' (hexadecimal lowercase)
print(f"{42:X}")  # '2A' (hexadecimal uppercase)
print(f"{42:#x}")  # '0x2a' (with prefix)

# Debugging (Python 3.8+)
print(f"{name=}, {age=}")  # "name='John', age=30"
```

## String Templates

String templates provide a simpler and less powerful mechanism for string substitution.

```python
from string import Template

# Create a template
template = Template("Name: $name, Age: $age")

# Substitute values
result = template.substitute(name="John", age=30)
print(result)  # 'Name: John, Age: 30'

# Using a dictionary
data = {"name": "John", "age": 30}
result = template.substitute(data)
print(result)  # 'Name: John, Age: 30'

# Safe substitution (doesn't raise KeyError for missing keys)
template = Template("Name: $name, Age: $age, Country: $country")
result = template.safe_substitute(data)
print(result)  # 'Name: John, Age: 30, Country: $country'
```

## Raw Strings

Raw strings are prefixed with `r` and treat backslashes as literal characters, which is useful for regular expressions and Windows file paths.

```python
# Normal string (backslash is an escape character)
print("C:\Users\John")  # 'C:\Users\John' (\U is interpreted as a Unicode escape)

# Raw string (backslashes are treated literally)
print(r"C:\Users\John")  # 'C:\Users\John'

# Useful for regular expressions
import re
pattern = r"\bword\b"  # \b represents a word boundary in regex
matches = re.findall(pattern, "word boundary")
print(matches)  # ['word']
```

## Bytes and Bytearray

For handling binary data, Python provides `bytes` and `bytearray` types.

```python
# Create bytes (immutable)
b = bytes([65, 66, 67, 68, 69])  # ASCII values for 'ABCDE'
print(b)  # b'ABCDE'

# Create from a string with encoding
b = "Hello".encode("utf-8")
print(b)  # b'Hello'

# Create bytearray (mutable)
ba = bytearray([65, 66, 67, 68, 69])
print(ba)  # bytearray(b'ABCDE')

# Modify bytearray
ba[0] = 90  # ASCII value for 'Z'
print(ba)  # bytearray(b'ZBCDE')

# Convert back to string
s = b.decode("utf-8")
print(s)  # 'Hello'
```

## Unicode and Encoding

Python 3 strings are Unicode by default, but you often need to convert between Unicode and various encodings.

```python
# Unicode string (Python 3 strings are Unicode by default)
s = "Hello, 世界"  # Mix of ASCII and Chinese characters

# Encode to bytes using different encodings
utf8_bytes = s.encode("utf-8")
print(utf8_bytes)  # b'Hello, \xe4\xb8\x96\xe7\x95\x8c'

latin1_bytes = s.encode("latin-1", errors="replace")
print(latin1_bytes)  # b'Hello, ???' (characters not in Latin-1 are replaced)

# Decode bytes back to string
s_from_utf8 = utf8_bytes.decode("utf-8")
print(s_from_utf8)  # 'Hello, 世界'

# Error handling when decoding
invalid_utf8 = b'\x80\x81'
try:
    s = invalid_utf8.decode("utf-8")  # This will raise UnicodeDecodeError
except UnicodeDecodeError:
    print("Cannot decode bytes")

# Different error handling modes
s = invalid_utf8.decode("utf-8", errors="replace")
print(s)  # '��' (replacement character)

s = invalid_utf8.decode("utf-8", errors="ignore")
print(s)  # '' (invalid bytes are ignored)

# Unicode escape sequences
s = "\u4F60\u597D"  # Unicode escape for '你好' (Chinese for 'hello')
print(s)  # '你好'
```

## Common String Operations

### Reversing a String

```python
s = "Python"

# Using slicing
reversed_s = s[::-1]
print(reversed_s)  # 'nohtyP'

# Using reversed() and join()
reversed_s = "".join(reversed(s))
print(reversed_s)  # 'nohtyP'
```

### Checking Palindromes

```python
def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    s = "".join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("race a car"))  # False
```

### Counting Words

```python
def count_words(text):
    # Split by whitespace and count non-empty words
    words = text.split()
    return len(words)

text = "The quick brown fox jumps over the lazy dog"
print(count_words(text))  # 9
```

### Removing Duplicates

```python
def remove_duplicates(s):
    return "".join(dict.fromkeys(s))

print(remove_duplicates("programming"))  # 'progamin'
```

### Case Conversion

```python
def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

def camel_to_snake(camel_str):
    import re
    return re.sub(r'(?<!^)(?=[A-Z])', '_', camel_str).lower()

print(snake_to_camel("hello_world"))  # 'helloWorld'
print(camel_to_snake("helloWorld"))  # 'hello_world'
```

## Regular Expressions

Regular expressions provide a powerful way to perform complex string operations.

```python
import re

text = "The quick brown fox jumps over the lazy dog. The dog was not very lazy after all."

# Search for a pattern
match = re.search(r"fox", text)
if match:
    print(f"Found 'fox' at position {match.start()}")  # Found 'fox' at position 16

# Find all occurrences
matches = re.findall(r"dog", text)
print(matches)  # ['dog', 'dog']

# Find all occurrences with positions
for match in re.finditer(r"dog", text):
    print(f"Found 'dog' at position {match.start()}")  # Found 'dog' at position 40, Found 'dog' at position 49

# Replace occurrences
new_text = re.sub(r"dog", "cat", text)
print(new_text)  # 'The quick brown fox jumps over the lazy cat. The cat was not very lazy after all.'

# Replace with a limit
new_text = re.sub(r"dog", "cat", text, count=1)
print(new_text)  # 'The quick brown fox jumps over the lazy cat. The dog was not very lazy after all.'

# Split by pattern
parts = re.split(r"\s+", "Hello   World   Python")
print(parts)  # ['Hello', 'World', 'Python']

# Case-insensitive search
matches = re.findall(r"the", text, re.IGNORECASE)
print(matches)  # ['The', 'the', 'The']
```

### Common Regular Expression Patterns

```python
import re

# Match a word
pattern = r"\bword\b"

# Match a digit
pattern = r"\d"  # Equivalent to [0-9]

# Match any non-digit
pattern = r"\D"  # Equivalent to [^0-9]

# Match whitespace
pattern = r"\s"  # Equivalent to [ \t\n\r\f\v]

# Match non-whitespace
pattern = r"\S"  # Equivalent to [^ \t\n\r\f\v]

# Match word character (alphanumeric or underscore)
pattern = r"\w"  # Equivalent to [a-zA-Z0-9_]

# Match non-word character
pattern = r"\W"  # Equivalent to [^a-zA-Z0-9_]

# Match beginning of string
pattern = r"^start"

# Match end of string
pattern = r"end$"

# Match zero or more occurrences
pattern = r"ab*c"  # Matches 'ac', 'abc', 'abbc', etc.

# Match one or more occurrences
pattern = r"ab+c"  # Matches 'abc', 'abbc', etc., but not 'ac'

# Match zero or one occurrence
pattern = r"ab?c"  # Matches 'ac' or 'abc', but not 'abbc'

# Match exactly n occurrences
pattern = r"ab{3}c"  # Matches 'abbbc', but not 'abc' or 'abbc'

# Match at least n occurrences
pattern = r"ab{3,}c"  # Matches 'abbbc', 'abbbbc', etc., but not 'abc' or 'abbc'

# Match between n and m occurrences
pattern = r"ab{2,4}c"  # Matches 'abbc', 'abbbc', 'abbbbc', but not 'abc' or 'abbbbbc'

# Grouping
pattern = r"(ab)+c"  # Matches 'abc', 'ababc', etc.

# Alternation
pattern = r"a|b"  # Matches 'a' or 'b'
pattern = r"(cat|dog)s"  # Matches 'cats' or 'dogs'

# Character classes
pattern = r"[aeiou]"  # Matches any vowel
pattern = r"[^aeiou]"  # Matches any character that is not a vowel
pattern = r"[a-z]"  # Matches any lowercase letter
pattern = r"[A-Za-z]"  # Matches any letter

# Common patterns
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
url_pattern = r"https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/[a-zA-Z0-9._~:/?#[\]@!$&'()*+,;=]*)?"
ip_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
date_pattern = r"\b\d{4}-\d{2}-\d{2}\b"  # YYYY-MM-DD
```

### Compiling Regular Expressions

For better performance when using the same pattern multiple times, you can compile it.

```python
import re

# Compile a pattern
pattern = re.compile(r"\bdog\b")

text = "The dog chased the cat. The dog was fast."

# Use the compiled pattern
matches = pattern.findall(text)
print(matches)  # ['dog', 'dog']

# Search with the compiled pattern
match = pattern.search(text)
if match:
    print(f"Found 'dog' at position {match.start()}")  # Found 'dog' at position 4

# Replace with the compiled pattern
new_text = pattern.sub("wolf", text)
print(new_text)  # 'The wolf chased the cat. The wolf was fast.'
```

### Named Groups

```python
import re

# Pattern with named groups
pattern = re.compile(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})")

text = "The event is scheduled for 2023-11-15."

# Search and access named groups
match = pattern.search(text)
if match:
    print(f"Year: {match.group('year')}")  # Year: 2023
    print(f"Month: {match.group('month')}")  # Month: 11
    print(f"Day: {match.group('day')}")  # Day: 15

# Replace with reference to named groups
new_text = pattern.sub(r"\g<day>/\g<month>/\g<year>", text)
print(new_text)  # 'The event is scheduled for 15/11/2023.'
```

## Performance Considerations

### String Concatenation

Repeated string concatenation with `+` can be inefficient. Use `join()` for better performance.

```python
import time

# Inefficient way (using + operator)
start = time.time()
result = ""
for i in range(100000):
    result += str(i)
end = time.time()
print(f"Time with + operator: {end - start:.6f} seconds")

# Efficient way (using join)
start = time.time()
result = "".join(str(i) for i in range(100000))
end = time.time()
print(f"Time with join: {end - start:.6f} seconds")
```

### String Interning

Python automatically interns (reuses) some strings to save memory.

```python
# These strings are interned (same object)
s1 = "hello"
s2 = "hello"
print(s1 is s2)  # True

# These strings are not interned (different objects)
s3 = "hello world"
s4 = "hello world"
print(s3 is s4)  # May be True or False depending on implementation

# Force interning
import sys
s5 = sys.intern("hello world")
s6 = sys.intern("hello world")
print(s5 is s6)  # True
```

### String Methods vs. Regular Expressions

String methods are generally faster than regular expressions for simple operations.

```python
import re
import time

text = "The quick brown fox jumps over the lazy dog." * 10000

# Using string method
start = time.time()
count1 = text.count("fox")
end = time.time()
print(f"Time with string method: {end - start:.6f} seconds")

# Using regular expression
start = time.time()
count2 = len(re.findall(r"fox", text))
end = time.time()
print(f"Time with regular expression: {end - start:.6f} seconds")

print(f"Both methods found {count1} occurrences")
```

## Best Practices

### Use f-Strings for Formatting

f-Strings are more readable and generally faster than other formatting methods.

```python
name = "John"
age = 30

# Prefer this
print(f"Name: {name}, Age: {age}")

# Over these
print("Name: %s, Age: %d" % (name, age))
print("Name: {}, Age: {}".format(name, age))
```

### Avoid Unnecessary String Operations

Minimize string operations in loops for better performance.

```python
# Inefficient
result = ""
for i in range(100):
    result += str(i)  # Creates a new string each time

# More efficient
parts = []
for i in range(100):
    parts.append(str(i))
result = "".join(parts)  # Creates the string once

# Even better with list comprehension
result = "".join(str(i) for i in range(100))
```

### Use String Methods Before Regular Expressions

String methods are simpler and faster for basic operations.

```python
text = "The quick brown fox jumps over the lazy dog."

# Prefer string methods for simple operations
if "fox" in text:  # Simple membership test
    print("Found fox")

words = text.split()  # Simple splitting

# Use regular expressions for complex patterns
import re
if re.search(r"\bfox\b", text):  # Word boundary matching
    print("Found the word 'fox'")
```

### Be Careful with Unicode

Handle Unicode correctly to avoid encoding/decoding errors.

```python
# Always specify encoding when reading/writing files
with open("file.txt", "r", encoding="utf-8") as f:
    text = f.read()

with open("file.txt", "w", encoding="utf-8") as f:
    f.write(text)

# Be explicit about encodings in string operations
bytes_data = text.encode("utf-8")
text = bytes_data.decode("utf-8")
```

## Common Pitfalls

### Immutability Confusion

Remember that strings are immutable, so methods like `replace()` return new strings.

```python
s = "Hello, World!"

# This doesn't modify s
s.replace("Hello", "Hi")
print(s)  # Still 'Hello, World!'

# You need to assign the result
s = s.replace("Hello", "Hi")
print(s)  # Now 'Hi, World!'
```

### Forgetting to Escape Special Characters

Special characters in strings need to be escaped with a backslash.

```python
# This will cause a syntax error
# s = "He said, "Hello!""

# Correct ways
s = "He said, \"Hello!\""
print(s)  # 'He said, "Hello!"'

s = 'He said, "Hello!"'
print(s)  # 'He said, "Hello!"'

s = """He said, "Hello!"""
print(s)  # 'He said, "Hello!"'
```

### Misunderstanding String Equality

Use `==` for string content comparison and `is` for identity comparison.

```python
s1 = "hello"
s2 = "hello"
s3 = "h" + "ello"

# Content comparison
print(s1 == s2)  # True
print(s1 == s3)  # True

# Identity comparison
print(s1 is s2)  # True (may be interned)
print(s1 is s3)  # May be True or False depending on implementation
```

### Incorrect Regular Expression Patterns

Regular expressions can be tricky to get right.

```python
import re

# Trying to match a dot character
text = "example.com"

# This won't work as expected (. matches any character)
print(re.findall(".", text))  # ['e', 'x', 'a', 'm', 'p', 'l', 'e', '.', 'c', 'o', 'm']

# Escape the dot to match it literally
print(re.findall("\.", text))  # ['.']

# Or use a raw string
print(re.findall(r"\.", text))  # ['.']
```

### Inefficient String Building

Building strings with repeated concatenation is inefficient.

```python
# Inefficient
result = ""
for i in range(1000):
    result += str(i)  # Creates a new string each time

# Efficient
result = "".join(str(i) for i in range(1000))
```

## Next Steps

Now that you understand string manipulation in Python, you're ready to move on to [File I/O](../11_File_IO/README.md).