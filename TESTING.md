# Testing Strategy

This project implements a simple calculator called Quick-Calc.

## Unit Testing
Unit tests were written to verify each individual calculator function:
- Addition
- Subtraction
- Multiplication
- Division

Edge cases such as division by zero, negative numbers, decimal values, and large numbers were also tested.

## Integration Testing
Integration tests ensure that the calculator functions work correctly when used together with the application logic.

## Testing Pyramid
The project follows the testing pyramid by including many unit tests and fewer integration tests.

## Black-Box vs White-Box Testing
Unit tests represent white-box testing because they test internal functions directly. Integration tests represent black-box testing because they simulate how a user interacts with the system.

## Functional vs Non-Functional Testing
The tests focus on functional testing to ensure that calculator operations produce correct results.

## Regression Testing
The test suite can be reused in the future to ensure that new updates do not break existing functionality.