# Claude Code Starter Kit

**→ Read the guide: https://phuazz.github.io/claude-code-starter-kit/**

A working example of the method: build things with Claude Code, host them free on GitHub Pages, and never re-explain yourself twice.

This kit is deliberately small. It contains one dashboard that actually works, and four text files that do most of the real work. Clone it, run it, then throw away my example and keep the structure.

The guide linked above is the same material as this README, laid out as a web page — and it is itself hosted by the mechanism it describes. This README is the version for people already reading the code.

---

## Part 1 — Install these four things first

Do these in order. Each takes a few minutes. You do not need to understand them yet.

### 1. Git

The tool that tracks every version of your files, so you can never permanently break anything.

- Windows: download from https://git-scm.com/download/win and accept every default.
- Mac: open Terminal and run `xcode-select --install`.

Check it worked. Open a terminal (Windows: search for "Git Bash"; Mac: "Terminal") and run:

```
git --version
```

You should see a version number. If you see "command not found", the install did not take — restart the terminal first, then re-install.

Then tell Git who you are, once, forever:

```
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

### 2. Python

Runs the build script that turns your data plus your template into the finished page.

- Download from https://www.python.org/downloads/
- **Windows: tick "Add Python to PATH" on the first screen.** This is the one box people miss, and skipping it causes every "python is not recognised" error you will hit later.

Check:

```
python --version     # Windows
python3 --version    # Mac
```

**On a Mac the command is `python3`.** Plain `python` does not exist and will say "command not found". Everywhere in this README you see `python`, type `python3` instead.

If Windows says it is not recognised, you missed the PATH box — re-run the installer and choose "Modify".

### 3. Node.js

You only need this for one command: a local web server, so you can look at your page before publishing it.

- Download the **LTS** version from https://nodejs.org/ and accept the defaults.

Check:

```
node --version
```

### 4. Claude Code

The thing that does the work.

You need a Claude account with a paid plan (Pro or Max). Then install:

```
npm install -g @anthropic-ai/claude-code
```

Check, and sign in when it prompts you:

```
claude
```

That opens Claude Code in whatever folder your terminal is currently in. **This matters more than it looks.** Claude Code can only see the folder you launched it from, and everything underneath it. Always `cd` into your project folder first, then run `claude`. Type `/exit` to leave.

### And one account: GitHub

Not an install, but you need it. Sign up free at https://github.com. This is where your code lives and where your finished pages get hosted, at no cost.

---

## Part 2 — Run this kit

In a terminal:

```
git clone https://github.com/<you>/claude-code-starter-kit.git
cd claude-code-starter-kit
python scripts/pipeline.py
npx serve docs
```

Open the URL it prints, usually http://localhost:3000. You should see the guide, with the working dashboard one click away.

Now the important part — look at what just happened:

- `template.html` is the **source**. It is small, and it is the only HTML you ever edit by hand.
- `data/metrics.json` is the **data**. Plain numbers, no code.
- `scripts/pipeline.py` is the **build**. It injects the data into the template and writes the result.
- `docs/demo.html` is the **output**. You never edit this. It is generated. It can be huge, and that is fine because nobody reads it.
- `docs/index.html` is the **guide** — hand-written, and the exception that proves the rule. Generated and hand-written pages coexist in `docs/` fine; you just have to know which is which, because you never hand-edit a generated one. In a project of your own there is usually no guide, and the build simply writes `docs/index.html`.

That split is the whole architecture, and it is why this stays cheap to maintain. When you change the look, you edit the template. When the numbers change, you edit the JSON. The two never fight.

You can also open `template.html` directly with `npx serve .` — it falls back to fetching `data/metrics.json` over HTTP, so it works standalone while you are developing. That fallback is worth keeping in anything you build.

---

## Part 3 — Publish it free

1. Create a new repository on GitHub. Do not add a README when it offers.
2. GitHub then shows you your repository URL. You cloned this kit, so your folder
   currently points at mine — this repoints it at yours:

```
git remote set-url origin https://github.com/<you>/<repo>.git
git add -A
git commit -m "Initial commit"
git push -u origin main
```

If the folder is your own and was never cloned, it has no remote yet, so use
`git remote add origin <url>` instead. If Git says `remote origin already
exists`, you want `set-url`.

**The first push asks who you are.** Do not type your GitHub password — it will
be rejected; GitHub removed password access for this years ago.

- **Windows:** nothing to do. Git for Windows ships Git Credential Manager, so a
  browser window opens, you sign in once, and it is remembered.
- **Mac:** Git has no such helper and the push simply fails. Install GitHub's
  CLI and log in once:

```
brew install gh
gh auth login
```

Choose **HTTPS** for the protocol, and answer **Y** when it offers to
authenticate Git with your GitHub credentials — that second answer is what makes
`git push` work. Once per machine, not once per project.

3. On GitHub: **Settings → Pages → Source: Deploy from a branch → Branch: `main`, folder: `/docs` → Save.**
4. Wait a minute. Your page is live at `https://<you>.github.io/<repo>/`.

That is it. Every time you push, the page updates. Free, permanent, no server.

---

## Part 4 — The actual method

Everything above is plumbing. This part is the reason the method works, and it is the part people skip.

**The productivity does not come from clever prompting.** It comes from four files that mean you never explain yourself twice. Every Claude Code session starts by reading them automatically, so it begins already knowing your rules instead of guessing.

### `CLAUDE.md` — your standing rules

Read automatically at the start of every session in this folder or any folder inside it. This is where you write down the things you would otherwise repeat in every conversation: how you want writing to sound, what your build command is, what Claude must never do.

The single highest-value line in mine is a guardrail:

> NEVER open any built output file larger than 500KB.

Because generated files are enormous, and one accidental read wastes the whole session. **Write your guardrails as rules, not as reminders you have to remember to give.** That is the difference between a setup that scales and one that does not.

Start small. Add a rule the moment you catch yourself correcting Claude twice on the same thing. That is the trigger. Mine grew to ~200 lines over months, purely by that rule, and I never sat down to write it.

### `PROMPT_TEMPLATE.md` — how to ask for work

A good prompt looks like a well-scoped engineering ticket, not a spell. Context, constraints, success criteria, output format. Everything else is decoration.

The file spells out what to leave out — personas, stakes, emotional framing, vague adjectives — and shows a before/after. The short version is worth internalising now:

> Project: <name>. Stage: <bug fix | new feature | tweak>.
> Change: <what>.
> Must: <the non-negotiables>.
> Show me the plan before you start.

That last line does more than the rest combined. It costs one turn and catches misunderstandings while they are still cheap.

### `KICKOFF_TEMPLATE.md` — how to start something new

The best trick in this kit. When you have a goal but not a spec, do not describe it badly and hope. Tell Claude to **interview you one question at a time** before writing any code.

You end up with a better-specified project than you would have written yourself, because you are answering questions rather than trying to imagine the whole thing up front.

### `design.md` — how it should look

One file with your colours, fonts, and layout rules. Reference it in a prompt ("style per `design.md`") and everything you build looks like it came from the same place, without you art-directing anything. Copy the token block verbatim into each project rather than inventing new values each time.

---

## Part 5 — Habits that matter more than they look

**Let it work, then check it.** Claude Code writes the file, runs the build, and reads the error. Your job is to check the output and push back — not to supervise each keystroke. Ask to see the plan on anything non-trivial; let the small stuff run.

**Commit constantly.** `git commit` after every working change. It is your undo button. Nothing you do is scary if the last good version is one command away.

**Every project gets a README.** Say what it is, how to build it, where the data comes from, what is broken. This is what you read when you come back in three months having forgotten everything, and it is the first thing Claude reads too. One file, two audiences.

**Push back.** When the output looks wrong, say so plainly. "That is wrong because X" gets a fix. "Hmm, not quite" gets a shuffle. The first pass gets you most of the way; the correction gets you the rest.

**Iterate across turns.** Do not try to one-shot the perfect prompt. Nobody does.

---

## What to do next

Do not start with something ambitious. Start by changing the numbers in `data/metrics.json`, running `python scripts/pipeline.py`, and watching the page change. That loop — edit, build, look — is the whole job. Everything else is detail.

Then delete my dashboard and ask Claude Code to build yours:

```
cd <your project folder>
claude
```

Then paste the Mode A interview prompt from `KICKOFF_TEMPLATE.md`, and answer the questions.
