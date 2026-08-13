# MIT Applied AI and Data Science — Great Learning

Coursework, projects, and notes for the MIT Applied AI & Data Science program (via Great Learning).
Program catalog: https://olympus.mygreatlearning.com/courses?pb_id=19855

This is a single umbrella repository. Each course gets a numbered folder; each project gets its own
subfolder inside its course. Every project is self-contained (its own data, notebooks, source, and reports).

## Courses & Projects

| # | Course | Project | Status |
|---|--------|---------|--------|
| 01 | AI-Assisted Coding and Data Analysis | [Project 1 — FoodHub EDA](Course01-AI-assisted-coding-and-data-analysis/project-1-foodhub-eda/) | In progress |
| 02 | Machine Learning | _none yet_ | Not started |

## Structure

```
mit-applied-ai-and-data-science/
├── README.md                          # this index
├── .gitignore                         # shared ignores (venvs, data-secrets, .claude)
└── CourseNN-course-name/
    └── project-N-name/
        ├── data/        raw & processed datasets
        ├── notebooks/   analysis notebooks
        ├── src/         reusable scripts
        ├── reports/     rendered outputs (HTML, etc.)
        └── docs/        problem statement, notes
```

## Conventions

- **One virtual environment per project** to avoid library-version conflicts across courses.
- Prefix course folders with `Course` + two digits (`Course01-`, `Course02-`, …) to keep ordering.
- Keep each project's `README.md` describing its goal, data source, and how to run it.
