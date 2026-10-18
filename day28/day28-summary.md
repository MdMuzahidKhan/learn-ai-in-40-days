# Day 28 Summary

## Topic
AI safety and limitations.

## Example 1: Hallucinated legal citations
In the Avianca case, lawyers used ChatGPT to help draft a legal brief. The problem was that the model produced fake legal citations that looked real but were not actually valid.

What went wrong:
- The AI generated convincing but false citations.
- The lawyers did not verify the citations before filing.
- The final brief included invented legal references.

Why it went wrong:
- LLMs generate text that sounds plausible, not text that is always true.
- The model was not grounded in a trusted legal source.
- Humans trusted the output too quickly.

What should have caught it:
- A human review step for every citation.
- Checking each case in a real legal database before filing.
- A rule that AI output is never accepted without source verification.

Source:
- Reuters coverage of the Avianca/ChatGPT sanctions case: https://www.reuters.com/technology/

## Example 2: Amazon hiring tool bias
Amazon reportedly built an internal recruiting tool that learned from past hiring data and ended up favoring male candidates over female candidates.

What went wrong:
- The model learned from historical hiring data.
- That historical data already reflected bias.
- The tool repeated and amplified the bias instead of correcting it.

Why it went wrong:
- AI models learn patterns from training data.
- If the data is biased, the output can also be biased.
- The system was treated like an objective decision-maker when it was not.

What should have caught it:
- Bias testing before deployment.
- Checking whether the model scored male and female candidates differently.
- Human review before using the tool for hiring decisions.

Source:
- Reuters coverage of Amazon’s recruiting tool bias: https://www.reuters.com/technology/

## One personal rule
I will never trust an AI answer, citation, or recommendation without checking the original source or a trusted system first.

## Presentation checklist
- Present both examples.
- Explain what went wrong.
- Explain what should have caught it.
- State one rule I will apply at work.
