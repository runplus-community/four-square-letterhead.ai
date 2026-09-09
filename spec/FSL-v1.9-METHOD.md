# FSL — Document Authority & Continuity

Project: four-square-letterhead.ai. Method edition: v1.9. Four-Square Template v1.9. Published branch-scoped release.

This Markdown file owns this proposed method's wording; PDF/DOCX are derived views. Adopting projects retain their approved document authority. The maintenance skill applies the method; it does not replace project intent.

## 1. Documents govern; stewardship maintains continuity

### Adopted documents hold the agreement

The project's adopted FSL documents are the **single source of truth for its agreed business and technical intent**: purpose, scope, responsibilities, commitments, rules and contracts. Business, services, operations, software, hardware, data and English deliverables all fit. No software or AI product is required. Documents state the agreement; evidence establishes observed outcomes.

Experience informs the maintenance skill's questions, reviews and proposals. A skill, agent or MEMORY MUST NOT silently create, reinterpret or override adopted requirements. Changing contributors, tools or skills does not change the contract. **Documents govern. Skills maintain. Evidence verifies.**

### Name responsibility; do not infer authority

A **steward** keeps documents, work, evidence and decisions understandable together. An observer reports; a steward maintains and proposes; an executor works within scope; the named decision authority approves intent. These are responsibilities, not new squares or compulsory job titles. One person may perform several; an agent needs explicit delegation. Stewardship is ongoing responsibility, not an installed monitor or schedule.

Record who can approve which decision and where that authority comes from. Authorship, repository access, assignment, silence or a previous unrelated approval is not permission. Intent approval, execution/spending permission and release acceptance are separate decisions. Unclear or expired authority pauses the dependent action; safe, unaffected work may continue. Do not require separate people unless the project's controls do.

### One entry point; four continuing responsibilities

Put **FSL first inside SPEC**, followed by adopted scope, business rules, contracts, guardrails, acceptance and routes. Identify document versions, approval and applicable changes. Use **one repository or several coordinated repositories**; name the entry point and authoritative paths/revisions. Every material artifact SHOULD have one authoritative home. References and generated views are not competing originals; links alone adopt no law. Do not force a split or merger or invent precedence between conflicting records.

Start with **[ SPEC | SYSTEM | AI | MEMORY ]**. SPEC and MEMORY stay fixed; SYSTEM and AI are recommended defaults with justified alternatives. **SPEC** owns adopted intent and optional appendix, errata and amendments. **SYSTEM** owns deliverables, operating work and checks, including English skills. **AI** owns AI-specific instructions and capabilities where relevant, not all automation. Declare inactivity rather than inventing capability. **MEMORY** retains rationale, decisions, glossary, mnemonics, limits and evidence links; it cannot make law.

**Squares own artifacts; routes cross only the artifacts needed for the claimed outcome.** They are not sequential phases. Ownership follows purpose, not authorship: agent-written product work belongs to SYSTEM. FSL may retain TEMPLATES / SKILL. Project work stays in declared project repositories; the FSL repository holds the reusable method, kit and labeled references.

### Plain English, one authoritative meaning

The **DNA** analogy means compact identity and commitments, not reconstruction of missing work. Choose one editable source per document; reading copies do not independently evolve. Start with one page; use two or three only when needed. Three is the letterhead maximum, not a limit on supporting records. No compulsory forms, route tables, YAML schema or iteration ledger. Remove duplication before shrinking type. English can be the entire product.

Separate project/contract from method/template identity on every page. MUST / MUST NOT bind; SHALL / SHALL NOT are aliases. SHOULD / SHOULD NOT give strong guidance; MAY permits. Labels such as law, contract, policy or guardrail alone set no force. Render normative words in capitals, bold and underline. Give material binding promises stable clause IDs with baseline context; never recycle them for unrelated obligations. Binding intent MUST NOT be silently weakened.

## 2. Work in focused rounds; verify meaningful paths

### Routes define coverage; iterations organize work

Use **R-01: input → required touchpoints → observable output**. State outcome, exclusions, clauses and baseline; identify material conditional, asynchronous and midpoint boundaries. Add routes for distinct important paths. Touchpoints are not branches; never delete a failing point to manufacture success.

**Route defines expected coverage; run records observed coverage.** An iteration is one focused round of work and learning, possibly with several runs. Several iterations may improve one route. No compulsory I-numbering. Close with the result and unresolved work.

### New work grows; existing work adopts the present

New projects SHOULD begin with four E2E learning goals: **tiny complete path → useful behavior → boundary/recovery → intended-use rehearsal → grow**. Repeat or split goals; explain material departures. These are not four compulsory iterations, routes or release approval. Preserve proven behavior unless reviewed intent changes it.

Existing systems may study or reverse-engineer a reviewed present baseline, separate observed behavior from adopted intent, disclose gaps and verify important routes. An old bug is not law. Historical and future iteration plans are optional. Do not reconstruct early loops, rebuild working capability or rewrite history for adoption.

### Collaborate close to the work

Prefer local tools, human judgment and bounded agent help. Minimize unnecessary changes, calls, delay, cost and coordination without weakening required controls or route coverage. A task identifies goal, baseline, route, scope, owner and expected result; return changes, evidence, limits and next decision there. Checklist-based work is recommended, not compulsory forms.

GitHub Projects/Issues, Codex and pull requests are optional adapters. Assignment is not execution; confirm receipt and result. Agents stay within granted scope. Background work needs identifiable progress, cancellation and a final receipt; this method starts none. Do not invent an integration or delegate approval implicitly.

### Actions stay off; approval has a budget

**GitHub Actions are OFF by default**, including FSL's development and releases. Agents MUST NOT enable, start or retry them without explicit, scoped user approval. Suggest a justified run and wait. A general develop, commit or release request is not permission. Inspect triggers before remote writes; pause writes that could cause unapproved starts. Do not silently change settings.

Estimate starts, jobs/downstream work, status reads, result fetches, duration and cost or uncertainty. Recommend zero starts when local work suffices; otherwise propose **one start per rolling 60 minutes**, with an explicit task total and expiry. Two per hour needs justification and approval. These are ceilings, not standing permission, schedules or targets.

Name the counted unit. Charge each start attempt, retry and downstream execution to its allowance, including failed, cancelled or uncertain attempts. Cap jobs and runner time; one dispatch is not unlimited work. Estimate and cap reads separately; an all-calls cap includes them. Share the budget across the named repositories and agents through one accountable dispatcher and checkable receipts. Unknown consumption means pause.

No tight polling or blind timeout retries. Stop at any cap or expiry; re-estimate and seek an extension before exceeding scope, counts or cost. Time passing does not renew expired approval. A required unapproved gate remains blocking and NOT YET PROVEN. OFF is policy, not a claim that remote settings or hourly enforcement were configured.

### Check the declared route, not a convenient substitute

Show every touchpoint before a run; retain PASS, FAIL or NOT RUN, including unreached points. Record revision, baseline, environment, substitutions, outcome and evidence in ordinary logs or prose. Never prefill PASS. Component success MUST NOT be called integrated E2E proof.

Unchanged components can participate without edits. Stubs prove only their disclosed boundary. Include AI only when the runtime claim depends on it. E2M/M2E stay partial until integrated; parallel paths retain their results and check shared state. Expected rejection can PASS a negative route. Prefer safe representative checks over destructive production tests.

## 3. Surface drift; resolve decisions; preserve the record

### Compare intent with reality without guessing

At adoption, material change, handover or release, the steward SHOULD compare documents, work/practice and evidence. **Drift is a mismatch, not permission to rewrite the agreement.** State expected/observed behavior, baseline/route, evidence, impact and decision owner. Distinguish confirmed mismatch from suspicion or missing proof. No monitor or automatic external call is required.

Repair implementation within scope for unchanged intent; correct stale summaries without editing released originals. Propose adoption for changed intent. Keep uncertain intent, authority, evidence or compatibility explicit; invent neither precedence, approval nor success. Pause dependent claims/actions; continue only safe, unaffected work. Resolve through authorized decisions, affected checks and evidence, not merely a closed task.

### Leave a useful current view, not a dashboard

A dated working note states baseline, key routes, supported claims, unproven scope, drift and **next decision with its owner**. Link evidence/approvals; never rewrite frozen documents for status updates. Missing owners stay unassigned. A successor should resume without the original chat. No health score or new form is required.

Older evidence retains its original scope, not automatic applicability after change. Assess reuse; recheck affected boundaries. A scoped review may conclude no change is needed. No ceremonial edits are required.

### Improve the skill; reuse what is proven

Version skills separately; learning does not adopt intent. An English route is **brief → source review → interpretation → draft → review → delivered document**. Check fidelity, usability and unresolved intent; one example proves no universal reliability. Analogies and homologies explain structural correspondences: a route is a map; a run is a journey. State limits; metaphors create neither law nor proof.

Name essential technologies/libraries/references with purpose/source; pin material versions. REUSE uses capability; INHERIT adopts a contract; REFERENCE consults without adopting law. Binding choices need clauses. Evaluate proven work before rebuilding; inventories stay outside. Add optional process only for understanding, coordination, evidence or release confidence; never waive binding controls.

### Amend intentionally; retain the released baseline

Review drafts directly; appendices may grow during discovery. Preserve released SPEC. **Appendix explains; errata corrects without changing intent; an adopted amendment changes intent.** These are optional documents, not required stages or folders. Intent-changing corrections need amendments.

A proposal is not approval. Adoption names authority, affected documents/baseline and clauses, exact change, effective scope/date and immutable record. Resolve overlapping changes before conformance claims. Reassess implementation, routes and evidence: approved intent is not implemented or verified behavior. The next release SHOULD incorporate applicable adopted corrections/amendments without altering earlier baselines.

### Review the compatible combination and scoped result

Preserve each repository's history: main1 is its original first commit. New lanes start there; existing systems adopt a reviewed present baseline. Later lanes continue matching predecessors. Suffixes follow project releases, not FSL. main is accepted integration; lanes validate scope and declared dependencies. Do not fabricate history or move roots.

Account for four responsibilities: stable SPEC, verified deliverable, aligned second concern or declared inactivity, and understandable MEMORY. Record four reviewed commits/integration in one repository, or authoritative repository/path/revisions and a compatible combined baseline across repositories. Check shared route boundaries. Squares need not be repositories. Git records identity; branch names alone do not. **One version, four squares, all green** is not a demand for CI.

Scope proof as **CLAIM / SCOPE / ENVIRONMENT / EVIDENCE / RESULT**. Missing evidence or unresolved intent is NOT YET PROVEN; a known binding violation is NON-CONFORMANT in the affected scope. CONFORMANT requires applicable evidence without unresolved violations. CONFORMANT WITH EXCEPTION needs authorized scope, clause, reason, evidence and review/expiry. A waiver cannot turn an unrun check into PASS.

Distinguish drafted, reviewed, tested, accepted and published. Local packaging is not publication; a public branch is not a Releases-page entry. Framework publication certifies no consuming project. MEMORY may remember law; MEMORY cannot make law.

**FSL owns the method. The project owns the work.**