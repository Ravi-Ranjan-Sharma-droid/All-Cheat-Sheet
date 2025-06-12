# Arrays & Objects

## Arrays

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

## Objects

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

## Advanced Object Patterns

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

## Pro Tips
- Use `const` for arrays and objects - you can still modify their contents
- Array methods like `map`, `filter`, `reduce` don't mutate the original array
- `for...of` for array values, `for...in` for object keys
- Use destructuring to extract multiple values cleanly

## Gotchas
- Arrays are objects: `typeof [] === "object"`
- `arr.length` is not always reliable (sparse arrays)
- Object property order is mostly preserved in modern JS, but don't rely on it for critical logic
- Mutating methods like `push`, `sort` modify the original array