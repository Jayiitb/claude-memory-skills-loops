---
name: meeting-to-actions
description: Turn a meeting transcript into structured action items, owners, and due dates, then create monday.com items and post a Slack recap. Use when the user says "process the meeting", "turn the call into actions", or after a new Fireflies transcript is available.
---

# meeting-to-actions

Convert a meeting into trustworthy, owned, dated follow-through. Builder does the
extraction; a reviewer pass validates before anything is written anywhere.

## When to use
- "Process the latest meeting / call."
- "Turn this transcript into action items."
- Automatically, when a new Fireflies transcript lands (via a loop).

## Inputs
- A meeting reference (Fireflies transcript ID, or "the latest one").
- Optional: target monday.com board and Slack channel (otherwise ask once).

## Steps
1. **Fetch** the transcript and summary (Fireflies MCP tools).
2. **Extract** into a table: `decision | action item | owner | due date | source quote`.
   - Every action item MUST have an owner and a due date. If missing, infer a
     candidate and mark it `(needs confirmation)`.
3. **Review (separate pass / sub-agent):** verify each item is real (grounded in a
   transcript quote), de-duplicate against existing open monday.com items, and reject
   anything vague. The extractor does not grade its own output.
4. **Write** confirmed items to the monday.com board.
5. **Recap:** post a tight Slack message — decisions, owners + due dates, and any
   `(needs confirmation)` items flagged for a human.

## Done means
- monday.com has one item per confirmed action (no duplicates).
- Slack has a single recap message.
- Anything uncertain is surfaced, not silently written.

## Guardrails
- Never invent owners or dates without flagging them.
- Drafts/recaps over auto-sends where a human should glance first.
- If the transcript is ambiguous or empty, stop and ask.
