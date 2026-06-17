# portfolio-qa — Akanksha Yadav

> A QA Engineer's personal portfolio that tests itself.

[![Playwright Tests](https://github.com/akanksha-yadav04/portfolio-qa/actions/workflows/playwright-tests.yml/badge.svg)](https://github.com/akanksha-yadav04/portfolio-qa/actions/workflows/playwright-tests.yml)

## 🌐 Live Site
**[akanksha-yadav04.github.io/portfolio-qa](https://akanksha-yadav04.github.io/portfolio-qa)**

## 📊 Test Report
**[View Latest Test Report →](https://akanksha-yadav04.github.io/portfolio-qa/test-report)**

---

## What makes this different

Most portfolio sites just list skills. This one *demonstrates* them.

Every push to `main` triggers a Playwright test suite via GitHub Actions that tests the site itself — nav links, section visibility, mobile viewport, UI elements. The HTML report is auto-published and linked from the live site.

---

## Tech Stack

| Layer | Tool |
|---|---|
| Site | HTML + CSS (vanilla) |
| Tests | Playwright + Python + Pytest |
| CI/CD | GitHub Actions |
| Reporting | pytest-html |
| Hosting | GitHub Pages |

---

## Project Structure

```
portfolio-qa/
├── index.html              # Main portfolio site
├── style.css               # Styling
├── script.js               # Nav interactions
├── requirements.txt        # Python deps
├── tests/
│   ├── conftest.py         # Playwright browser config
│   └── test_homepage.py    # 10 automated tests
└── .github/
    └── workflows/
        └── playwright-tests.yml   # CI pipeline
```

---

## Running tests locally

```bash
# Install dependencies
pip install -r requirements.txt
playwright install chromium

# Run tests
pytest tests/ -v

# Run with HTML report
pytest tests/ -v --html=report/index.html --self-contained-html
```

---

## What the tests cover

- ✅ Page title validation
- ✅ Hero heading visibility
- ✅ Navigation links count
- ✅ All sections present (About, Skills, Projects, AI Testing, Contact)
- ✅ Skills cards count (6)
- ✅ AI Testing cards count (4)
- ✅ Mobile viewport — no horizontal overflow
- ✅ Footer visibility

---

## AI Testing section

The portfolio includes a dedicated section on testing AI/LLM products:
- Non-deterministic output testing
- RAG pipeline validation (RAGAS metrics)
- Prompt injection testing
- Hallucination detection

---

*Built by Akanksha Yadav · Tested by Playwright · Deployed via GitHub Actions*
