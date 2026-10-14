# Showcase repo: how to build it

Goal: one repo where your philosophy can be checked in code, not just read. Pick the project you can most easily keep small and finished (a focused slice of the PMS works well).

## What a reviewer should find in under 5 minutes

| They look for | Where it lives |
|---|---|
| What it does and why | `README.md`, first screen |
| How to run it | `README.md`, "Run it" section, 3 commands max |
| That it is tested | CI badge, `tests/`, a coverage number |
| Why decisions were made | `docs/decisions/` (short notes) |
| That quality is automated | `.github/workflows/ci.yml` |

## Suggested structure

```
your-project/
├── README.md
├── docs/
│   └── decisions/
│       └── 001-why-this-stack.md
├── src/
├── tests/
│   ├── unit/        (Jest)
│   └── e2e/         (Cypress)
└── .github/
    └── workflows/
        └── ci.yml
```

## Steps

1. Pick the slice: one user flow, end to end (for example "create a reservation").
2. Write acceptance criteria first, in the README, as a checklist.
3. Turn each criterion into a test (e2e for the flow, unit for the rules).
4. Add the CI workflow below and keep it green.
5. Write one decision note per non-obvious choice: context, decision, alternatives rejected.
6. Add real numbers to the README: test count, coverage, time to run the suite.

## README template

```markdown
# Project name

One sentence: who it is for and what problem it solves.

![CI](https://github.com/USER/REPO/actions/workflows/ci.yml/badge.svg)

## The problem
[2-3 sentences. What was slow or error-prone before.]

## What "done" meant
- [ ] [Acceptance criterion 1]
- [ ] [Acceptance criterion 2]
- [ ] [Acceptance criterion 3]

## Results
- [N] tests ([N] unit, [N] e2e), suite runs in [N] minutes
- [Coverage]% line coverage on [module]
- [Any real outcome: time saved, errors avoided]

## Run it
    npm install
    npm test
    npm start

## Decisions
See [docs/decisions](docs/decisions).
```

## CI workflow (`.github/workflows/ci.yml`)

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: npm
      - run: npm ci
      - run: npm test -- --coverage
      - name: End-to-end tests
        uses: cypress-io/github-action@v6
        with:
          start: npm start
          wait-on: "http://localhost:3000"
```

Adjust the port and scripts to your project.

## Decision note template (`docs/decisions/001-title.md`)

```markdown
# 001. Title

**Status:** accepted
**Context:** what forced a choice.
**Decision:** what you chose.
**Alternatives rejected:** and why.
**Consequences:** what gets easier, what gets harder.
```
