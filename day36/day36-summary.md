# Day 36 Summary

## Topic
Agentic SDLC mapping.

## Goal
See where AI fits across the full software delivery lifecycle, not just at the coding step.

## SDLC AI-fit map

### 1. Requirements
AI helps a little today.
It can summarize existing tickets, extract candidate user stories from code or tests, and turn rough notes into a clearer spec draft.
It cannot reliably decide business-critical acceptance criteria or resolve conflicting stakeholder priorities.

### 2. Design
AI helps moderately today.
It can propose architecture options, sketch module boundaries, draft sequence diagrams, and point out common tradeoffs.
It still needs a human to choose the design that matches the system constraints, team skill set, and long-term maintenance goals.

### 3. Code
AI helps a lot today.
It can generate feature scaffolds, write repetitive boilerplate, refactor small slices, and produce example implementations from nearby code.
It is best when the prompt includes exact files, constraints, and existing patterns.

### 4. Test
AI helps a lot today.
It can generate edge-case unit tests from a function signature, turn a bug report into a regression test, and suggest missing branches.
It cannot guarantee the tests reflect the right business behavior without human review.

### 5. Review
AI helps moderately today.
It can flag style issues, suspicious logic, missing checks, and likely regressions in a pull request.
It cannot be the final reviewer for correctness because it may miss domain context or overreport issues that are intentional.

### 6. Deploy
AI helps a little to moderately today.
It can draft Dockerfiles, pipeline YAML, and deployment checklists, and it can explain missing config.
It cannot safely choose production settings on its own because it does not know the real subscription, quota, security, or release constraints.

### 7. Monitor
AI helps the least today.
It can summarize logs, cluster recurring errors, and suggest likely causes.
It cannot observe the live system directly or know whether an anomaly is truly acceptable without real telemetry, alert context, and operator judgment.

## Stage where AI helps least today
Monitoring.
The reason is simple: AI can interpret evidence, but it cannot replace actual runtime signals, production access, or incident ownership.

## Presentation point
The best current use of AI is as an accelerator inside each stage, not as the decision-maker for the stages that carry business or operational risk.
