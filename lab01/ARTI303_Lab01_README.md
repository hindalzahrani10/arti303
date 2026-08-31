# Lab 1 — Building Your AI Development Environment
**ARTI 303 — Programming for AI** · Week 1

## What's in this folder
- `README.md` — this file: setup, workflow, submission
- [lab01.ipynb](./ARTI303_Lab01_Starter.ipynb) — the actual lab content (Part B and Part C). Open this once your environment is working.

## What you'll do this session
- Install a Python toolchain (Python, VS Code, Git, Jupyter) with Google Colab as a no-install fallback
- Create the GitHub repository you'll build on all semester
- Learn the branch → commit → push → pull-request workflow used every week from now on
- Work through `lab01.ipynb`: variables, data types, operators, string formatting, and an AI-assisted coding checkpoint

Every lab this semester follows the same five stages: **Recall → Guided walkthrough → Your own work → AI checkpoint → Commit and log.** This week is the one exception — there's no previous week to recall, and "setup" means installing tools rather than syncing an existing repo. From Lab 2 onward, the standard rhythm applies every week.

## Before you start
- Windows 10/11, macOS, or Linux — or a department lab machine (ask your instructor if Python/VS Code/Git are already installed)
- An email, for GitHub + Kaggle
- About 90 minutes from scratch, ~30 if the tools below are already installed

---

## 1 · Install your tools

Work through these **in order** — later steps depend on earlier ones.

**Step 1 — Python.** Install **Python 3.12** from [python.org](https://python.org) — not the newest 3.14. Several data-science and deep-learning libraries used from Week 5 onward support 3.12/3.13 well before they support a brand-new release ([pyreadiness.org](https://pyreadiness.org) tracks this live). **Windows:** tick *"Add python.exe to PATH"* during install — the single most common setup failure.

**Step 2 — VS Code.** Install [VS Code](https://code.visualstudio.com), then install the official **Python** extension (Microsoft) from the Extensions panel.

**Step 3 — Git.** Install from [git-scm.com](https://git-scm.com), default options. On Windows this also installs Git Bash.

**Step 4 — Set up your terminal.** Every command below runs in VS Code's built-in terminal (`View → Terminal`, or `` Ctrl+` ``).

> **Windows — switch to Git Bash.** VS Code defaults to PowerShell, which doesn't understand several commands used this semester. Git Bash does, and behaves like a Mac/Linux terminal — so commands work identically for everyone in the room. In the terminal panel: dropdown arrow next to `+` → *Select Default Profile* → **Git Bash** → reopen the terminal.
>
> **macOS/Linux:** nothing to change.

**Step 5 — Find your Python command.**
```bash
python --version
python3 --version
```
Note whichever one prints `Python 3.12.x` — use that for the rest of the semester. Neither working? See [Troubleshooting](#troubleshooting).

**Step 6 — Git identity** (attached to every commit you make this semester):
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

**Step 7 — Notebook support:**
```bash
python -m pip install notebook ipykernel
```

**Step 8 — Colab fallback.** Open [Google Colab](https://colab.research.google.com), new notebook, run one cell: `print("Colab is working")`. Keep this tab open all semester as a backup.

**Step 9 — GitHub repo.**
1. Create a free account at [github.com](https://github.com).
2. Create a repo named `arti303-<your-student-id>-<lastname>`, e.g. `arti303-2231045-alharbi`.
3. Make sure it is (((Public))).
4. Clone it:
   ```bash
   git clone https://github.com/<your-username>/arti303-<your-id>-<lastname>.git
   ```

**Step 10 — Kaggle account.** Not needed until Week 5, but set it up now: create a free account at [kaggle.com](https://kaggle.com), then Account Settings → **Create New API Token** (downloads `kaggle.json`). **Don't commit this file** — Part A below `.gitignore`s it before it can be created.

---

## 3 · Do the lab

Copy `lab01.ipynb` from this folder into your repo's `notebooks/` folder, open it in VS Code, and work through Core → Stretch → Challenge, then the AI checkpoint. Each task has a self-check cell — an `AssertionError` means it isn't done yet. First time running a cell, VS Code will ask for a kernel: pick the Python 3.12 interpreter from Step 1.

**Done when:** every self-check prints "looks correct," and Restart Kernel + Run All completes with no errors.

## 4 · Submit

```bash
git checkout -b lab01
git add .
git commit -m "lab01: environment setup and Python basics"
git push -u origin lab01
```
Open a pull request `lab01 → main` on GitHub, then paste the PR link where your instructor asks for it.

**Checklist**
- [ ] `src/`, `notebooks/`, `docs/`, `requirements.txt`, `.gitignore`, `README.md` all present
- [ ] `README.md` has your name, student ID, section
- [ ] `notebooks/lab01.ipynb` runs top to bottom, all self-checks pass
- [ ] `docs/ai-log.md` has at least one entry
- [ ] `kaggle.json` is **not** tracked (`git status` should not show it)
- [ ] Commit messages describe the change, not "update"
- [ ] PR opened `lab01 → main`, link submitted

---


## Sources

Material and specific claims in this lab draw on:
- [Python documentation](https://docs.python.org) — language reference for Section 3 concepts
- [GitHub Docs](https://docs.github.com) — repository/authentication workflow, incl. the Personal Access Token requirement
- [pyreadiness.org](https://pyreadiness.org) — checked Aug 2026 to confirm current library support before recommending Python 3.12 over 3.14
