# Day 33 Report

## Topic
AI for code review and debugging.

## Review target
I created a small code-review target in `day33/review_target.py` and seeded 3 issues into it:
- missing null check
- logic error
- style/convention violation

## Bugs seeded vs found
### 1. Missing null check
- Seeded: `author` can be `None`, but the code calls `author.strip()` without checking.
- Found: Yes.
- Why it matters: this would crash if the caller passes `None`.

### 2. Logic error
- Seeded: the filter checks `book["title"]` instead of `book["author"]`.
- Found: Yes.
- Why it matters: the function would return the wrong books even when the author query is valid.

### 3. Style / convention violation
- Seeded: `print(...)` is used in the function instead of proper logging or quiet library behavior.
- Found: Yes.
- Why it matters: debug printing in production code is noisy and inconsistent with the project style.

## False positives
- None found in this small exercise.

## How to verify a flagged issue before trusting it
1. Reproduce the behavior with a simple input.
2. Trace the exact line in the code.
3. Check whether the code matches the project convention and expected behavior.
4. Only then treat it as a real issue.

## Presentation checklist
- Present the three seeded bugs.
- Show the issues the review caught.
- Mention that there were no false positives.
- Explain how each issue was verified before trusting it.
