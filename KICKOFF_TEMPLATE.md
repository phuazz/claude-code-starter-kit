# Kickoff Template

How to start something new. Copy this to `KICKOFF_<project>.md`, fill in the placeholders, and keep it **outside** the project folder — it is your brief, not part of the code.

Two modes. Use **Mode A** when you have a goal but not a spec — this is most of the time, and it is the more useful of the two. Use **Mode B** when you already know exactly what you want.

## Setup

```
cd <your project folder>
claude
```

Then paste one of the prompts below.

---

## Mode A — Interview first (the spec is not formed yet)

This is the best trick in the kit. When the idea is real but vague, do not describe it badly and hope. Make Claude interview you.

You end up with a better-specified project than you would have written alone, because answering a pointed question is far easier than imagining the whole thing up front.

```
We are starting a new <build | tool | dashboard | script> at <path>.
I have the goal but not a full spec. Before proposing any code or plan, interview
me to scope it — ONE question at a time, waiting for my answer before the next.

Cover, in roughly this order, and stop asking about an item once it is settled:
- Objective: the one decision or output this must produce.
- Users: who looks at this, and what they do differently as a result.
- Data: what goes in, where it comes from, what shape it is in, how often it changes.
- Success criteria: what "done" looks like — must-haves, nice-to-haves, out of scope.
- Constraints: anything that must not break, and any standing rules that bind here.
- Failure modes: the three ways this could be silently wrong, and the guard for each.

Ask only what you cannot reasonably infer. Where you can infer, state the assumption
and move on rather than asking. Do not write code during the interview. When the spec
is settled, output (1) the completed Full template from PROMPT_TEMPLATE.md and (2) a
multi-turn plan, then stop and wait for my go-ahead. Push back if any answer looks wrong.
Read README.md and CLAUDE.md in this folder first.
```

Two things make this work, and both are easy to drop:

**"ONE question at a time, waiting for my answer."** Without it you get twenty questions in a wall of text and you answer none of them properly.

**"Do not write code during the interview... then stop and wait for my go-ahead."** Without it, enthusiasm takes over and you are reviewing an implementation of the wrong thing.

---

## Mode B — Full spec (you already know what you want)

Fill in the Full template from `PROMPT_TEMPLATE.md`. Skeleton:

```
We are starting/continuing <project> at <path>. Read README.md and CLAUDE.md
here first.

Before writing code, state the three ways this could be silently wrong and the
guard for each.

Session goal — <one line>, in this order:
1. ...
2. ...
3. ...

Hold to: <project-specific non-negotiables>. Push back if any step looks wrong
rather than pressing on.
```

---

## Why the brief lives outside the project

Two reasons. The brief is often longer than the code and would clutter the repo. More importantly, it is a record of *why* you decided what you decided — which outlives the code, and which you will want when you come back in six months wondering what you were thinking.
