# Day 19 Summary

## Topic
Debugging and structured logging.

## What was implemented
- Seeded and fixed a bug in duplicate-title validation.
- Added structured logging across controller, service, and repository layers.
- Used `INFO`, `WARNING`, and `ERROR` levels appropriately.
- Verified the backend tests still passed after the fix.

## Main files
- `day07/app.py`
- `day07/service.py`
- `day07/repository.py`

## Result
- The API now has clearer traceability for normal flow and failures.
