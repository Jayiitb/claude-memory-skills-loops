---
name: linkedin-daily
description: Draft one daily LinkedIn post for JP (co-founder and CTO of bQ), grounded in fresh tech-trend research but written as his own founder journey, plus a matching image. Short, punchy, built for views and comments. Draft only, never post. Use for "today's LinkedIn post" or inside the linkedin-daily loop.
---

# linkedin-daily

Draft one strong LinkedIn post a day for JP. It is research-backed but reads as his
own voice and journey as a co-founder and CTO. Draft only. JP reviews and posts.

## What each post should feel like
- **His journey, first person.** A co-founder and CTO building bQ. Not a news report,
  not a brand account. "Here is what I am seeing / learning / deciding."
- A reader learns one real thing in under a minute, and wants to comment.
- Tied to something **live in tech today**, but the take is his.

## Steps

### 1. Research what is trending (do this fresh every run)
- Use WebSearch / WebFetch to find what is actually picking up in tech right now:
  AI agents, dev tooling, model releases, startup and founder topics, infra shifts.
- Pull 2 to 4 current threads. Note what is genuinely new or contrarian, not evergreen.
- Pick the one angle JP can speak to as a builder.

### 2. Pull a little real flavor from JP's world (read-only)
- Skim recent signals from his connected tools for an honest detail to ground the post:
  recent Slack threads, monday.com progress, Fireflies meeting themes, recent commits.
- Use it as texture only ("this week I was deep in X"). Keep it light and true.
- **Confidentiality guardrail:** never expose client names, customer data, revenue or
  internal numbers, unreleased plans, or anything private. When unsure, leave it out.

### 3. Draft using one template (see below)
- First person. Hook on line one. One idea. End with a line or question that pulls comments.
- Connect the trend (step 1) to his lived experience (step 2).

### 4. Image
- Write a tight image prompt, then run:
  `python scripts/ideogram_image.py "<image prompt>" out/linkedin-YYYYMMDD.png --aspect 1x1`
  (Needs `IDEOGRAM_API_KEY` in the environment.) Clean, bold, reinforces the one idea.
  Minimal, readable text on the image.

### 5. Voice pass and hand off
- Run all copy through the **comms-voice** skill: human, crisp, no em-dashes,
  no AI tells, no hashtag spam.
- Output: the post text, the image path, two alternate hooks, and one line citing the
  trend it is built on. Do not post.

## Templates

**1. Trend, my take**
```
Everyone is talking about <trend>.

Building bQ, here is what I actually see:

<2-3 short, specific lines from the trenches.>

<One line that reframes it.>

Are you seeing the same?
```

**2. The lesson (story to point)**
```
This week I <concrete moment / decision / mistake>.

What it taught me:

- <point>
- <point>

<One line takeaway.>

How would you have called it?
```

**3. The contrarian builder note**
```
Hot take: <common belief about the trend> is wrong.

As a CTO shipping with <X>, the opposite is true.

<2-3 short lines on why.>

What would change your mind?
```

## Hard rules
- **Never post.** Draft and hand off only.
- Research is mandatory. No generic, undated, evergreen filler.
- His voice, his journey. Trend is the hook, not the subject.
- Keep it tight. If it does not earn the read, cut it.

## Done means
- One first-person post + image + two alternate hooks + the trend it cites, ready
  for JP to review and post.
