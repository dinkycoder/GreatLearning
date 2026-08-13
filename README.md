# MIT Applied AI and Data Science — Great Learning

Coursework, projects, and notes for the MIT Applied AI & Data Science program (via Great Learning).
Program catalog: https://olympus.mygreatlearning.com/courses?pb_id=19855

This is a single umbrella repository. Each course gets a numbered folder; each project gets its own
subfolder inside its course. Every project is self-contained (its own data, notebooks, source, and reports).

## Courses & Projects

| # | Course | Project | Status |
|---|--------|---------|--------|
| 01 | Python Foundations | [Project 1 — FoodHub EDA](01-python-foundations/project-1-foodhub-eda/) | In progress |

## Structure

```
mit-applied-ai-and-data-science/
├── README.md                          # this index
├── .gitignore                         # shared ignores (venvs, data-secrets, .claude)
└── NN-course-name/
    └── project-N-name/
        ├── data/        raw & processed datasets
        ├── notebooks/   analysis notebooks
        ├── src/         reusable scripts
        ├── reports/     rendered outputs (HTML, etc.)
        └── docs/        problem statement, notes
```

## Conventions

- **One virtual environment per project** to avoid library-version conflicts across courses.
- Prefix course folders with a two-digit number (`01-`, `02-`, …) to keep ordering.
- Keep each project's `README.md` describing its goal, data source, and how to run it.
