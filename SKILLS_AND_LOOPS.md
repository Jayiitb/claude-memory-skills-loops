# Skills & Loops, Becoming Quotient (bQ)

> The build sheet for JP, CTO of bQ. Skills (reusable know-how) and loops
> (self-running tasks), built on the loop-engineering ideas in [`MEMORY.md`](./MEMORY.md).
> Owner: jp@becomingquotient.com

The rule from the video: **stop being the loop.** Move recurring CTO work from
"JP types the prompt every time" to "a skill encodes it once" and "a loop runs it
unattended." Everything drafts, nothing sends.

---

## House rules (every skill obeys these)
- **Draft, never send.** Outlook, Slack, LinkedIn, code. JP reviews and sends.
- **Crisp.** Yes/no when that is enough, else about ten words. One-minute read.
- **Human voice, no em-dashes.** Enforced by the `comms-voice` skill.
- **Confirm before assuming** on real decisions.

---

## Built now (in this repo)

### Skill: `comms-voice`
JP's writing-voice guard. Human, crisp, finite, no em-dashes. Every draft runs
through it. **Placeholder until JP pastes his own comms skill, which replaces it.**

### Skill: `draft-reply`
Finds what genuinely needs the CTO across Outlook (personal mail awaiting reply),
Slack (threads needing a real decision or deep technical call), and coding problem
statements. Drafts a crisp reply in JP's voice. Never sends.

### Skill: `linkedin-daily`
Drafts one short, punchy, thought-provoking LinkedIn post a day plus a matching
image, built for views and comments. Includes four post templates. Never posts.

### Skill: `meeting-to-actions`
Turns a Fireflies meeting into owned, dated action items, writes them to monday.com,
posts a Slack recap. A reviewer pass validates before anything is written. Secondary
priority, kept because Fireflies and monday are connected.

### Helper: `scripts/ideogram_image.py`
Generates the LinkedIn image via Ideogram. Reads `IDEOGRAM_API_KEY` from the
environment. Key is never stored in the repo.

---

## Loops to wire up next

### Loop: `attention-triage` (weekday mornings, cron)
Runs `draft-reply` across Outlook + Slack. Returns a short "needs you" list with a
ready draft for each. Silent when nothing is actionable. Never sends.

### Loop: `linkedin-daily` (once a day, cron)
Runs the `linkedin-daily` skill. Produces the post draft + image + two alternate
hooks for JP to review and post. Never posts.

### Loop: `pr-babysitter` (this repo, on open PRs)
Watches CI. On failure, diagnoses, pushes a fix, re-kicks until green or stuck. A
separate reviewer agent confirms the fix is real, not a silenced test.

---

## Build order
1. `comms-voice` (done) and `draft-reply` (done). JP pastes his real comms skill to
   replace the placeholder.
2. `linkedin-daily` (done) once `IDEOGRAM_API_KEY` is set as an env secret.
3. Wire the `attention-triage` and `linkedin-daily` **loops** as cron triggers.
4. `pr-babysitter` once there is active development here.

---

## Setup JP needs to do
1. **Rotate the Ideogram key** that was shared in chat, then set the new one as an
   **environment secret** named `IDEOGRAM_API_KEY` (Claude Code web env settings).
   Never paste it in chat or commit it.
2. **Paste your comms skill** so it replaces the placeholder and the voice is exactly yours.
3. Confirm the **cron schedules** you want (for example: triage 7:30am weekdays,
   LinkedIn 8:00am daily).
