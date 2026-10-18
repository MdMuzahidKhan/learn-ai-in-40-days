# Day 39 Summary

## Topic
Team tools and workflow walkthrough.

## Goal
Trace a small ticket from pick-up to done using the real workflow where possible.

## What I could verify in this workspace
The repository has a clear inner workflow already:
- code changes in the relevant day folder
- validation with `pytest`
- GitLab CI in `.gitlab-ci.yml`
- integration history in the Day 14 and Day 20 notes

## What I could not do here
I could not actually shadow your org's ticketing system, branch naming rules, review tool, or deployment pipeline from this workspace.
So I cannot honestly claim a real end-to-end ticket lifecycle in the org tools themselves.

## Closest local proxy workflow
For the small brownfield ticket in Day 7, the lifecycle looked like this:
- pick up a narrow bug fix in `day07/service.py` / `day07/factory.py`
- make the smallest code change needed
- add or update a regression test in `day07/tests/test_app.py`
- run `pytest -q tests/test_app.py`
- keep the repo's existing FastAPI and repository/service style intact

## One convention that differed from a newer training sandbox
The repo expects tests to be run from the Day 7 folder with the Day 7 test path, not from a fresh single-project sandbox layout.
The CI file also reflects that convention by changing into `day07` before running `pytest`.

## Presentation note
If I had org tool access, the missing pieces to show would be:
- ticket creation and assignment
- branch creation from the ticket
- pull request review
- merge approval
- CI/CD deploy step
- post-deploy verification

## Honest conclusion
I can document the local code/test/CI side of the workflow here, but the real org ticket-to-deploy walkthrough needs access to your ticketing and deployment tools.
