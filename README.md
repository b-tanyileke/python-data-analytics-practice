# Python Data Analytics Practice Lab

An ungraded practice repository for the Python Data Analytics course. New material will be added week by week to support learning alongside the course.

This repository is for practice, exploration, and discussion. It is not an assessment platform, and the solutions are intentionally visible. Please attempt each activity yourself before opening a solution.

## Current status

The repository structure and student setup guidance are ready. Week 3 activities will be added separately; there are no exercises to complete yet.

## Getting started

### 1. Install Python

Install a current version of Python 3 from [python.org](https://www.python.org/downloads/).

- **Windows:** During installation, select **Add Python to PATH** if the installer offers it.
- **macOS:** Use the official installer, or a Python 3 installation provided by your institution.
- **Linux:** Python 3 is often already installed. If it is not, install it using your distribution's package manager.

### 2. Download the repository

If you are comfortable with Git, clone the repository:

```text
git clone https://github.com/OWNER/python-data-analytics-practice.git
cd python-data-analytics-practice
```

Replace `OWNER` with the GitHub account or organization name shown in the repository URL. You may also use GitHub's **Code → Download ZIP** option, then extract the downloaded folder.

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

If `py` is not available on Windows, try `python` in its place. To leave the environment later, run `deactivate`.

### 4. Install repository requirements

```text
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

There are no third-party packages required in Step A, so this command is quick. Keep using it as the repository grows; any needed packages will be listed in `requirements.txt`.

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

## For the maintainer

`main` is the protected, release-ready branch. Make changes on `development` or a short-lived feature branch, open a pull request, let the automated checks finish, and merge through GitHub. Do not push directly to `main`.
# Python Data Analytics Practice Lab

An ungraded practice repository for the Python Data Analytics course. New material will be added week by week to support learning alongside the course.

This repository is for practice, exploration, and discussion. It is not an assessment platform, and the solutions are intentionally visible. Please attempt each activity yourself before opening a solution.

## Current status

The repository structure and student setup guidance are ready. Week 3 activities will be added separately; there are no exercises to complete yet.

## Getting started

### 1. Install Python

Install a current version of Python 3 from [python.org](https://www.python.org/downloads/).

- **Windows:** During installation, select **Add Python to PATH** if the installer offers it.
- **macOS:** Use the official installer, or a Python 3 installation provided by your institution.
- **Linux:** Python 3 is often already installed. If it is not, install it using your distribution's package manager.

### 2. Download the repository

If you are comfortable with Git, clone the repository:

```text
git clone https://github.com/OWNER/python-data-analytics-practice.git
cd python-data-analytics-practice
```

Replace `OWNER` with the GitHub account or organization name shown in the repository URL. You may also use GitHub's **Code → Download ZIP** option, then extract the downloaded folder.

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

If `py` is not available on Windows, try `python` in its place. To leave the environment later, run `deactivate`.

### 4. Install repository requirements

```text
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

There are no third-party packages required in Step A, so this command is quick. Keep using it as the repository grows; any needed packages will be listed in `requirements.txt`.

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

## For the maintainer

`main` is the protected, release-ready branch. Make changes on `development` or a short-lived feature branch, open a pull request, let the automated checks finish, and merge through GitHub. Do not push directly to `main`.
