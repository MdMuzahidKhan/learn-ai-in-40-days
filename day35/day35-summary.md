# Day 35 Summary

## Topic
AI for documentation.

## Goal
Use AI to speed up docs without letting inaccuracies slip through.

## Project documented
The Day 7 FastAPI book API.

## Documentation updated
- Added a project README in `day07/README.md`
- Added route docstrings in `day07/app.py`
- Added a code comment in `day07/service.py`

## Inaccuracy caught and fixed
I initially described the author filter as an exact match.
That was wrong.

The actual code in `day07/service.py` does a case-insensitive substring match, so `author=john` can match `John Smith`.

## What I verified
I checked the docs against the real code for:
- login behavior
- required bearer auth on write endpoints
- author filtering
- duplicate-title handling
- in-memory storage behavior

## Habit to keep
Always verify example requests and response fields against the running code or tests before trusting AI-generated docs.
