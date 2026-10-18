# Day 26 Summary

## Topic
AI Agents, ReAct, and memory.

## What is an agent?
An AI agent is a system that can think about a task, use a tool, see the result, and then decide what to do next.

## What is ReAct?
ReAct means Reason → Act → Observe.

- Reason: the agent thinks about what it needs to do.
- Act: the agent uses a tool.
- Observe: the agent reads the tool result.
- Then it reasons again and chooses the next step.

## Example: booking a flight
1. Reason: I need to book a flight from Hyderabad to Bangalore next Friday.
2. Act: Search for available flights.
3. Observe: See the flight options, prices, and times.
4. Reason again: Choose the best option based on price and timing.
5. Act: Book the selected flight.
6. Observe: Confirm the booking number and details.

## Why does an agent need Observe?
Observe is important because the agent cannot know what happened after a tool call unless it reads the result. Without Observe, the agent would guess instead of making the next decision using real data.

## Three types of memory in an agent

### 1. Short-term memory / context memory
This is the current working context for the task.
Example: the current trip details like source, destination, and travel date.

### 2. Long-term memory / persisted memory
This is saved information that stays available later.
Example: the user prefers aisle seats and budget airlines.

### 3. Tool-call history
This is the record of previous tool actions and results.
Example: the agent already searched flights and saw three options, so it does not need to search again from scratch.

## Framework note
A framework like LangGraph helps manage the agent loop, tool calls, state, and memory more cleanly.

## Presentation checklist
- Explain the ReAct loop step by step.
- Walk through the flight booking example.
- Show the three memory types with examples.
- Explain why Observe is needed and why Reason → Act alone is not enough.