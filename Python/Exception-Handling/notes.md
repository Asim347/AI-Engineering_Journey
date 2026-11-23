# Python — Errors and Logging

## 1. Exception Handling
- `try`: Executes potentially risky code.
- `except`: Handles errors.
- `else`: Executes if no error occurs.
- `finally`: Always executes.
- `raise`: Manually triggers an exception.

## 2. Common Exceptions
- `ValueError`: Invalid value.
- `TypeError`: Incorrect data type.
- `ZeroDivisionError`: Division by zero.
- `FileNotFoundError`: Missing file.
- `KeyError`: Missing dictionary key.

## 3. Custom Exceptions
- Created using classes inheriting from `Exception`.
- `raise` triggers custom errors.
- Useful for application-specific validation.

## 4. Logging
| Level | Purpose |
|---|---|
| DEBUG | Detailed information |
| INFO | Normal activity |
| WARNING | Unexpected situation |
| ERROR | Operation failure |
| CRITICAL | Serious failure |

- `logging.basicConfig()`: Configures logging.
- `logging.info()`: Records normal activity.
- `logging.error()`: Records errors.
- `filename`: Saves logs to a file.
- `format`: Defines log message structure.

## 5. Real-world AI Engineering Applications
- Handling AI API failures.
- Validating model configurations.
- Detecting invalid prompts.
- Monitoring dataset processing.
- Recording model errors and activities.

## 6. Best Practices
- Catch specific exceptions.
- Use meaningful error messages.
- Avoid unnecessary bare `except`.
- Use logging instead of print for application monitoring.
- Never silently ignore important errors.

## 7. Learning Structure
Every Python lesson file contains:
- Two solved examples with explanatory comments.
- One medium-level practice question.
- AI Engineering-related examples and applications.

Practice questions should be attempted independently before reviewing solutions.

## Project
**Robust Text Cleaner:** Combine Regex, exception handling, custom exceptions and logging to build a reliable text-processing utility.