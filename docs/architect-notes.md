# Claude Certified Architect — Study Trail

A running log of Claude-architecture lessons as they come up *while building Great Learning coursework*.
Each entry ties a real decision we made to one of the five exam domains, so by exam time this is a
personalized, worked-example study guide — not abstract theory.

## The five domains (exam scope)

| Tag | Domain |
|-----|--------|
| **AAO** | Agentic Architecture & Orchestration |
| **TDM** | Tool Design & MCP Integration |
| **CCW** | Claude Code Configuration & Workflows |
| **PES** | Prompt Engineering & Structured Output |
| **CMR** | Context Management & Reliability |

## How to read the log

Newest entries on top. Each entry: **date · domain tag · the decision · why an architect frames it that way.**

---

## Log

### 2026-08-14 · CCW · One umbrella repo for all coursework
**Decision:** Made `dinkycoder/GreatLearning` a single repo holding every course as a subfolder
(`Course01-…/`, `Course02-…/`), rather than one repo per project.
**Architect lens:** Repo/workspace boundaries *are* a configuration decision. A single well-structured
workspace gives Claude Code consistent context and a stable mental model across sessions; scattered repos
force re-onboarding each time. The trade-off an architect weighs: shared context & simplicity (one repo)
vs. isolation & independent submission (many repos). We chose shared context because it's a personal
learning portfolio.

### 2026-08-14 · CMR · Per-project virtual environments + scoped `.gitignore`
**Decision:** One venv per project; root `.gitignore` excludes `.venv/`, secrets (`.env`), and `.claude/`.
**Architect lens:** Reliability starts with isolating state. Per-project environments prevent
dependency drift from silently breaking a reproduction later — the same principle as isolating an agent's
context so one task can't corrupt another. Keeping secrets and tooling config out of version control is
basic context hygiene: only commit what should be part of the shared, reproducible state.

### 2026-08-14 · CCW · Clean default branch (`main`)
**Decision:** Renamed the auto-generated `claude/eda-prompts-sequential-n1md25` branch to `main` and set
it as default.
**Architect lens:** Predictable, conventional defaults reduce cognitive load and tooling friction — the
workflow equivalent of a clear tool schema. Agents and humans both work better against conventions they
can assume without checking.

---

## Domain coverage tracker

Tick as each domain gets a real worked example. AAO and TDM will need deliberate call-outs since pure
EDA/ML work surfaces them less often.

- [x] **CCW** — Claude Code Configuration & Workflows
- [x] **CMR** — Context Management & Reliability
- [ ] **PES** — Prompt Engineering & Structured Output
- [ ] **TDM** — Tool Design & MCP Integration
- [ ] **AAO** — Agentic Architecture & Orchestration
