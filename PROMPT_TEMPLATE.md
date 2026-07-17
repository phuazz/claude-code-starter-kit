# Prompt Template Reference

How to ask Claude Code for work. Two versions: the full template for new builds and significant changes, the short one for patches. For a new project whose spec is not yet formed, start from the interview mode in `KICKOFF_TEMPLATE.md` instead — it has Claude scope the work with you before anything gets written.

---

## Short template (small patches, quick fixes)

Use this for most things. It is four lines and it is usually enough.

```
Project: <name>. Stage: <bug fix | new feature | tweak>.
Change: <what should be different>.
Must: <the non-negotiables>.
Show me the plan before you start.
```

That last line is doing most of the work. It costs one turn and catches a misunderstanding while it is still cheap to fix.

---

## Full template (new builds, significant refactors)

```
[CONTEXT]
- Project: <name>
- Stage: <new build | new feature | bug fix | refactor | data update>
- Architecture: template.html + data/*.json + scripts/pipeline.py → docs/
- Local test: npx serve .

[WHAT I AM CHANGING]
- Component: ...
- What it should do: ...
- What it currently does (if this is a bug): ...

[DATA SPEC]
- Input: <where the data comes from, what shape it is in>
- Expected output shape: <JSON structure>
- Source of truth: <the file or API that decides what is correct>

[SUCCESS CRITERIA]
- Must: ...
- Must: ...
- Nice to have: ...
- Out of scope: ...

[CONSTRAINTS]
- Flag before editing any file >200KB; ask for the source file instead
- <Your standing visual rules — theme, contrast>
- <Anything that must not break>

[OUTPUT FORMAT]
- Multi-turn plan upfront if the scope is non-trivial
- Patches via grep anchors and targeted replacements, not full-file rewrites
- Show the plan and the anchors before patching
```

Most of these fields collapse to one line each. The template is a checklist for you, not an essay to fill in.

---

## Add-ons

### For code review, append:

```
[REVIEW AXIS]
Review for: <robustness | performance | readability | specific failure modes>
Specifically look for: <three to five concrete things>
Flag anything uncertain rather than papering over it.
```

### For anything with a correctness risk, append:

```
Before writing code, state the three ways this could be silently wrong.
Then address each one in the implementation.
```

"Silently wrong" is the key phrase. Loudly wrong is easy — it crashes. The dangerous failures are the ones that produce a plausible number that is not true, and asking for them by name up front surfaces them while they are still hypothetical.

---

## What to leave out

Skip these entirely. They are decoration, not instruction.

- Personas — "you are a world-class engineer", "act as a senior developer"
- Stakes and incentives — "this is critical", "I will tip you $200"
- Emotional framing — "take a deep breath", "I bet you cannot"
- Vague adjectives without checklists — "rigorous", "thorough", "best-in-class"
- Self-confidence scoring — "rate your answer 0-1"

The test: **if a phrase does not change what a correct output would look like, it is decoration.** Replace adjectives with checklists. "Rigorous review" becomes the three specific things rigour means in this case.

---

## Before and after

### Before — theatre

> Act as a world-class engineer. This is critical work. Take a deep breath and
> rigorously review my data pipeline for robustness. I bet you cannot find real issues.

### After — actual instruction

> Review the data pipeline. Check specifically:
> (1) what happens when the input JSON is missing a field,
> (2) whether dates are parsed with a library rather than string slicing,
> (3) month and year boundary handling,
> (4) what happens on an empty input file,
> (5) whether the build fails loudly or writes a broken page.
> Flag anything uncertain rather than papering over it.

Same length. Zero persona. Dramatically better output, because every clause constrains what "done" looks like.

---

## The meta-rule

A good prompt looks like a well-scoped engineering ticket, not a spell. Context, constraints, success criteria, output format. The rest is noise.

Iterate across turns rather than trying to one-shot a perfect prompt. The first pass gets you most of the way; the pushback gets you the rest. Nobody writes the perfect prompt first time, and trying to is slower than correcting a draft.
