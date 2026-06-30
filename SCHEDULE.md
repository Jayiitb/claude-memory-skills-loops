# Schedule: bQ loops

JP's loops, timezone **IST (Asia/Kolkata)**. Both loops draft only. Nothing sends.

> **Why this is a setup file, not auto-created.** A permanent daily schedule needs a
> Claude Code **web scheduled trigger** on this environment (it starts a fresh session
> at the set time). The in-session cron tool only runs while a session is open and
> expires after 7 days, so it cannot serve a real 6 AM daily job. Create the two
> triggers below in the Claude Code web UI: open this environment, add a scheduled
> trigger, paste the cron and the prompt. Docs: https://code.claude.com/docs/en/claude-code-on-the-web

---

## Trigger 1: LinkedIn daily draft

- **When:** 5:00 AM IST, every day (ready before JP wakes)
- **Cron (IST):** `0 5 * * *`   ·   **Cron (UTC):** `30 23 * * *`
- **Prompt:**

```
Use the linkedin-daily skill. First research what is trending and picking up in
tech right now (AI agents, dev tooling, startups, whatever is live today). Then
draft one post for JP, co-founder and CTO of bQ, written as his own journey and
viewpoint, with a little real flavor from what he is actually working on. Make a
matching image via scripts/ideogram_image.py. Run all copy through the comms-voice
skill: human, crisp, no em-dashes. Output the post, the image path, and two
alternate hooks. Never post. Draft only.
```

---

## Trigger 2: Attention triage (Outlook + Slack)

- **When:** 6:00 AM and 3:00 PM IST, every day
- **Cron (IST):** `0 6,15 * * *`   ·   **Cron (UTC):** `30 0,9 * * *`
- **Prompt:**

```
Use the draft-reply skill. Scan Outlook (mail sent to JP, awaiting his reply) and
Slack (threads needing a real decision or a deep technical CTO call). Return a short
"needs you" list, each item with one line on why and a ready draft run through the
comms-voice skill. Crisp, human, no em-dashes. Never send. Draft only.
```

> To run weekdays only, use `0 6,15 * * 1-5`.

---

## Before these work
1. **`IDEOGRAM_API_KEY`** set as an environment variable on this environment (exact
   name, no spaces). Needed by the LinkedIn image step.
2. **Outlook and Slack** connected and authorized for scheduled runs. OAuth MCP
   servers can be absent in headless runs, so confirm the first triage run sees them.
3. Skills live in `.claude/skills/` in this repo, so any session on this repo has them.
