# Error Handling in Python

Error handling is a critical aspect of writing robust Python code. This section covers how to handle exceptions, create custom exceptions, and implement error handling best practices.

## Understanding Exceptions

Exceptions are events that occur during the execution of a program that disrupt the normal flow of instructions. When an error occurs, Python creates an exception object containing information about the error.

### Types of Errors

Python has two main categories of errors:

1. **Syntax Errors**: Errors in the syntax of the code that prevent the program from running.
2. **Exceptions**: Errors detected during execution that may allow the program to continue if handled properly.

#### Syntax Errors

Syntax errors occur when the Python parser is unable to understand the code due to incorrect syntax.

```python
# Syntax error example
if True
    print("This will cause a syntax error")
# SyntaxError: invalid syntax
```

Syntax errors must be fixed before the program can run.

#### Exceptions

Exceptions occur during the execution of a program when something unexpected happens.

```python
# Exception example
x = 10 / 0  # Raises ZeroDivisionError

my_list = [1, 2, 3]
print(my_list[5])  # Raises IndexError

print(undefined_variable)  # Raises NameError
```

### Common Built-in Exceptions

Python provides many built-in exceptions that are raised when specific errors occur.

| Exception | Description |
|-----------|-------------|
| `ArithmeticError` | Base class for arithmetic errors |
| `AssertionError` | Raised when an `assert` statement fails |
| `AttributeError` | Raised when attribute reference or assignment fails |
| `EOFError` | Raised when `input()` hits end-of-file condition |
| `FileExistsError` | Raised when trying to create a file that already exists |
| `FileNotFoundError` | Raised when a file or directory is requested but doesn't exist |
| `ImportError` | Raised when an import statement fails |
| `IndentationError` | Raised when there is incorrect indentation |
| `IndexError` | Raised when a sequence subscript is out of range |
| `KeyError` | Raised when a dictionary key is not found |
| `KeyboardInterrupt` | Raised when the user hits the interrupt key (Ctrl+C) |
| `MemoryError` | Raised when an operation runs out of memory |
| `NameError` | Raised when a local or global name is not found |
| `NotImplementedError` | Raised when an abstract method requires an override |
| `OSError` | Raised when a system operation causes a system-related error |
| `OverflowError` | Raised when a calculation exceeds maximum limit for a numeric type |
| `RecursionError` | Raised when the interpreter detects maximum recursion depth |
| `RuntimeError` | Raised when an error doesn't fall under any other category |
| `StopIteration` | Raised by `next()` when an iterator has no more items |
| `SyntaxError` | Raised when there is a syntax error in the code |
| `TabError` | Raised when indentation consists of inconsistent tabs and spaces |
| `TypeError` | Raised when an operation is applied to an object of inappropriate type |
| `UnboundLocalError` | Raised when a reference is made to a local variable before assignment |
| `UnicodeError` | Raised when a Unicode-related encoding or decoding error occurs |
| `ValueError` | Raised when a function receives an argument of correct type but inappropriate value |
| `ZeroDivisionError` | Raised when division or modulo operation has a second argument of zero |

### Exception Hierarchy

Python exceptions form a hierarchy, with `BaseException` at the top.

```
BaseException
 ├── SystemExit
 ├── KeyboardInterrupt
 ├── GeneratorExit
 └── Exception
      ├── StopIteration
      ├── ArithmeticError
      │    ├── FloatingPointError
      │    ├── OverflowError
      │    └── ZeroDivisionError
      ├── AssertionError
      ├── AttributeError
      ├── BufferError
      ├── EOFError
      ├── ImportError
      │    └── ModuleNotFoundError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      ├── MemoryError
      ├── NameError
      │    └── UnboundLocalError
      ├── OSError
      │    ├── BlockingIOError
      │    ├── ChildProcessError
      │    ├── ConnectionError
      │    │    ├── BrokenPipeError
      │    │    ├── ConnectionAbortedError
      │    │    ├── ConnectionRefusedError
      │    │    └── ConnectionResetError
      │    ├── FileExistsError
      │    ├── FileNotFoundError
      │    ├── InterruptedError
      │    ├── IsADirectoryError
      │    ├── NotADirectoryError
      │    ├── PermissionError
      │    ├── ProcessLookupError
      │    └── TimeoutError
      ├── ReferenceError
      ├── RuntimeError
      │    ├── NotImplementedError
      │    └── RecursionError
      ├── SyntaxError
      │    └── IndentationError
      │         └── TabError
      ├── SystemError
      ├── TypeError
      ├── ValueError
      │    └── UnicodeError
      │         ├── UnicodeDecodeError
      │         ├── UnicodeEncodeError
      │         └── UnicodeTranslateError
      └── Warning
           ├── DeprecationWarning
           ├── PendingDeprecationWarning
           ├── RuntimeWarning
           ├── SyntaxWarning
           ├── UserWarning
           ├── FutureWarning
           ├── ImportWarning
           ├── UnicodeWarning
           ├── BytesWarning
           └── ResourceWarning
```

Understanding this hierarchy is important when catching exceptions, as catching a parent exception will also catch all of its child exceptions.

## Basic Exception Handling

### The `try`-`except` Block

The `try`-`except` block is used to catch and handle exceptions.

```python
try:
    # Code that might raise an exception
    x = 10 / 0
except ZeroDivisionError:
    # Code to handle the exception
    print("Cannot divide by zero!")
```

### Handling Multiple Exceptions

You can handle multiple exceptions in different ways.

```python
# Handling multiple exceptions with separate except blocks
try:
    value = int(input("Enter a number: "))
    result = 10 / value
    print(result)
except ValueError:
    print("Invalid input. Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Handling multiple exceptions with a single except block
try:
    value = int(input("Enter a number: "))
    result = 10 / value
    print(result)
except (ValueError, ZeroDivisionError):
    print("Invalid input or division by zero.")
```

### Catching All Exceptions

You can catch all exceptions using a bare `except` clause, but this is generally not recommended as it can hide bugs.

```python
try:
    # Some code that might raise an exception
    x = 10 / 0
except:
    # This will catch any exception
    print("An error occurred.")
```

A better approach is to catch `Exception`, which will catch all standard exceptions but not system exits, keyboard interrupts, etc.

```python
try:
    # Some code that might raise an exception
    x = 10 / 0
except Exception as e:
    # This will catch all standard exceptions
    print(f"An error occurred: {e}")
```

### Accessing Exception Information

You can access information about the exception using the `as` keyword.

```python
try:
    x = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
    print(f"Type: {type(e).__name__}")
    print(f"Args: {e.args}")
```

### The `else` Clause

The `else` clause is executed if no exceptions are raised in the `try` block.

```python
try:
    value = int(input("Enter a number: "))
    result = 10 / value
except ValueError:
    print("Invalid input. Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    # This block executes if no exceptions were raised
    print(f"Result: {result}")
```

### The `finally` Clause

The `finally` clause is always executed, whether an exception was raised or not. It's typically used for cleanup operations.

```python
try:
    file = open("file.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    # This block always executes
    if 'file' in locals() and not file.closed:
        file.close()
        print("File closed.")
```

### Combining `try`, `except`, `else`, and `finally`

You can combine all these clauses in a single `try` statement.

```python
try:
    value = int(input("Enter a number: "))
    result = 10 / value
except ValueError:
    print("Invalid input. Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(f"Result: {result}")
finally:
    print("Execution completed.")
```

## Raising Exceptions

### The `raise` Statement

You can raise exceptions using the `raise` statement.

```python
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return a / b

try:
    result = divide(10, 0)
except ZeroDivisionError as e:
    print(f"Error: {e}")
```

### Re-raising Exceptions

You can re-raise an exception after handling it.

```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Handling division by zero...")
    raise  # Re-raises the last exception
```

You can also catch an exception and raise a different one.

```python
try:
    x = 10 / 0
except ZeroDivisionError:
    raise ValueError("A value error occurred due to division by zero")
```

### Exception Chaining

You can chain exceptions to preserve the original exception information.

```python
try:
    x = 10 / 0
except ZeroDivisionError as e:
    raise ValueError("A value error occurred") from e
```

This will show both exceptions in the traceback, making it clear that the `ValueError` was caused by the `ZeroDivisionError`.

## Custom Exceptions

### Creating Custom Exceptions

You can create custom exceptions by subclassing `Exception` or one of its subclasses.

```python
class CustomError(Exception):
    """Base class for custom exceptions in this module."""
    pass

class ValueTooSmallError(CustomError):
    """Raised when the input value is too small."""
    pass

class ValueTooLargeError(CustomError):
    """Raised when the input value is too large."""
    pass

def check_value(value):
    if value < 10:
        raise ValueTooSmallError("Value is too small. It should be at least 10.")
    if value > 100:
        raise ValueTooLargeError("Value is too large. It should be at most 100.")
    return value

try:
    check_value(5)
except ValueTooSmallError as e:
    print(f"Error: {e}")
except ValueTooLargeError as e:
    print(f"Error: {e}")
```

### Adding Attributes to Custom Exceptions

You can add attributes to custom exceptions to provide more information.

```python
class InsufficientFundsError(Exception):
    """Raised when a withdrawal is attempted with insufficient funds."""
    def __init__(self, balance, amount, message="Insufficient funds"):
        self.balance = balance
        self.amount = amount
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}: balance={self.balance}, amount={self.amount}"

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return self.balance

try:
    account = BankAccount(50)
    account.withdraw(100)
except InsufficientFundsError as e:
    print(f"Error: {e}")
    print(f"Balance: {e.balance}, Amount: {e.amount}")
```

## Advanced Exception Handling

### Context Managers

Context managers (`with` statement) can be used for automatic resource management and exception handling.

```python
# Using a context manager for file handling
with open("file.txt", "r") as file:
    content = file.read()
# File is automatically closed, even if an exception occurs

# Creating a custom context manager
class MyContextManager:
    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting the context")
        if exc_type is not None:
            print(f"An exception occurred: {exc_val}")
            # Return True to suppress the exception
            return True

with MyContextManager() as cm:
    print("Inside the context")
    raise ValueError("An error occurred")

print("After the context")
```

### Exception Handling in Generators

Generators can use `try`-`except` blocks to handle exceptions.

```python
def generator_with_exception_handling():
    try:
        yield 1
        yield 2
        yield 3 / 0  # This will raise a ZeroDivisionError
        yield 4
    except ZeroDivisionError:
        yield "Division by zero caught"
        yield 5

for item in generator_with_exception_handling():
    print(item)
```

### Cleanup with `try`-`finally`

The `try`-`finally` block is useful for cleanup operations that must be performed regardless of whether an exception occurs.

```python
def process_file(filename):
    file = None
    try:
        file = open(filename, "r")
        content = file.read()
        return content
    finally:
        if file is not None and not file.closed:
            file.close()
            print("File closed.")

try:
    content = process_file("nonexistent_file.txt")
except FileNotFoundError:
    print("File not found.")
```

### Exception Groups (Python 3.11+)

Python 3.11 introduced exception groups, which allow multiple exceptions to be raised and caught together.

```python
# This feature requires Python 3.11 or later
import sys

if sys.version_info >= (3, 11):
    from exceptiongroup import ExceptionGroup

    def process_items(items):
        errors = []
        results = []
        
        for i, item in enumerate(items):
            try:
                results.append(process_item(item))
            except Exception as e:
                errors.append((i, e))
        
        if errors:
            exceptions = [e for _, e in errors]
            raise ExceptionGroup("Multiple errors occurred", exceptions)
        
        return results

    def process_item(item):
        if item == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        if item < 0:
            raise ValueError("Negative values not allowed")
        return 10 / item

    try:
        results = process_items([2, 0, -1, 5])
    except* ZeroDivisionError as e:
        print(f"Division errors: {e}")
    except* ValueError as e:
        print(f"Value errors: {e}")
```

## Debugging Techniques

### Using `print` Statements

The simplest debugging technique is to add `print` statements to your code.

```python
def divide(a, b):
    print(f"Dividing {a} by {b}")
    try:
        result = a / b
        print(f"Result: {result}")
        return result
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        raise

try:
    divide(10, 0)
except ZeroDivisionError:
    print("Caught division by zero in main code")
```

### Using the `logging` Module

The `logging` module provides a more flexible way to output debug information.

```python
import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='app.log',
    filemode='w'
)

# Create a console handler
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

def divide(a, b):
    logging.debug(f"Dividing {a} by {b}")
    try:
        result = a / b
        logging.debug(f"Result: {result}")
        return result
    except ZeroDivisionError as e:
        logging.error(f"Error: {e}", exc_info=True)
        raise

try:
    divide(10, 0)
except ZeroDivisionError:
    logging.info("Caught division by zero in main code")
```

### Using the `traceback` Module

The `traceback` module provides functions to extract, format, and print stack traces of exceptions.

```python
import traceback

def func3():
    raise ValueError("An error occurred in func3")

def func2():
    func3()

def func1():
    try:
        func2()
    except ValueError:
        print("Traceback (most recent call last):")
        traceback.print_exc()

func1()
```

### Using the `pdb` Module

The `pdb` module provides an interactive debugger for Python programs.

```python
import pdb

def complex_function(a, b):
    result = a + b
    pdb.set_trace()  # Start the debugger here
    result = result * 2
    return result

complex_function(3, 4)
```

When the debugger starts, you can use commands like:
- `n` (next): Execute the current line and move to the next line
- `s` (step): Step into a function call
- `c` (continue): Continue execution until the next breakpoint
- `q` (quit): Quit the debugger
- `p expression`: Print the value of an expression
- `l` (list): List the source code around the current line

### Using `breakpoint()` (Python 3.7+)

Python 3.7 introduced the `breakpoint()` function, which is a more convenient way to start the debugger.

```python
def complex_function(a, b):
    result = a + b
    breakpoint()  # Start the debugger here
    result = result * 2
    return result

complex_function(3, 4)
```

## Best Practices

### Be Specific When Catching Exceptions

Catch only the specific exceptions you expect and can handle.

```python
# Good practice
try:
    value = int(input("Enter a number: "))
except ValueError:
    print("Invalid input. Please enter a number.")

# Bad practice
try:
    value = int(input("Enter a number: "))
except:
    print("An error occurred.")
```

### Use Exceptions for Exceptional Cases

Exceptions should be used for exceptional cases, not for normal control flow.

```python
# Good practice
def get_user_by_id(user_id):
    user = database.find_user(user_id)
    if user is None:
        raise UserNotFoundError(f"User with ID {user_id} not found")
    return user

# Bad practice (using exceptions for normal control flow)
def get_user_by_id(user_id):
    try:
        return database.find_user(user_id)
    except DatabaseError:
        return None
```

### Clean Up Resources

Always clean up resources, even if an exception occurs.

```python
# Good practice
try:
    file = open("file.txt", "r")
    content = file.read()
finally:
    if 'file' in locals() and not file.closed:
        file.close()

# Better practice (using context manager)
with open("file.txt", "r") as file:
    content = file.read()
```

### Provide Meaningful Error Messages

Provide clear and informative error messages in your exceptions.

```python
# Good practice
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError(f"Cannot divide {a} by zero")
    return a / b

# Bad practice
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError()
    return a / b
```

### Document Exceptions

Document the exceptions that your functions can raise.

```python
def process_file(filename):
    """
    Process a file and return its content.
    
    Args:
        filename (str): The name of the file to process.
        
    Returns:
        str: The content of the file.
        
    Raises:
        FileNotFoundError: If the file does not exist.
        PermissionError: If the file cannot be read due to permission issues.
    """
    with open(filename, "r") as file:
        return file.read()
```

### Use Custom Exceptions for Domain-Specific Errors

Create custom exceptions for domain-specific errors to make your code more readable and maintainable.

```python
class DatabaseError(Exception):
    """Base class for database-related exceptions."""
    pass

class ConnectionError(DatabaseError):
    """Raised when a database connection fails."""
    pass

class QueryError(DatabaseError):
    """Raised when a database query fails."""
    pass

def execute_query(query):
    try:
        # Execute the query
        pass
    except Exception as e:
        raise QueryError(f"Query failed: {query}") from e
```

### Avoid Catching `BaseException`

Avoid catching `BaseException` as it includes exceptions like `SystemExit`, `KeyboardInterrupt`, and `GeneratorExit` that are typically not meant to be caught.

```python
# Good practice
try:
    # Some code
    pass
except Exception as e:
    # Handle standard exceptions
    pass

# Bad practice
try:
    # Some code
    pass
except BaseException as e:
    # This will catch SystemExit, KeyboardInterrupt, etc.
    pass
```

### Use `else` Clause Appropriately

Use the `else` clause to clearly separate code that should run only if no exceptions are raised.

```python
# Good practice
try:
    value = int(input("Enter a number: "))
except ValueError:
    print("Invalid input. Please enter a number.")
else:
    # This code runs only if no exceptions were raised
    print(f"You entered: {value}")
```

### Use `finally` for Cleanup

Use the `finally` clause for cleanup operations that must be performed regardless of whether an exception occurs.

```python
lock = threading.Lock()

try:
    lock.acquire()
    # Critical section
    pass
finally:
    # This will always execute, ensuring the lock is released
    lock.release()
```

## Common Pitfalls

### Catching Too Many Exceptions

Catching too many exceptions can hide bugs and make debugging difficult.

```python
# Bad practice
try:
    # A lot of code
    pass
except Exception:
    # Catches all standard exceptions
    pass
```

### Silencing Exceptions

Silencing exceptions without proper handling can lead to unexpected behavior.

```python
# Bad practice
try:
    result = 10 / 0
except ZeroDivisionError:
    pass  # Silently ignoring the exception
```

### Using Bare `except` Clauses

Using bare `except` clauses can catch unexpected exceptions and hide bugs.

```python
# Bad practice
try:
    # Some code
    pass
except:
    # Catches all exceptions, including SystemExit, KeyboardInterrupt, etc.
    pass
```

### Not Cleaning Up Resources

Failing to clean up resources can lead to resource leaks.

```python
# Bad practice
file = open("file.txt", "r")
content = file.read()
# File is not closed if an exception occurs
```

### Raising Exceptions in `__del__`

Raising exceptions in `__del__` methods can lead to unexpected behavior, as exceptions in `__del__` are ignored in some cases.

```python
# Bad practice
class MyClass:
    def __del__(self):
        raise Exception("An error occurred during cleanup")
```

### Using Exceptions for Control Flow

Using exceptions for normal control flow can make the code harder to understand and less efficient.

```python
# Bad practice
def find_index(lst, value):
    try:
        return lst.index(value)
    except ValueError:
        return -1

# Good practice
def find_index(lst, value):
    if value in lst:
        return lst.index(value)
    return -1
```

### Not Preserving Exception Context

Not preserving the original exception context can make debugging difficult.

```python
# Bad practice
try:
    # Some code
    pass
except SomeException:
    raise AnotherException("An error occurred")  # Original exception context is lost

# Good practice
try:
    # Some code
    pass
except SomeException as e:
    raise AnotherException("An error occurred") from e  # Original exception context is preserved
```

## Next Steps

Now that you understand error handling in Python, you're ready to move on to [Modules & Packages](../13_Modules_Packages/README.md).