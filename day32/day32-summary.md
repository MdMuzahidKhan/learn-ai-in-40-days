# Day 32 Summary

## Topic
Effective AI-assisted coding.

## Goal
Redo the Day 31 feature with better context and better iteration, instead of accepting the first draft.

## Feature used for comparison
Search books by author in the Phase 2 project.

## v2 implementation summary
The same author-search feature was treated as a second version.

This time, the assistant was given:
- exact backend files
- exact frontend file
- project architecture expectations
- endpoint constraints
- test expectations

Then the output was refined in at least two iterations instead of accepting the first response.

## Explicit context given to the assistant
- Backend files:
  - day07/app.py
  - day07/service.py
  - day07/tests/test_app.py
- Frontend file:
  - day14/app.js
- Architecture:
  - keep controller logic in app.py
  - keep business logic in service.py
  - use the existing `/books` endpoint
- Constraint:
  - use `GET /books?author=...`
  - do not create a new endpoint
- Test requirements:
  - exact match
  - case-insensitive match
  - no match

## Iteration 1
The first refinement focused on backend correctness and test shape.

What was checked:
- indentation in service.py
- author filter logic
- correct route signature in app.py
- test coverage in test_app.py

Result:
- the backend logic became correct
- the tests matched the existing file style
- the feature stayed inside the current architecture

## Iteration 2
The second refinement focused on frontend behavior and project conventions.

What was checked:
- author input UI
- reset button behavior
- API query parameter usage
- consistency with existing Day 14 UI patterns

Result:
- the frontend search flow became cleaner
- reset properly reloads the full books list
- the feature matched the existing app structure better

## v1 vs v2 comparison

### 1. Correctness
- v1: working idea, but the service-layer draft had indentation mistakes and needed manual correction.
- v2: the backend logic was more correct because the assistant had explicit file-level context and constraints.

### 2. Adherence to project conventions
- v1: the assistant needed more human correction to stay inside the current `/books` flow.
- v2: the assistant followed the existing controller-service structure more closely.

### 3. Need for manual fixes
- v1: more manual cleanup was needed in formatting, architecture decisions, and frontend flow checking.
- v2: fewer manual fixes were needed because the prompts were more specific.

## Biggest context change
The single biggest improvement was giving the assistant:
- exact file names
- exact architecture expectations
- one strict API constraint: keep the feature inside the existing `/books` endpoint

This reduced ambiguity and improved the result.

## Files involved in v2
- day07/app.py
- day07/service.py
- day07/tests/test_app.py
- day14/app.js

## Final result
The v2 feature is more reliable because it was guided with context and improved through iteration, not accepted by luck.

## Presentation checklist
- Show Day 31 as v1 and Day 32 as v2.
- Explain the same feature was used for both.
- Show what changed in the prompting process.
- Compare correctness, conventions, and manual fixes.
- Name the biggest improvement: explicit context and endpoint constraint.
