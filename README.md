# JAN SUARJ Overseas Election Documentation

    This repository maintains the official documentation for the **JAN SUARJ Overseas Election** process.  
    It serves as a centralized source for election-related information, guidelines, governance rules, and historical election outcomes.
    
    The goal of this repository is to ensure **transparency, consistency, and accessibility** for all members involved in the election process.
    
    ---

## 📌 Purpose

    This repository documents and preserves:

    - Election guidelines and procedures
      - Roles and responsibilities of election officials
      - JAN SUARJ constitution and governance structure
      - Member information relevant to elections
      - Official results and records of each election cycle

---

## 📂 Repository Structure

    ├── guidelines/
    │ └── election-guidelines.md
    │
    ├── roles/
    │ └── election-roles-responsibilities.md
    │
    ├── constitution/
    │ └── jso-constitution.md
    │
    ├── members/
    │ └── member-details.md
    │
    ├── elections/
    │ ├── 2024/
    │ │ └── election-results.md
    │ ├── 2025/
    │ │ └── election-results.md
    │ └── archive/
    │
    └── README.md



# Steps to Run locally one time setup

## Install python

    python --version

## Create a Virtual Environment

    python -m venv venv

    source venv/bin/activate

## Install Documentation Dependencies

    pip install -r requirements.txt

## Verify Project Structure

    election-docs/
    │
    ├── docs/
    │   ├── index.md
    │   ├── guidelines/
    │   │   └── election-guidelines.md
    │   ├── roles/
    │   ├── constitution/
    │   ├── members/
    │   ├── elections/
    │      ├── 2026/
    │     
    │  
    │
    ├── requirements.txt
    └── .readthedocs.yaml

## Build Documentation Locally

    cd docs

### Build HTML:

    make clean
    make html

### Output will be generated in:

    docs/_build/html/

## Open the Documentation

    Open this file in your browser:
    docs/_build/html/index.html

## Auto-Rebuild While Editing

    sphinx-autobuild . _build/html

### Now your docs will be available at:
    http://127.0.0.1:8000/

## Things to Verify Locally
    Check that:
    
    ✅ Pages open correctly
    ✅ Links work
    ✅ Images load
    ✅ Folder navigation works
    ✅ Markdown renders properly

## Push to GitHub

    git add .
    git commit -m "Add documentation"
    git push
