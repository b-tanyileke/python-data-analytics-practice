# Python Data Analytics Practice Lab

Use this repository for ungraded Python Data Analytics practice. New material will be added week by week to support the course.

The activities and their solutions are visible to everyone. Please attempt an activity independently before viewing its solution.

## Getting started

### 1. Install Python

Install a current version of Python 3 from [python.org](https://www.python.org/downloads/).

- **Windows:** Select **Add Python to PATH** if the installer offers it.
- **macOS:** Use the official installer, or the Python 3 installation provided by your institution.
- **Linux:** Python 3 is often already installed. If it is not, install it using your distribution's package manager.

### 2. Download the repository

If you are comfortable with Git, clone the repository:

```text
git clone https://github.com/b-tanyileke/python-data-analytics-practice.git
cd python-data-analytics-practice
```

Alternatively, select **Code → Download ZIP** on GitHub and extract the downloaded folder.

### 3. Create and activate a virtual environment

A virtual environment keeps the tools used for this repository separate from other Python projects.

**Windows (PowerShell):**

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS or Linux (Terminal):**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

If `py` is not available on Windows, try `python` instead. Run `deactivate` when you are finished working in the virtual environment.

### 4. Install repository requirements

```text
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Any packages needed for future activities will be listed in `requirements.txt`.

## Repository layout

```text
python-data-analytics-practice/
├── README.md
├── requirements.txt
├── week-03/
│   └── README.md
└── .github/workflows/
    └── checks.yml
```
