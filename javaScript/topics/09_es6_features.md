# ES6+ Features

## Let, Const, and Block Scope

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

## Template Literals

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

## Destructuring Assignment

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

## Arrow Functions

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

## Spread and Rest Operators

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

## Default Parameters

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

## Enhanced Object Literals

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

## Classes (ES6+)

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

## Modules (ES6)

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

## Symbols

```javascript
// Creating symbols
let sym1 = Symbol();
let sym2 = Symbol("description");
let sym3 = Symbol("description");

console.log(sym2 === sym3); // false (each symbol is unique)

// Using symbols as object keys
let obj = {
  [sym1]: "value1",
  [sym2]: "value2"
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

## Iterators and Generators

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

## Map and Set

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

## Proxy and Reflect

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