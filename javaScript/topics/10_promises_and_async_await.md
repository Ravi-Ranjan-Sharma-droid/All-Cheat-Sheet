# Promises & Async/Await

## Understanding Promises

```javascript
// Creating a promise
const myPromise = new Promise((resolve, reject) => {
  // Asynchronous operation
  const success = true;
  
  if (success) {
    resolve("Operation completed successfully");
  } else {
    reject(new Error("Operation failed"));
  }
});

// Using a promise
myPromise
  .then(result => {
    console.log(result); // "Operation completed successfully"
    return "Next step";
  })
  .then(nextResult => {
    console.log(nextResult); // "Next step"
  })
  .catch(error => {
    console.error(error);
  })
  .finally(() => {
    console.log("Cleanup operations");
  });
```

## Promise States and Methods

```javascript
// Promise states: pending, fulfilled, rejected

// Promise.resolve() - creates a resolved promise
const resolvedPromise = Promise.resolve("Already resolved");
resolvedPromise.then(value => console.log(value)); // "Already resolved"

// Promise.reject() - creates a rejected promise
const rejectedPromise = Promise.reject(new Error("Failure"));
rejectedPromise.catch(error => console.error(error)); // Error: Failure

// Promise.all() - waits for all promises to resolve
const promise1 = Promise.resolve(1);
const promise2 = new Promise(resolve => setTimeout(() => resolve(2), 100));
const promise3 = Promise.resolve(3);

Promise.all([promise1, promise2, promise3])
  .then(values => {
    console.log(values); // [1, 2, 3]
  })
  .catch(error => {
    // If any promise rejects, catch will be called
    console.error(error);
  });

// Promise.allSettled() - waits for all promises to settle
const promises = [
  Promise.resolve(1),
  Promise.reject(new Error("Error")),
  Promise.resolve(3)
];

Promise.allSettled(promises).then(results => {
  console.log(results);
  // [
  //   {status: "fulfilled", value: 1},
  //   {status: "rejected", reason: Error},
  //   {status: "fulfilled", value: 3}
  // ]
});

// Promise.race() - resolves/rejects as soon as one promise resolves/rejects
const fast = new Promise(resolve => setTimeout(() => resolve("fast"), 100));
const slow = new Promise(resolve => setTimeout(() => resolve("slow"), 200));

Promise.race([fast, slow])
  .then(result => {
    console.log(result); // "fast"
  });

// Promise.any() - resolves as soon as one promise resolves
const rejected1 = Promise.reject(new Error("Error 1"));
const rejected2 = Promise.reject(new Error("Error 2"));
const resolved = Promise.resolve("Success");

Promise.any([rejected1, rejected2, resolved])
  .then(result => {
    console.log(result); // "Success"
  })
  .catch(errors => {
    // Only called if all promises reject
    console.log(errors); // AggregateError
  });
```

## Async/Await

```javascript
// Basic async/await
async function fetchData() {
  try {
    const response = await fetch('https://api.example.com/data');
    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error fetching data:", error);
    throw error; // Re-throw to propagate
  }
}

// Using async/await with Promise methods
async function fetchMultipleResources() {
  try {
    const [users, posts, comments] = await Promise.all([
      fetch('https://api.example.com/users').then(r => r.json()),
      fetch('https://api.example.com/posts').then(r => r.json()),
      fetch('https://api.example.com/comments').then(r => r.json())
    ]);
    
    return { users, posts, comments };
  } catch (error) {
    console.error("Error fetching resources:", error);
    throw error;
  }
}

// Error handling with async/await
async function processData() {
  try {
    const data = await fetchData();
    return processResult(data);
  } catch (error) {
    // Handle errors from fetchData() or processResult()
    console.error("Processing error:", error);
    return defaultData;
  } finally {
    // Cleanup code
    console.log("Processing completed");
  }
}
```

## Advanced Async Patterns

```javascript
// Sequential vs Parallel execution
async function sequential() {
  console.time('sequential');
  
  // Sequential execution
  const result1 = await slowOperation(1);
  const result2 = await slowOperation(2);
  const result3 = await slowOperation(3);
  
  console.timeEnd('sequential');
  return [result1, result2, result3];
}

async function parallel() {
  console.time('parallel');
  
  // Parallel execution
  const [result1, result2, result3] = await Promise.all([
    slowOperation(1),
    slowOperation(2),
    slowOperation(3)
  ]);
  
  console.timeEnd('parallel');
  return [result1, result2, result3];
}

// Async iteration
async function processItems(items) {
  // Sequential processing with for...of
  for (const item of items) {
    await processItem(item);
  }
  
  // Parallel processing with Promise.all and map
  await Promise.all(items.map(item => processItem(item)));
  
  // Controlled concurrency
  const results = [];
  const batchSize = 3;
  
  for (let i = 0; i < items.length; i += batchSize) {
    const batch = items.slice(i, i + batchSize);
    const batchResults = await Promise.all(batch.map(processItem));
    results.push(...batchResults);
  }
  
  return results;
}

// Promise timeout utility
function withTimeout(promise, timeoutMs) {
  const timeout = new Promise((_, reject) => {
    setTimeout(() => reject(new Error('Operation timed out')), timeoutMs);
  });
  
  return Promise.race([promise, timeout]);
}

async function fetchWithTimeout() {
  try {
    const result = await withTimeout(fetch('https://api.example.com/data'), 5000);
    return await result.json();
  } catch (error) {
    if (error.message === 'Operation timed out') {
      console.error('The request took too long to complete');
    } else {
      console.error('An error occurred:', error);
    }
    throw error;
  }
}
```

## Common Async Patterns

```javascript
// Retry mechanism
async function fetchWithRetry(url, options = {}, maxRetries = 3, delay = 1000) {
  let lastError;
  
  for (let attempt = 0; attempt < maxRetries; attempt++) {
    try {
      return await fetch(url, options);
    } catch (error) {
      console.warn(`Attempt ${attempt + 1} failed. Retrying in ${delay}ms...`);
      lastError = error;
      
      // Wait before next retry
      await new Promise(resolve => setTimeout(resolve, delay));
      
      // Exponential backoff
      delay *= 2;
    }
  }
  
  throw new Error(`Max retries reached. Last error: ${lastError.message}`);
}

// AsyncQueue for concurrency control
class AsyncQueue {
  constructor(concurrency = 1) {
    this.concurrency = concurrency;
    this.running = 0;
    this.queue = [];
  }
  
  async add(fn) {
    return new Promise((resolve, reject) => {
      this.queue.push({ fn, resolve, reject });
      this.next();
    });
  }
  
  async next() {
    if (this.running >= this.concurrency || this.queue.length === 0) {
      return;
    }
    
    this.running++;
    const { fn, resolve, reject } = this.queue.shift();
    
    try {
      const result = await fn();
      resolve(result);
    } catch (error) {
      reject(error);
    } finally {
      this.running--;
      this.next();
    }
  }
}

// Usage
const queue = new AsyncQueue(3); // 3 concurrent tasks

for (let i = 0; i < 10; i++) {
  queue.add(async () => {
    await new Promise(resolve => setTimeout(resolve, Math.random() * 1000));
    return `Task ${i} completed`;
  }).then(console.log);
}
```

## Pro Tips for Async Operations

1. **Always return promises from async functions**
   - Even if you're not using `await`, return the promise for proper chaining

2. **Use Promise.all for parallel operations**
   - When operations don't depend on each other, run them in parallel

3. **Handle errors at the appropriate level**
   - Don't catch errors too early if higher-level code needs to handle them

4. **Be careful with loops and async operations**
   - Use `for...of` with `await` for sequential execution
   - Use `Promise.all` with `map` for parallel execution

5. **Avoid unnecessary async/await**
   - Don't use async/await when simple promise chaining is clearer

6. **Remember that async functions always return promises**
   - Even if you return a non-promise value, it will be wrapped in a promise

7. **Use Promise.allSettled for operations that should all complete**
   - When you need results from all operations, even if some fail

8. **Consider AbortController for cancellable operations**
   ```javascript
   const controller = new AbortController();
   const { signal } = controller;
   
   fetch('https://api.example.com/data', { signal })
     .then(response => response.json())
     .then(data => console.log(data))
     .catch(error => {
       if (error.name === 'AbortError') {
         console.log('Fetch was aborted');
       } else {
         console.error('Error:', error);
       }
     });
   
   // Later, to abort the fetch:
   controller.abort();
   ```

## Gotchas for Async Operations

1. **Forgetting to await promises**
   ```javascript
   // Wrong
   async function processData() {
     const data = fetchData(); // Missing await!
     return data.result; // Will fail - data is a Promise, not the resolved value
   }
   
   // Correct
   async function processData() {
     const data = await fetchData();
     return data.result;
   }
   ```

2. **Not handling errors properly**
   ```javascript
   // Wrong - unhandled promise rejection
   async function processData() {
     const data = await fetchData(); // If this throws, the error propagates
     return process(data);
   }
   
   // Correct
   async function processData() {
     try {
       const data = await fetchData();
       return process(data);
     } catch (error) {
       console.error("Error processing data:", error);
       throw error; // Re-throw if needed
     }
   }
   ```

3. **Forgetting that async functions always return promises**
   ```javascript
   // This won't work as expected
   function getData() {
     let result;
     fetchData().then(data => {
       result = data; // This happens asynchronously
     });
     return result; // Will be undefined
   }
   
   // Correct approach
   async function getData() {
     return await fetchData();
   }
   ```

4. **Sequential vs parallel execution confusion**
   ```javascript
   // Sequential (slower)
   async function fetchAll() {
     const users = await fetchUsers();
     const posts = await fetchPosts();
     const comments = await fetchComments();
     return { users, posts, comments };
   }
   
   // Parallel (faster if operations are independent)
   async function fetchAll() {
     const [users, posts, comments] = await Promise.all([
       fetchUsers(),
       fetchPosts(),
       fetchComments()
     ]);
     return { users, posts, comments };
   }
   ```

5. **Async loops pitfalls**
   ```javascript
   // Wrong - forEach doesn't wait for async operations
   async function processItems(items) {
     items.forEach(async (item) => {
       await processItem(item); // These run in parallel and processItems() won't wait
     });
     console.log('All done!'); // This runs immediately, not after processing
   }
   
   // Correct - using for...of
   async function processItems(items) {
     for (const item of items) {
       await processItem(item);
     }
     console.log('All done!'); // This runs after all items are processed
   }
   ```

6. **Ignoring the returned promise**
   ```javascript
   // Wrong - ignoring the returned promise
   function handleClick() {
     processData(); // Async function, but we're not handling the promise
     showSuccessMessage(); // This runs before processData() completes
   }
   
   // Correct
   async function handleClick() {
     try {
       await processData();
       showSuccessMessage(); // This runs after processData() completes
     } catch (error) {
       showErrorMessage(error);
     }
   }
   ```