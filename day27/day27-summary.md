# Day 27 Summary

## Topic
Multi-agent patterns.

## What is a multi-agent system?
A multi-agent system is a setup where more than one AI agent works on the same task. Instead of one agent doing everything, the work is divided into smaller roles.

## Why not use one agent?
Some tasks are too broad for one agent to do well. A single agent may miss details, mix different responsibilities, or take more time trying to do everything alone.

For a task like pull request review, different skills are needed:
- understanding what the code change does
- checking code style and readability
- checking tests, risks, and missing coverage

Because of that, splitting the work into multiple agents is easier to manage.

## Example task
Review a pull request.

## Multi-agent design
### 1. Coordinator Agent
Input:
- pull request link or diff
- changed files
- task goal

Role:
- receives the pull request
- decides which specialist agents should run
- collects the outputs
- prepares the final review summary

Output:
- combined review report

### 2. Code Understanding Agent
Input:
- pull request diff
- changed files

Role:
- reads the code changes
- explains what behavior changed
- identifies the main logic changes

Output:
- code change summary
- important files/functions affected

### 3. Style and Quality Agent
Input:
- changed code
- coding standards or style expectations

Role:
- checks formatting, readability, naming, duplication, and code quality
- flags maintainability concerns

Output:
- style findings
- quality suggestions

### 4. Test and Risk Agent
Input:
- changed code
- existing tests
- test coverage expectations

Role:
- checks whether tests cover the change
- identifies missing test cases
- highlights possible regression risks

Output:
- test gaps
- risk findings

## Handoffs
1. The Coordinator Agent receives the PR.
2. It sends the code diff to the Code Understanding Agent.
3. It sends the same PR to the Style and Quality Agent.
4. It sends the changed behavior and tests to the Test and Risk Agent.
5. All specialist agents return their findings to the Coordinator Agent.
6. The Coordinator Agent merges the results into one final review.

## One risk in multi-agent systems
A common risk is that cost and latency increase because multiple agents are running instead of one.

## One mitigation
Use a coordinator that only calls specialist agents when needed. For example, if a PR only changes documentation, the test agent may not need to run.

## Why this split makes sense
This split works because each agent has one clear job. That improves focus and makes the final output easier to understand. It also reduces the chance that one agent misses important details while trying to do too much.

## Presentation checklist
- Explain why PR review is too broad for one agent.
- Walk through each agent role.
- Explain what input each agent gets.
- Explain what output each agent returns.
- Name the risk: cost and latency increase.
- Explain the mitigation: coordinator decides which agents really need to run.
