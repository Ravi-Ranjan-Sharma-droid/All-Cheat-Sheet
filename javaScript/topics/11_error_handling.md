# Error Handling

## Try-Catch-Finally

```javascript
// Basic try-catch
try {
  // Code that might throw an error
  const result = riskyOperation();
  console.log(result);
} catch (error) {
  // Handle the error
  console.error("An error occurred:", error.message);
}

// Try-catch-finally
try {
  const connection = openDatabaseConnection();
  const data = connection.query("SELECT * FROM users");
  processData(data);
} catch (error) {
  console.error("Database error:", error.message);
  // Handle specific error types
  if (error instanceof ConnectionError) {
    notifyAdmin("Database connection failed");
  } else if (error instanceof QueryError) {
    logQueryError(error);
  }
} finally {
  // This block always executes, regardless of whether an error occurred
  if (connection) {
    connection.close(); // Clean up resources
  }
  console.log("Operation completed");
}

// Nested try-catch blocks
try {
  try {
    riskyOperation();
  } catch (innerError) {
    console.log("Inner catch:", innerError.message);
    if (innerError.critical) {
      throw innerError; // Re-throw to outer catch
    }
  }
} catch (outerError) {
  console.log("Outer catch:", outerError.message);
}
```

## Throwing Custom Errors

```javascript
// Throwing basic errors
function divide(a, b) {
  if (b === 0) {
    throw new Error("Division by zero is not allowed");
  }
  return a / b;
}

// Using built-in error types
function validateUser(user) {
  if (!user) {
    throw new TypeError("User object is required");
  }
  
  if (!user.name) {
    throw new ReferenceError("User name is missing");
  }
  
  if (user.age < 0) {
    throw new RangeError("Age cannot be negative");
  }
}

// Custom error classes
class ValidationError extends Error {
  constructor(message, field) {
    super(message);
    this.name = "ValidationError";
    this.field = field;
    this.date = new Date();
    
    // Capture stack trace (Node.js and modern browsers)
    if (Error.captureStackTrace) {
      Error.captureStackTrace(this, ValidationError);
    }
  }
  
  toString() {
    return `${this.name}: ${this.message} (${this.field})`;
  }
}

class DatabaseError extends Error {
  constructor(message, query) {
    super(message);
    this.name = "DatabaseError";
    this.query = query;
  }
}

// Using custom errors
function validateEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(email)) {
    throw new ValidationError("Invalid email format", "email");
  }
  return true;
}

try {
  validateEmail("invalid-email");
} catch (error) {
  if (error instanceof ValidationError) {
    console.error(`Validation failed for ${error.field}: ${error.message}`);
  } else {
    console.error("An unexpected error occurred:", error);
  }
}
```

## Async Error Handling

```javascript
// Promise error handling
fetchData()
  .then(data => {
    return processData(data);
  })
  .then(result => {
    displayResult(result);
  })
  .catch(error => {
    // Handles errors from fetchData, processData, or displayResult
    console.error("Operation failed:", error);
  })
  .finally(() => {
    hideLoadingIndicator();
  });

// Error handling with async/await
async function fetchUserData(userId) {
  try {
    const response = await fetch(`/api/users/${userId}`);
    
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    
    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Failed to fetch user data:", error);
    // Re-throw or return a default value
    throw new Error(`User data fetch failed: ${error.message}`);
  }
}

// Combining multiple async operations with error handling
async function loadDashboard() {
  try {
    const [userData, statsData, notificationsData] = await Promise.all([
      fetchUserData(),
      fetchStats(),
      fetchNotifications()
    ]);
    
    renderDashboard(userData, statsData, notificationsData);
  } catch (error) {
    showErrorMessage("Failed to load dashboard");
    console.error(error);
  } finally {
    hideLoadingSpinner();
  }
}
```

## Error Handling Patterns

```javascript
// Error boundary pattern
class ErrorBoundary {
  constructor(errorHandler) {
    this.errorHandler = errorHandler;
  }
  
  async execute(fn) {
    try {
      return await fn();
    } catch (error) {
      this.errorHandler(error);
      return null;
    }
  }
}

const boundary = new ErrorBoundary(error => {
  console.error("Operation failed:", error);
  showUserFriendlyMessage();
});

boundary.execute(() => fetchAndProcessData());

// Fallback pattern
async function fetchDataWithFallback(primaryUrl, fallbackUrl) {
  try {
    return await fetchData(primaryUrl);
  } catch (error) {
    console.warn(`Primary source failed: ${error.message}. Trying fallback...`);
    try {
      return await fetchData(fallbackUrl);
    } catch (fallbackError) {
      console.error("Both primary and fallback sources failed");
      throw new Error("All data sources unavailable");
    }
  }
}

// Retry pattern
async function fetchWithRetry(url, options = {}, maxRetries = 3) {
  let lastError;
  
  for (let attempt = 0; attempt < maxRetries; attempt++) {
    try {
      return await fetch(url, options);
    } catch (error) {
      console.warn(`Attempt ${attempt + 1} failed: ${error.message}`);
      lastError = error;
      
      // Wait before next retry (with exponential backoff)
      await new Promise(resolve => setTimeout(resolve, 1000 * Math.pow(2, attempt)));
    }
  }
  
  throw new Error(`All ${maxRetries} attempts failed. Last error: ${lastError.message}`);
}
```

## Global Error Handling

```javascript
// Browser: Global error handler
window.addEventListener('error', (event) => {
  console.error('Global error:', event.error);
  showErrorNotification('An unexpected error occurred');
  // Optionally send error to analytics or logging service
  sendErrorToAnalytics(event.error);
  
  // Prevent default browser error handling
  event.preventDefault();
});

// Browser: Unhandled promise rejection handler
window.addEventListener('unhandledrejection', (event) => {
  console.error('Unhandled promise rejection:', event.reason);
  showErrorNotification('An async operation failed');
  sendErrorToAnalytics(event.reason);
});

// Node.js: Global error handlers
process.on('uncaughtException', (error) => {
  console.error('Uncaught exception:', error);
  // Log error, notify monitoring service, etc.
  logErrorToService(error);
  
  // Gracefully shut down the application
  gracefulShutdown();
});

process.on('unhandledRejection', (reason, promise) => {
  console.error('Unhandled rejection at:', promise, 'reason:', reason);
  // Log error, notify monitoring service, etc.
  logErrorToService(reason);
});
```

## Error Logging and Monitoring

```javascript
// Basic error logging function
function logError(error, context = {}) {
  const errorLog = {
    message: error.message,
    name: error.name,
    stack: error.stack,
    timestamp: new Date().toISOString(),
    context,
    userAgent: navigator.userAgent,
    url: window.location.href
  };
  
  // Send to logging service
  fetch('/api/logs/error', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(errorLog)
  }).catch(e => console.error('Failed to log error:', e));
}

// Usage
try {
  riskyOperation();
} catch (error) {
  logError(error, { 
    operation: 'riskyOperation',
    userId: currentUser.id,
    additionalData: 'relevant context'
  });
  showUserFriendlyError();
}

// Error monitoring with severity levels
const ErrorSeverity = {
  INFO: 'info',
  WARNING: 'warning',
  ERROR: 'error',
  CRITICAL: 'critical'
};

function monitorError(error, severity = ErrorSeverity.ERROR, context = {}) {
  // Add additional diagnostic information
  const diagnosticInfo = {
    memory: performance.memory ? performance.memory.usedJSHeapSize : 'unavailable',
    timing: performance.timing ? performance.timing.domComplete : 'unavailable',
    // Add other relevant metrics
  };
  
  const errorReport = {
    message: error.message,
    stack: error.stack,
    severity,
    context,
    diagnosticInfo,
    timestamp: Date.now()
  };
  
  // Send to monitoring service
  sendToMonitoringService(errorReport);
  
  // For critical errors, also notify developers
  if (severity === ErrorSeverity.CRITICAL) {
    notifyDevelopersImmediately(errorReport);
  }
}
```

## Pro Tips for Error Handling

1. **Be specific with error messages**
   - Include details about what went wrong and possible solutions
   - Error messages should help both users and developers

2. **Use appropriate error types**
   - Create custom error classes for different categories of errors
   - Extend built-in error types when appropriate

3. **Don't swallow errors**
   - Always handle or propagate errors
   - Avoid empty catch blocks

4. **Log errors with context**
   - Include relevant information about the state when the error occurred
   - Add user ID, session information, and other contextual data

5. **Implement global error handling**
   - Catch unhandled errors and promise rejections
   - Provide fallback UI for unexpected errors

6. **Use error boundaries in component-based frameworks**
   - Isolate errors to prevent entire application crashes
   - Provide fallback UI for components that fail

7. **Consider error severity**
   - Not all errors are equal - some require immediate attention
   - Implement different handling strategies based on severity

8. **Validate inputs early**
   - Catch potential errors at the source
   - Provide clear validation messages

9. **Use feature detection instead of error handling when possible**
   - Check if a feature exists before trying to use it
   - Avoid try-catch for control flow

10. **Implement circuit breakers for external services**
    - Temporarily stop calling services that repeatedly fail
    - Automatically retry after a cooldown period

## Gotchas in Error Handling

1. **Using throw outside of a function**
   ```javascript
   // This will cause an immediate error that can't be caught locally
   if (somethingBad) {
     throw new Error("Something bad happened");
   }
   
   // Better approach
   function checkCondition() {
     if (somethingBad) {
       throw new Error("Something bad happened");
     }
   }
   
   try {
     checkCondition();
   } catch (error) {
     // Handle error
   }
   ```

2. **Forgetting that async errors need to be caught differently**
   ```javascript
   // This won't catch the error
   try {
     fetchData().then(data => processData(data));
   } catch (error) {
     console.error(error); // This won't execute for promise rejections
   }
   
   // Correct approaches
   // 1. Using .catch()
   fetchData()
     .then(data => processData(data))
     .catch(error => console.error(error));
   
   // 2. Using async/await
   async function handleData() {
     try {
       const data = await fetchData();
       processData(data);
     } catch (error) {
       console.error(error);
     }
   }
   ```

3. **Not checking for specific error types**
   ```javascript
   try {
     // Multiple operations that could fail for different reasons
     validateInput(data);
     processData(data);
     saveResult(result);
   } catch (error) {
     // Generic error handling doesn't distinguish between error types
     showErrorMessage("An error occurred");
   }
   
   // Better approach
   try {
     validateInput(data);
     processData(data);
     saveResult(result);
   } catch (error) {
     if (error instanceof ValidationError) {
       showValidationError(error.field, error.message);
     } else if (error instanceof DatabaseError) {
       showDatabaseError("Could not save result");
       logError(error);
     } else {
       showGenericError("An unexpected error occurred");
       reportCriticalError(error);
     }
   }
   ```

4. **Throwing non-Error objects**
   ```javascript
   // Bad practice
   throw "Something went wrong"; // Throwing a string
   throw 404; // Throwing a number
   
   // Good practice
   throw new Error("Something went wrong");
   throw new HttpError(404, "Resource not found");
   ```

5. **Losing the stack trace**
   ```javascript
   // This loses the original stack trace
   try {
     riskyOperation();
   } catch (error) {
     throw new Error("Operation failed: " + error.message);
   }
   
   // Better approach - preserve the stack trace
   try {
     riskyOperation();
   } catch (error) {
     const newError = new Error("Operation failed: " + error.message);
     newError.stack = error.stack;
     newError.originalError = error;
     throw newError;
   }
   
   // Or even better, use the cause property (ES2022)
   try {
     riskyOperation();
   } catch (error) {
     throw new Error("Operation failed", { cause: error });
   }
   ```

6. **Inconsistent error handling across async and sync code**
   ```javascript
   // Inconsistent approach
   function syncOperation() {
     try {
       // Synchronous code
       return processData(data);
     } catch (error) {
       logError(error);
       return null;
     }
   }
   
   function asyncOperation() {
     return fetchData()
       .then(data => processData(data))
       .catch(error => {
         showErrorDialog(error); // Different handling strategy
         throw error; // Re-throwing
       });
   }
   
   // Better approach - consistent error handling strategy
   function handleError(error, operation) {
     logError(error, { operation });
     notifyUser("Operation failed");
     return null; // Or a default value
   }
   
   function syncOperation() {
     try {
       return processData(data);
     } catch (error) {
       return handleError(error, "syncOperation");
     }
   }
   
   async function asyncOperation() {
     try {
       const data = await fetchData();
       return processData(data);
     } catch (error) {
       return handleError(error, "asyncOperation");
     }
   }
   ```