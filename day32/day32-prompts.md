# Day 32 Prompt Log

## Initial Explicit-Context Prompt

Context: I am working in an existing FastAPI + React project.

Relevant files:
- Backend controller: day07/app.py
- Backend service: day07/service.py
- Tests: day07/tests/test_app.py
- Frontend UI: day14/app.js

Project structure:
- app.py should stay thin and only handle routing
- service.py should contain business logic
- tests should follow the existing pytest style already used in test_app.py
- frontend should follow the existing React patterns already used in app.js

Task:
Add a search books by author feature.

Requirements:
1. Keep the existing `/books` endpoint.
2. Add an optional `author` query parameter.
3. Implement case-insensitive filtering in service.py.
4. Add tests for exact match, case-insensitive match, and no match.
5. Update the frontend to let users search by author.
6. Keep reset behavior working so all books reload after clearing the author filter.

Constraint:
Do not create a new endpoint like `/books/search`. Keep the feature inside the existing `/books` flow.

Expected output:
- updated day07/app.py
- updated day07/service.py
- updated day07/tests/test_app.py
- updated day14/app.js
- minimal, project-consistent changes only

---

## Iteration Prompt 1: Backend and Tests

Review the backend draft again.

Check these carefully:
- Is the indentation correct in service.py?
- Is the author filter logic inside get_all_books correct?
- Does app.py pass the `author` query parameter correctly?
- Do the new tests match the style of the existing tests?
- Are exact match, case-insensitive match, and no-match all covered?

Only suggest changes needed to make the backend correct and consistent with this repo.

---

## Iteration Prompt 2: Frontend and Conventions

Now review the frontend draft again.

Check these carefully:
- Does the author search input follow the current UI structure in app.js?
- Does clicking reset clear the author filter and reload all books?
- Does the frontend call the backend with `/books?author=...` correctly?
- Does the feature fit the existing Day 14 patterns without unnecessary redesign?

Only suggest changes needed to keep the UI behavior clean and consistent.

---

## Biggest Prompting Improvement

The most useful change was giving:
- exact file names
- exact architecture roles
- exact API constraint

This prevented the assistant from guessing the structure and helped it stay inside the existing project design.
