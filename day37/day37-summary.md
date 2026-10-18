# Day 37 Summary

## Topic
AI + brownfield / legacy code.

## Goal
See where AI struggles when the codebase is already large, layered, and full of existing conventions.

## Codebase used
The Day 7 FastAPI book API.

## Small change made
I added a tiny normalization helper in `day07/service.py` so blank author filters are treated as no filter instead of accidentally running through the substring search path.

I also added a regression test in `day07/tests/test_app.py` to confirm that a whitespace-only author query returns the full book list.

## What was harder than the toy projects
- The code already had controller, service, repository, auth, DTO, and test layers, so one small change had to respect the existing structure.
- I had to check how the service layer, route layer, and tests already fit together before changing anything.
- The repo already had established behavior for login and book filtering, so a small edit could easily break an existing expectation.

## Friction notes
- The assistant needed tighter file-level context than on the earlier toy examples.
- The existing code style was not uniform everywhere, so it was easy to over-assume patterns that were not actually used.
- The brownfield change was small, but proving it was safe required reading the surrounding test file and validating the full API test suite.

## Technique that helped
Pointing the assistant at specific files instead of the whole repo kept the context manageable.
For this change, the useful anchors were:
- `day07/app.py`
- `day07/service.py`
- `day07/tests/test_app.py`

## Verification
I ran the Day 7 API tests after the change, and they passed.

## Presentation point
AI is still useful on legacy code, but it works best when the task is narrow, the relevant files are explicit, and every behavioral change is backed by a regression test.
