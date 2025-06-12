# File I/O in Python

File Input/Output (I/O) operations are essential for working with external data in Python. This section covers how to read from and write to files, work with different file formats, and handle file-related operations.

## File Basics

### File Paths

Before working with files, you need to understand file paths. Python supports both absolute and relative paths.

```python
# Absolute path (starts from the root directory)
absolute_path = "/home/user/documents/file.txt"  # Unix/Linux/macOS
absolute_path = "C:\\Users\\user\\Documents\\file.txt"  # Windows

# Relative path (relative to the current working directory)
relative_path = "data/file.txt"
relative_path = "../parent_directory/file.txt"  # Go up one directory
```

### Working with Paths Using `os.path`

The `os.path` module provides functions for working with file paths in a platform-independent way.

```python
import os.path

# Join path components
path = os.path.join("directory", "subdirectory", "file.txt")
print(path)  # 'directory/subdirectory/file.txt' (Unix) or 'directory\subdirectory\file.txt' (Windows)

# Get the directory name and base name
directory = os.path.dirname("/home/user/documents/file.txt")
print(directory)  # '/home/user/documents'

base = os.path.basename("/home/user/documents/file.txt")
print(base)  # 'file.txt'

# Split path into directory and file
directory, filename = os.path.split("/home/user/documents/file.txt")
print(directory)  # '/home/user/documents'
print(filename)  # 'file.txt'

# Split filename into name and extension
name, extension = os.path.splitext("file.txt")
print(name)  # 'file'
print(extension)  # '.txt'

# Check if a path exists
exists = os.path.exists("/home/user/documents/file.txt")
print(exists)  # True or False

# Check if a path is a file or directory
is_file = os.path.isfile("/home/user/documents/file.txt")
print(is_file)  # True or False

is_dir = os.path.isdir("/home/user/documents")
print(is_dir)  # True or False

# Get the absolute path
absolute = os.path.abspath("data/file.txt")
print(absolute)  # Full absolute path

# Get the size of a file in bytes
size = os.path.getsize("/home/user/documents/file.txt")
print(size)  # File size in bytes
```

### Working with Paths Using `pathlib` (Python 3.4+)

The `pathlib` module provides an object-oriented approach to file paths, which is often more convenient than `os.path`.

```python
from pathlib import Path

# Create a Path object
path = Path("directory/subdirectory/file.txt")

# Join path components
path = Path("directory") / "subdirectory" / "file.txt"
print(path)  # directory/subdirectory/file.txt

# Get the parent directory
parent = path.parent
print(parent)  # directory/subdirectory

# Get the filename
name = path.name
print(name)  # file.txt

# Get the stem (filename without extension)
stem = path.stem
print(stem)  # file

# Get the suffix (extension)
suffix = path.suffix
print(suffix)  # .txt

# Check if a path exists
exists = path.exists()
print(exists)  # True or False

# Check if a path is a file or directory
is_file = path.is_file()
print(is_file)  # True or False

is_dir = path.is_dir()
print(is_dir)  # True or False

# Get the absolute path
absolute = path.absolute()
print(absolute)  # Full absolute path

# Get the size of a file in bytes
size = path.stat().st_size
print(size)  # File size in bytes

# Create directories
Path("new_directory/subdirectory").mkdir(parents=True, exist_ok=True)

# List directory contents
for item in Path("directory").iterdir():
    print(item)

# Find files matching a pattern
for python_file in Path("directory").glob("*.py"):
    print(python_file)

# Recursive globbing
for python_file in Path("directory").rglob("*.py"):
    print(python_file)
```

## Opening and Closing Files

### Using the `open()` Function

The `open()` function is used to open a file and returns a file object.

```python
# Basic syntax: open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

# Open a file for reading (default mode is 'r')
file = open("file.txt", "r")

# Read the entire file content
content = file.read()
print(content)

# Close the file when done
file.close()
```

### File Modes

The `mode` parameter in the `open()` function specifies how the file should be opened.

- `'r'`: Read (default). Opens a file for reading; error if the file doesn't exist.
- `'w'`: Write. Opens a file for writing; creates the file if it doesn't exist or truncates it if it does.
- `'a'`: Append. Opens a file for appending; creates the file if it doesn't exist.
- `'x'`: Exclusive creation. Opens a file for writing, but fails if the file already exists.
- `'b'`: Binary mode. Opens a file in binary mode (e.g., `'rb'`, `'wb'`).
- `'t'`: Text mode (default). Opens a file in text mode (e.g., `'rt'`, `'wt'`).
- `'+'`: Update mode. Opens a file for updating (reading and writing) (e.g., `'r+'`, `'w+'`).

```python
# Open for reading (text mode)
file = open("file.txt", "r")  # or "rt"

# Open for writing (text mode)
file = open("file.txt", "w")  # or "wt"

# Open for appending (text mode)
file = open("file.txt", "a")  # or "at"

# Open for reading and writing (text mode)
file = open("file.txt", "r+")  # or "rt+"

# Open for reading (binary mode)
file = open("file.bin", "rb")

# Open for writing (binary mode)
file = open("file.bin", "wb")

# Open for appending (binary mode)
file = open("file.bin", "ab")

# Open for reading and writing (binary mode)
file = open("file.bin", "rb+")
```

### Using the `with` Statement (Context Manager)

The `with` statement is the recommended way to open files because it automatically closes the file when the block is exited, even if an exception is raised.

```python
# Using with statement
with open("file.txt", "r") as file:
    content = file.read()
    print(content)
# File is automatically closed when the block is exited

# Multiple files can be opened in a single with statement
with open("input.txt", "r") as input_file, open("output.txt", "w") as output_file:
    content = input_file.read()
    output_file.write(content.upper())
# Both files are automatically closed
```

## Reading from Files

### Reading the Entire File

```python
# Read the entire file as a string
with open("file.txt", "r") as file:
    content = file.read()
    print(content)

# Read the entire file as a list of lines
with open("file.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())  # strip() removes the newline character

# Read the entire file as a list of lines (alternative)
with open("file.txt", "r") as file:
    lines = [line.strip() for line in file]
    print(lines)
```

### Reading Line by Line

```python
# Read line by line (memory-efficient for large files)
with open("file.txt", "r") as file:
    for line in file:
        print(line.strip())

# Read a single line
with open("file.txt", "r") as file:
    first_line = file.readline().strip()
    second_line = file.readline().strip()
    print(first_line)
    print(second_line)
```

### Reading a Specific Number of Characters

```python
with open("file.txt", "r") as file:
    # Read the first 10 characters
    chunk = file.read(10)
    print(chunk)
    
    # Read the next 10 characters
    chunk = file.read(10)
    print(chunk)
```

### Reading Binary Files

```python
# Read a binary file
with open("file.bin", "rb") as file:
    binary_data = file.read()
    print(binary_data)  # bytes object
    
    # Read a specific number of bytes
    file.seek(0)  # Go back to the beginning of the file
    first_10_bytes = file.read(10)
    print(first_10_bytes)
```

## Writing to Files

### Writing Text

```python
# Write a string to a file
with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a new line.\n")

# Write multiple lines at once
with open("output.txt", "w") as file:
    file.writelines(["Line 1\n", "Line 2\n", "Line 3\n"])

# Write a list of strings with newlines
lines = ["Line 1", "Line 2", "Line 3"]
with open("output.txt", "w") as file:
    for line in lines:
        file.write(line + "\n")
```

### Appending to Files

```python
# Append to a file
with open("output.txt", "a") as file:
    file.write("This line is appended.\n")
    file.write("This is another appended line.\n")
```

### Writing Binary Data

```python
# Write binary data
with open("output.bin", "wb") as file:
    file.write(b"\x00\x01\x02\x03\x04")
    
    # Write an integer as bytes
    file.write((42).to_bytes(4, byteorder="little"))
    
    # Write a string as bytes
    file.write("Hello".encode("utf-8"))
```

## File Positions

### Getting and Setting the File Position

```python
with open("file.txt", "r") as file:
    # Get the current position
    position = file.tell()
    print(f"Current position: {position}")  # 0
    
    # Read some data
    data = file.read(10)
    print(data)
    
    # Get the new position
    position = file.tell()
    print(f"New position: {position}")  # 10
    
    # Set the position to the beginning of the file
    file.seek(0)
    print(f"Position after seek(0): {file.tell()}")  # 0
    
    # Set the position to the 5th byte
    file.seek(5)
    print(f"Position after seek(5): {file.tell()}")  # 5
    
    # Set the position relative to the current position
    file.seek(3, 1)  # Move 3 bytes forward from the current position
    print(f"Position after seek(3, 1): {file.tell()}")  # 8
    
    # Set the position relative to the end of the file
    file.seek(0, 2)  # Go to the end of the file
    print(f"Position after seek(0, 2): {file.tell()}")  # End of file
    
    # Set the position relative to the beginning of the file
    file.seek(0, 0)  # Same as file.seek(0)
    print(f"Position after seek(0, 0): {file.tell()}")  # 0
```

## File and Directory Operations

### Checking if a File or Directory Exists

```python
import os
from pathlib import Path

# Using os.path
if os.path.exists("file.txt"):
    print("File exists")
else:
    print("File does not exist")

if os.path.isfile("file.txt"):
    print("It's a file")

if os.path.isdir("directory"):
    print("It's a directory")

# Using pathlib
path = Path("file.txt")
if path.exists():
    print("File exists")
else:
    print("File does not exist")

if path.is_file():
    print("It's a file")

if path.is_dir():
    print("It's a directory")
```

### Creating Directories

```python
import os
from pathlib import Path

# Using os
os.mkdir("new_directory")  # Create a single directory

# Create nested directories
os.makedirs("parent/child/grandchild", exist_ok=True)  # exist_ok=True prevents error if directory exists

# Using pathlib
Path("new_directory").mkdir(exist_ok=True)  # Create a single directory

# Create nested directories
Path("parent/child/grandchild").mkdir(parents=True, exist_ok=True)
```

### Listing Directory Contents

```python
import os
from pathlib import Path

# Using os
entries = os.listdir("directory")  # List all files and directories
print(entries)

# Using os.scandir (Python 3.5+)
with os.scandir("directory") as entries:
    for entry in entries:
        print(entry.name)
        print(f"Is file: {entry.is_file()}")
        print(f"Is directory: {entry.is_dir()}")

# Using pathlib
directory = Path("directory")
for entry in directory.iterdir():
    print(entry.name)
    print(f"Is file: {entry.is_file()}")
    print(f"Is directory: {entry.is_dir()}")
```

### Finding Files

```python
import os
import glob
from pathlib import Path

# Using glob
python_files = glob.glob("**/*.py", recursive=True)  # Find all .py files recursively
print(python_files)

# Using os.walk
python_files = []
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".py"):
            python_files.append(os.path.join(root, file))
print(python_files)

# Using pathlib
directory = Path(".")
python_files = list(directory.rglob("*.py"))  # Find all .py files recursively
print(python_files)
```

### Renaming and Moving Files

```python
import os
import shutil
from pathlib import Path

# Using os
os.rename("old_name.txt", "new_name.txt")  # Rename a file

# Using shutil
shutil.move("source.txt", "destination.txt")  # Move or rename a file
shutil.move("source.txt", "directory/")  # Move a file to a directory

# Using pathlib
path = Path("old_name.txt")
path.rename("new_name.txt")  # Rename a file

# Move a file to a directory
path = Path("source.txt")
path.rename(Path("directory") / path.name)
```

### Copying Files

```python
import shutil
from pathlib import Path

# Using shutil
shutil.copy("source.txt", "destination.txt")  # Copy a file
shutil.copy2("source.txt", "destination.txt")  # Copy a file with metadata

# Copy a directory and its contents
shutil.copytree("source_directory", "destination_directory")

# Using pathlib with shutil
source = Path("source.txt")
destination = Path("destination.txt")
shutil.copy2(source, destination)
```

### Deleting Files and Directories

```python
import os
import shutil
from pathlib import Path

# Using os
os.remove("file.txt")  # Delete a file
os.rmdir("empty_directory")  # Delete an empty directory

# Using shutil
shutil.rmtree("directory")  # Delete a directory and its contents

# Using pathlib
path = Path("file.txt")
path.unlink()  # Delete a file

directory = Path("empty_directory")
directory.rmdir()  # Delete an empty directory
```

### Getting File Information

```python
import os
import time
from pathlib import Path

# Using os
stat_info = os.stat("file.txt")
print(f"Size: {stat_info.st_size} bytes")
print(f"Mode: {stat_info.st_mode}")
print(f"Created: {time.ctime(stat_info.st_ctime)}")
print(f"Last modified: {time.ctime(stat_info.st_mtime)}")
print(f"Last accessed: {time.ctime(stat_info.st_atime)}")

# Using pathlib
path = Path("file.txt")
stat_info = path.stat()
print(f"Size: {stat_info.st_size} bytes")
print(f"Mode: {stat_info.st_mode}")
print(f"Created: {time.ctime(stat_info.st_ctime)}")
print(f"Last modified: {time.ctime(stat_info.st_mtime)}")
print(f"Last accessed: {time.ctime(stat_info.st_atime)}")
```

## Working with Different File Formats

### CSV Files

CSV (Comma-Separated Values) files are a common format for storing tabular data.

```python
import csv

# Reading a CSV file
with open("data.csv", "r", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # Each row is a list of strings

# Reading a CSV file with headers
with open("data.csv", "r", newline="") as file:
    reader = csv.DictReader(file)  # Assumes the first row contains headers
    for row in reader:
        print(row)  # Each row is a dictionary with column headers as keys

# Writing a CSV file
data = [
    ["Name", "Age", "City"],
    ["John", 30, "New York"],
    ["Jane", 25, "Boston"],
    ["Bob", 35, "Chicago"]
]

with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)  # Write multiple rows at once

# Writing a CSV file with headers
headers = ["Name", "Age", "City"]
rows = [
    {"Name": "John", "Age": 30, "City": "New York"},
    {"Name": "Jane", "Age": 25, "City": "Boston"},
    {"Name": "Bob", "Age": 35, "City": "Chicago"}
]

with open("output.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()  # Write the header row
    writer.writerows(rows)  # Write multiple rows at once
```

### JSON Files

JSON (JavaScript Object Notation) is a lightweight data interchange format.

```python
import json

# Reading a JSON file
with open("data.json", "r") as file:
    data = json.load(file)
    print(data)  # Python object (dict, list, etc.)

# Writing a JSON file
data = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "languages": ["Python", "JavaScript", "C++"],
    "is_employee": True,
    "salary": None
}

with open("output.json", "w") as file:
    json.dump(data, file, indent=4)  # indent for pretty-printing

# Converting Python objects to JSON strings
json_string = json.dumps(data, indent=4)
print(json_string)

# Converting JSON strings to Python objects
python_object = json.loads(json_string)
print(python_object)
```

### INI Files

INI files are a simple way to store configuration settings.

```python
import configparser

# Reading an INI file
config = configparser.ConfigParser()
config.read("config.ini")

# Accessing sections and values
for section in config.sections():
    print(f"[{section}]")
    for key, value in config[section].items():
        print(f"{key} = {value}")

# Accessing specific values
database_host = config["database"]["host"]
database_port = config["database"].getint("port")  # Convert to integer
debug_mode = config["settings"].getboolean("debug")  # Convert to boolean

# Writing an INI file
config = configparser.ConfigParser()

config["database"] = {
    "host": "localhost",
    "port": "5432",
    "user": "postgres",
    "password": "secret"
}

config["settings"] = {
    "debug": "true",
    "log_level": "info"
}

with open("output.ini", "w") as file:
    config.write(file)
```

### YAML Files

YAML (YAML Ain't Markup Language) is a human-readable data serialization format.

```python
# Requires the PyYAML package: pip install pyyaml
import yaml

# Reading a YAML file
with open("data.yaml", "r") as file:
    data = yaml.safe_load(file)
    print(data)  # Python object (dict, list, etc.)

# Writing a YAML file
data = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "languages": ["Python", "JavaScript", "C++"],
    "is_employee": True,
    "salary": None
}

with open("output.yaml", "w") as file:
    yaml.dump(data, file, default_flow_style=False)  # default_flow_style=False for block style
```

### XML Files

XML (eXtensible Markup Language) is a markup language for storing and transporting data.

```python
import xml.etree.ElementTree as ET

# Reading an XML file
tree = ET.parse("data.xml")
root = tree.getroot()

# Accessing elements and attributes
for child in root:
    print(f"Tag: {child.tag}, Attributes: {child.attrib}")
    for subchild in child:
        print(f"  Subtag: {subchild.tag}, Text: {subchild.text}")

# Finding elements
for element in root.findall("./person/name"):
    print(element.text)

# Writing an XML file
root = ET.Element("data")

person1 = ET.SubElement(root, "person", {"id": "1"})
ET.SubElement(person1, "name").text = "John"
ET.SubElement(person1, "age").text = "30"
ET.SubElement(person1, "city").text = "New York"

person2 = ET.SubElement(root, "person", {"id": "2"})
ET.SubElement(person2, "name").text = "Jane"
ET.SubElement(person2, "age").text = "25"
ET.SubElement(person2, "city").text = "Boston"

tree = ET.ElementTree(root)
tree.write("output.xml", encoding="utf-8", xml_declaration=True)
```

### Excel Files

Excel files are a common format for storing tabular data with multiple sheets.

```python
# Requires the openpyxl package: pip install openpyxl
import openpyxl

# Reading an Excel file
workbook = openpyxl.load_workbook("data.xlsx")

# Get sheet names
print(workbook.sheetnames)

# Access a sheet
sheet = workbook["Sheet1"]

# Iterate through rows and columns
for row in sheet.iter_rows(values_only=True):
    print(row)

# Access specific cells
cell_value = sheet.cell(row=1, column=1).value
print(cell_value)

# Writing an Excel file
workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = "Data"

# Write data to cells
sheet["A1"] = "Name"
sheet["B1"] = "Age"
sheet["C1"] = "City"

data = [
    ["John", 30, "New York"],
    ["Jane", 25, "Boston"],
    ["Bob", 35, "Chicago"]
]

for row_idx, row_data in enumerate(data, start=2):
    for col_idx, cell_value in enumerate(row_data, start=1):
        sheet.cell(row=row_idx, column=col_idx, value=cell_value)

# Create a new sheet
new_sheet = workbook.create_sheet(title="Summary")
new_sheet["A1"] = "This is a summary sheet"

# Save the workbook
workbook.save("output.xlsx")
```

### Pickle Files

Pickle is a Python-specific binary serialization format for Python objects.

```python
import pickle

# Reading a pickle file
with open("data.pkl", "rb") as file:
    data = pickle.load(file)
    print(data)  # Python object

# Writing a pickle file
data = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "languages": ["Python", "JavaScript", "C++"],
    "is_employee": True,
    "salary": None
}

with open("output.pkl", "wb") as file:
    pickle.dump(data, file)

# Pickle multiple objects
with open("multiple.pkl", "wb") as file:
    pickle.dump(data, file)
    pickle.dump([1, 2, 3], file)
    pickle.dump("Hello", file)

# Load multiple objects in the same order
with open("multiple.pkl", "rb") as file:
    data1 = pickle.load(file)
    data2 = pickle.load(file)
    data3 = pickle.load(file)
    print(data1, data2, data3)
```

## Temporary Files and Directories

The `tempfile` module provides functions for creating temporary files and directories.

```python
import tempfile
import os

# Create a temporary file
with tempfile.NamedTemporaryFile(delete=False) as temp_file:
    temp_file.write(b"Hello, World!")
    temp_file_path = temp_file.name

print(f"Temporary file created at: {temp_file_path}")

# Read the temporary file
with open(temp_file_path, "rb") as file:
    content = file.read()
    print(content)  # b'Hello, World!'

# Delete the temporary file
os.unlink(temp_file_path)

# Create a temporary directory
temp_dir = tempfile.mkdtemp()
print(f"Temporary directory created at: {temp_dir}")

# Create a file in the temporary directory
temp_file_path = os.path.join(temp_dir, "temp.txt")
with open(temp_file_path, "w") as file:
    file.write("Hello, World!")

# Delete the temporary directory and its contents
shutil.rmtree(temp_dir)
```

## File Compression

Python provides modules for working with compressed files.

### ZIP Files

```python
import zipfile
import os

# Creating a ZIP file
with zipfile.ZipFile("archive.zip", "w") as zip_file:
    # Add files to the ZIP
    zip_file.write("file1.txt")
    zip_file.write("file2.txt")
    
    # Add a file with a different name in the ZIP
    zip_file.write("file3.txt", arcname="renamed.txt")
    
    # Add all files in a directory
    for root, dirs, files in os.walk("directory"):
        for file in files:
            zip_file.write(os.path.join(root, file))

# Reading a ZIP file
with zipfile.ZipFile("archive.zip", "r") as zip_file:
    # List all files in the ZIP
    print(zip_file.namelist())
    
    # Extract all files
    zip_file.extractall("extracted_files")
    
    # Extract a specific file
    zip_file.extract("file1.txt", "extracted_files")
    
    # Read a file without extracting
    with zip_file.open("file1.txt") as file:
        content = file.read()
        print(content)
```

### TAR Files

```python
import tarfile
import os

# Creating a TAR file
with tarfile.open("archive.tar", "w") as tar_file:
    # Add files to the TAR
    tar_file.add("file1.txt")
    tar_file.add("file2.txt")
    
    # Add a file with a different name in the TAR
    tar_file.add("file3.txt", arcname="renamed.txt")
    
    # Add all files in a directory
    tar_file.add("directory")

# Creating a compressed TAR file (TAR.GZ)
with tarfile.open("archive.tar.gz", "w:gz") as tar_file:
    tar_file.add("file1.txt")
    tar_file.add("directory")

# Reading a TAR file
with tarfile.open("archive.tar", "r") as tar_file:
    # List all files in the TAR
    print(tar_file.getnames())
    
    # Extract all files
    tar_file.extractall("extracted_files")
    
    # Extract a specific file
    tar_file.extract("file1.txt", "extracted_files")
    
    # Read a file without extracting
    file = tar_file.extractfile("file1.txt")
    if file:
        content = file.read()
        print(content)
```

### GZIP Files

```python
import gzip

# Compressing a file
with open("file.txt", "rb") as f_in:
    with gzip.open("file.txt.gz", "wb") as f_out:
        f_out.write(f_in.read())

# Decompressing a file
with gzip.open("file.txt.gz", "rb") as f_in:
    with open("file_decompressed.txt", "wb") as f_out:
        f_out.write(f_in.read())

# Reading and writing compressed text files
with gzip.open("file.txt.gz", "wt", encoding="utf-8") as f:
    f.write("Hello, World!\n")
    f.write("This is a compressed text file.\n")

with gzip.open("file.txt.gz", "rt", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
```

## Memory-Mapped Files

Memory-mapped files allow you to access file content as if it were in memory, which can be more efficient for large files.

```python
import mmap
import os

# Create a file with some content
with open("mmap_file.txt", "wb") as f:
    f.write(b"Hello, World!\nThis is a memory-mapped file.\n")

# Memory-map the file for reading
with open("mmap_file.txt", "rb") as f:
    # Get the file size
    file_size = os.path.getsize("mmap_file.txt")
    
    # Create a memory-mapped file
    with mmap.mmap(f.fileno(), file_size, access=mmap.ACCESS_READ) as mm:
        # Read the entire content
        print(mm.read().decode("utf-8"))
        
        # Seek to the beginning
        mm.seek(0)
        
        # Read a line
        print(mm.readline().decode("utf-8").strip())
        
        # Find a substring
        index = mm.find(b"memory")
        if index != -1:
            mm.seek(index)
            print(mm.read(20).decode("utf-8"))

# Memory-map the file for writing
with open("mmap_file.txt", "r+b") as f:
    file_size = os.path.getsize("mmap_file.txt")
    with mmap.mmap(f.fileno(), file_size, access=mmap.ACCESS_WRITE) as mm:
        # Modify the content
        mm.seek(0)
        mm.write(b"Modified")
```

## File Locking

File locking is used to prevent multiple processes from modifying a file simultaneously.

```python
import fcntl
import time
import os

# Create a file
with open("lock_file.txt", "w") as f:
    f.write("Initial content\n")

# Exclusive lock (for writing)
def write_with_lock():
    with open("lock_file.txt", "a") as f:
        try:
            # Acquire an exclusive lock (blocking)
            fcntl.flock(f, fcntl.LOCK_EX)
            print("Acquired exclusive lock")
            
            # Simulate some work
            time.sleep(2)
            
            # Write to the file
            f.write(f"Process {os.getpid()} wrote this at {time.ctime()}\n")
            
        finally:
            # Release the lock
            fcntl.flock(f, fcntl.LOCK_UN)
            print("Released exclusive lock")

# Shared lock (for reading)
def read_with_lock():
    with open("lock_file.txt", "r") as f:
        try:
            # Acquire a shared lock (blocking)
            fcntl.flock(f, fcntl.LOCK_SH)
            print("Acquired shared lock")
            
            # Simulate some work
            time.sleep(1)
            
            # Read from the file
            content = f.read()
            print(f"Read content: {content}")
            
        finally:
            # Release the lock
            fcntl.flock(f, fcntl.LOCK_UN)
            print("Released shared lock")

# Non-blocking lock
def try_lock():
    with open("lock_file.txt", "a") as f:
        try:
            # Try to acquire an exclusive lock (non-blocking)
            result = fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
            print("Acquired exclusive lock")
            
            # Write to the file
            f.write(f"Process {os.getpid()} wrote this at {time.ctime()}\n")
            
        except IOError:
            print("Could not acquire lock")
            
        finally:
            # Release the lock
            fcntl.flock(f, fcntl.LOCK_UN)
            print("Released exclusive lock")
```

## File Watching

File watching allows you to monitor files or directories for changes.

```python
# Requires the watchdog package: pip install watchdog
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            print(f"File created: {event.src_path}")
    
    def on_modified(self, event):
        if not event.is_directory:
            print(f"File modified: {event.src_path}")
    
    def on_deleted(self, event):
        if not event.is_directory:
            print(f"File deleted: {event.src_path}")
    
    def on_moved(self, event):
        if not event.is_directory:
            print(f"File moved from {event.src_path} to {event.dest_path}")

# Set up the observer
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, path=".", recursive=True)
observer.start()

try:
    print("Monitoring directory for changes...")
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()
```

## Best Practices

### Use Context Managers

Always use the `with` statement when working with files to ensure they are properly closed.

```python
# Good practice
with open("file.txt", "r") as file:
    content = file.read()

# Avoid this
file = open("file.txt", "r")
content = file.read()
file.close()  # Might not be executed if an exception occurs
```

### Specify Encoding

Always specify the encoding when working with text files to avoid encoding issues.

```python
# Good practice
with open("file.txt", "r", encoding="utf-8") as file:
    content = file.read()

# Avoid this
with open("file.txt", "r") as file:  # Uses system default encoding
    content = file.read()
```

### Use Binary Mode for Binary Files

Use binary mode (`"rb"`, `"wb"`) when working with binary files to avoid encoding issues.

```python
# Good practice for binary files
with open("image.jpg", "rb") as file:
    content = file.read()

# Avoid this for binary files
with open("image.jpg", "r") as file:  # May cause encoding errors
    content = file.read()
```

### Handle Exceptions

Handle exceptions when working with files to gracefully handle errors.

```python
try:
    with open("file.txt", "r", encoding="utf-8") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
except Exception as e:
    print(f"An error occurred: {e}")
```

### Use `pathlib` for Path Manipulation

Use the `pathlib` module for path manipulation instead of `os.path` for more readable and maintainable code.

```python
# Good practice
from pathlib import Path

path = Path("directory") / "subdirectory" / "file.txt"
if path.exists():
    with path.open("r", encoding="utf-8") as file:
        content = file.read()

# Avoid this
import os

path = os.path.join("directory", "subdirectory", "file.txt")
if os.path.exists(path):
    with open(path, "r", encoding="utf-8") as file:
        content = file.read()
```

### Use Appropriate File Formats

Choose the appropriate file format based on your data and requirements.

- **Text files**: Simple data, logs, configuration files
- **CSV**: Tabular data, spreadsheets
- **JSON**: Structured data, configuration files, API responses
- **YAML**: Configuration files, data serialization
- **XML**: Structured data, document markup
- **Excel**: Complex tabular data with multiple sheets
- **Pickle**: Python-specific data serialization
- **SQLite**: Relational data, databases

### Avoid Hardcoding Paths

Avoid hardcoding paths to make your code more portable.

```python
# Good practice
import os
from pathlib import Path

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.join(script_dir, "data", "file.txt")

# Or using pathlib
script_dir = Path(__file__).parent
data_file = script_dir / "data" / "file.txt"
```

### Use Buffering for Large Files

Use buffering when working with large files to improve performance.

```python
# Process a large file line by line
with open("large_file.txt", "r", encoding="utf-8", buffering=1024*1024) as file:
    for line in file:
        process_line(line)

# Or use a specific buffer size
with open("large_file.txt", "r", encoding="utf-8", buffering=1024*1024) as file:
    while True:
        chunk = file.read(1024*1024)  # Read 1 MB at a time
        if not chunk:
            break
        process_chunk(chunk)
```

## Common Pitfalls

### Not Closing Files

Not closing files can lead to resource leaks and data corruption.

```python
# Bad practice
file = open("file.txt", "r")
content = file.read()
# File is not closed

# Good practice
with open("file.txt", "r") as file:
    content = file.read()
# File is automatically closed
```

### Ignoring Encoding

Ignoring encoding can lead to unexpected behavior and errors.

```python
# Bad practice
with open("file.txt", "r") as file:  # Uses system default encoding
    content = file.read()

# Good practice
with open("file.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

### Using the Wrong Mode

Using the wrong mode can lead to errors or unexpected behavior.

```python
# Bad practice
with open("binary_file.bin", "r") as file:  # Should be "rb"
    content = file.read()

# Good practice
with open("binary_file.bin", "rb") as file:
    content = file.read()
```

### Not Handling Exceptions

Not handling exceptions can lead to program crashes.

```python
# Bad practice
with open("file.txt", "r") as file:  # Will crash if file doesn't exist
    content = file.read()

# Good practice
try:
    with open("file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found")
```

### Using Relative Paths Incorrectly

Relative paths are relative to the current working directory, not the script directory.

```python
# Bad practice (assumes current working directory)
with open("data/file.txt", "r") as file:
    content = file.read()

# Good practice
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.join(script_dir, "data", "file.txt")

with open(data_file, "r") as file:
    content = file.read()
```

### Not Checking if a File Exists

Not checking if a file exists before opening it can lead to errors.

```python
# Bad practice
with open("file.txt", "r") as file:  # Will raise FileNotFoundError if file doesn't exist
    content = file.read()

# Good practice
import os

if os.path.exists("file.txt"):
    with open("file.txt", "r") as file:
        content = file.read()
else:
    print("File not found")
```

### Using `os.path.join()` with Absolute Paths

Using `os.path.join()` with absolute paths can lead to unexpected results.

```python
# Bad practice
import os

# If second path is absolute, it will ignore the first path
path = os.path.join("directory", "/absolute/path/file.txt")
print(path)  # '/absolute/path/file.txt'

# Good practice
path = os.path.join("directory", "relative/path/file.txt")
print(path)  # 'directory/relative/path/file.txt'
```

## Next Steps

Now that you understand file I/O in Python, you're ready to move on to [Error Handling](../12_Error_Handling/README.md).