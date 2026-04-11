# AREC 261: Agricultural Data Analytics I

Source repository for the AREC 261 textbook at the University of Saskatchewan. Built with [Quarto](https://quarto.org/) and published via GitHub Pages.

**Live site:** <https://pjs998.github.io/arec261-textbook/>

## About

AREC 261 is a two-term undergraduate sequence in agricultural data analytics. This repo contains the textbook for the first term (AREC 261 — Foundations and Inference), covering descriptive statistics, Excel, R, visualization, probability, simulation, and inference through modules 1 through 12.

The second-term textbook for AREC 262 (Modelling, Forecasting, and Decision Analytics) will live in a separate repository.

## Repo layout

```
.
├── _quarto.yml           # Book config (chapters, sidebar, theme)
├── index.qmd             # Preface
├── intro.qmd             # Introduction
├── module01.qmd ... module12.qmd
├── references.qmd        # References chapter
├── references.bib        # BibTeX bibliography
├── practice/             # Practice questions and auto-quiz site
│   ├── module01_practice.qmd
│   ├── generate_data.py
│   ├── data/             # Synthetic CSVs for practice
│   └── quiz/             # Random-draw quiz page (HTML + JSON)
└── .github/workflows/    # Auto-render on push
```

## Building locally

You need [Quarto](https://quarto.org/docs/get-started/) installed.

```bash
# Render the full book to _book/
quarto render

# Preview with live reload
quarto preview
```

## Publishing

The book auto-publishes on every push to `main` via the GitHub Actions workflow in `.github/workflows/publish.yml`. To publish manually:

```bash
quarto publish gh-pages
```

## Contributing

This is a work in progress. Errors, unclear passages, and suggestions are welcome — please open an issue or pull request.

## License

Textbook content is © Peter Slade 2026. Course materials are released for educational use. Specific licensing terms TBD.

AI tools were used for brainstorming, drafting, and editing. The author is responsible for all errors.
