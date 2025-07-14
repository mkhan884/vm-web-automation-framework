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

project-root/
│
├── tests/ # All test files
├── pages/ # Page object classes
├── utils/ # Utility functions or drivers
├── allure-reports/ # Allure reports directory (generated after tests)
├── conftest.py # Pytest fixtures and setup
├── requirements.txt # Python dependencies
└── README.md

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

## Running Tests

```bash
pytest
```

## Running Tests with Allure

```bash
pytest --alluredir=./allure-results
```

## Generate and Open the Report

```bash
allure serve ./allure-results 
```