# CLAUDE.md — Working Specs

Claude Code reads this file automatically at the start of every session in this folder or any folder beneath it. Anything written here applies without being repeated. A `CLAUDE.md` inside a subfolder layers on top of this one and wins where the two conflict.

**How to use this template:** replace the bracketed parts, delete what does not apply, and keep it short at first. Add a rule the moment you catch yourself correcting Claude on the same thing twice. That is the only trigger you need. Do not try to write it all up front — it will be wrong, and you will not know which parts.

---

## Who I am

[One or two sentences. Your role, what you actually do, and the level you want to be spoken to at.]

Example: I am a [role] working on [domain]. Treat me as a peer who knows [field] well — do not re-explain basics. I am learning [the thing you are new at], so be explicit there.

## Context disambiguation

[Delete this section if you only have one context.]

If you work across genuinely separate contexts — different projects, employers, or a work/personal split — list them, and add:

> When a task could plausibly belong to more than one context, ask which applies before starting. Do not assume.

The same request means different things in different contexts. This one rule prevents most wasted work.

---

## Writing style

State your preferences as rules. These apply to every output — chat replies, drafted messages, documents, code comments, commit messages.

- [Contractions: allowed, or not.]
- [Spelling: British, American, or other.]
- **Tone.** [Concise and direct? Warm? Detailed?] Avoid hedging filler and breathless adjectives.
- **Format minimally.** Prose by default. Bullets and headers only when the content is genuinely list-shaped. Do not over-format short answers.

---

## How to work with me

- **Push back when you disagree.** If I propose something that looks wrong, say so directly with the reasoning. I would rather be corrected than agreed with.
- **Surface assumptions.** When you fill a gap in my instructions with a judgement call, say so inline so I can correct it.
- **Default to action over clarification.** On minor ambiguity, pick the most plausible reading, proceed, and note the assumption at the end. Ask only when the request is genuinely unanswerable without the missing piece.
- **Propose a plan upfront** for anything non-trivial. Do not start patching blindly.

---

## Project architecture

[Describe the shape of your projects so Claude does not have to work it out each time.]

```
project_name/
├── template.html          # Source. Small. The only HTML edited by hand.
├── data/                  # JSON data files
├── scripts/
│   └── pipeline.py        # Injects data into template.html → writes the built page
├── docs/
│   └── index.html         # Generated output. Never edited by hand. Often very large.
└── README.md              # What this is, how to build it, what is broken
```

**Build command:** `python scripts/pipeline.py`
**Local preview:** `npx serve docs` (full build) or `npx serve .` (source only, uses the fetch fallback)

### Hard rules

These are the guardrails. Write them as rules so they bind automatically, rather than as things you must remember to say.

- **NEVER open generated output larger than 500KB** (the built page in `docs/`). It wastes the session. Work on `template.html` instead. Name the generated file explicitly here so there is no ambiguity about which files in `docs/` are generated and which are hand-written.
- **Check file size before opening anything unfamiliar.** Over 200KB, stop and ask me to point you at the source file.
- **For files over 200KB, use `grep -n` to locate lines, view narrow line ranges, and patch with targeted replacements.** Never read the whole file into context.
- **Pattern consistency.** When fixing a pattern, apply the fix to every instance of that pattern, and audit for others before calling it done. Scope narrowly only when I ask for that explicitly.
- **Never commit credentials, API keys, or personal identifiers.** If in doubt, ask.

---

## Styling

- **Canonical design system: `design.md`.** Copy the token block and font link from there verbatim. If a project has drifted, correct it towards `design.md`, not the reverse. Add new shared values to `design.md` first, then use them.
- [Light or dark default. High contrast. Any other standing visual rule.]

---

## Approval calibration

Tell Claude what it may do without asking. This is the difference between a useful tool and one that interrupts you constantly.

- **Read-only inspection** (file reads, `git status`/`log`/`diff`, grep, builds) — proceed without asking.
- **Writes inside the project folder** — single approval.
- **Writes outside the project, network calls, installs** — single approval.
- **Destructive commands** (`rm`, `git reset`, `push --force`) — always ask individually, with an explicit warning.

---

## Session discipline

- **Start of session:** run `git pull --rebase origin main` to sync before starting work. Confirm the working tree is clean afterwards.
- **Sessions as units of work.** Define what "done" means at the start — usually two to four commits. Ship the last one, tidy up, and stop. Resist "one more thing" once the planned work is finished.

---

*Last updated: [date]*
