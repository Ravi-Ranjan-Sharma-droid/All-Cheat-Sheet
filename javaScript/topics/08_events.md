# Events

## Adding Event Listeners

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

## Event Object

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

## Event Types

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

## Event Propagation

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

## Event Delegation

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

## Custom Events

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

## Event Best Practices

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

## Pro Tips
- Use event delegation for dynamic content and better performance
- Always remove event listeners when elements are removed from DOM
- Use passive listeners for touch and scroll events to improve performance
- Prefer `addEventListener` over event handler properties for flexibility

## Gotchas
- `this` in event handlers refers to the element (unless using arrow functions)
- Event handlers attached via HTML attributes execute in global scope
- Some events don't bubble (focus, blur, load, unload)
- `preventDefault()` doesn't stop propagation, `stopPropagation()` doesn't prevent default