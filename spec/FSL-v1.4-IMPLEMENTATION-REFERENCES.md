# FSL v1.4 Implementation References

FSL v1.4 can name important implementation material without becoming a dependency catalog.

## Classes

- `TECHNOLOGY` — language, runtime, platform, protocol or implementation technology.
- `LIBRARY` — package, SDK, framework or implementation dependency.
- `REFERENCE` — repository, implementation, standard, document, UI, prior work or evidence source.
- `LINK` — canonical location for the referenced material.

## Recommended entry shape

```yaml
class: LIBRARY
item: Playwright
force: SHOULD
relation: REUSE
purpose: E2E browser validation
source: <canonical link>
```

Recommended fields:

`CLASS / ITEM / FORCE / RELATION / PURPOSE / SOURCE`

The relation uses the v1.3 semantics:
- `REUSE` — use an existing proven capability.
- `INHERIT` — explicitly adopt an existing requirement or contract.
- `REFERENCE` — use knowledge/evidence without adopting its law.

The class does not imply force. `MUST`, `SHOULD`, `MAY`, or another normative term must be stated when force matters.
