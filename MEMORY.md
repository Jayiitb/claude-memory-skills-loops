# Memory: Loop Engineering with Claude Code

> Distilled from the video **"Stop Prompting Claude. Start Loop Engineering."**
> (YouTube: `YAS4ojuhbW4`) plus Claude Code's actual loop primitives.
> This file is the **knowledge spine** for this repo — it survives between
> sessions because the model forgets and the repo does not.

---

## 1. The core idea

> "I don't prompt Claude anymore. I have loops running that prompt Claude and
> figure out what to do. My job is to write the loops." — Boris Cherny (creator of Claude Code)

- **Prompting is tactical** — one instruction, one result, you are the loop.
- **Loop engineering is strategic** — you design the system that *issues* the
  instructions, checks its own work, and keeps going until "done."
- The shift: stop *doing* the work, start *managing the worker*.

A loop = a goal + state that persists + a way to check progress + a stop
condition. You stop being the thing that re-types the next step.

---

## 2. The five building blocks

| Block | What it does | Why it matters |
|-------|--------------|----------------|
| **Goal / `/loop`** | A task that runs turn after turn on its own until "done" is met | Removes the human from the inner loop |
| **Memory** | On-disk state file (this file, `CLAUDE.md`) that survives between runs | The model forgets; the repo remembers |
| **Skills** | Saved instruction sets (`SKILL.md` folders) that freeze project knowledge | Agent stops re-learning the same context every session |
| **Worktrees** | Isolated git checkouts per agent (`--worktree`, `isolation: worktree`) | Parallel agents don't overwrite each other |
| **Sub-agents** | Separate builder vs. reviewer agents | The agent that *does* the work should not be the one that *grades* it |

The reviewer/sub-agent split is what makes a loop **trustworthy enough to run
unattended**. Never let one agent be both author and judge.

---

## 3. How each block maps to real Claude Code features

### Goal → `/loop` and `ScheduleWakeup`
- `/loop <interval> <prompt-or-command>` runs a task on a recurring interval
  (e.g. `/loop 10m /check-ci`). Defaults to ~10m.
- For self-paced loops, the agent schedules its own next wake-up.
- For wall-clock schedules (nightly, hourly), use **cron** triggers.
- Define **"done" explicitly** — a measurable stop condition (tests green, 0
  open review comments, count reached). A loop with no terminal state runs forever.

### Memory → `MEMORY.md` / `CLAUDE.md`
- The durable state file Claude reads at the start of every session.
- Keep it: project facts, decisions, conventions, "what done looks like," and
  pointers to skills. Update it as the source of truth changes.

### Skills → `.claude/skills/<name>/SKILL.md`
- A folder with a `SKILL.md` describing *when* to use it and *how* to do a
  recurring task. Reusable across sessions and teammates.
- Good skills are narrow, named for a trigger, and encode the steps you'd
  otherwise re-explain every time.

### Worktrees → `isolation: worktree`
- Each parallel agent gets a fresh checkout that auto-cleans on finish.
- Use only when agents mutate files concurrently and would otherwise collide.

### Sub-agents → the `Agent` tool / reviewer agents
- Spawn a separate agent to independently verify the builder's output.
- Pattern: **build → adversarially verify → only accept if it survives review.**

---

## 4. Patterns worth reusing

- **Loop-until-done:** keep iterating until an explicit, checkable condition.
- **Build/review split:** one agent produces, a different one critiques.
- **Loop-until-dry:** for open-ended discovery, stop after N rounds find nothing new.
- **Scheduled heartbeat:** a cron/`/loop` tick re-checks external state (CI, PRs,
  inbox) and acts only when something is actionable — otherwise stays silent.
- **State in the repo, not the chat:** anything worth keeping gets written to a
  memory file or skill, never left in conversation context.

---

## 5. Repo intent

This repo (`claude-memory-skills-loops`) is the home for:
- `MEMORY.md` — this knowledge spine.
- `.claude/skills/` — the reusable skills (see `SKILLS_AND_LOOPS.md` for the backlog).
- Loop / cron definitions that run unattended.

See **`SKILLS_AND_LOOPS.md`** for the proposed skills and loops to build.

---

## 6. Sources
- [Stop Prompting Claude. Start Loop Engineering. (video)](https://www.youtube.com/watch?v=YAS4ojuhbW4)
- [Loop Engineering — Addy Osmani](https://addyosmani.com/blog/loop-engineering/)
- [The head of Claude Code stopped prompting Claude — The AI Corner](https://www.the-ai-corner.com/p/loop-engineering-coding-agents-2026)
- [How to design AI agent loops — Lenny's Newsletter](https://www.lennysnewsletter.com/p/how-to-design-ai-agent-loops-schedules)
