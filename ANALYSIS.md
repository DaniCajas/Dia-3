# Analysis

## Objective

Refactor the Gilded Rose inventory update logic while improving
maintainability and readability.

## Approach

The solution uses a Strategy-style architecture where each item type
delegates its behaviour to a dedicated handler.

## Benefits

- Reduced cyclomatic complexity.
- Better separation of responsibilities.
- Easier extension for future item types.
- Improved unit test isolation.

## Trade-offs

- More classes than a single-method solution.
- Slightly higher structural complexity.

## Conclusion

The chosen architecture prioritizes maintainability and extensibility over
compactness while preserving the behaviour required by the kata.
