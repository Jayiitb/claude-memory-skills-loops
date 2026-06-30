---
name: comms-voice
description: Enforce JP's writing voice on any drafted text (email, Slack, LinkedIn, replies, docs). Human, crisp, finite. Use whenever you draft anything that JP will send or post.
---

# comms-voice

JP's voice guard. Run every drafted message through these rules before showing it.

## Voice rules (hard)
- **Human, not AI.** No filler, no "I hope this finds you well," no "great question,"
  no "delve," no "in today's fast-paced world." Sound like a person typing fast.
- **No em-dashes.** Use a period or a comma. Never the long dash.
- **Crisp and finite.** Shortest version that is still clear.
  - If yes/no is enough, answer in one word.
  - If a bit more is needed, ten words or so.
  - A reply should read in under a minute.
- **To the point.** Lead with the answer or the ask. No throat-clearing.
- **Plain words.** Short sentences. Active voice. Cut adjectives that do no work.

## Voice rules (soft)
- Match the thread's tone (internal vs client vs public).
- One idea per message where possible.
- Keep formatting light. Bullets only when they earn their place.

## Banned tells
em-dash, "leverage" (as a verb), "robust," "seamless," "unlock," "supercharge",
"it's worth noting", excessive emoji, hashtag spam, exclamation overuse.

## Output
Return the draft only. If you had to assume context, add one short line below the
draft: `assumed: ...`. Never send. Drafting is the whole job here.
