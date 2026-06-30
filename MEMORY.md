# Memory: Loop Engineering with Claude Code

> Distilled from the video **"Stop Prompting Claude. Start Loop Engineering."**
> (YouTube: `YAS4ojuhbW4`) plus Claude Code's actual loop primitives.
> This file is the **knowledge spine** for this repo. It survives between
> sessions because the model forgets and the repo does not.

**Owner:** JP, CTO of Becoming Quotient (bQ). jp@becomingquotient.com

---

## 1. The core idea

> "I don't prompt Claude anymore. I have loops running that prompt Claude and
> figure out what to do. My job is to write the loops." (Boris Cherny, creator of Claude Code)

- **Prompting is tactical.** One instruction, one result. You are the loop.
- **Loop engineering is strategic.** You design the system that issues the
  instructions, checks its own work, and keeps going until "done."
- The shift: stop *doing* the work, start *managing the worker*.

A loop is a goal, plus state that persists, plus a way to check progress, plus a
stop condition. You stop being the thing that re-types the next step.

---

## 2. The five building blocks

| Block | What it does | Why it matters |
|-------|--------------|----------------|
| **Goal / `/loop`** | A task that runs turn after turn on its own until "done" is met | Removes the human from the inner loop |
| **Memory** | On-disk state file (this file, `CLAUDE.md`) that survives between runs | The model forgets, the repo remembers |
| **Skills** | Saved instruction sets (`SKILL.md` folders) that freeze project knowledge | Agent stops re-learning the same context every session |
| **Worktrees** | Isolated git checkouts per agent (`--worktree`, `isolation: worktree`) | Parallel agents do not overwrite each other |
| **Sub-agents** | Separate builder and reviewer agents | The agent that *does* the work should not be the one that *grades* it |

The reviewer split is what makes a loop **trustworthy enough to run unattended**.
Never let one agent be both author and judge.

---

## 3. How each block maps to real Claude Code features

### Goal: `/loop` and `ScheduleWakeup`
- `/loop <interval> <prompt-or-command>` runs a task on a recurring interval,
  for example `/loop 10m /check-ci`. Defaults to about 10m.
- For self-paced loops, the agent schedules its own next wake-up.
- For wall-clock schedules (nightly, hourly), use **cron** triggers.
- Define "done" explicitly. A measurable stop condition (tests green, zero open
  review comments, count reached). A loop with no terminal state runs forever.

### Memory: `MEMORY.md` and `CLAUDE.md`
- The durable state file Claude reads at the start of every session.
- Keep it current: project facts, decisions, conventions, what "done" looks like,
  and pointers to skills.

### Skills: `.claude/skills/<name>/SKILL.md`
- A folder with a `SKILL.md` describing *when* to use it and *how* to do a
  recurring task. Reusable across sessions and teammates.
- Good skills are narrow, named for a trigger, and encode the steps you would
  otherwise re-explain every time.

### Worktrees: `isolation: worktree`
- Each parallel agent gets a fresh checkout that auto-cleans on finish.
- Use only when agents change files at the same time and would otherwise collide.

### Sub-agents: the `Agent` tool and reviewer agents
- Spawn a separate agent to independently verify the builder's output.
- Pattern: build, then adversarially verify, then accept only if it survives review.

---

## 4. Patterns worth reusing

- **Loop-until-done:** keep iterating until an explicit, checkable condition.
- **Build/review split:** one agent produces, a different one critiques.
- **Loop-until-dry:** for open-ended discovery, stop after N rounds find nothing new.
- **Scheduled heartbeat:** a cron or `/loop` tick re-checks external state (mail,
  Slack, CI, PRs) and acts only when something is actionable, otherwise stays silent.
- **State in the repo, not the chat:** anything worth keeping gets written to a
  memory file or skill, never left in conversation context.

---

## 5. bQ house rules (apply to everything drafted)

- **Draft, never send.** Across Outlook, Slack, LinkedIn, and code. JP reviews and sends.
- **Crisp and finite.** Yes/no in one word when that is enough. Otherwise about ten
  words. A reply reads in under a minute.
- **Human voice, no em-dashes.** See the `comms-voice` skill. It must not read as AI.
- **Confirm before assuming.** Use the ask-user tool on real decisions.

---

## 6. Repo intent

This repo (`claude-memory-skills-loops`) is the home for:
- `MEMORY.md`: this knowledge spine.
- `.claude/skills/`: the reusable skills (`comms-voice`, `draft-reply`,
  `linkedin-daily`, `meeting-to-actions`).
- `scripts/`: helpers such as `ideogram_image.py` for LinkedIn images.
- Loop and cron definitions that run unattended.

See **`SKILLS_AND_LOOPS.md`** for the backlog and build order.

---

## 7. Sources
- [Stop Prompting Claude. Start Loop Engineering. (video)](https://www.youtube.com/watch?v=YAS4ojuhbW4)
- [Loop Engineering, Addy Osmani](https://addyosmani.com/blog/loop-engineering/)
- [The head of Claude Code stopped prompting Claude, The AI Corner](https://www.the-ai-corner.com/p/loop-engineering-coding-agents-2026)
- [How to design AI agent loops, Lenny's Newsletter](https://www.lennysnewsletter.com/p/how-to-design-ai-agent-loops-schedules)
