# claude-memory-skills-loops

bQ's working repo for **loop engineering** with Claude Code. Stop prompting, start
building loops that prompt Claude for you. Maintained by JP, CTO of Becoming Quotient.

## Contents
- **[`MEMORY.md`](./MEMORY.md)**: the knowledge spine. What loop engineering is and
  the five building blocks (goal, memory, skills, worktrees, sub-agents), distilled
  from the video *"Stop Prompting Claude. Start Loop Engineering."*
- **[`SKILLS_AND_LOOPS.md`](./SKILLS_AND_LOOPS.md)**: the build sheet of skills and
  loops for bQ, with build order and setup steps.
- **`.claude/skills/`**: reusable skills.
  - `comms-voice`: JP's writing-voice guard (human, crisp, no em-dashes).
  - `draft-reply`: triage Outlook + Slack + code, draft replies, never send.
  - `linkedin-daily`: draft a daily LinkedIn post plus image, never post.
  - `meeting-to-actions`: Fireflies meeting to monday.com items plus Slack recap.
- **`scripts/ideogram_image.py`**: LinkedIn image generation via Ideogram.

## House rules
- Draft, never send. Crisp and finite. Human voice, no em-dashes. Confirm before assuming.

## Secrets
Never commit keys. Set `IDEOGRAM_API_KEY` as an environment secret, not in code or chat.
