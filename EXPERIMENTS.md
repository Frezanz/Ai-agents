# Experiments

## Experiment 001 — Deterministic Grid Agent

**Date:** 2026-10-04

**Hypothesis:** A small deterministic controller can complete the full perception → state → decision → action → feedback loop without an LLM.

**Environment:** 5×6 grid with obstacles and one goal.

**Agent configuration:** Rule-based policy.

**Expected result:** Reach the goal using only legal actions.

**Actual result:** Run the experiment and record the result here.

**Metrics:**
- Goal reached
- Number of steps
- Invalid actions
- Runtime

**FACT / INFERENCE / HYPOTHESIS:**
- FACT: The implementation contains all core agent-loop components.
- INFERENCE: The system qualifies as a minimal agent under this project's operational definition.
- HYPOTHESIS: It will remain effective when the environment changes unexpectedly.

**Next experiment:** Introduce an unexpected obstacle after the agent has started moving.
