# 🧬 papers-fetcher

A Python CLI tool to fetch research papers from PubMed that include **at least one non-academic author** affiliated with a **pharmaceutical or biotech company**.

Built as part of a backend take-home project. This tool supports full PubMed query syntax, filters out academic-only papers, and outputs the result to console or CSV.

---

## 🚀 Features

- 🔎 Query PubMed using any valid search term  
- 🏢 Identify authors affiliated with **non-academic institutions** (e.g., biotech/pharma)  
- 📧 Extract corresponding author email (if available)  
- 📄 Export results to a structured CSV file  
- 🐍 Written in **typed Python**, modular and testable  
- 🧪 Includes unit tests for filters and utilities  

---

## 📦 Installation

### Clone & Run Locally

```
git clone https://github.com/your-username/papers-fetcher.git
cd papers-fetcher
python -m venv venv
venv\Scripts\activate  # On Windows
pip install -r requirements.txt
```

---

## 🧠 Usage

```
get-papers-list "cancer immunotherapy" --file results.csv --debug
```

### Arguments

| Name            | Required | Description                         |
|-----------------|----------|-------------------------------------|
| `query`         | ✅       | PubMed search term                  |
| `--file`, `-f`  | Optional | Output CSV file name                |
| `--debug`, `-d` | Optional | Show debug info during execution    |

---

## 📄 Example CSV Output

```
PubmedID,Title,Publication Date,Non-academic Author(s),Company Affiliation(s),Corresponding Author Email
40632497,Deciphering the MHC immunopeptidome...,2025,Suo S,Guangzhou National Laboratory...,N/A
...
```

---

## 🧱 Project Structure

```
papers-fetcher/
├── papers_fetcher/
│   ├── fetcher.py        # Fetch papers from PubMed
│   ├── filters.py        # Detect non-academic authors
│   ├── utils.py          # Email extraction, CSV export
├── cli/
│   └── main.py           # Typer-based CLI entry
├── tests/                # Unit tests
├── README.md
├── pyproject.toml        # Build & dependency config
```

---

## 🧪 Running Tests

Run all unit tests:

```
pytest
```

---

## 🧰 Tools Used

- [Typer](https://typer.tiangolo.com/) – for CLI interface  
- [Requests](https://docs.python-requests.org/) – for PubMed API calls  
- [lxml](https://lxml.de/) – for XML parsing  
- [pytest](https://docs.pytest.org/) – for unit testing  
- [Test PyPI](https://test.pypi.org/) – for test publishing  
- [twine](https://twine.readthedocs.io/) – for packaging  

---

## 🧠 Non-Academic Detection Heuristic

Authors are classified as **non-academic** if their affiliation does **not** include terms like:

- `university`, `college`, `institute`, `school`, `hospital`, `center`, `faculty`, etc.

This simple heuristic helps filter out academic institutions and highlight biotech/pharma contributors.

---

## 👤 Author

**Udaya I**  
