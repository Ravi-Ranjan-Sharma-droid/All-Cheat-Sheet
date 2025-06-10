# Complete JavaScript Learning Guide
## From Beginner to Advanced

---

## Table of Contents
1. [Introduction to JavaScript](#introduction-to-javascript)
2. [Variables & Data Types](#variables--data-types)
3. [Operators](#operators)
4. [Control Flow](#control-flow)
5. [Functions](#functions)
6. [Arrays & Objects](#arrays--objects)
7. [DOM Manipulation](#dom-manipulation)
8. [Events](#events)
9. [ES6+ Features](#es6-features)
10. [Promises & Async/Await](#promises--asyncawait)
11. [Error Handling](#error-handling)
12. [Modules](#modules)
13. [Classes & OOP](#classes--oop)
14. [Functional Programming](#functional-programming)
15. [Browser APIs](#browser-apis)
16. [Fetch/AJAX](#fetchajax)
17. [Local Storage](#local-storage)
18. [Advanced Topics](#advanced-topics)
19. [Common Interview Questions](#common-interview-questions)

---

## Introduction to JavaScript

JavaScript is a high-level, interpreted programming language that runs in browsers and Node.js environments. It's the language of the web and enables interactive, dynamic websites.

### Key Characteristics
- **Dynamically typed**: Variables don't need explicit type declarations
- **Interpreted**: No compilation step required
- **Event-driven**: Responds to user interactions and system events
- **Prototype-based**: Objects can inherit directly from other objects

### Where JavaScript Runs
- **Frontend**: Browsers (Chrome V8, Firefox SpiderMonkey, Safari JavaScriptCore)
- **Backend**: Node.js, Deno, Bun
- **Mobile**: React Native, Ionic
- **Desktop**: Electron

### Pro Tips
- Use browser developer tools for debugging (F12)
- Enable strict mode with `'use strict';` for better error catching
- JavaScript is case-sensitive: `myVariable` ≠ `myvariable`

---

## Variables & Data Types

### Variable Declarations

```javascript
// var - function-scoped, hoisted, can be redeclared
var name = "John";

// let - block-scoped, hoisted but not initialized, cannot be redeclared
let age = 25;

// const - block-scoped, must be initialized, cannot be reassigned
const PI = 3.14159;
```

### Primitive Data Types

```javascript
// String
let firstName = "Alice";
let lastName = 'Smith';
let template = `Hello, ${firstName}!`; // Template literal

// Number (integers and floats)
let integer = 42;
let float = 3.14;
let scientific = 2.5e6; // 2,500,000

// Boolean
let isActive = true;
let isComplete = false;

// Undefined
let undefinedVar; // undefined
let explicitUndefined = undefined;

// Null
let emptyValue = null;

// Symbol (ES6)
let sym = Symbol('id');

// BigInt (ES2020)
let bigNumber = 123456789012345678901234567890n;
```

### Non-Primitive Data Types

```javascript
// Object
let person = {
  name: "John",
  age: 30,
  city: "New York"
};

// Array
let numbers = [1, 2, 3, 4, 5];
let mixed = [1, "hello", true, null];

// Function
function greet() {
  return "Hello!";
}
```

### Type Checking & Conversion

```javascript
// Type checking
console.log(typeof "hello"); // "string"
console.log(typeof 42); // "number"
console.log(typeof true); // "boolean"
console.log(typeof undefined); // "undefined"
console.log(typeof null); // "object" (JavaScript quirk!)
console.log(Array.isArray([])); // true

// Type conversion
let str = "123";
let num = Number(str); // 123
let bool = Boolean(0); // false

// Implicit conversion (coercion)
console.log(5 + "3"); // "53" (number to string)
console.log("5" - 3); // 2 (string to number)
console.log(!""); // true (empty string is falsy)
```

### Gotchas
- `null` has type "object" (historical bug in JavaScript)
- `NaN` (Not a Number) is of type "number"
- Empty strings, 0, null, undefined, NaN are falsy values
- Arrays and objects are always truthy, even when empty

---

## Operators

### Arithmetic Operators

```javascript
let a = 10, b = 3;

console.log(a + b); // 13 (addition)
console.log(a - b); // 7 (subtraction)
console.log(a * b); // 30 (multiplication)
console.log(a / b); // 3.333... (division)
console.log(a % b); // 1 (modulus/remainder)
console.log(a ** b); // 1000 (exponentiation - ES2016)

// Increment/Decrement
let x = 5;
console.log(x++); // 5 (post-increment: use then increment)
console.log(++x); // 7 (pre-increment: increment then use)
```

### Comparison Operators

```javascript
let a = 5, b = "5";

// Equality (loose - with type coercion)
console.log(a == b); // true (5 == "5")

// Strict equality (no type coercion)
console.log(a === b); // false (5 !== "5")

// Inequality
console.log(a != b); // false
console.log(a !== b); // true

// Relational
console.log(a > 3); // true
console.log(a <= 5); // true
```

### Logical Operators

```javascript
let isAdult = true;
let hasLicense = false;

// AND (&&) - returns first falsy value or last value
console.log(isAdult && hasLicense); // false
console.log("hello" && 42); // 42

// OR (||) - returns first truthy value or last value
console.log(isAdult || hasLicense); // true
console.log("" || "default"); // "default"

// NOT (!)
console.log(!isAdult); // false

// Nullish coalescing (??) - ES2020
let username = null;
console.log(username ?? "guest"); // "guest"
```

### Assignment Operators

```javascript
let x = 10;

x += 5; // x = x + 5 (15)
x -= 3; // x = x - 3 (12)
x *= 2; // x = x * 2 (24)
x /= 4; // x = x / 4 (6)
x %= 5; // x = x % 5 (1)

// Logical assignment (ES2021)
let a = null;
a ??= "default"; // a = a ?? "default"
```

### Ternary Operator

```javascript
let age = 20;
let status = age >= 18 ? "adult" : "minor";

// Chaining ternary operators
let grade = score >= 90 ? "A" : score >= 80 ? "B" : score >= 70 ? "C" : "F";
```

### Pro Tips
- Use `===` instead of `==` to avoid unexpected type coercion
- Use nullish coalescing (`??`) instead of OR (`||`) when you want to preserve falsy values like 0 or ""
- Logical operators return values, not just booleans

---

## Control Flow

### Conditional Statements

```javascript
// if...else
let weather = "sunny";

if (weather === "sunny") {
  console.log("Wear sunglasses!");
} else if (weather === "rainy") {
  console.log("Bring an umbrella!");
} else {
  console.log("Check the weather app!");
}

// switch statement
let day = "Monday";

switch (day) {
  case "Monday":
  case "Tuesday":
  case "Wednesday":
  case "Thursday":
  case "Friday":
    console.log("Weekday");
    break;
  case "Saturday":
  case "Sunday":
    console.log("Weekend");
    break;
  default:
    console.log("Invalid day");
}
```

### Loops

```javascript
// for loop
for (let i = 0; i < 5; i++) {
  console.log(`Iteration ${i}`);
}

// for...in (iterates over object keys/array indices)
let person = { name: "John", age: 30, city: "NYC" };
for (let key in person) {
  console.log(`${key}: ${person[key]}`);
}

// for...of (iterates over iterable values)
let fruits = ["apple", "banana", "orange"];
for (let fruit of fruits) {
  console.log(fruit);
}

// while loop
let count = 0;
while (count < 3) {
  console.log(`Count: ${count}`);
  count++;
}

// do...while loop
let num = 0;
do {
  console.log(`Number: ${num}`);
  num++;
} while (num < 3);
```

### Loop Control

```javascript
// break - exit loop entirely
for (let i = 0; i < 10; i++) {
  if (i === 5) break;
  console.log(i); // 0, 1, 2, 3, 4
}

// continue - skip current iteration
for (let i = 0; i < 5; i++) {
  if (i === 2) continue;
  console.log(i); // 0, 1, 3, 4
}

// Labeled break/continue (rarely used)
outer: for (let i = 0; i < 3; i++) {
  for (let j = 0; j < 3; j++) {
    if (i === 1 && j === 1) break outer;
    console.log(`${i}, ${j}`);
  }
}
```

### Pro Tips
- Use `for...of` for arrays and iterables, `for...in` for objects
- Avoid modifying arrays while iterating over them
- Consider using array methods like `forEach`, `map`, `filter` instead of traditional loops

---

## Functions

### Function Declarations

```javascript
// Function declaration (hoisted)
function greet(name) {
  return `Hello, ${name}!`;
}

// Function expression (not hoisted)
const greet2 = function(name) {
  return `Hi, ${name}!`;
};

// Arrow function (ES6)
const greet3 = (name) => `Hey, ${name}!`;
const greet4 = name => `Hello, ${name}!`; // Single parameter, no parentheses
const greet5 = () => "Hello, World!"; // No parameters

// Multi-line arrow function
const calculate = (a, b) => {
  const sum = a + b;
  return sum * 2;
};
```

### Parameters & Arguments

```javascript
// Default parameters
function greet(name = "World") {
  return `Hello, ${name}!`;
}

// Rest parameters
function sum(...numbers) {
  return numbers.reduce((total, num) => total + num, 0);
}
console.log(sum(1, 2, 3, 4)); // 10

// Destructuring parameters
function createUser({name, age, email}) {
  return { name, age, email, id: Date.now() };
}

const user = createUser({
  name: "John",
  age: 30,
  email: "john@example.com"
});
```

### Higher-Order Functions

```javascript
// Function that takes another function as parameter
function applyOperation(a, b, operation) {
  return operation(a, b);
}

const add = (x, y) => x + y;
const multiply = (x, y) => x * y;

console.log(applyOperation(5, 3, add)); // 8
console.log(applyOperation(5, 3, multiply)); // 15

// Function that returns another function
function createMultiplier(factor) {
  return function(number) {
    return number * factor;
  };
}

const double = createMultiplier(2);
const triple = createMultiplier(3);

console.log(double(5)); // 10
console.log(triple(4)); // 12
```

### Immediately Invoked Function Expression (IIFE)

```javascript
// IIFE - runs immediately and creates private scope
(function() {
  let privateVariable = "I'm private";
  console.log("IIFE executed!");
})();

// Arrow function IIFE
(() => {
  console.log("Arrow IIFE executed!");
})();

// IIFE with parameters
((name) => {
  console.log(`Hello, ${name}!`);
})("World");
```

### Pro Tips
- Use arrow functions for short, inline functions and when you need to preserve `this` context
- Use regular functions for methods and when you need `arguments` object
- Functions are first-class objects - they can be stored in variables, passed as arguments, and returned from other functions

### Gotchas
- Arrow functions don't have their own `this`, `arguments`, or `super`
- Function declarations are hoisted, but function expressions are not
- `this` in arrow functions is lexically bound (inherited from surrounding scope)

---

## Arrays & Objects

### Arrays

```javascript
// Array creation
let fruits = ["apple", "banana", "orange"];
let numbers = new Array(1, 2, 3, 4, 5);
let empty = new Array(5); // Creates array with 5 empty slots

// Array methods
let arr = [1, 2, 3, 4, 5];

// Adding/removing elements
arr.push(6); // Add to end: [1, 2, 3, 4, 5, 6]
arr.pop(); // Remove from end: [1, 2, 3, 4, 5]
arr.unshift(0); // Add to beginning: [0, 1, 2, 3, 4, 5]
arr.shift(); // Remove from beginning: [1, 2, 3, 4, 5]

// Splice: arr.splice(start, deleteCount, ...itemsToAdd)
arr.splice(2, 1, "new"); // [1, 2, "new", 4, 5]

// Iteration methods
let doubled = arr.map(x => x * 2); // Transform each element
let evens = arr.filter(x => x % 2 === 0); // Filter elements
let sum = arr.reduce((acc, curr) => acc + curr, 0); // Reduce to single value

arr.forEach((item, index) => {
  console.log(`${index}: ${item}`);
});

// Finding elements
let found = arr.find(x => x > 3); // First element matching condition
let foundIndex = arr.findIndex(x => x > 3); // Index of first match
let includes = arr.includes(3); // Check if element exists

// Sorting and reversing
let names = ["Charlie", "Alice", "Bob"];
names.sort(); // ["Alice", "Bob", "Charlie"]
names.reverse(); // ["Charlie", "Bob", "Alice"]

// Advanced sorting
let people = [{name: "John", age: 30}, {name: "Alice", age: 25}];
people.sort((a, b) => a.age - b.age); // Sort by age
```

### Objects

```javascript
// Object creation
let person = {
  name: "John",
  age: 30,
  city: "New York",
  hobbies: ["reading", "coding"],
  
  // Method
  greet() {
    return `Hello, I'm ${this.name}`;
  },
  
  // Method with arrow function (careful with 'this')
  greetArrow: () => {
    return `Hello!`; // 'this' doesn't refer to the object
  }
};

// Property access
console.log(person.name); // Dot notation
console.log(person["name"]); // Bracket notation
console.log(person["full-name"]); // Use brackets for special characters

// Dynamic property names
let property = "age";
console.log(person[property]); // 30

// Adding/modifying properties
person.email = "john@example.com";
person["phone"] = "123-456-7890";

// Deleting properties
delete person.city;

// Object methods
let keys = Object.keys(person); // Array of property names
let values = Object.values(person); // Array of property values
let entries = Object.entries(person); // Array of [key, value] pairs

// Object destructuring
let {name, age, email = "N/A"} = person;
console.log(name, age, email);

// Nested destructuring
let user = {
  profile: {
    name: "Alice",
    settings: {
      theme: "dark"
    }
  }
};

let {profile: {name: userName, settings: {theme}}} = user;
```

### Advanced Object Patterns

```javascript
// Computed property names
let prop = "dynamic";
let obj = {
  [prop]: "value",
  [`${prop}Count`]: 42
};

// Property shorthand
let name = "John";
let age = 30;
let person = {name, age}; // Same as {name: name, age: age}

// Method shorthand
let calculator = {
  add(a, b) { return a + b; }, // Same as add: function(a, b) { return a + b; }
  multiply(a, b) { return a * b; }
};

// Object spread
let defaults = {theme: "light", lang: "en"};
let userPrefs = {theme: "dark"};
let settings = {...defaults, ...userPrefs}; // {theme: "dark", lang: "en"}

// Object.assign
let target = {a: 1};
let source = {b: 2, c: 3};
Object.assign(target, source); // target is now {a: 1, b: 2, c: 3}
```

### Pro Tips
- Use `const` for arrays and objects - you can still modify their contents
- Array methods like `map`, `filter`, `reduce` don't mutate the original array
- `for...of` for array values, `for...in` for object keys
- Use destructuring to extract multiple values cleanly

### Gotchas
- Arrays are objects: `typeof [] === "object"`
- `arr.length` is not always reliable (sparse arrays)
- Object property order is mostly preserved in modern JS, but don't rely on it for critical logic
- Mutating methods like `push`, `sort` modify the original array

---

## DOM Manipulation

### Selecting Elements

```javascript
// Single element selection
let element = document.getElementById("myId");
let element2 = document.querySelector(".myClass"); // First match
let element3 = document.querySelector("#myId > .child");

// Multiple elements selection
let elements = document.getElementsByClassName("myClass"); // HTMLCollection
let elements2 = document.getElementsByTagName("div"); // HTMLCollection
let elements3 = document.querySelectorAll(".myClass"); // NodeList

// Convert HTMLCollection to Array
let elementsArray = Array.from(elements);
```

### Creating and Modifying Elements

```javascript
// Creating elements
let div = document.createElement("div");
let textNode = document.createTextNode("Hello World");

// Setting content
div.textContent = "Plain text content";
div.innerHTML = "<strong>HTML content</strong>"; // Be careful with XSS!

// Setting attributes
div.setAttribute("id", "myDiv");
div.setAttribute("class", "container");
div.id = "myDiv"; // Direct property access
div.className = "container active";

// Modern class manipulation
div.classList.add("new-class");
div.classList.remove("old-class");
div.classList.toggle("active");
div.classList.contains("container"); // true/false

// Style manipulation
div.style.color = "red";
div.style.backgroundColor = "blue";
div.style.fontSize = "16px";

// Better approach: use CSS classes
div.classList.add("highlighted"); // Define .highlighted in CSS
```

### DOM Tree Manipulation

```javascript
// Adding elements
let parent = document.getElementById("container");
let child = document.createElement("p");
child.textContent = "New paragraph";

parent.appendChild(child); // Add to end
parent.insertBefore(child, parent.firstChild); // Add to beginning
parent.insertAdjacentHTML("beforeend", "<p>HTML string</p>");

// Modern insertion methods
parent.append(child); // Can append multiple nodes/strings
parent.prepend(child); // Add to beginning
parent.before(child); // Insert before parent
parent.after(child); // Insert after parent

// Removing elements
child.remove(); // Modern way
parent.removeChild(child); // Older way

// Replacing elements
let newElement = document.createElement("div");
parent.replaceChild(newElement, child);
```

### Traversing the DOM

```javascript
let element = document.getElementById("myElement");

// Parent navigation
let parent = element.parentNode;
let parentElement = element.parentElement; // null if parent is not an element

// Child navigation
let children = element.children; // HTMLCollection of element children
let childNodes = element.childNodes; // NodeList including text nodes
let firstChild = element.firstElementChild;
let lastChild = element.lastElementChild;

// Sibling navigation
let nextSibling = element.nextElementSibling;
let prevSibling = element.previousElementSibling;

// Searching within element
let descendant = element.querySelector(".descendant-class");
let descendants = element.querySelectorAll("p");
```

### Working with Forms

```javascript
let form = document.getElementById("myForm");
let input = document.getElementById("username");
let select = document.getElementById("country");
let checkbox = document.getElementById("subscribe");

// Getting form values
let username = input.value;
let selectedCountry = select.value;
let isSubscribed = checkbox.checked;

// Setting form values
input.value = "john_doe";
select.value = "USA";
checkbox.checked = true;

// Form validation
if (input.validity.valid) {
  console.log("Input is valid");
} else {
  console.log("Validation errors:", input.validationMessage);
}

// Custom validation
input.setCustomValidity("Username must be at least 3 characters");
input.reportValidity(); // Show validation message
```

### Pro Tips
- Use `textContent` instead of `innerHTML` when setting plain text (safer)
- Cache DOM queries in variables to avoid repeated lookups
- Use `documentFragment` for multiple DOM insertions to improve performance
- Modern browsers support `closest()` method for upward traversal

### Performance Considerations
```javascript
// Bad: Multiple DOM queries
for (let i = 0; i < 100; i++) {
  document.getElementById("container").appendChild(createChild(i));
}

// Good: Cache the reference
let container = document.getElementById("container");
let fragment = document.createDocumentFragment();

for (let i = 0; i < 100; i++) {
  fragment.appendChild(createChild(i));
}
container.appendChild(fragment);
```

---

## Events

### Adding Event Listeners

```javascript
// Method 1: addEventListener (recommended)
let button = document.getElementById("myButton");

button.addEventListener("click", function(event) {
  console.log("Button clicked!");
  console.log("Event type:", event.type);
  console.log("Target element:", event.target);
});

// Arrow function
button.addEventListener("click", (e) => {
  console.log("Arrow function handler");
});

// Method 2: Event handler properties
button.onclick = function(e) {
  console.log("Property handler");
};

// Method 3: Inline HTML (not recommended)
// <button onclick="handleClick()">Click me</button>
```

### Event Object

```javascript
function handleEvent(event) {
  // Common event properties
  console.log("Type:", event.type); // "click", "keydown", etc.
  console.log("Target:", event.target); // Element that triggered the event
  console.log("CurrentTarget:", event.currentTarget); // Element with the listener
  console.log("Timestamp:", event.timeStamp);
  
  // Mouse events
  if (event.type === "click") {
    console.log("Mouse position:", event.clientX, event.clientY);
    console.log("Button pressed:", event.button); // 0=left, 1=middle, 2=right
  }
  
  // Keyboard events
  if (event.type === "keydown") {
    console.log("Key pressed:", event.key);
    console.log("Key code:", event.code);
    console.log("Modifiers:", {
      ctrl: event.ctrlKey,
      shift: event.shiftKey,
      alt: event.altKey,
      meta: event.metaKey
    });
  }
}
```

### Event Types

```javascript
let element = document.getElementById("myElement");

// Mouse events
element.addEventListener("click", handleEvent);
element.addEventListener("dblclick", handleEvent);
element.addEventListener("mousedown", handleEvent);
element.addEventListener("mouseup", handleEvent);
element.addEventListener("mousemove", handleEvent);
element.addEventListener("mouseenter", handleEvent); // No bubbling
element.addEventListener("mouseleave", handleEvent); // No bubbling
element.addEventListener("mouseover", handleEvent); // Bubbles
element.addEventListener("mouseout", handleEvent); // Bubbles

// Keyboard events
element.addEventListener("keydown", handleEvent);
element.addEventListener("keypress", handleEvent); // Deprecated
element.addEventListener("keyup", handleEvent);

// Form events
let form = document.getElementById("myForm");
form.addEventListener("submit", handleEvent);
element.addEventListener("change", handleEvent); // When value changes and loses focus
element.addEventListener("input", handleEvent); // When value changes immediately
element.addEventListener("focus", handleEvent);
element.addEventListener("blur", handleEvent);

// Window events
window.addEventListener("load", handleEvent); // All resources loaded
window.addEventListener("DOMContentLoaded", handleEvent); // DOM ready
window.addEventListener("resize", handleEvent);
window.addEventListener("scroll", handleEvent);
window.addEventListener("beforeunload", handleEvent); // Before page unload
```

### Event Propagation

```javascript
// Event bubbling (default): event travels from target to root
// Event capturing: event travels from root to target

let parent = document.getElementById("parent");
let child = document.getElementById("child");

// Bubbling phase (default)
parent.addEventListener("click", () => {
  console.log("Parent clicked (bubbling)");
});

child.addEventListener("click", () => {
  console.log("Child clicked (bubbling)");
});

// Capturing phase
parent.addEventListener("click", () => {
  console.log("Parent clicked (capturing)");
}, true); // Third parameter = useCapture

// Stopping propagation
child.addEventListener("click", (e) => {
  console.log("Child clicked");
  e.stopPropagation(); // Prevents bubbling
  e.stopImmediatePropagation(); // Stops other listeners on same element
});

// Preventing default behavior
let link = document.getElementById("myLink");
link.addEventListener("click", (e) => {
  e.preventDefault(); // Prevents following the link
  console.log("Link click prevented");
});
```

### Event Delegation

```javascript
// Instead of adding listeners to many child elements,
// add one listener to parent and use event bubbling

let list = document.getElementById("todoList");

// Bad: Adding listener to each item
document.querySelectorAll(".todo-item").forEach(item => {
  item.addEventListener("click", handleItemClick);
});

// Good: Event delegation
list.addEventListener("click", (e) => {
  if (e.target.classList.contains("todo-item")) {
    handleItemClick(e);
  }
  
  // Or use closest() for nested elements
  let todoItem = e.target.closest(".todo-item");
  if (todoItem) {
    handleItemClick(e, todoItem);
  }
});

function handleItemClick(event, item = event.target) {
  console.log("Todo item clicked:", item.textContent);
}
```

### Custom Events

```javascript
// Creating custom events
let customEvent = new CustomEvent("userLogin", {
  detail: {
    username: "john_doe",
    timestamp: Date.now()
  },
  bubbles: true,
  cancelable: true
});

// Dispatching custom event
document.dispatchEvent(customEvent);

// Listening for custom event
document.addEventListener("userLogin", (e) => {
  console.log("User logged in:", e.detail.username);
});

// Older way (broader browser support)
let event = document.createEvent("CustomEvent");
event.initCustomEvent("userLogin", true, true, {username: "john_doe"});
document.dispatchEvent(event);
```

### Event Best Practices

```javascript
// Removing event listeners (important for memory management)
function myHandler(e) {
  console.log("Handled");
}

element.addEventListener("click", myHandler);
element.removeEventListener("click", myHandler); // Must be same function reference

// Using AbortController (modern approach)
let controller = new AbortController();

element.addEventListener("click", myHandler, {
  signal: controller.signal
});

// Remove all listeners added with this controller
controller.abort();

// Passive listeners (better performance for touch/scroll)
element.addEventListener("touchstart", handleTouch, {passive: true});

// Once listeners (automatically removed after first execution)
element.addEventListener("click", handleOnce, {once: true});
```

### Pro Tips
- Use event delegation for dynamic content and better performance
- Always remove event listeners when elements are removed from DOM
- Use passive listeners for touch and scroll events to improve performance
- Prefer `addEventListener` over event handler properties for flexibility

### Gotchas
- `this` in event handlers refers to the element (unless using arrow functions)
- Event handlers attached via HTML attributes execute in global scope
- Some events don't bubble (focus, blur, load, unload)
- `preventDefault()` doesn't stop propagation, `stopPropagation()` doesn't prevent default

---

## ES6+ Features

### Let, Const, and Block Scope

```javascript
// var vs let vs const
function scopeExample() {
  if (true) {
    var varVariable = "I'm function-scoped";
    let letVariable = "I'm block-scoped";
    const constVariable = "I'm block-scoped and immutable";
  }
  
  console.log(varVariable); // Works
  // console.log(letVariable); // ReferenceError
  // console.log(constVariable); // ReferenceError
}

// Temporal Dead Zone
console.log(myVar); // undefined (hoisted)
// console.log(myLet); // ReferenceError (TDZ)

var myVar = "var";
let myLet = "let";
```

### Template Literals

```javascript
let name = "Alice";
let age = 30;

// Multi-line strings
let multiline = `
  Hello, ${name}!
  You are ${age} years old.
  Next year you'll be ${age + 1}.
`;

// Tagged templates
function highlight(strings, ...values) {
  return strings.reduce((result, string, i) => {
    let value = values[i] ? `<mark>${values[i]}</mark>` : '';
    return result + string + value;
  }, '');
}

let message = highlight`Hello ${name}, you are ${age} years old!`;
```

### Destructuring Assignment

```javascript
// Array destructuring
let [first, second, ...rest] = [1, 2, 3, 4, 5];
console.log(first); // 1
console.log(second); // 2
console.log(rest); // [3, 4, 5]

// Skipping elements
let [a, , c] = [1, 2, 3];
console.log(a, c); // 1, 3

// Default values
let [x = 10, y = 20] = [5];
console.log(x, y); // 5, 20

// Object destructuring
let person = {name: "John", age: 30, city: "NYC"};
let {name, age, city} = person;

// Renaming variables
let {name: personName, age: personAge} = person;

// Default values
let {name, age, country = "USA"} = person;

// Nested destructuring
let user = {
  id: 1,
  profile: {
    name: "Alice",
    settings: {theme: "dark"}
  }
};

let {profile: {name: userName, settings: {theme}}} = user;

// Function parameter destructuring
function greetUser({name, age = 0}) {
  return `Hello ${name}, you are ${age} years old`;
}

greetUser({name: "Bob", age: 25});
```

### Arrow Functions

```javascript
// Traditional function
function add(a, b) {
  return a + b;
}

// Arrow function
const add = (a, b) => a + b;

// Single parameter (no parentheses needed)
const square = x => x * x;

// No parameters
const greet = () => "Hello!";

// Multi-line arrow function
const processData = (data) => {
  const processed = data.map(item => item * 2);
  return processed.filter(item => item > 10);
};

// Arrow functions and 'this'
const obj = {
  name: "Object",
  
  regularMethod() {
    console.log(this.name); // "Object"
    
    setTimeout(function() {
      console.log(this.name); // undefined (or global object)
    }, 100);
    
    setTimeout(() => {
      console.log(this.name); // "Object" (lexical this)
    }, 100);
  }
};
```

### Spread and Rest Operators

```javascript
// Spread operator (...)
// Arrays
let arr1 = [1, 2, 3];
let arr2 = [4, 5, 6];
let combined = [...arr1, ...arr2]; // [1, 2, 3, 4, 5, 6]

// Objects
let obj1 = {a: 1, b: 2};
let obj2 = {c: 3, d: 4};
let merged = {...obj1, ...obj2}; // {a: 1, b: 2, c: 3, d: 4}

// Overriding properties
let defaults = {theme: "light", lang: "en"};
let userPrefs = {theme: "dark"};
let settings = {...defaults, ...userPrefs}; // {theme: "dark", lang: "en"}

// Function arguments
function sum(a, b, c) {
  return a + b + c;
}
let numbers = [1, 2, 3];
console.log(sum(...numbers)); // 6

// Rest operator (...)
// Function parameters
function sum(...args) {
  return args.reduce((total, num) => total + num, 0);
}

// Array destructuring
let [first, ...others] = [1, 2, 3, 4, 5];
console.log(first); // 1
console.log(others); // [2, 3, 4, 5]

// Object destructuring
let {name, ...otherProps} = {name: "John", age: 30, city: "NYC"};
console.log(name); // "John"
console.log(otherProps); // {age: 30, city: "NYC"}
```

### Default Parameters

```javascript
// ES6 default parameters
function greet(name = "World", punctuation = "!") {
  return `Hello, ${name}${punctuation}`;
}

console.log(greet()); // "Hello, World!"
console.log(greet("Alice")); // "Hello, Alice!"
console.log(greet("Bob", "?")); // "Hello, Bob?"

// Default parameters with expressions
function createUser(name, id = Date.now()) {
  return {name, id};
}

// Default parameters can reference earlier parameters
function greetWithTitle(name, title = `Mr. ${name}`) {
  return `Hello, ${title}`;
}
```

### Enhanced Object Literals

```javascript
let name = "John";
let age = 30;

// Property shorthand
let person = {name, age}; // Same as {name: name, age: age}

// Method shorthand
let calculator = {
  add(a, b) { return a + b; },
  multiply(a, b) { return a * b; }
};

// Computed property names
let propName = "dynamicProp";
let obj = {
  [propName]: "value",
  [`${propName}Count`]: 42,
  [Symbol.iterator]: function*() {
    yield 1;
    yield 2;
    yield 3;
  }
};

// Getters and setters
let user = {
  _name: "",
  
  get name() {
    return this._name.toUpperCase();
  },
  
  set name(value) {
    this._name = value;
  }
};

user.name = "alice";
console.log(user.name); // "ALICE"
```

### Classes (ES6+)

```javascript
// Basic class
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }
  
  greet() {
    return `Hello, I'm ${this.name}`;
  }
  
  // Getter
  get info() {
    return `${this.name}, ${this.age} years old`;
  }
  
  // Setter
  set age(value) {
    if (value < 0) throw new Error("Age cannot be negative");
    this._age = value;
  }
  
  get age() {
    return this._age;
  }
  
  // Static method
  static createAnonymous() {
    return new Person("Anonymous", 0);
  }
}

// Inheritance
class Employee extends Person {
  constructor(name, age, jobTitle) {
    super(name, age); // Call parent constructor
    this.jobTitle = jobTitle;
  }
  
  greet() {
    return `${super.greet()}, I'm a ${this.jobTitle}`;
  }
  
  // Private fields (ES2022)
  #salary = 0;
  
  setSalary(amount) {
    this.#salary = amount;
  }
  
  getSalary() {
    return this.#salary;
  }
}

let emp = new Employee("Alice", 30, "Developer");
console.log(emp.greet()); // "Hello, I'm Alice, I'm a Developer"
```

### Modules (ES6)

```javascript
// math.js - Named exports
export const PI = 3.14159;
export function add(a, b) {
  return a + b;
}
export class Calculator {
  multiply(a, b) {
    return a * b;
  }
}

// Alternative export syntax
const subtract = (a, b) => a - b;
const divide = (a, b) => a / b;
export {subtract, divide};

// Default export
export default function factorial(n) {
  return n <= 1 ? 1 : n * factorial(n - 1);
}

// main.js - Importing
import factorial from './math.js'; // Default import
import {PI, add, Calculator} from './math.js'; // Named imports
import {subtract as minus} from './math.js'; // Renamed import
import * as MathUtils from './math.js'; // Import all

// Dynamic imports (ES2020)
async function loadMath() {
  const mathModule = await import('./math.js');
  console.log(mathModule.PI);
}
```

### Symbols

```javascript
// Creating symbols
let sym1 = Symbol();
let sym2 = Symbol("description");
let sym3 = Symbol("description");

console.log(sym2 === sym3); // false (each symbol is unique)

// Using symbols as object keys
let obj = {
  [sym1]: "value1",
  [sym2): "value2"
};

// Symbols are not enumerable
console.log(Object.keys(obj)); // []
console.log(Object.getOwnPropertySymbols(obj)); // [sym1, sym2]

// Well-known symbols
let myIterable = {
  [Symbol.iterator]: function*() {
    yield 1;
    yield 2;
    yield 3;
  }
};

for (let value of myIterable) {
  console.log(value); // 1, 2, 3
}
```

### Iterators and Generators

```javascript
// Iterator protocol
let customIterable = {
  data: [1, 2, 3],
  [Symbol.iterator]() {
    let index = 0;
    let data = this.data;
    
    return {
      next() {
        if (index < data.length) {
          return {value: data[index++], done: false};
        } else {
          return {done: true};
        }
      }
    };
  }
};

// Generator functions
function* numberGenerator() {
  yield 1;
  yield 2;
  yield 3;
  return 4; // Final value
}

let gen = numberGenerator();
console.log(gen.next()); // {value: 1, done: false}
console.log(gen.next()); // {value: 2, done: false}
// ... continues until done: true

// Generator with infinite sequence
function* fibonacci() {
  let [a, b] = [0, 1];
  while (true) {
    yield a;
    [a, b] = [b, a + b];
  }
}

// Using generators
let fib = fibonacci();
console.log(fib.next().value); // 0
console.log(fib.next().value); // 1
console.log(fib.next().value); // 1
```

### Map and Set

```javascript
// Map - key-value pairs with any type of keys
let map = new Map();

// Setting values
map.set("string", "value");
map.set(42, "number key");
map.set(true, "boolean key");

let objKey = {};
map.set(objKey, "object key");

// Getting values
console.log(map.get("string")); // "value"
console.log(map.get(42)); // "number key"

// Map methods
console.log(map.has("string")); // true
console.log(map.size); // 4
map.delete(42);
map.clear(); // Remove all

// Iterating over Map
let userRoles = new Map([
  ["alice", "admin"],
  ["bob", "user"],
  ["charlie", "moderator"]
]);

for (let [user, role] of userRoles) {
  console.log(`${user}: ${role}`);
}

// Set - unique values
let set = new Set([1, 2, 3, 3, 4]); // {1, 2, 3, 4}

set.add(5);
set.add(3); // No effect, already exists
console.log(set.has(3)); // true
set.delete(2);
console.log(set.size); // 4

// Converting to array
let uniqueArray = [...set];

// WeakMap and WeakSet (keys/values can be garbage collected)
let weakMap = new WeakMap();
let obj = {};
weakMap.set(obj, "value");
// When obj is no longer referenced, it can be garbage collected
```

### Proxy and Reflect

```javascript
// Proxy - intercept and customize operations
let target = {
  name: "John",
  age: 30
};

let proxy = new Proxy(target, {
  get(target, prop) {
    console.log(`Getting ${prop}`);
    return target[prop];
  },
  
  set(target, prop, value) {
    console.log(`Setting ${prop} to ${value}`);
    if (prop === "age" && value < 0) {
      throw new Error("Age cannot be negative");
    }
    target[prop] = value;
    return true;
  },
  
  has(target, prop) {
    console.log(`Checking if ${prop} exists`);
    return prop in target;
  }
});

console.log(proxy.name); // "Getting name", then "John"
proxy.age = 31; // "Setting age to 31"

// Reflect - provides methods for interceptable operations
let obj = {x: 1, y: 2};
console.log(Reflect.has(obj, "x")); // true
Reflect.set(obj, "z", 3);
console.log(Reflect.ownKeys(obj)); // ["x", "y", "z"]
```

---

## Promises & Async/Await

### Understanding Promises

```javascript
// Creating a Promise
let promise = new Promise((resolve, reject) => {
  let success = Math.random() > 0.5;
  
  setTimeout(() => {
    if (success) {
      resolve("Operation successful!");
    } else {
      reject(new Error("Operation failed!"));
    }
  }, 1000);
});

// Consuming Promises with .then()/.catch()
promise
  .then(result => {
    console.log(result);
    return "Next value"; // Return value for next .then()
  })
  .then(value => {
    console.log(value); // "Next value"
  })
  .catch(error => {
    console.error(error.message);
  })
  .finally(() => {
    console.log("Always executes");
  });
```

### Promise States and Methods

```javascript
// Promise states: pending, fulfilled, rejected

// Promise.resolve() - creates resolved promise
let resolvedPromise = Promise.resolve("Immediate value");

// Promise.reject() - creates rejected promise
let rejectedPromise = Promise.reject(new Error("Immediate error"));

// Promise.all() - waits for all promises
let promises = [
  Promise.resolve(1),
  Promise.resolve(2),
  Promise.resolve(3)
];

Promise.all(promises)
  .then(results => {
    console.log(results); // [1, 2, 3]
  })
  .catch(error => {
    console.log("One promise failed:", error);
  });

// Promise.allSettled() - waits for all, doesn't fail fast
Promise.allSettled([
  Promise.resolve(1),
  Promise.reject("error"),
  Promise.resolve(3)
]).then(results => {
  console.log(results);
  // [
  //   {status: "fulfilled", value: 1},
  //   {status: "rejected", reason: "error"},
  //   {status: "fulfilled", value: 3}
  // ]
});

// Promise.race() - resolves with first settled promise
Promise.race([
  new Promise(resolve => setTimeout(() => resolve("fast"), 100)),
  new Promise(resolve => setTimeout(() => resolve("slow"), 200))
]).then(result => {
  console.log(result); // "fast"
});

// Promise.any() - resolves with first fulfilled promise
Promise.any([
  Promise.reject("error1"),
  Promise.resolve("success"),
  Promise.reject("error2")
]).then(result => {
  console.log(result); // "success"
});
```

### Async/Await

```javascript
// Async function returns a Promise
async function fetchData() {
  return "data"; // Automatically wrapped in Promise.resolve()
}

fetchData().then(data => console.log(data)); // "data"

// Await pauses execution until Promise resolves
async function processData() {
  try {
    let data = await fetchData();
    let processed = await processStep1(data);
    let final = await processStep2(processed);
    return final;
  } catch (error) {
    console.error("Error processing data:", error);
    throw error; // Re-throw if needed
  }
}

// Error handling with async/await
async function fetchUser(id) {
  try {
    let response = await fetch(`/api/users/${id}`);
    
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }
    
    let user = await response.json();
    return user;
  } catch (error) {
    if (error instanceof TypeError) {
      console.error("Network error:", error.message);
    } else {
      console.error("Fetch error:", error.message);
    }
    throw error;
  }
}
```

### Advanced Async Patterns

```javascript
// Sequential vs Parallel execution
async function sequentialExecution() {
  console.time("sequential");
  
  let result1 = await slowOperation1(); // Wait 1 second
  let result2 = await slowOperation2(); // Wait another 1 second
  let result3 = await slowOperation3(); // Wait another 1 second
  
  console.timeEnd("sequential"); // ~3 seconds
  return [result1, result2, result3];
}

async function parallelExecution() {
  console.time("parallel");
  
  // Start all operations simultaneously
  let [result1, result2, result3] = await Promise.all([
    slowOperation1(),
    slowOperation2(),
    slowOperation3()
  ]);
  
  console.timeEnd("parallel"); // ~1 second
  return [result1, result2, result3];
}

// Async iteration
async function* asyncGenerator() {
  for (let i = 0; i < 3; i++) {
    await new Promise(resolve => setTimeout(resolve, 1000));
    yield i;
  }
}

async function useAsyncGenerator() {
  for await (let value of asyncGenerator()) {
    console.log(value); // 0, 1, 2 (with 1 second delays)
  }
}

// Promise timeout utility
function withTimeout(promise, ms) {
  return Promise.race([
    promise,
    new Promise((_, reject) => 
      setTimeout(() => reject(new Error("Timeout")), ms)
    )
  ]);
}

// Usage
try {
  let result = await withTimeout(fetch("/api/data"), 5000);
  console.log(await result.json());
} catch (error) {
  if (error.message === "Timeout") {
    console.log("Request timed out");
  }
}
```

### Common Async Patterns

```javascript
// Retry mechanism
async function retryOperation(operation, maxRetries = 3, delay = 1000) {
  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    try {
      return await operation();
    } catch (error) {
      if (attempt === maxRetries) {
        throw error;
      }
      console.log(`Attempt ${attempt} failed, retrying in ${delay}ms...`);
      await new Promise(resolve => setTimeout(resolve, delay));
      delay *= 2; // Exponential backoff
    }
  }
}

// Queue for limiting concurrent operations
class AsyncQueue {
  constructor(concurrency = 1) {
    this.concurrency = concurrency;
    this.running = 0;
    this.queue = [];
  }
  
  async add(task) {
    return new Promise((resolve, reject) => {
      this.queue.push({
        task,
        resolve,
        reject
      });
      this.tryNext();
    });
  }
  
  async tryNext() {
    if (this.running >= this.concurrency || this.queue.length === 0) {
      return;
    }
    
    this.running++;
    let {task, resolve, reject} = this.queue.shift();
    
    try {
      let result = await task();
      resolve(result);
    } catch (error) {
      reject(error);
    } finally {
      this.running--;
      this.tryNext();
    }
  }
}

// Usage
let queue = new AsyncQueue(2); // Max 2 concurrent operations

queue.add(() => fetch("/api/data1"));
queue.add(() => fetch("/api/data2"));
queue.add(() => fetch("/api/data3")); // Will wait for slot
```

### Pro Tips
- Use `async/await` for cleaner, more readable asynchronous code
- Don't forget `await` - async functions without await are often mistakes
- Use `Promise.all()` for independent parallel operations
- Use `Promise.allSettled()` when you need all results regardless of failures
- Always handle errors in async functions

### Gotchas
- `await` only works inside `async` functions (or top-level in modules)
- Forgotten `await` returns a Promise instead of the value
- `forEach` doesn't work with `await` - use `for...of` or `Promise.all()`
- Async functions always return Promises, even if you return a regular value

---

## Error Handling

### Try-Catch-Finally

```javascript
// Basic error handling
try {
  let result = riskyOperation();
  console.log(result);
} catch (error) {
  console.error("Something went wrong:", error.message);
} finally {
  console.log("This always runs");
}

// Catching specific error types
try {
  JSON.parse("invalid json");
} catch (error) {
  if (error instanceof SyntaxError) {
    console.log("Invalid JSON syntax");
  } else if (error instanceof ReferenceError) {
    console.log("Reference error");
  } else {
    console.log("Unknown error:", error);
  }
}

// Nested try-catch
try {
  try {
    let data = JSON.parse(jsonString);
    processData(data);
  } catch (parseError) {
    console.log("JSON parsing failed, using defaults");
    let data = getDefaultData();
    processData(data);
  }
} catch (processingError) {
  console.error("Data processing failed:", processingError);
}
```

### Throwing Custom Errors

```javascript
// Throwing basic errors
function divide(a, b) {
  if (b === 0) {
    throw new Error("Division by zero is not allowed");
  }
  return a / b;
}

// Custom error classes
class ValidationError extends Error {
  constructor(message, field) {
    super(message);
    this.name = "ValidationError";
    this.field = field;
  }
}

class NetworkError extends Error {
  constructor(message, statusCode) {
    super(message);
    this.name = "NetworkError";
    this.statusCode = statusCode;
  }
}

// Using custom errors
function validateUser(user) {
  if (!user.email) {
    throw new ValidationError("Email is required", "email");
  }
  if (!user.name) {
    throw new ValidationError("Name is required", "name");
  }
}

try {
  validateUser({name: "John"}); // Missing email
} catch (error) {
  if (error instanceof ValidationError) {
    console.log(`Validation failed for ${error.field}: ${error.message}`);
  }
}
```

### Async Error Handling

```javascript
// Promise error handling
fetchUserData(userId)
  .then(user => {
    return processUser(user);
  })
  .then(result => {
    console.log("Success:", result);
  })
  .catch(error => {
    if (error instanceof NetworkError) {
      console.log("Network issue:", error.message);
    } else if (error instanceof ValidationError) {
      console.log("Validation issue:", error.message);
    } else {
      console.log("Unexpected error:", error);
    }
  });

// Async/await error handling
async function handleUser(userId) {
  try {
    let user = await fetchUserData(userId);
    let result = await processUser(user);
    console.log("Success:", result);
    return result;
  } catch (error) {
    // Handle specific error types