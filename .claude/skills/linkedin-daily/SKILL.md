---
name: linkedin-daily
description: Draft one daily LinkedIn post for JP (CTO of bQ) plus a matching image, in a short, punchy, thought-provoking style built for views, impressions, and comments. Draft only, never post. Use when asked for "today's LinkedIn post", "draft a LinkedIn post", or inside the linkedin-daily loop.
---

# linkedin-daily

Draft one strong LinkedIn post a day for JP. Short, sharp, makes people think.
Draft only. JP reviews and posts himself.

## Goal of each post
- A reader learns one real thing in under a minute.
- It provokes thought and invites a comment.
- It reads like JP (a CTO), not like marketing or AI.

## Style
- Run all copy through the **comms-voice** skill. Human, crisp, no em-dashes.
- Very few sentences. Each one short. Hook on line one.
- One idea per post. End with a question or a sharp line that pulls comments.
- No hashtag spam (0 to 3, only if they help). No emoji walls.

## Steps
1. **Topic.** Use a topic JP gives. If none, pick one from his world: engineering
   leadership, AI agents and loops, building bQ, hard technical calls, team and craft.
2. **Draft** using one template below.
3. **Image brief + image.** Write a tight image prompt, then run:
   `python scripts/ideogram_image.py "<image prompt>" out/linkedin-YYYYMMDD.png --aspect 1x1`
   (Needs `IDEOGRAM_API_KEY` set as an env secret.) Image should be clean, bold,
   and reinforce the one idea. Readable text on image, minimal words.
4. **Hand off.** Show the post text, the image path, and 2 alternate hooks. Do not post.

## Templates

**1. The contrarian take**
```
Most people think <common belief>.
After <experience>, I think the opposite.

<2-3 short lines on why.>

<One line that reframes it.>

What would change your mind?
```

**2. The lesson (story to point)**
```
<One concrete moment / number / mistake.>

Here is what it taught me:

- <point>
- <point>
- <point>

<One line takeaway.>

Have you seen the same?
```

**3. The framework**
```
<Problem> in 3 steps:

1. <step>
2. <step>
3. <step>

Simple, not easy.

Which step do teams skip most?
```

**4. The build-in-public note**
```
Building bQ taught me <one thing> this week.

<2-4 short lines, honest, specific.>

<One line forward.>

Curious how others handle this.
```

## Hard rules
- **Never post.** No LinkedIn send. Draft and hand off only.
- Keep it tight. If it does not earn the read, cut it.

## Done means
- One post draft + image file + two alternate hooks, ready for JP to review and post.
