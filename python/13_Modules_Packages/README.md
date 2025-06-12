# Modules and Packages in Python

Modules and packages are essential for organizing and reusing code in Python. This section covers how to create, import, and use modules and packages effectively.

## Modules

A module is a file containing Python definitions and statements. The file name is the module name with the suffix `.py` added.

### Creating a Module

Creating a module is as simple as creating a Python file. For example, let's create a module called `my_module.py`:

```python
# my_module.py

def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"

def add(a, b):
    """Add two numbers and return the result."""
    return a + b

PI = 3.14159

class Person:
    """A simple class representing a person."""
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def say_hello(self):
        return f"{self.name} says hello!"

# Code that runs when the module is executed directly
if __name__ == "__main__":
    print(greet("World"))
    print(f"The sum of 5 and 3 is {add(5, 3)}")
    person = Person("Alice", 30)
    print(person.say_hello())
```

### Importing Modules

There are several ways to import modules in Python:

#### Import the Entire Module

```python
import my_module

print(my_module.greet("Alice"))  # Output: Hello, Alice!
print(my_module.add(5, 3))      # Output: 8
print(my_module.PI)             # Output: 3.14159

person = my_module.Person("Bob", 25)
print(person.say_hello())       # Output: Bob says hello!
```

#### Import Specific Items from a Module

```python
from my_module import greet, add, PI, Person

print(greet("Alice"))  # Output: Hello, Alice!
print(add(5, 3))      # Output: 8
print(PI)             # Output: 3.14159

person = Person("Bob", 25)
print(person.say_hello())  # Output: Bob says hello!
```

#### Import with an Alias

```python
import my_module as mm

print(mm.greet("Alice"))  # Output: Hello, Alice!
```

```python
from my_module import greet as say_hello

print(say_hello("Alice"))  # Output: Hello, Alice!
```

#### Import All Items from a Module

```python
from my_module import *

print(greet("Alice"))  # Output: Hello, Alice!
print(add(5, 3))      # Output: 8
print(PI)             # Output: 3.14159

person = Person("Bob", 25)
print(person.say_hello())  # Output: Bob says hello!
```

> **Note**: Using `from module import *` is generally discouraged as it can lead to namespace pollution and make it unclear where functions and variables are coming from.

### The Module Search Path

When you import a module, Python searches for it in the following locations:

1. The directory containing the input script (or the current directory if no file is specified).
2. The directories listed in the `PYTHONPATH` environment variable.
3. The installation-dependent default directories (e.g., site-packages).

You can view the search path by checking the `sys.path` list:

```python
import sys
print(sys.path)
```

You can also modify the search path at runtime:

```python
import sys
sys.path.append('/path/to/my/modules')
```

### The `dir()` Function

The `dir()` function returns a sorted list of names in the specified module. If no argument is provided, it returns the names in the current local scope.

```python
import my_module

# Get all names defined in the module
print(dir(my_module))

# Get all names in the current scope
print(dir())
```

### The `__name__` Variable

Every module has a `__name__` variable. If the module is being run directly, `__name__` is set to `"__main__"`. If the module is being imported, `__name__` is set to the module's name.

This allows you to write code that runs only when the module is executed directly:

```python
# my_module.py

def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    # This code runs only when the module is executed directly
    print(greet("World"))
```

### Reloading a Module

If you've made changes to a module and want to reload it without restarting the Python interpreter, you can use the `importlib.reload()` function:

```python
import importlib
import my_module

# Make changes to my_module.py

# Reload the module
importlib.reload(my_module)
```

## Packages

A package is a way of organizing related modules into a directory hierarchy. A package is simply a directory that contains a special file called `__init__.py` (which can be empty) and other Python files.

### Creating a Package

Let's create a simple package called `my_package` with the following structure:

```
my_package/
├── __init__.py
├── module1.py
├── module2.py
└── subpackage/
    ├── __init__.py
    └── module3.py
```

Here's what each file might contain:

```python
# my_package/__init__.py

# This file can be empty, or it can contain initialization code for the package
print("Initializing my_package")

# You can also import specific items from modules to make them available at the package level
from .module1 import function1
from .module2 import function2
```

```python
# my_package/module1.py

def function1():
    return "This is function1 from module1"
```

```python
# my_package/module2.py

def function2():
    return "This is function2 from module2"
```

```python
# my_package/subpackage/__init__.py

# This file can be empty, or it can contain initialization code for the subpackage
print("Initializing my_package.subpackage")
```

```python
# my_package/subpackage/module3.py

def function3():
    return "This is function3 from module3 in subpackage"
```

### Importing from a Package

There are several ways to import modules from a package:

#### Import a Module from a Package

```python
import my_package.module1

print(my_package.module1.function1())  # Output: This is function1 from module1
```

#### Import a Specific Item from a Module in a Package

```python
from my_package.module1 import function1

print(function1())  # Output: This is function1 from module1
```

#### Import a Module from a Subpackage

```python
import my_package.subpackage.module3

print(my_package.subpackage.module3.function3())  # Output: This is function3 from module3 in subpackage
```

#### Import a Specific Item from a Module in a Subpackage

```python
from my_package.subpackage.module3 import function3

print(function3())  # Output: This is function3 from module3 in subpackage
```

### Relative Imports

Relative imports use dots to indicate the package hierarchy. A single dot means the current package, two dots mean the parent package, and so on.

```python
# my_package/module2.py

# Import function1 from module1 in the same package
from .module1 import function1

def function2():
    return f"This is function2 from module2, calling {function1()}"
```

```python
# my_package/subpackage/module3.py

# Import function1 from module1 in the parent package
from ..module1 import function1

def function3():
    return f"This is function3 from module3 in subpackage, calling {function1()}"
```

> **Note**: Relative imports only work for modules that are part of a package. They cannot be used in the main script.

### The `__all__` Variable

The `__all__` variable in a module or package's `__init__.py` file defines what is imported when `from package import *` is used.

```python
# my_package/__init__.py

# Define what is imported when `from my_package import *` is used
__all__ = ['module1', 'function1', 'function2']

from .module1 import function1
from .module2 import function2
```

```python
# my_package/module1.py

# Define what is imported when `from my_package.module1 import *` is used
__all__ = ['function1']

def function1():
    return "This is function1 from module1"

def _internal_function():
    return "This is an internal function that won't be imported with *"
```

### Namespace Packages (Python 3.3+)

Namespace packages allow you to split a package across multiple directories. They don't require an `__init__.py` file.

For example, you could have the following directory structure:

```
dir1/
└── my_namespace_package/
    └── module1.py

dir2/
└── my_namespace_package/
    └── module2.py
```

If both `dir1` and `dir2` are in the Python path, you can import modules from both directories as if they were part of the same package:

```python
import my_namespace_package.module1
import my_namespace_package.module2
```

## Standard Library Modules

Python comes with a rich standard library that provides modules for various tasks. Here are some commonly used standard library modules:

### `os` - Operating System Interface

```python
import os

# Get the current working directory
cwd = os.getcwd()
print(cwd)

# List files and directories
files = os.listdir(cwd)
print(files)

# Create a directory
os.mkdir('new_directory')

# Remove a file
os.remove('file.txt')

# Check if a path exists
if os.path.exists('file.txt'):
    print('File exists')
```

### `sys` - System-specific Parameters and Functions

```python
import sys

# Get command-line arguments
args = sys.argv
print(args)

# Get Python version
version = sys.version
print(version)

# Exit the program
sys.exit(0)
```

### `datetime` - Date and Time

```python
from datetime import datetime, timedelta

# Get the current date and time
now = datetime.now()
print(now)

# Format a date
formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
print(formatted_date)

# Parse a date string
date_string = '2023-01-01 12:00:00'
parsed_date = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
print(parsed_date)

# Add or subtract time
tomorrow = now + timedelta(days=1)
print(tomorrow)
```

### `math` - Mathematical Functions

```python
import math

# Constants
print(math.pi)      # Output: 3.141592653589793
print(math.e)       # Output: 2.718281828459045

# Trigonometric functions
print(math.sin(math.pi/2))  # Output: 1.0
print(math.cos(math.pi))    # Output: -1.0
print(math.tan(math.pi/4))  # Output: 0.9999999999999999

# Logarithmic functions
print(math.log(math.e))     # Output: 1.0
print(math.log10(100))      # Output: 2.0

# Other functions
print(math.sqrt(16))        # Output: 4.0
print(math.factorial(5))    # Output: 120
print(math.gcd(12, 8))      # Output: 4
```

### `random` - Generate Random Numbers

```python
import random

# Generate a random float between 0 and 1
print(random.random())  # Output: 0.123456789...

# Generate a random integer between a and b (inclusive)
print(random.randint(1, 10))  # Output: 5

# Choose a random element from a sequence
print(random.choice(['apple', 'banana', 'cherry']))  # Output: 'banana'

# Shuffle a list in place
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list)  # Output: [3, 1, 5, 2, 4]

# Generate a random sample without replacement
print(random.sample(range(1, 11), 3))  # Output: [7, 3, 9]
```

### `json` - JSON Encoder and Decoder

```python
import json

# Convert a Python object to a JSON string
data = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}
json_string = json.dumps(data, indent=4)
print(json_string)

# Convert a JSON string to a Python object
parsed_data = json.loads(json_string)
print(parsed_data['name'])  # Output: 'John'

# Write JSON to a file
with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)

# Read JSON from a file
with open('data.json', 'r') as f:
    loaded_data = json.load(f)
    print(loaded_data)
```

### `re` - Regular Expressions

```python
import re

# Search for a pattern in a string
text = 'The quick brown fox jumps over the lazy dog'
match = re.search(r'fox', text)
if match:
    print(f"Found '{match.group()}' at position {match.start()}")

# Find all occurrences of a pattern
matches = re.findall(r'\b\w{4}\b', text)  # Find all 4-letter words
print(matches)  # Output: ['quick', 'over', 'lazy']

# Replace a pattern
new_text = re.sub(r'fox', 'cat', text)
print(new_text)  # Output: 'The quick brown cat jumps over the lazy dog'

# Split a string by a pattern
split_text = re.split(r'\s+', text)
print(split_text)  # Output: ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
```

### `collections` - Container Data Types

```python
from collections import Counter, defaultdict, namedtuple, deque

# Counter: Count occurrences of elements
counter = Counter(['apple', 'banana', 'apple', 'cherry', 'apple'])
print(counter)  # Output: Counter({'apple': 3, 'banana': 1, 'cherry': 1})
print(counter['apple'])  # Output: 3
print(counter.most_common(1))  # Output: [('apple', 3)]

# defaultdict: Dictionary with default values
dd = defaultdict(list)
dd['a'].append(1)
dd['a'].append(2)
dd['b'].append(3)
print(dd)  # Output: defaultdict(<class 'list'>, {'a': [1, 2], 'b': [3]})

# namedtuple: Tuple with named fields
Person = namedtuple('Person', ['name', 'age', 'city'])
person = Person('John', 30, 'New York')
print(person.name)  # Output: 'John'
print(person.age)   # Output: 30
print(person.city)  # Output: 'New York'

# deque: Double-ended queue
d = deque([1, 2, 3])
d.append(4)        # Add to the right
d.appendleft(0)    # Add to the left
print(d)           # Output: deque([0, 1, 2, 3, 4])
print(d.pop())     # Output: 4
print(d.popleft()) # Output: 0
print(d)           # Output: deque([1, 2, 3])
```

## Third-Party Packages

Python has a vast ecosystem of third-party packages that extend its functionality. These packages can be installed using package managers like `pip` or `conda`.

### Installing Packages with `pip`

```bash
# Install a package
pip install package_name

# Install a specific version
pip install package_name==1.2.3

# Upgrade a package
pip install --upgrade package_name

# Uninstall a package
pip uninstall package_name

# List installed packages
pip list

# Show information about a package
pip show package_name

# Install packages from a requirements file
pip install -r requirements.txt
```

### Creating a `requirements.txt` File

A `requirements.txt` file lists the packages required for a project, making it easy to recreate the environment.

```
# requirements.txt
numpy==1.21.0
pandas>=1.3.0
matplotlib
```

You can generate a `requirements.txt` file from your current environment:

```bash
pip freeze > requirements.txt
```

### Popular Third-Party Packages

Here are some popular third-party packages:

- **NumPy**: Numerical computing with arrays and matrices
- **Pandas**: Data analysis and manipulation
- **Matplotlib**: Data visualization
- **Requests**: HTTP library for making requests
- **Beautiful Soup**: Web scraping library
- **Django**: Web framework
- **Flask**: Lightweight web framework
- **SQLAlchemy**: SQL toolkit and ORM
- **PyTorch**: Deep learning framework
- **TensorFlow**: Machine learning framework

### Example: Using the `requests` Package

```python
import requests

# Make a GET request
response = requests.get('https://api.github.com/user', auth=('username', 'password'))
print(response.status_code)  # Output: 200
print(response.json())       # Output: {'login': 'username', ...}

# Make a POST request
data = {'key': 'value'}
response = requests.post('https://httpbin.org/post', data=data)
print(response.text)
```

## Creating Distributable Packages

You can create your own distributable packages that others can install using `pip`.

### Project Structure

A typical project structure for a distributable package might look like this:

```
my_project/
├── LICENSE
├── README.md
├── pyproject.toml
├── setup.py
├── setup.cfg
├── src/
│   └── my_package/
│       ├── __init__.py
│       ├── module1.py
│       └── module2.py
└── tests/
    ├── __init__.py
    ├── test_module1.py
    └── test_module2.py
```

### `setup.py`

The `setup.py` file contains metadata about your package and is used by `setuptools` to build and distribute your package.

```python
# setup.py

from setuptools import setup, find_packages

setup(
    name="my_package",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A short description of your package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my_package",
    packages=find_packages(where="src"),
    package_dir={"":"src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "numpy>=1.18.0",
        "pandas>=1.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "pytest-cov>=2.10.0",
            "black>=20.8b1",
        ],
    },
)
```

### Modern Python Packaging with `pyproject.toml`

Modern Python packaging uses a `pyproject.toml` file instead of `setup.py`.

```toml
# pyproject.toml

[build-system]
requires = ["setuptools>=42", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "my_package"
version = "0.1.0"
authors = [
    {name = "Your Name", email = "your.email@example.com"},
]
description = "A short description of your package"
readme = "README.md"
requires-python = ">=3.6"
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]
dependencies = [
    "numpy>=1.18.0",
    "pandas>=1.0.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=6.0.0",
    "pytest-cov>=2.10.0",
    "black>=20.8b1",
]

[project.urls]
"Homepage" = "https://github.com/yourusername/my_package"
"Bug Tracker" = "https://github.com/yourusername/my_package/issues"
```

### Building and Distributing Your Package

```bash
# Install build tools
pip install build twine

# Build your package
python -m build

# Upload your package to PyPI
twine upload dist/*
```

## Best Practices

### Module Organization

- Keep modules small and focused on a single responsibility.
- Use clear and descriptive names for modules and packages.
- Organize related modules into packages.
- Use `__init__.py` files to expose a clean API.

### Import Style

- Prefer explicit imports (`from module import item`) over wildcard imports (`from module import *`).
- Group imports in the following order:
  1. Standard library imports
  2. Related third-party imports
  3. Local application/library specific imports
- Within each group, sort imports alphabetically.

```python
# Good import style
import os
import sys
from datetime import datetime

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from my_package import module1
from my_package.subpackage import module2
```

### Documentation

- Document your modules, classes, and functions with docstrings.
- Use a consistent docstring format (e.g., Google style, NumPy style, or reStructuredText).
- Include examples in your docstrings.

```python
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.
        
    Returns:
        float: The area of the rectangle.
        
    Examples:
        >>> calculate_area(5, 3)
        15.0
        >>> calculate_area(2.5, 2)
        5.0
    """
    return length * width
```

### Version Management

- Use semantic versioning (MAJOR.MINOR.PATCH) for your packages.
- Specify version requirements for dependencies.
- Use version control (e.g., Git) to track changes to your code.

### Testing

- Write tests for your modules and packages.
- Use a testing framework like `pytest` or `unittest`.
- Run tests automatically using continuous integration (CI) tools.

```python
# test_module1.py

import pytest
from my_package import module1

def test_function1():
    assert module1.function1() == "This is function1 from module1"

def test_function2():
    assert module1.function2(2, 3) == 5
```

## Common Pitfalls

### Circular Imports

Circular imports occur when two or more modules import each other, directly or indirectly.

```python
# module_a.py
from module_b import function_b

def function_a():
    return "Function A"
```

```python
# module_b.py
from module_a import function_a

def function_b():
    return "Function B"
```

To avoid circular imports:
- Restructure your code to eliminate the circular dependency.
- Move the import statement inside the function that needs it.
- Import the module, not the specific function.

```python
# module_a.py
def function_a():
    return "Function A"
```

```python
# module_b.py
import module_a

def function_b():
    return f"Function B calling {module_a.function_a()}"
```

### Shadowing Built-in Names

Avoiding using names that shadow built-in functions or modules.

```python
# Bad practice
list = [1, 2, 3]  # Shadows the built-in list type
print(list)       # Output: [1, 2, 3]
list = list(range(5))  # TypeError: 'list' object is not callable
```

```python
# Good practice
my_list = [1, 2, 3]
print(my_list)       # Output: [1, 2, 3]
my_list = list(range(5))  # Works fine
```

### Import Side Effects

Avoid side effects in module-level code, as they occur when the module is imported.

```python
# Bad practice
# my_module.py
print("This will be printed when the module is imported")
data = fetch_data_from_api()  # This will run when the module is imported
```

```python
# Good practice
# my_module.py
def fetch_and_process_data():
    print("Fetching data...")
    data = fetch_data_from_api()
    return process_data(data)

if __name__ == "__main__":
    # This will only run when the module is executed directly
    fetch_and_process_data()
```

### Namespace Pollution

Avoid polluting the namespace with too many imports.

```python
# Bad practice
from module1 import *
from module2 import *
# It's unclear where function1 comes from
result = function1()
```

```python
# Good practice
from module1 import function1
from module2 import function2
result = function1()
```

### Hardcoded Paths

Avoid hardcoded paths in your modules.

```python
# Bad practice
with open('C:/Users/username/data/file.txt', 'r') as f:
    data = f.read()
```

```python
# Good practice
import os

# Use relative paths
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, 'data', 'file.txt')

with open(file_path, 'r') as f:
    data = f.read()
```

### Not Using `__all__`

When a module is intended to be used with `from module import *`, not defining `__all__` can lead to unexpected imports.

```python
# Bad practice
# my_module.py
def public_function():
    return "This is a public function"

def _internal_function():
    return "This is an internal function"

# When someone does `from my_module import *`, _internal_function will also be imported
```

```python
# Good practice
# my_module.py
__all__ = ['public_function']

def public_function():
    return "This is a public function"

def _internal_function():
    return "This is an internal function"

# When someone does `from my_module import *`, only public_function will be imported
```

## Next Steps

Now that you understand modules and packages in Python, you're ready to move on to [Object-Oriented Programming](../14_Object_Oriented_Programming/README.md).