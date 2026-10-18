# Day 31 Summary

## Topic
AI coding assistant overview.

## Feature implemented
Added a search books by author feature to the Phase 2 project.

## Files touched
- day07/app.py
- day07/service.py
- day07/tests/test_app.py
- day14/app.js

## What the AI assistant got right
1. It identified the correct backend and frontend files to update.
2. It suggested adding the filter in the existing books flow instead of creating a large new feature.
3. It helped generate test cases for exact match, case-insensitive match, and no match.

## What the AI assistant got wrong or missed
1. It produced a first draft in the service layer with broken indentation that needed manual correction.
2. It did not fully reason about the existing frontend flow until the current UI was reviewed carefully.
3. It still needed human judgment to keep the feature small and consistent with the current controller-service structure.

## Manual corrections needed
- Fixed the service formatting and verified the author filter logic manually.
- Reviewed the route design and kept author search inside the existing `/books` endpoint.
- Checked the frontend flow to make sure reset behavior still reloads the full list.

## One surprising behavior
The assistant was fast at generating a working draft across backend and frontend, but it still introduced a small structural mistake in otherwise simple code.

## Demo checklist
- Show the author search working in the UI.
- Show the API filtering books by author.
- Share the AI scorecard.
