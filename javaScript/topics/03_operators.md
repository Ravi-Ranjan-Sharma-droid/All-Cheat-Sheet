# Operators

## Arithmetic Operators

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

## Comparison Operators

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

## Logical Operators

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

## Assignment Operators

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

## Ternary Operator

```javascript
let age = 20;
let status = age >= 18 ? "adult" : "minor";

// Chaining ternary operators
let grade = score >= 90 ? "A" : score >= 80 ? "B" : score >= 70 ? "C" : "F";
```

## Pro Tips
- Use `===` instead of `==` to avoid unexpected type coercion
- Use nullish coalescing (`??`) instead of OR (`||`) when you want to preserve falsy values like 0 or ""
- Logical operators return values, not just booleans