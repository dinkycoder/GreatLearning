# EDA Project

Exploratory Data Analysis project.

## Directory Structure

```
.
├── data/
│   ├── raw/          # Original, immutable source datasets (place inputs here)
│   └── processed/    # Cleaned / feature-engineered analytical datasets
├── notebooks/        # Jupyter notebooks for analysis
│   ├── 01_univariate_analysis.ipynb
│   ├── 02_bivariate_analysis.ipynb
│   └── 03_multivariate_analysis.ipynb
├── reports/          # Generated outputs (HTML report, figures)
├── docs/             # Problem definition, data dictionary, notes
└── README.md
```

## Workflow

1. Define the problem, KPIs, and hypotheses (`docs/`)
2. Profile the raw data and build a data dictionary (`docs/`)
3. Construct the analytical dataset (`data/processed/`)
4. Clean and align the data
5. Univariate → bivariate → multivariate analysis (`notebooks/`)
6. Hypothesis testing
7. Synthesize insights into a final report (`reports/`)
