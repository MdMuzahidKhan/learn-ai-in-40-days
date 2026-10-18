# Day 29 Summary

## Topic
Responsible AI use at work.

## Org policy check
I searched the workspace for an AI usage policy and did not find a dedicated org policy file. Because of that, this checklist uses conservative best practices that are safe for normal dev work.

## Personal AI-use checklist
1. Never paste customer PII, secrets, passwords, tokens, API keys, or private source code into a public AI tool.
2. Use AI for help, not final truth. Always review the output before using it in code, docs, or decisions.
3. Verify AI-generated code before committing it.
4. Verify AI-cited facts, APIs, library names, and legal or compliance claims against trusted sources.
5. Treat AI output as a draft, not as production-ready work.
6. Do not let AI make security decisions without human review.
7. Keep a human in the loop for code review, approvals, and customer-facing text.
8. Disclose AI-assisted work where company policy or project rules require it.
9. Check that any copied code does not violate license, policy, or confidentiality rules.
10. When in doubt, ask a teammate or manager before using AI on sensitive work.

## Why these items matter
- PII and secrets can leak if they are pasted into the wrong tool.
- AI can sound correct even when it is wrong.
- Generated code can compile but still contain bugs, insecure logic, or bad assumptions.
- Facts, APIs, and citations must be real before they are used in work.
- Human review is still required for quality, safety, and accountability.

## Three items to present
### 1. Never paste sensitive data into a public tool
This matters because once data leaves the company boundary, it can be stored, logged, or exposed in ways you do not control.

### 2. Always review AI-generated code before committing it
This matters because code can look correct while still being buggy, insecure, or inconsistent with project standards.

### 3. Verify AI-cited facts and APIs actually exist
This matters because AI can hallucinate names, functions, or references that sound real but are not valid.

## Gap between checklist and org policy
No org-specific AI policy file was found in the workspace, so there is no direct policy text to compare against. If an internal policy exists elsewhere, the checklist should be updated to match it.

## Presentation checklist
- Walk through the three items above.
- Explain why each item matters.
- Mention that no org AI policy file was found in the repo.
- State one rule you will personally follow at work.
