# Functions

## Function Declarations

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

## Parameters & Arguments

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

## Higher-Order Functions

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

## Immediately Invoked Function Expression (IIFE)

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

## Pro Tips
- Use arrow functions for short, inline functions and when you need to preserve `this` context
- Use regular functions for methods and when you need `arguments` object
- Functions are first-class objects - they can be stored in variables, passed as arguments, and returned from other functions

## Gotchas
- Arrow functions don't have their own `this`, `arguments`, or `super`
- Function declarations are hoisted, but function expressions are not
- `this` in arrow functions is lexically bound (inherited from surrounding scope)