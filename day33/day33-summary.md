# Day 33 Summary

## Topic
AI for code review and debugging.

## Goal
Use AI as a second pair of eyes and verify its findings before trusting them.

## Exercise
I created a small code-review target in `day33/review_target.py` and seeded 3 issues into it:
- a missing null check
- a logic error
- a style/convention violation

## What the review found
- Missing null check: found
- Logic error: found
- Style / convention violation: found
- False positives: none

## Why the findings were real
Each flagged issue was checked by:
- reproducing the behavior
- reading the exact line in the code
- comparing it to the intended project pattern

## One rule I will use at work
I will verify any AI-raised issue by tracing the code path and reproducing the behavior before I trust the result.
