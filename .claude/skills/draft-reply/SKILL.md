---
name: draft-reply
description: Detect things that genuinely need JP (CTO of bQ) and draft a crisp reply in his voice, across Outlook, Slack, and coding problem statements. Always draft, never send. Use when asked to "triage", "draft replies", "what needs me", or inside the attention-triage loop.
---

# draft-reply

Find what needs the CTO, then hand JP a ready reply. Drafting only. Never send on
any platform.

## What counts as "needs JP"
- **Outlook:** mail sent to him personally and awaiting his reply. Skip newsletters,
  CCs, automated notices, FYIs.
- **Slack:** threads where a decision, a thought process, or a deep technical CTO
  call is required. Skip chatter and threads already handled by others.
- **Coding sessions:** when there is a real problem statement to think through, draft
  the reasoning or the response.

## Steps
1. Pull the items (Outlook MCP / Slack MCP). Filter to the "needs JP" set above.
2. For each, write a one-line "why this needs you."
3. Draft the reply. Run it through the **comms-voice** skill (human, crisp, no
   em-dashes, yes/no or about ten words when that is enough, one-minute read).
4. Present as a short list: source, who, why, and the draft. Nothing else.

## Hard rules
- **Never send.** No `send_message`, no email send, no Slack post. Drafts only.
- Keep every draft as short as the situation allows.
- If a reply needs info you do not have, say so in one line instead of inventing it.

## Done means
- A short, scannable list of only the items that need JP, each with a ready draft.
- Zero messages sent anywhere.
