# Day 30 Summary

## Topic
Phase 3 checkpoint: RAG plus routing agent.

## Goal
Show that the RAG pipeline can work as a small agent that decides whether to retrieve documents or answer directly.

## Documents used
- Employees may work from home on Fridays.
- The office kitchen closes at 6 PM.
- All vacation requests must be approved by a manager.
- Passwords must be changed every 90 days.

## Routing logic
The prototype checks the question first.
- If the question matches the sample policy topics, it routes to retrieval.
- If the question is general small talk, it answers directly.
- If the question is outside the document scope, it declines instead of guessing.

## Example question 1: grounded question
Question:
- What is the password policy?

Expected output:
- The router sends the question to retrieval.
- The agent returns the matching policy document.
- The answer stays grounded in the documents.

## Example question 2: ungrounded question
Question:
- What is our PTO policy?

Expected output:
- The router does not find a strong document match.
- The agent declines with "I don't know based on the provided documents."
- This avoids a hallucinated answer.

## Good output example
- Question: What is the password policy?
- Router: retrieve
- Result: grounded answer from the policy documents

## Bad output example
- Question: What is our PTO policy?
- Router: decline
- Result: no unsupported guess, only a safe refusal

## Why this checkpoint matters
This proves the earlier RAG work can be turned into a small practical agent:
- it routes based on the question
- it retrieves only when needed
- it avoids answering when the docs do not support the question

## Limitation
This prototype uses simple keyword routing and cosine similarity. A production version would use better intent detection, stronger embeddings, and more robust confidence thresholds.

## Demo checklist
- Run two questions live.
- Show how the router decided.
- Show one grounded answer and one safe decline.
- Explain the main limitation and how production would improve it.
