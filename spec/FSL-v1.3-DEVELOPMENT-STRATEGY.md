# FSL v1.3 Development Strategy

Status: DEVELOPMENT DRAFT

## Principle
Develop through small ordered end-to-end iterations. Each iteration proves one useful requirement across the relevant touchpoints, then becomes the baseline for the next iteration.

> **Small requirement. End-to-end path. Explicit touchpoints. Working proof. Learn. Increment. Repeat.**

## End-to-end rule
End-to-end means end-to-end for the iteration's requirement, not for the entire final product.

A normal path is:

```text
requirement -> rule -> implementation -> usable state -> checker -> evidence -> PROVEN
```

An iteration does not finish at implementation alone.

## Touchpoints
Touchpoints are system surfaces, not branches. A project keeps a small durable vocabulary such as:

`SPEC | Template | Foundation | Materialization | Runtime | Manager | Access | Checker | AI | Memory | Evidence | Package`

For each iteration, relevant touchpoints are classified as:

- `CHANGE`
- `VERIFY`
- `NOT AFFECTED`

Branches answer **who owns the responsibility**. Touchpoints answer **where the iteration crosses the system**.

## Ordered sequence CSV
Use one short ordered CSV as the development spine:

```csv
Seq,Iteration,Requirement,Touchpoints,E2E Path,Proof,Status
```

Recommended status values:

`PLANNED | ACTIVE | PROVEN | BLOCKED`

Example:

```csv
Seq,Iteration,Requirement,Touchpoints,E2E Path,Proof,Status
1,I01,Neutral foundation,"SPEC|Foundation|Checker|Evidence","define>create>inspect>check>record","foundation valid",PLANNED
2,I02,Template from foundation,"Foundation|Template|Checker|Evidence","copy>materialize>inspect>check>record","seed unchanged + template valid",PLANNED
3,I03,Private runtime,"Template|Manager|Runtime|Access|Checker|Evidence","instance>mount>use>verify>unmount>record","owner pass + outsider denied",PLANNED
```

## Iteration contract
Each row needs only:

1. `Requirement` — one small useful outcome.
2. `Starting baseline` — latest PROVEN iteration.
3. `Touchpoints` — relevant surfaces and CHANGE / VERIFY / NOT AFFECTED classification.
4. `E2E Path` — smallest complete route through the system.
5. `Proof` — observable checker/test/evidence.
6. `Status` — PLANNED / ACTIVE / PROVEN / BLOCKED.

## Cumulative development

```text
I01 -> proven baseline 1
I02 -> proven baseline 2
I03 -> proven baseline 3
...
```

Each next iteration SHOULD preserve already proven behavior unless its requirement explicitly changes it. If new evidence disproves an earlier assumption, amend the relevant contract explicitly and rerun the affected touchpoints.

## Four-Square impact
A development change SHOULD touch the smallest number of branches necessary, but all four branches SHOULD be inspected before acceptance.

Example:

```text
SPEC         changed? yes/no
LANE A       changed? yes/no
LANE B       affected? verify/no
MEMORY       recall affected? verify/no
```

## Development loop

```text
SELECT SMALL REQUIREMENT
        ↓
MAP TOUCHPOINTS
        ↓
BUILD END TO END
        ↓
CHECK EACH TOUCHPOINT
        ↓
VERIFY + RECORD EVIDENCE
        ↓
ACCEPT ITERATION
        ↓
LEARN
        ↓
NEXT ITERATION
```

Short axiom:

> **ITERATE -> TOUCH -> PROVE -> LEARN -> INCREMENT**

## Exit rule
A row becomes `PROVEN` only when its required end-to-end result and evidence exist. A successful code change, build, agent run or partial test is not sufficient by itself.
