# Introduction to Python

## What is Python?

Python is a high-level, interpreted programming language known for its readability, simplicity, and versatility. Created by Guido van Rossum and first released in 1991, Python has grown to become one of the most popular programming languages in the world.

## Key Features of Python

- **Readability**: Python's syntax is designed to be readable and straightforward, using indentation to define code blocks.
- **Versatility**: Python can be used for web development, data analysis, artificial intelligence, scientific computing, automation, and more.
- **Interpreted**: Python code is executed line by line, making debugging easier.
- **Dynamically Typed**: Variable types are determined at runtime, not in advance.
- **Extensive Libraries**: Python has a vast ecosystem of libraries and frameworks that extend its functionality.
- **Cross-Platform**: Python runs on various operating systems, including Windows, macOS, and Linux.

## Python 2 vs Python 3

Python has two major versions: Python 2 and Python 3. Python 2 reached its end of life on January 1, 2020, and is no longer supported. This guide focuses exclusively on Python 3, which includes significant improvements and is the future of the language.

Key differences between Python 2 and 3:

| Feature | Python 2 | Python 3 |
|---------|----------|----------|
| Print statement | `print "Hello"` | `print("Hello")` |
| Integer division | `5 / 2 = 2` | `5 / 2 = 2.5` |
| Unicode | ASCII by default | UTF-8 by default |
| Error handling | `except Exception, e` | `except Exception as e` |

## Installing Python

### Windows

1. Download the latest Python installer from [python.org](https://www.python.org/downloads/)
2. Run the installer
3. Check "Add Python to PATH" during installation
4. Click "Install Now"

### macOS

1. Install Homebrew (if not already installed) by running:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
2. Install Python using Homebrew:
   ```bash
   brew install python
   ```

### Linux

Most Linux distributions come with Python pre-installed. To install the latest version:

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-pip

# Fedora
sudo dnf install python3 python3-pip

# Arch Linux
sudo pacman -S python python-pip
```

## Verifying Installation

To verify that Python is installed correctly, open a terminal or command prompt and type:

```bash
python --version  # or python3 --version on some systems
```

You should see the Python version number displayed.

## Python Development Environments

### Interactive Shell

Python comes with an interactive shell where you can execute code line by line. To start it, open a terminal and type `python` or `python3`.

### Integrated Development Environments (IDEs)

- **PyCharm**: A powerful IDE with code completion, debugging, and more
- **Visual Studio Code**: A lightweight, extensible editor with Python support
- **Jupyter Notebook**: An interactive environment for data science and exploration
- **IDLE**: Python's built-in development environment (simple but useful for beginners)

## Your First Python Program

Let's write the traditional "Hello, World!" program:

1. Open a text editor
2. Type the following code:

```python
# This is a comment
print("Hello, World!")
```

3. Save the file as `hello.py`
4. Run the program:
   - From the command line: `python hello.py`
   - From an IDE: Use the run button

## Python Syntax Basics

### Comments

```python
# This is a single-line comment

"""
This is a multi-line comment
or docstring that can span
multiple lines
"""
```

### Indentation

Python uses indentation (whitespace) to define code blocks, unlike many other languages that use braces `{}`. The standard is to use 4 spaces for each level of indentation.

```python
if True:
    print("This is indented")  # 4 spaces
    if True:
        print("Another level")  # 8 spaces
print("Back to no indentation")
```

## Python Zen

Python has a set of guiding principles known as "The Zen of Python." You can view it by running:

```python
import this
```

Some key principles include:
- Beautiful is better than ugly
- Explicit is better than implicit
- Simple is better than complex
- Readability counts

## Next Steps

Now that you have Python installed and understand the basics, you're ready to move on to [Variables and Data Types](../02_Variables_Data_Types/README.md).