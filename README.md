# First AI Agent — V1

A minimal autonomous agent built without an LLM, neural network, or agent framework.

## Goal

Reach `G` in a grid world while avoiding obstacles.

The complete loop is:

Goal → Observe → State → Decide → Act → Environment → Observe

## Run

```bash
python main.py
```

## V1 capabilities

- identifies current state
- identifies the goal
- chooses an action
- executes it
- observes the resulting state
- avoids invalid moves
- detects goal completion

## Deliberate limitation

The policy is deterministic and simple. It is NOT learning yet.

The next step is to add an unexpected environmental change and test recovery.
