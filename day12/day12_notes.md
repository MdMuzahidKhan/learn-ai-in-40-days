# Day 12 Clean Code and SOLID Notes

## Code smell in the before version
The before version had duplicated dictionary creation, hardcoded values like "physical" and "ebook", and validation mixed with object creation logic.

## SOLID principles applied

### 1. Single Responsibility Principle (SRP)
In the refactored version, book type validation is separated into `_normalize_book_type()`, and object creation is separated into `_build_book_data()`.
This means each method has one clear job.

### 2. Open/Closed Principle (OCP)
The refactored version is easier to extend for new book types because supported types are collected in `SUPPORTED_BOOK_TYPES`.
We can add new supported types with less duplication and fewer code changes.

### 3. Dependency Inversion / better abstraction direction
The refactored code now depends on small helper methods instead of mixing all logic inside one large method.
This reduces direct dependence on low-level branching logic in the main creation function.

## Readability improvement not directly SOLID
Variable names are clearer now, such as `book_input`, `normalized_book_type`, and `book_type_value`.
Also, magic strings were moved into named constants, which makes the code easier to read and maintain.