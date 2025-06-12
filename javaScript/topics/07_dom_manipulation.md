# DOM Manipulation

## Selecting Elements

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

## Creating and Modifying Elements

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

## DOM Tree Manipulation

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

## Traversing the DOM

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

## Working with Forms

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

## Pro Tips
- Use `textContent` instead of `innerHTML` when setting plain text (safer)
- Cache DOM queries in variables to avoid repeated lookups
- Use `documentFragment` for multiple DOM insertions to improve performance
- Modern browsers support `closest()` method for upward traversal

## Performance Considerations
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