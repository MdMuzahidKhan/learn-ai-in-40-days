# Day 15 Summary

## Topic
Layered backend architecture and dependency injection.

## What was implemented
- Split the backend into Controller -> Service -> Repository.
- Added DTOs for requests and responses.
- Added dependency injection wiring for the service and repository.
- Kept route handlers thin and moved business rules into the service layer.

## Main files
- `day07/app.py`
- `day07/service.py`
- `day07/repository.py`
- `day07/dependencies.py`
- `day07/dtos.py`

## Result
- The codebase became more modular and easier to maintain.
