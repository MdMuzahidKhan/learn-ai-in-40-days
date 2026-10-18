# Day 11 Summary

## Topic
Repository pattern and factory pattern.

## What was implemented
- Extracted book storage into a repository abstraction.
- Added `InMemoryBookRepository`.
- Added `BookFactory` to centralize book object creation.
- Reduced direct data access inside route handlers.

## Main files
- `day07/repository.py`
- `day07/factory.py`
- `day07/app.py`

## Result
- The API became easier to test and refactor.
