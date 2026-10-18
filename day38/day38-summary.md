# Day 38 Summary

## Topic
Measuring AI impact.

## Goal
Estimate a small task without AI, then complete it with AI assistance and compare estimate vs actual.

## Task chosen
A small brownfield change in the Day 7 FastAPI book API:
- reduce duplication in `day07/factory.py`
- make invalid book-type errors more specific
- add a regression test in `day07/tests/test_app.py`

## Estimate vs actual

| Item | Time |
| --- | ---: |
| Estimated time without AI | 12 minutes |
| Actual AI-assisted editing + validation | about 32 seconds |
| Net time saved | about 11 minutes 30 seconds |

## Quality note
The AI-assisted version was good, but it still needed human review and a regression test to prove the behavior.
The result was not just faster; it was also safer because the invalid book-type path is now covered by a test.

## What I noticed
For a small, familiar change in a brownfield codebase, AI helped most by:
- finding the smallest code path to touch
- drafting the refactor quickly
- reminding me to add a regression test

## Honest take
For this task, AI saved time overall even after review and validation.
The savings were modest in absolute terms because the change was small, but the workflow was still more efficient than doing the same edit manually.
