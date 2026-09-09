# FSL v1.9 — Memory

## Core alignment

FSL v1.9 treats the project's adopted FSL documents as the single source of truth for agreed business and technical intent. The reusable skill maintains those documents using experience, review and evidence; it does not replace or silently reinterpret them.

Mnemonic: **Documents govern. Skills maintain. Evidence verifies.**

## Stewardship

A steward keeps documents, implementation/work, evidence and decisions mutually understandable. Stewardship is a responsibility, not a fifth square, monitoring service or approval authority. Observer, steward, executor and decision-authority responsibilities may be held by one person where project controls allow.

Intent approval, execution/spending permission and release acceptance are distinct decisions. Authorship, repository access, task assignment, silence or prior unrelated approval does not grant them.

## Drift and uncertainty

Drift is a mismatch between adopted intent and implementation, operating practice or applicable evidence. Drift is not permission to rewrite the agreement. Resolve unchanged-intent defects in the work, stale summaries from their source, and intent changes through the adopted lifecycle. Suspected drift and missing proof remain explicit; do not guess precedence, approval or success.

A useful handover note states the effective baseline, key routes, supported claims, NOT YET PROVEN scope, open drift, next decision and owner. A scoped review may correctly conclude that no change is needed.

## Development and collaboration

Iteration means one focused round of work and learning. Routes remain stable coverage definitions; runs record observed coverage. New projects should use the first four E2E learning goals: tiny complete path, useful behavior, boundary/recovery, intended-use rehearsal, then grow. Existing projects adopt the reviewed present rather than reconstructing history.

GitHub Projects/Issues, Codex, pull requests and CI are optional adapters. One repository or several coordinated repositories are both valid; every material artifact should have one authoritative home and compatible revisions must be identifiable.

## External automation

GitHub Actions are OFF by default, including FSL development and releases. A general develop, commit or release request is not Actions permission. Before any proposed run, estimate starts, downstream jobs, reads/fetches, duration, cost/uncertainty and least permission; recommend zero starts when local work is sufficient. Otherwise recommend one start per rolling 60 minutes with a task-total cap and expiry; two per hour requires explicit justification and approval. Failed, cancelled, uncertain and retry attempts consume the allowance. Stop and ask before exceeding any approved bound.

FSL v1.9 branch-scoped release was prepared without starting GitHub Actions; local rendered-document and package verification supplied the release evidence.

## Lifecycle

Released SPEC remains immutable. Appendix explains; errata corrects without changing intent; an adopted amendment changes intent. A proposal is not approval. Changed intent requires reassessing affected work, routes and evidence.

**FSL owns the method. The project owns the work.**
