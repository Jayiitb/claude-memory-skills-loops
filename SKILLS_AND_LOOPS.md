# Skills & Loops to Build — Becoming Quotient (BQ)

> A backlog of skills (reusable instruction sets) and loops (self-running tasks)
> for BQ, derived from the loop-engineering principles in [`MEMORY.md`](./MEMORY.md).
> Owner: jp@becomingquotient.com

The guiding rule from the video: **stop being the loop.** Each item below moves
a recurring BQ task from "JP types the prompt every time" to "a skill encodes it
once" or "a loop runs it unattended with a reviewer checking the work."

---

## How to read this

- **Skill** = frozen know-how. Lives in `.claude/skills/<name>/SKILL.md`. Invoked
  on demand (or auto-triggered). Build these first — they're cheap and compounding.
- **Loop** = a skill that runs on a schedule or until a "done" condition, usually
  with a separate reviewer agent. Build these once the underlying skill is solid.
- Every loop needs an explicit **stop condition** and a **reviewer** (the builder
  never grades itself).

Legend: 🟢 high value / low effort · 🟡 medium · 🔵 bigger build

---

## Tier 1 — Build first (high leverage, low risk)

### 🟢 Skill: `meeting-to-actions` (Fireflies → monday.com + Slack)
Turn every client/internal call into structured output.
- **Trigger:** "process the latest meeting" or auto after a Fireflies transcript lands.
- **Does:** pull transcript → extract decisions, action items, owners, due dates →
  create monday.com items → post a clean recap to the relevant Slack channel.
- **Reviewer:** a second agent checks every action item maps to a real owner and date
  before anything is written to monday.com.

### 🟢 Skill: `inbox-triage` (Outlook/M365)
- **Trigger:** "triage my inbox" / morning loop.
- **Does:** classify unread mail (client, internal, vendor, noise) → draft replies
  for routine ones → surface a 5-line "needs JP" list. **Drafts only — never sends.**

### 🟢 Skill: `weekly-review` (monday.com → doc/email)
- **Does:** roll up board state into a one-page status: what shipped, what's blocked,
  what's at risk, what's due next week. Output as a doc and an optional email draft.

---

## Tier 2 — Loops (run unattended, with a reviewer)

### 🟡 Loop: `morning-brief` (cron, weekdays ~7:30am)
- **Runs:** `inbox-triage` + `weekly-review` deltas + calendar for the day +
  any monday.com items due today → one Slack DM / email.
- **Stop condition:** single brief delivered; silent if nothing material changed.

### 🟡 Loop: `meeting-follow-through` (heartbeat, hourly)
- **Runs:** check for new Fireflies transcripts → run `meeting-to-actions` →
  also nudge on action items from prior meetings that are now overdue.
- **Reviewer:** verifies no duplicate items and that nudges aren't spammy.

### 🟡 Loop: `client-cadence-guard` (daily)
- **Does:** flag clients/contacts with no touchpoint in N days (from Outlook + monday)
  so relationships don't go cold. Output: a short "reach out to…" list. Silent if clean.

---

## Tier 3 — Repo / build loops (for this and BQ's web properties)

### 🟡 Loop: `pr-babysitter` (this repo + Vercel)
- **Does:** on an open PR, watch CI → on failure, diagnose and push a fix → re-kick →
  repeat until green or genuinely stuck. Report Vercel preview URL when ready.
- **Reviewer:** separate agent confirms the fix is real, not a test silencer.

### 🔵 Skill: `design-to-page` (Figma → Vercel)
- **Does:** take a Figma frame → generate the page/component → open a preview deploy.
- Pairs with a reviewer agent that checks the build matches the design tokens.

### 🟢 Skill: `repo-memory-keeper`
- **Does:** at the end of a work session, update `MEMORY.md` with new decisions and
  conventions so the next session starts informed. Keeps the spine current.

---

## Suggested build order

1. `meeting-to-actions` + `inbox-triage` (Tier 1 skills) — immediate daily payoff.
2. `weekly-review` + `repo-memory-keeper`.
3. Wrap them in the `morning-brief` and `meeting-follow-through` loops.
4. `pr-babysitter` once there's active development here.
5. `design-to-page` when there's a Figma → web pipeline to automate.

---

## Open questions for JP
- **"Convert with the BQ email"** — did you want me to (a) tailor everything to BQ
  (done here), (b) actually *email* this summary to jp@becomingquotient.com, or
  (c) just brand/attribute it? Tell me and I'll do it.
- What does a typical BQ week actually look like? The more I know about the real
  recurring tasks, the sharper these get.
- Which of the connected tools (Slack / Outlook / Fireflies / monday / Figma /
  Vercel) is most central to your week? That sets the build order.
