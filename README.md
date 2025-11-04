# ci-pipeline-ca

## Overview
Python calculator application demonstrating CI practices using GitHub and Azure Pipeline

## Technologies Used
-- Python 3.11.9
-- pytest 7.4.3
-- coverage.py 7.3.2
-- Pylint 3.0.2
-- Azure Pipelines
-- Github
-- Dependency management - pip w/ requirements.txt

## Local development setup
# Needs python 3.9 or higher, git and pip package manager

### Installation Steps
1. Clone the repo

2. Create & activate virtual environment
python -m venv venv
venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

4. Run tests
pytest

5. View coverage report
coverage html
open htmlcov\index.html

## Application Features
-Calculator provides the 4 arithmetic operations of addition, subtraction, multiplication and division

- Found in src/calculator.py

- Test coverage: 28 unit tests covering 100%

## References

All external resources used in this project:

- pytest Documentation (2024) *pytest: helps you write better programs*. Available at: https://docs.pytest.org/ (Accessed: 1 November 2024).

- Coverage.py Documentation (2024) *Coverage.py*. Available at: https://coverage.readthedocs.io/ (Accessed: 1 November 2024).