# FSL v1.4 Development Strategies

This reference defines the compact strategy vocabulary used by FSL v1.4. Binding force comes from the Constitution, not this explanatory file.

## Iteration declaration
A material iteration records:

```text
ITERATION
STRATEGY
TOUCHPOINT SET
START / MIDPOINT / END (as applicable)
EXPECTED EVIDENCE
EXIT CONDITION
```

## Strategies

### E2E
`END -> ...touchpoints... -> END`

Use when one complete vertical path can be proven directly.

### E2M
`END -> ...touchpoints... -> MIDPOINT`

Use when the outer/input side can advance independently toward an agreed midpoint contract.

### M2E
`MIDPOINT -> ...touchpoints... -> END`

Use when a proven midpoint can drive the remaining path independently.

### PARALLEL E2E
```text
E2E-A ----------------->
E2E-B ----------------->
```

Use for independent vertical slices that can progress concurrently and later coexist or integrate.

### MEET-IN-THE-MIDDLE
```text
START ------> MIDPOINT <------ END
        E2M             M2E
```

Both sides MUST name the same midpoint contract before integration can be claimed.

### INCREMENTAL E2E
```text
tiny E2E -> richer E2E -> broader E2E -> mature E2E
```

Each increment begins from a proven path and grows one or more dimensions deliberately.

## Touchpoint Set
A Touchpoint Set is the ordered or declared set of system surfaces an iteration claims to cross. Examples include `SEED / CURRENT / TEMPLATE / DB / API / UI / TEST`, but projects choose their own durable vocabulary.

Touchpoints are not branches. A touchpoint may be exercised by a tiny implementation, a verification step, a stub with a proven contract, a fixture, or another meaningful mechanism sufficient for the claimed path.

## Core axiom
**TOUCH EVERYTHING REQUIRED; COMPLETE LITTLE; GROW WHAT IS PROVEN.**
