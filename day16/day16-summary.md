# Day 16 Summary

## Topic
JWT authentication basics.

## What was implemented
- Added `/login` endpoint.
- Returned a bearer token on successful login.
- Protected `POST`, `PUT`, and `DELETE /books`.
- Kept `GET` endpoints public.
- Added auth tests for success and failure cases.

## Main files
- `day07/auth.py`
- `day07/app.py`
- `day07/dtos.py`
- `day07/tests/test_app.py`

## Result
- The API now supports basic authenticated and unauthenticated flows.
