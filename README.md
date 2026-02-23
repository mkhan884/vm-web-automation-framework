# Web Automation Framework

This is a modular and scalable web automation testing framework built using **Python**, **Pytest**, and **Selenium WebDriver**. It follows the **Page Object Model (POM)** design pattern to ensure maintainability and reusability. **Allure** is integrated for generating detailed test execution reports.

---

## 🚀 Tech Stack

- **Language:** Python 3.x  
- **Test Runner:** Pytest  
- **Automation Tool:** Selenium WebDriver  
- **Design Pattern:** Page Object Model (POM)  
- **Reporting:** Allure Framework  

## 🧪 Features

- Clean separation of test logic using POM
- Readable and scalable test structure
- Integrated reporting with Allure
- Easy test execution via command line

## 🛠️ Project Structure

<pre> web-automation-framework/ 
├── tests/ # All test case files 
├── pages/ # Page Object Model classes 
├── utils/ # Utility functions (e.g., driver setup) 
├── reports/ # Allure reports output directory (generated after tests) 
├── conftest.py # Pytest fixtures and setup 
├── requirements.txt # Project dependencies 
├── run_tests.sh # bash script to run tests and auto save allure history
└── README.md # Project documentation
</pre>

## 🧰 Installation & Setup

1. **Clone the Repository:**

```bash
git clone https://github.com/your-username/web-automation-framework.git
cd web-automation-framework
```
2. **Install the requirements:**

```bash
pip install -r requirements.txt
```

## Running Tests Locally

Before running tests you need a working Python environment and
project dependencies installed.  From the workspace root:

```bash
# install dependencies once
pip install -r requirements.txt
```

Then run the suite in whichever granularity you need:

```bash
# run everything
pytest

# run a single test file
pytest tests/test_001.py

# run a single test function by node id or keyword
pytest tests/test_001.py::test_sign_up_flow
pytest -k sign_up_flow
```

The `run_tests.sh` helper script is a thin wrapper that adds the
Allure arguments and rerun options; you can use it interchangeably:

```bash
./run_tests.sh             # runs full suite with allure results
./run_tests.sh tests/test_002.py  # passes arguments through to pytest
```

The examples above are all local commands: they don’t require GitHub
Actions or any external services.  If you do want to reproduce the CI
environment, export `CI=true` before running, or use `act` as described
later in this document.

## Running Tests with Allure

```bash
pytest --alluredir=./allure-results
```

## Serve the Report

```bash
allure serve ./allure-results 
```

## Generate and Open the report

```bash
allure generate allure-results --clean -o allure-report
allure open allure-report
```

## Script to run and generate report
```bash
./run_tests.sh
```
