# Control Flow

## Conditional Statements

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

## Loops

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

## Loop Control

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

## Pro Tips
- Use `for...of` for arrays and iterables, `for...in` for objects
- Avoid modifying arrays while iterating over them
- Consider using array methods like `forEach`, `map`, `filter` instead of traditional loops