# Object-Oriented Programming in Python

Object-Oriented Programming (OOP) is a programming paradigm that uses objects and classes to structure code. Python is a multi-paradigm language that fully supports OOP. This section covers the core concepts of OOP in Python.

## Classes and Objects

### Defining a Class

A class is a blueprint for creating objects. It defines a set of attributes and methods that the objects created from the class will have.

```python
class Person:
    """A class representing a person."""
    
    def __init__(self, name, age):
        """Initialize a new Person object.
        
        Args:
            name (str): The person's name
            age (int): The person's age
        """
        self.name = name
        self.age = age
    
    def greet(self):
        """Return a greeting message."""
        return f"Hello, my name is {self.name} and I am {self.age} years old."
```

### Creating Objects

An object is an instance of a class. You can create multiple objects from the same class.

```python
# Create Person objects
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Access attributes
print(person1.name)  # Output: Alice
print(person2.age)   # Output: 25

# Call methods
print(person1.greet())  # Output: Hello, my name is Alice and I am 30 years old.
print(person2.greet())  # Output: Hello, my name is Bob and I am 25 years old.
```

### The `__init__` Method

The `__init__` method is a special method (constructor) that is called when an object is created. It initializes the object's attributes.

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = width * height  # Calculated attribute
```

### Instance Variables vs. Class Variables

Instance variables are specific to each object, while class variables are shared among all instances of a class.

```python
class Dog:
    # Class variable
    species = "Canis familiaris"
    
    def __init__(self, name, breed):
        # Instance variables
        self.name = name
        self.breed = breed

# Create Dog objects
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "German Shepherd")

# Access instance variables
print(dog1.name)   # Output: Buddy
print(dog2.breed)  # Output: German Shepherd

# Access class variable
print(dog1.species)  # Output: Canis familiaris
print(dog2.species)  # Output: Canis familiaris
print(Dog.species)   # Output: Canis familiaris

# Modify class variable
Dog.species = "Canis lupus familiaris"
print(dog1.species)  # Output: Canis lupus familiaris
print(dog2.species)  # Output: Canis lupus familiaris

# Create instance variable with same name as class variable
dog1.species = "Changed for dog1"
print(dog1.species)  # Output: Changed for dog1
print(dog2.species)  # Output: Canis lupus familiaris (unchanged)
```

### Instance Methods, Class Methods, and Static Methods

Python supports three types of methods in a class:

1. **Instance Methods**: Regular methods that operate on an instance of the class. They take `self` as the first parameter.
2. **Class Methods**: Methods that operate on the class itself. They take `cls` as the first parameter and are decorated with `@classmethod`.
3. **Static Methods**: Methods that don't operate on the instance or the class. They don't take `self` or `cls` as parameters and are decorated with `@staticmethod`.

```python
class MyClass:
    class_var = "I am a class variable"
    
    def __init__(self, instance_var):
        self.instance_var = instance_var
    
    def instance_method(self):
        """Regular instance method that can access self."""
        return f"Instance method called with {self.instance_var}"
    
    @classmethod
    def class_method(cls):
        """Class method that can access cls but not self."""
        return f"Class method called with {cls.class_var}"
    
    @staticmethod
    def static_method():
        """Static method that can't access self or cls."""
        return "Static method called"

# Create an object
obj = MyClass("instance value")

# Call instance method
print(obj.instance_method())  # Output: Instance method called with instance value

# Call class method
print(MyClass.class_method())  # Output: Class method called with I am a class variable
print(obj.class_method())      # Output: Class method called with I am a class variable

# Call static method
print(MyClass.static_method())  # Output: Static method called
print(obj.static_method())      # Output: Static method called
```

### Class Methods as Alternative Constructors

Class methods are often used as alternative constructors.

```python
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    @classmethod
    def from_string(cls, date_string):
        """Create a Date object from a string in the format 'YYYY-MM-DD'."""
        year, month, day = map(int, date_string.split('-'))
        return cls(year, month, day)
    
    @classmethod
    def today(cls):
        """Create a Date object with today's date."""
        import datetime
        today = datetime.date.today()
        return cls(today.year, today.month, today.day)

# Create Date objects using different constructors
date1 = Date(2023, 1, 15)             # Using __init__
date2 = Date.from_string("2023-02-20")  # Using from_string
date3 = Date.today()                   # Using today

print(f"{date1.year}-{date1.month}-{date1.day}")  # Output: 2023-1-15
print(f"{date2.year}-{date2.month}-{date2.day}")  # Output: 2023-2-20
print(f"{date3.year}-{date3.month}-{date3.day}")  # Output: Current date
```

## Inheritance

Inheritance allows a class to inherit attributes and methods from another class.

### Basic Inheritance

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Create objects
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Call methods
print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!
```

### The `super()` Function

The `super()` function is used to call methods from the parent class.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Call the parent class's __init__ method
        self.student_id = student_id
    
    def introduce(self):
        # Call the parent class's introduce method and extend it
        return f"{super().introduce()} My student ID is {self.student_id}."

# Create a Student object
student = Student("Alice", 20, "S12345")

# Call method
print(student.introduce())  # Output: My name is Alice and I am 20 years old. My student ID is S12345.
```

### Multiple Inheritance

Python supports multiple inheritance, allowing a class to inherit from multiple parent classes.

```python
class A:
    def method_a(self):
        return "Method A"

class B:
    def method_b(self):
        return "Method B"

class C(A, B):
    def method_c(self):
        return "Method C"

# Create a C object
c = C()

# Call methods
print(c.method_a())  # Output: Method A
print(c.method_b())  # Output: Method B
print(c.method_c())  # Output: Method C
```

### Method Resolution Order (MRO)

When a class inherits from multiple classes, Python uses the Method Resolution Order (MRO) to determine which method to call.

```python
class A:
    def method(self):
        return "Method from A"

class B(A):
    def method(self):
        return "Method from B"

class C(A):
    def method(self):
        return "Method from C"

class D(B, C):
    pass

# Create a D object
d = D()

# Call method
print(d.method())  # Output: Method from B

# Check the MRO
print(D.__mro__)  # Output: (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
```

Python uses the C3 linearization algorithm to determine the MRO. You can view the MRO using the `__mro__` attribute or the `mro()` method.

### Abstract Base Classes

Abstract Base Classes (ABCs) are classes that cannot be instantiated and are designed to be subclassed. They can define abstract methods that must be implemented by subclasses.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        import math
        return 2 * math.pi * self.radius

# This would raise TypeError: Can't instantiate abstract class Shape with abstract methods area, perimeter
# shape = Shape()

# Create objects
rectangle = Rectangle(5, 3)
circle = Circle(2)

# Call methods
print(f"Rectangle area: {rectangle.area()}")        # Output: Rectangle area: 15
print(f"Rectangle perimeter: {rectangle.perimeter()}")  # Output: Rectangle perimeter: 16
print(f"Circle area: {circle.area()}")              # Output: Circle area: 12.566370614359172
print(f"Circle perimeter: {circle.perimeter()}")    # Output: Circle perimeter: 12.566370614359172
```

## Encapsulation

Encapsulation is the bundling of data and methods that operate on the data within a single unit (class) and restricting access to some of the object's components.

### Private Attributes and Methods

In Python, there is no strict enforcement of private attributes or methods, but there is a convention to prefix names with an underscore (`_`) for protected members and double underscores (`__`) for private members.

```python
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number  # Public attribute
        self._balance = balance               # Protected attribute (convention)
        self.__transaction_log = []           # Private attribute (name mangling)
    
    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self._balance += amount
            self.__log_transaction("deposit", amount)
            return True
        return False
    
    def withdraw(self, amount):
        """Withdraw money from the account."""
        if 0 < amount <= self._balance:
            self._balance -= amount
            self.__log_transaction("withdraw", amount)
            return True
        return False
    
    def get_balance(self):
        """Get the current balance."""
        return self._balance
    
    def __log_transaction(self, transaction_type, amount):
        """Log a transaction (private method)."""
        self.__transaction_log.append((transaction_type, amount))
    
    def get_transaction_log(self):
        """Get a copy of the transaction log."""
        return self.__transaction_log.copy()

# Create a BankAccount object
account = BankAccount("123456", 1000)

# Access public attribute
print(account.account_number)  # Output: 123456

# Access protected attribute (possible, but not recommended)
print(account._balance)  # Output: 1000

# Access private attribute (name mangling)
try:
    print(account.__transaction_log)  # This will raise an AttributeError
except AttributeError as e:
    print(f"Error: {e}")  # Output: Error: 'BankAccount' object has no attribute '__transaction_log'

# Access private attribute using name mangling
print(account._BankAccount__transaction_log)  # Output: []

# Call methods
account.deposit(500)
account.withdraw(200)
print(account.get_balance())         # Output: 1300
print(account.get_transaction_log())  # Output: [('deposit', 500), ('withdraw', 200)]
```

### Properties

Properties provide a way to define getter, setter, and deleter methods for an attribute.

```python
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    @property
    def name(self):
        """Get the person's name."""
        return self._name
    
    @name.setter
    def name(self, value):
        """Set the person's name."""
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value
    
    @property
    def age(self):
        """Get the person's age."""
        return self._age
    
    @age.setter
    def age(self, value):
        """Set the person's age."""
        if not isinstance(value, int):
            raise TypeError("Age must be an integer")
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value
    
    @property
    def is_adult(self):
        """Check if the person is an adult."""
        return self._age >= 18

# Create a Person object
person = Person("Alice", 30)

# Access properties
print(person.name)      # Output: Alice
print(person.age)       # Output: 30
print(person.is_adult)  # Output: True

# Modify properties
person.name = "Bob"
person.age = 25
print(person.name)      # Output: Bob
print(person.age)       # Output: 25

# Try to set invalid values
try:
    person.name = ""  # This will raise a ValueError
except ValueError as e:
    print(f"Error: {e}")  # Output: Error: Name cannot be empty

try:
    person.age = -5  # This will raise a ValueError
except ValueError as e:
    print(f"Error: {e}")  # Output: Error: Age cannot be negative
```

### Property Decorators

You can also define properties using decorators.

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value
    
    @property
    def diameter(self):
        return 2 * self._radius
    
    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2
    
    @property
    def area(self):
        import math
        return math.pi * self._radius ** 2

# Create a Circle object
circle = Circle(5)

# Access properties
print(f"Radius: {circle.radius}")    # Output: Radius: 5
print(f"Diameter: {circle.diameter}")  # Output: Diameter: 10
print(f"Area: {circle.area}")        # Output: Area: 78.53981633974483

# Modify properties
circle.radius = 7
print(f"Radius: {circle.radius}")    # Output: Radius: 7
print(f"Diameter: {circle.diameter}")  # Output: Diameter: 14
print(f"Area: {circle.area}")        # Output: Area: 153.93804002589985

circle.diameter = 10
print(f"Radius: {circle.radius}")    # Output: Radius: 5.0
print(f"Diameter: {circle.diameter}")  # Output: Diameter: 10.0
print(f"Area: {circle.area}")        # Output: Area: 78.53981633974483
```

## Polymorphism

Polymorphism allows objects of different classes to be treated as objects of a common superclass. It enables the same interface to be used for different underlying forms.

### Duck Typing

Python uses duck typing, which means that the type or class of an object is less important than the methods it defines or the operations you can perform on it. "If it walks like a duck and quacks like a duck, then it's a duck."

```python
class Duck:
    def speak(self):
        return "Quack!"
    
    def swim(self):
        return "Duck swimming"

class Person:
    def speak(self):
        return "Hello!"
    
    def swim(self):
        return "Person swimming"

def make_speak(entity):
    """Make an entity speak."""
    return entity.speak()

def make_swim(entity):
    """Make an entity swim."""
    return entity.swim()

# Create objects
duck = Duck()
person = Person()

# Call functions with different objects
print(make_speak(duck))    # Output: Quack!
print(make_speak(person))  # Output: Hello!
print(make_swim(duck))     # Output: Duck swimming
print(make_swim(person))   # Output: Person swimming
```

### Method Overriding

Method overriding is the ability of a subclass to provide a specific implementation of a method that is already defined in its superclass.

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

class Cow(Animal):
    def speak(self):
        return f"{self.name} says Moo!"

# Create objects
animals = [
    Dog("Buddy"),
    Cat("Whiskers"),
    Cow("Bessie")
]

# Call methods polymorphically
for animal in animals:
    print(animal.speak())
# Output:
# Buddy says Woof!
# Whiskers says Meow!
# Bessie says Moo!
```

### Operator Overloading

Operator overloading allows you to define how operators behave for objects of your class.

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __add__(self, other):
        """Add two vectors."""
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """Subtract two vectors."""
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        """Multiply a vector by a scalar."""
        return Vector(self.x * scalar, self.y * scalar)
    
    def __eq__(self, other):
        """Check if two vectors are equal."""
        return self.x == other.x and self.y == other.y

# Create Vector objects
v1 = Vector(1, 2)
v2 = Vector(3, 4)

# Use operators
v3 = v1 + v2
print(v3)  # Output: Vector(4, 6)

v4 = v2 - v1
print(v4)  # Output: Vector(2, 2)

v5 = v1 * 3
print(v5)  # Output: Vector(3, 6)

print(v1 == Vector(1, 2))  # Output: True
print(v1 == v2)            # Output: False
```

## Special Methods

Python classes can define special methods (also called magic methods or dunder methods) that enable objects to respond to operators and built-in functions.

### Common Special Methods

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        """Return a string representation for end users."""
        return f"{self.name}, {self.age} years old"
    
    def __repr__(self):
        """Return a string representation for developers."""
        return f"Person('{self.name}', {self.age})"
    
    def __eq__(self, other):
        """Check if two Person objects are equal."""
        if not isinstance(other, Person):
            return False
        return self.name == other.name and self.age == other.age
    
    def __lt__(self, other):
        """Compare two Person objects based on age."""
        if not isinstance(other, Person):
            return NotImplemented
        return self.age < other.age
    
    def __len__(self):
        """Return the length of the person's name."""
        return len(self.name)
    
    def __bool__(self):
        """Return True if the person's age is positive."""
        return self.age > 0

# Create Person objects
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)
person3 = Person("Alice", 30)

# Use special methods
print(str(person1))    # Output: Alice, 30 years old
print(repr(person1))   # Output: Person('Alice', 30)
print(person1 == person2)  # Output: False
print(person1 == person3)  # Output: True
print(person1 < person2)   # Output: False
print(len(person1))        # Output: 5
print(bool(person1))       # Output: True

# Sort a list of Person objects
people = [Person("Alice", 30), Person("Bob", 25), Person("Charlie", 35)]
people.sort()
for person in people:
    print(person)  # Output: Bob, 25 years old\nAlice, 30 years old\nCharlie, 35 years old
```

### Container Special Methods

```python
class MyList:
    def __init__(self, items=None):
        self.items = items or []
    
    def __getitem__(self, index):
        """Get an item at the specified index."""
        return self.items[index]
    
    def __setitem__(self, index, value):
        """Set an item at the specified index."""
        self.items[index] = value
    
    def __delitem__(self, index):
        """Delete an item at the specified index."""
        del self.items[index]
    
    def __len__(self):
        """Return the number of items."""
        return len(self.items)
    
    def __contains__(self, item):
        """Check if an item is in the list."""
        return item in self.items
    
    def __iter__(self):
        """Return an iterator for the list."""
        return iter(self.items)

# Create a MyList object
my_list = MyList([1, 2, 3, 4, 5])

# Use container methods
print(my_list[0])      # Output: 1
my_list[0] = 10
print(my_list[0])      # Output: 10
del my_list[0]
print(my_list[0])      # Output: 2
print(len(my_list))    # Output: 4
print(3 in my_list)    # Output: True

# Iterate over the list
for item in my_list:
    print(item)  # Output: 2\n3\n4\n5
```

### Context Manager Special Methods

```python
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        """Enter the context manager."""
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit the context manager."""
        if self.file:
            self.file.close()
        # Return True to suppress exceptions, False to propagate them
        return False

# Use the context manager
with FileManager("example.txt", "w") as f:
    f.write("Hello, World!")

with FileManager("example.txt", "r") as f:
    content = f.read()
    print(content)  # Output: Hello, World!
```

## Composition vs. Inheritance

Composition and inheritance are two ways to reuse code in object-oriented programming.

### Inheritance

Inheritance is an "is-a" relationship. A subclass is a specialized version of its superclass.

```python
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def start(self):
        return f"The {self.year} {self.make} {self.model} is starting."

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors
    
    def drive(self):
        return f"The {self.year} {self.make} {self.model} with {self.num_doors} doors is driving."

# Create a Car object
car = Car("Toyota", "Camry", 2023, 4)

# Call methods
print(car.start())  # Output: The 2023 Toyota Camry is starting.
print(car.drive())  # Output: The 2023 Toyota Camry with 4 doors is driving.
```

### Composition

Composition is a "has-a" relationship. A class contains instances of other classes as attributes.

```python
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
    
    def start(self):
        return f"Engine with {self.horsepower} HP is starting."

class Transmission:
    def __init__(self, type_):
        self.type = type_
    
    def shift(self):
        return f"{self.type} transmission is shifting."

class Car:
    def __init__(self, make, model, year, engine_hp, transmission_type):
        self.make = make
        self.model = model
        self.year = year
        self.engine = Engine(engine_hp)
        self.transmission = Transmission(transmission_type)
    
    def start(self):
        engine_start = self.engine.start()
        return f"The {self.year} {self.make} {self.model} is starting. {engine_start}"
    
    def drive(self):
        transmission_shift = self.transmission.shift()
        return f"The {self.year} {self.make} {self.model} is driving. {transmission_shift}"

# Create a Car object
car = Car("Toyota", "Camry", 2023, 200, "Automatic")

# Call methods
print(car.start())  # Output: The 2023 Toyota Camry is starting. Engine with 200 HP is starting.
print(car.drive())  # Output: The 2023 Toyota Camry is driving. Automatic transmission is shifting.
```

### When to Use Each

- **Use Inheritance When**:
  - There is a clear "is-a" relationship between classes.
  - The subclass is a specialized version of the superclass.
  - The subclass reuses most of the superclass's behavior.

- **Use Composition When**:
  - There is a clear "has-a" relationship between classes.
  - You want to reuse code without creating a tight coupling between classes.
  - You want to change behavior at runtime by swapping components.

## Mixins

Mixins are classes that provide methods to other classes without being their parent class. They are a way to share behavior without using inheritance.

```python
class LoggerMixin:
    def log(self, message):
        print(f"[LOG] {message}")

class TimerMixin:
    def __init__(self):
        self.start_time = None
    
    def start_timer(self):
        import time
        self.start_time = time.time()
    
    def stop_timer(self):
        import time
        if self.start_time is None:
            return "Timer not started"
        elapsed_time = time.time() - self.start_time
        self.start_time = None
        return f"Elapsed time: {elapsed_time:.2f} seconds"

class DataProcessor(LoggerMixin, TimerMixin):
    def __init__(self):
        super().__init__()
    
    def process_data(self, data):
        self.log("Starting data processing")
        self.start_timer()
        
        # Simulate data processing
        import time
        time.sleep(2)
        result = [x * 2 for x in data]
        
        elapsed_time = self.stop_timer()
        self.log(f"Data processing completed. {elapsed_time}")
        return result

# Create a DataProcessor object
processor = DataProcessor()

# Process data
result = processor.process_data([1, 2, 3, 4, 5])
print(result)  # Output: [2, 4, 6, 8, 10]
```

## Metaclasses

Metaclasses are classes that define how other classes are created. They are the "class of a class".

```python
class Meta(type):
    def __new__(mcs, name, bases, attrs):
        # Add a new attribute to the class
        attrs['added_by_meta'] = 'This attribute was added by the metaclass'
        
        # Modify existing methods
        if 'greet' in attrs:
            original_greet = attrs['greet']
            def new_greet(self):
                return f"Modified: {original_greet(self)}"
            attrs['greet'] = new_greet
        
        # Create the class
        return super().__new__(mcs, name, bases, attrs)

class Person(metaclass=Meta):
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return f"Hello, my name is {self.name}"

# Create a Person object
person = Person("Alice")

# Access the attribute added by the metaclass
print(person.added_by_meta)  # Output: This attribute was added by the metaclass

# Call the modified method
print(person.greet())  # Output: Modified: Hello, my name is Alice
```

## Design Patterns

Design patterns are reusable solutions to common problems in software design. Here are a few examples implemented in Python:

### Singleton Pattern

The Singleton pattern ensures that a class has only one instance and provides a global point of access to it.

```python
class Singleton:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# Create Singleton objects
s1 = Singleton()
s2 = Singleton()

print(s1 is s2)  # Output: True
```

A more modern approach using a metaclass:

```python
class SingletonMeta(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    def __init__(self, value=None):
        self.value = value

# Create Singleton objects
s1 = Singleton(1)
s2 = Singleton(2)

print(s1 is s2)      # Output: True
print(s1.value)      # Output: 1 (not 2, because __init__ is only called once)
print(s2.value)      # Output: 1
```

### Factory Pattern

The Factory pattern provides an interface for creating objects without specifying their concrete classes.

```python
from abc import ABC, abstractmethod

# Product interface
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# Concrete products
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Cow(Animal):
    def speak(self):
        return "Moo!"

# Factory
class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type.lower() == "dog":
            return Dog()
        elif animal_type.lower() == "cat":
            return Cat()
        elif animal_type.lower() == "cow":
            return Cow()
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")

# Client code
factory = AnimalFactory()

animals = [
    factory.create_animal("dog"),
    factory.create_animal("cat"),
    factory.create_animal("cow")
]

for animal in animals:
    print(animal.speak())
# Output:
# Woof!
# Meow!
# Moo!
```

### Observer Pattern

The Observer pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.

```python
class Subject:
    def __init__(self):
        self._observers = []
    
    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)
    
    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass
    
    def notify(self, *args, **kwargs):
        for observer in self._observers:
            observer.update(self, *args, **kwargs)

class Observer:
    def update(self, subject, *args, **kwargs):
        pass

# Concrete subject
class WeatherStation(Subject):
    def __init__(self):
        super().__init__()
        self._temperature = 0
    
    @property
    def temperature(self):
        return self._temperature
    
    @temperature.setter
    def temperature(self, value):
        self._temperature = value
        self.notify()

# Concrete observers
class TemperatureDisplay(Observer):
    def update(self, subject, *args, **kwargs):
        print(f"Temperature Display: {subject.temperature}°C")

class Fan(Observer):
    def update(self, subject, *args, **kwargs):
        if subject.temperature > 25:
            print("Fan: Turning on")
        else:
            print("Fan: Turning off")

class Heater(Observer):
    def update(self, subject, *args, **kwargs):
        if subject.temperature < 15:
            print("Heater: Turning on")
        else:
            print("Heater: Turning off")

# Client code
weather_station = WeatherStation()

temp_display = TemperatureDisplay()
fan = Fan()
heater = Heater()

weather_station.attach(temp_display)
weather_station.attach(fan)
weather_station.attach(heater)

weather_station.temperature = 20
# Output:
# Temperature Display: 20°C
# Fan: Turning off
# Heater: Turning off

weather_station.temperature = 30
# Output:
# Temperature Display: 30°C
# Fan: Turning on
# Heater: Turning off

weather_station.temperature = 10
# Output:
# Temperature Display: 10°C
# Fan: Turning off
# Heater: Turning on
```

## Best Practices

### Class Design

- **Single Responsibility Principle**: A class should have only one reason to change.
- **Open/Closed Principle**: Classes should be open for extension but closed for modification.
- **Liskov Substitution Principle**: Subtypes must be substitutable for their base types.
- **Interface Segregation Principle**: Clients should not be forced to depend on methods they do not use.
- **Dependency Inversion Principle**: High-level modules should not depend on low-level modules. Both should depend on abstractions.

### Naming Conventions

- **Class Names**: Use CamelCase (e.g., `MyClass`).
- **Method and Attribute Names**: Use snake_case (e.g., `my_method`, `my_attribute`).
- **Private Attributes and Methods**: Prefix with an underscore (e.g., `_private_attribute`).
- **Constants**: Use ALL_CAPS (e.g., `MAX_VALUE`).

### Documentation

- Document your classes and methods with docstrings.
- Include examples in your docstrings.
- Use type hints to indicate parameter and return types.

```python
class Rectangle:
    """A class representing a rectangle.
    
    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
    """
    
    def __init__(self, width: float, height: float) -> None:
        """Initialize a new Rectangle object.
        
        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        self.width = width
        self.height = height
    
    def area(self) -> float:
        """Calculate the area of the rectangle.
        
        Returns:
            float: The area of the rectangle.
        
        Examples:
            >>> rect = Rectangle(5, 3)
            >>> rect.area()
            15.0
        """
        return self.width * self.height
```

### Testing

- Write unit tests for your classes and methods.
- Test edge cases and error conditions.
- Use a testing framework like `unittest` or `pytest`.

```python
import unittest
from my_module import Rectangle

class TestRectangle(unittest.TestCase):
    def test_area(self):
        rect = Rectangle(5, 3)
        self.assertEqual(rect.area(), 15.0)
    
    def test_negative_dimensions(self):
        with self.assertRaises(ValueError):
            Rectangle(-5, 3)

if __name__ == "__main__":
    unittest.main()
```

## Common Pitfalls

### Mutable Default Arguments

Default arguments in Python are evaluated only once, when the function is defined. This can lead to unexpected behavior with mutable default arguments.

```python
# Bad practice
class Person:
    def __init__(self, name, friends=[]):
        self.name = name
        self.friends = friends
    
    def add_friend(self, friend):
        self.friends.append(friend)

# Create Person objects
person1 = Person("Alice")
person2 = Person("Bob")

person1.add_friend("Charlie")
print(person1.friends)  # Output: ['Charlie']
print(person2.friends)  # Output: ['Charlie'] (unexpected!)
```

```python
# Good practice
class Person:
    def __init__(self, name, friends=None):
        self.name = name
        self.friends = friends if friends is not None else []
    
    def add_friend(self, friend):
        self.friends.append(friend)

# Create Person objects
person1 = Person("Alice")
person2 = Person("Bob")

person1.add_friend("Charlie")
print(person1.friends)  # Output: ['Charlie']
print(person2.friends)  # Output: [] (as expected)
```

### Not Using `super()` Correctly

When overriding methods in a subclass, it's important to call the parent class's method using `super()`.

```python
# Bad practice
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        # Parent.__init__(self, name)  # Old-style, not recommended
        self.age = age

# Create a Child object
child = Child("Alice", 10)
print(child.age)    # Output: 10
try:
    print(child.name)  # This will raise an AttributeError
except AttributeError as e:
    print(f"Error: {e}")  # Output: Error: 'Child' object has no attribute 'name'
```

```python
# Good practice
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Call the parent class's __init__ method
        self.age = age

# Create a Child object
child = Child("Alice", 10)
print(child.name)  # Output: Alice
print(child.age)   # Output: 10
```

### Circular References

Circular references can lead to memory leaks if not handled properly.

```python
# Potential memory leak
class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)
        child.parent = self

# Create nodes
root = Node("Root")
child1 = Node("Child 1")
child2 = Node("Child 2")

# Create circular references
root.add_child(child1)
root.add_child(child2)

# Even if we delete the root, the circular references prevent garbage collection
del root
# child1 and child2 still have references to their parent, and vice versa
```

```python
# Using weak references to avoid memory leaks
import weakref

class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)
        child.parent = weakref.ref(self)  # Use a weak reference

# Create nodes
root = Node("Root")
child1 = Node("Child 1")
child2 = Node("Child 2")

# Create references
root.add_child(child1)
root.add_child(child2)

# Now when we delete the root, it can be garbage collected
del root
# The weak reference in child1.parent and child2.parent doesn't prevent garbage collection
```

### Not Using Properties

Directly accessing attributes can lead to inconsistent state.

```python
# Bad practice
class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.diameter = 2 * radius
        self.area = 3.14159 * radius ** 2

# Create a Circle object
circle = Circle(5)
print(f"Radius: {circle.radius}")    # Output: Radius: 5
print(f"Diameter: {circle.diameter}")  # Output: Diameter: 10
print(f"Area: {circle.area}")        # Output: Area: 78.53975

# Modify the radius
circle.radius = 7
print(f"Radius: {circle.radius}")    # Output: Radius: 7
print(f"Diameter: {circle.diameter}")  # Output: Diameter: 10 (inconsistent!)
print(f"Area: {circle.area}")        # Output: Area: 78.53975 (inconsistent!)
```

```python
# Good practice
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        self._radius = value
    
    @property
    def diameter(self):
        return 2 * self._radius
    
    @property
    def area(self):
        return 3.14159 * self._radius ** 2

# Create a Circle object
circle = Circle(5)
print(f"Radius: {circle.radius}")    # Output: Radius: 5
print(f"Diameter: {circle.diameter}")  # Output: Diameter: 10
print(f"Area: {circle.area}")        # Output: Area: 78.53975

# Modify the radius
circle.radius = 7
print(f"Radius: {circle.radius}")    # Output: Radius: 7
print(f"Diameter: {circle.diameter}")  # Output: Diameter: 14 (consistent)
print(f"Area: {circle.area}")        # Output: Area: 153.93781 (consistent)
```

## Next Steps

Now that you understand object-oriented programming in Python, you're ready to move on to [Functional Programming](../15_Functional_Programming/README.md).