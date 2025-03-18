# Web Automation Framework with POM in Python(Selenium)

Search Google "Python selenium install" ==> https://pypi.org/project/selenium/
copy and pest in CMD and enter

selenium and web driver-manager

chrome driver search 
                                    
https://storage.googleapis.com/chrome-for-testing-public/131.0.6778.85/win64/chromedriver-win64.zip


### Tech Stack

- Python, PyTest
- Selenium
- Allure Report
- Gitignore, PyTest Report
- Page Object Model and Page Factory both
- Highlight element while run
- Parallel Run with xdist
- MY SQL data base connect to verify data.

### All the dependencies used
PIP install before executing pytest
- pip install pytest
- pip install selenium
- pip install pytest-html
- pip install allure-pytest
- pip install allure-pytest selenium
- pip install requests
- pip install pytest selenium pytest-html openpyxl
- pip install selenium-page-factory
- pip install pyyaml faker openpyxl
- pip install pytest-xdist
- pip install mysql-connector-python
- pip install pytest-reportportal
- pip install python-dotenv
- pip install selenium-page-factory
- pip install pyyaml
- pip install behave-to-cucumber
- pip install behave
- pip install requests pytest pytest-html faker allure-pytest jsonschema
- pip list
- pip install --upgrade pip
- pip install --upgrade selenium

### How to run the test case

pytest "path"

### How to run the mark test case

pytest -m "smoke" "path"

### How to run the pytest html report

pytest --html=report.html "path"

### How to run the Allure report

pytest "path" --alluredir=allure_results

### How to run the Allure report

allure serve allure-results

### How to run the Framework?

pytest -n auto "path"

### How to run Testcase parallel?

pytest -n auto "path"

### How to run the test case With parallel browser

pytest -n auto -s "path"

![Screenshot 2024-11-22 at 9 12 15 PM](https://github.com/user-attachments/assets/1108a0d3-2f71-472a-8121-f4f3d62f1291)

Dry Run Testcases

![Screenshot 2025-01-24 at 8 52 25 PM](https://github.com/user-attachments/assets/09bdd621-9e36-4787-846b-75a8332e0666)

File Explain:
A README.md file is typically used to provide information about your project,
including an overview, installation instructions, usage guidelines, and more.
It's written in Markdown, which is a lightweight markup language.