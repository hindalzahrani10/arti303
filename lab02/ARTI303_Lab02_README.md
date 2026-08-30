# Lab 2 — Conditions, Loops, Functions & Your First Module
**ARTI 303 — Programming for AI** · Week 2

## What's in this folder
- `README.md` — this file: what to build in Part A, workflow, submission
- `lab02.ipynb` — Part B and Part C: tests the module you build here, in the notebook

## What you'll do this session
- Build `src/students.py` — the first module in your repository that another file *imports*, rather than a notebook you just run top to bottom
- Practice conditionals, loops, and functions by extending that module yourself
- Review Python's approach to classes — and why it looks different from the C++ classes you already know
- Run an AI checkpoint that compares your class against an AI-generated one, attribute access vs. getters/setters

Class starts with a few quick recall questions on Lab 1 — no prep needed, just show up with a working repo from last week.

## Before you start
- [ ] `lab01.ipynb` still runs top to bottom with no errors (Restart Kernel and Run All)
- [ ] `git pull origin main` — make sure you have anything you might be missing
- No new installs this week.

```bash
git checkout main
git pull origin main
git checkout -b lab02
```

---

## Part A · Guided walkthrough — build the `Student` class

Follow along with your instructor. In VS Code, create `src/students.py`
and type this in:

```python
"""Student record utilities for ARTI 303."""


class Student:
    """A single student record."""

    def __init__(self, name, age, gpa, is_enrolled=True):
        self.name = name
        self.age = age
        self.gpa = gpa
        self.is_enrolled = is_enrolled

    def is_dean_list(self):
        """Return True if this student's GPA qualifies for the Dean's list."""
        return self.gpa >= 3.5

    def report_line(self):
        """Return a one-line, human-readable summary of this student."""
        status = "made the Dean's list" if self.is_dean_list() else "did not make the Dean's list"
        enrollment = "is enrolled" if self.is_enrolled else "is not enrolled"
        return f"{self.name} (age {self.age}, GPA {self.gpa:.2f}) {enrollment} and {status}."

    def __repr__(self):
        return f"Student(name={self.name!r}, age={self.age}, gpa={self.gpa})"
```

A few things worth noticing:
- No `private` fields, no explicit getters/setters — Python attributes are public by default. `student.name` is idiomatic; writing `student.get_name()` isn't needed here. (Part C comes back to this.)
- `self` is always the first parameter, always explicit — Python never hides it the way C++'s implicit `this` does.
- `__repr__` is what prints when you type a `Student` object directly, or print a list of them — without it you'd see `<students.Student object at 0x...>`, which tells you nothing.

**Checkpoint:** copy `lab02.ipynb` from this folder into your repo's `notebooks/` folder, open it, and run the first two cells. You should see a `Student` printed with a real name and report line. If you get an import error, see [Troubleshooting](#troubleshooting).

---

## Part B & Part C · Your own work

Open `notebooks/lab02.ipynb` and work through it there — it's the actual content for this lab. In short, you'll:

- **Core:** add three functions to `students.py` — `average_gpa`, `dean_list_students`, `letter_grade` — each with a self-check cell in the notebook
- **Stretch:** add GPA validation to `__init__`, plus `oldest_student` and `group_by_enrollment`
- **Challenge:** design and add one function of your own — no fixed answer
- **AI checkpoint:** compare an AI-generated `Student` class (with getters/setters) against the one you built here

**Important:** every time you change `students.py`, save it, then **Restart Kernel and Run All** in the notebook — Python caches the module on import, so editing the file alone won't update what the notebook sees.

**Done when:** every self-check cell prints "looks correct," and Restart Kernel + Run All completes with no errors.

---

## Submit

```bash
git add .
git commit -m "lab02: students module — conditions, loops, functions, OOP review"
git push -u origin lab02
```
Open a pull request `lab02 → main`, paste the link where your instructor asks for it.

**Checklist**
- [ ] `src/students.py` has all Core + Stretch functions, plus your own Challenge addition
- [ ] `notebooks/lab02.ipynb` runs top to bottom, all self-checks pass
- [ ] `docs/ai-log.md` has a new entry for this lab
- [ ] Commit message describes the change
- [ ] PR opened `lab02 → main`, link submitted

---

## Troubleshooting

| Symptom | Fix |
|---|---|
| `ModuleNotFoundError: No module named 'students'` | Check `lab02.ipynb` is actually inside `notebooks/`, as a sibling of `src/` — the import assumes that exact layout |
| Edited `students.py` but the notebook still shows old behaviour | Restart Kernel and Run All — imports are cached, editing the file alone doesn't reload it |
| `TypeError: is_dean_list() takes 0 positional arguments but 1 was given` | You're missing `self` as the first parameter of a method — every method needs it, even if unused |
| A method "doesn't exist" but you're sure you wrote it | Check its indentation — a method indented one level too far *left* becomes a separate top-level function, not part of the class |
| `letter_grade` returns the wrong grade for a boundary value like exactly `3.7` | Check your chain is `elif`, not separate `if` statements, and that thresholds are checked highest-first |
| `ValueError` isn't raised for an out-of-range GPA | Confirm the check is the *first* line inside `__init__`, before `self.gpa = gpa` — otherwise invalid data gets assigned before you catch it |

Still stuck after five minutes? Ask your instructor.

---

## Sources

- [Python documentation — Classes](https://docs.python.org/3/tutorial/classes.html) — reference for this week's OOP content
- [PEP 8](https://peps.python.org/pep-0008/) — naming and style conventions followed in `students.py`
