# Variables & Data Types

## Variable Declarations

```javascript
// var - function-scoped, hoisted, can be redeclared
var name = "John";

// let - block-scoped, hoisted but not initialized, cannot be redeclared
let age = 25;

// const - block-scoped, must be initialized, cannot be reassigned
const PI = 3.14159;
```

## Primitive Data Types

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

## Non-Primitive Data Types

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

## Type Checking & Conversion

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

## Gotchas
- `null` has type "object" (historical bug in JavaScript)
- `NaN` (Not a Number) is of type "number"
- Empty strings, 0, null, undefined, NaN are falsy values
- Arrays and objects are always truthy, even when empty