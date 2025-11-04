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
- Calculator provides the 4 arithmetic operations of addition, subtraction, multiplication and division

- Found in src/calculator.py

- Test coverage: 28 unit tests covering 100%

## CI Pipeline Implementation
- The CI pipeline is defined in the azure-pipelines.yml file and does the following

#### 1. Environment setup
```yaml
strategy:
  matrix:
    Python310:
      python.version: '3.10'

steps:
- task: UsePythonVersion@0
  inputs:
    versionSpec: '$(python.version)'
  displayName: 'Use Python $(python.version)'
```
- Sets up python 3.10 on the ubuntu VM (modified from the original python default yml file i just removed the other 3 versions since it was making 4 jobs)

#### 2. Dependency Installation
```bash
pip install -r requirements.txt
```
- Installs pytest, coverage, pylint, and pytest-cov.

#### 3. Test Execution with Coverage Enforcement
```bash
pytest --cov-fail-under=80
```
- runs all unit tests and generates coverage reports and enforces 80% coverage

#### 4. Coverage publishing 
```yaml
- task: PublishCodeCoverageResults@2
  inputs:
    codeCoverageTool: 'Cobertura'
    summaryFileLocation: '$(System.DefaultWorkingDirectory)/coverage.xml'
```
- Publishes coverage results to Azure pipelines UI for visibility

#### 5. Static code analysis
```bash
pylint src/ --exit-zero
```
- Runs pylint analysis on source code and publishes results as build artifact

### Pipeline triggers
- Pipeline automatically runs on every commit to 'main' and 'development'

## References

All external resources used in this project:

- pytest Documentation (2024) *pytest: helps you write better programs*. Available at: https://docs.pytest.org/ (Accessed: 1 November 2024).

- Coverage.py Documentation (2024) *Coverage.py*. Available at: https://coverage.readthedocs.io/ (Accessed: 1 November 2024).

- Pylint (2024) *Pylint User Manual*. Available at: https://pylint.pycqa.org/en/latest/ (Accessed: 4 November 2024).

- Microsoft (2024) *Azure Pipelines documentation*. Available at: https://docs.microsoft.com/en-us/azure/devops/pipelines/ (Accessed: 4 November 2024).

- Microsoft (2024) *Use Python Version task*. Available at: https://docs.microsoft.com/en-us/azure/devops/pipelines/tasks/tool/use-python-version (Accessed: 4 November 2024).

- Microsoft (2024d) *Publish Code Coverage Results task*. Available at: https://docs.microsoft.com/en-us/azure/devops/pipelines/tasks/test/publish-code-coverage-results (Accessed: 4 November 2024).

- Microsoft (2024) *Publish Build Artifacts task*. Available at: https://docs.microsoft.com/en-us/azure/devops/pipelines/tasks/utility/publish-build-artifacts (Accessed: 4 November 2024).