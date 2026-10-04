# Project Status

## STATUS
Phase 0 completed enough to begin implementation. V1 deterministic environment and agent are implemented.

## DISCOVERY
The minimal agent architecture can be represented as:
Goal → Observe → State → Decide → Act → Environment → Feedback.

## DECISION
Start without an LLM, machine learning, or external agent framework.

## FAILED
No failure recorded yet. V1 has not been experimentally evaluated in this environment.

## OPEN
- Add unexpected environmental changes.
- Add quantitative metrics.
- Test recovery.
- Replace reactive policy with planning.
- Record experiments.

## NEXT
Run `python main.py`, then deliberately change the environment so the original decision strategy encounters something unexpected.
