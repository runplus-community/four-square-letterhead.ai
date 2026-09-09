# FSL v1.7 - Routes and visible runs

**Iterations are optional. Routes define coverage. Runs produce evidence.**

SPEC defines the route and expected outcome. SYSTEM owns product touchpoints. AI owns AI-specific touchpoints only where they actually participate. MEMORY preserves rationale and links to exact evidence. These are responsibilities, not mandatory runtime hops.

## Put the important path on the letterhead

`R-01: [input] -> [touchpoint 1] -> [touchpoint 2] -> [observable output]`

Add the expected result and applicable SPEC/route baseline. R-01 identifies a route, not a requirement, iteration or run. Relate it to the relevant contract clause IDs. R-02 or R-03 may describe other critical paths; FSL is not a catalog of every test case. A route can express a named branch condition, negative outcome or asynchronous completion boundary when material.

## Show the whole list on each run

Print or display the route's declared list before execution. Keep a result for every point, including points not reached. A normal test log or short Markdown sheet is enough; no run database or prescribed serialization is required.

### Reusable run sheet - blank, not execution evidence

Run: [unique ID/date]  
Route: R-01 at [immutable route reference / SPEC version]  
Applicable SPEC and adopted changes: [base reference + IDs/references, or NONE]  
Implementation: [actual commit/artifact identity]  
Environment: [host/runtime/dependency versions material to this claim]  
Expected outcome: [observable assertion]  
Substitutions or exclusions: [NONE / exact fixture, stub or partial boundary]

| Required touchpoint, in route order | Expected observation | Result | Evidence |
|---|---|---|---|
| [input] | [request/event/data] | NOT RUN | [reference] |
| [touchpoint 1] | [participation/assertion] | NOT RUN | [reference] |
| [touchpoint 2] | [participation/assertion] | NOT RUN | [reference] |
| [observable output] | [outcome assertion] | NOT RUN | [reference] |

Observed outcome: [not supplied]  
Route conformance: **NOT YET PROVEN**

Replace the rows with the actual declared points, not a passing subset. Repeated touchpoints in a route keep their positions. A failure at an early point leaves later points NOT RUN unless the connected workflow actually continued.

## What the result means

PASS / FAIL / NOT RUN are execution labels, not additional constitutional conformance states. PASS at all points is necessary but not sufficient: verify the end outcome and the connections between those points. Independently passing components or manually checked boxes cannot substitute for integrated evidence. A negative route may PASS when the promised rejection is observed.

A skipped point leaves the full route unproven. A known binding violation is NON-CONFORMANT; a mere missing observation is NOT YET PROVEN. An authorized exception does not turn a skipped test into a passed test. Do not prefill PASS or copy a previous run's result.

A fixture/stub supports the stated test boundary, not the live system it replaces. E2M and M2E are partial paths until their combined path is checked. Independent parallel routes keep separate results; where they share state or contracts, verify the interaction. Use a safe representative environment and disclose it; FSL does not require destructive production testing.

## Stable route, evolving implementation

An unchanged touchpoint can be exercised without being edited. Keep the route and evidence bound to the actual SPEC, implementation and environment. A significant change to the claimed route or promise is reviewed in draft SPEC, or through the released SPEC's amendment lifecycle. Do not silently remove a hard-to-test point or turn a historic PASS into a permanent badge.

For new projects: `I-001: build a tiny R-01 -> run -> verify -> grow`.

For existing projects: `study as needed -> reviewed current baseline -> run R-01`.

Historical and future iteration plans are optional for existing projects. Route-based evidence does not require an artificial iteration history. One representative route supports its own scope, not every capability of a mature product.

Authority: Constitution LAW-ROUTE-002, LAW-RUN-001, LAW-DEV-005 / 006, LAW-PROOF-001. This guide explains their application; it does not authorize new project requirements.
