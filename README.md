# Continuous Testing Pipeline Using GitHub Actions

An automated Continuous Integration (CI) and Continuous Testing pipeline built using Python, `pytest`, Git, and GitHub Actions for the Software Testing and Quality Assurance (STQA) practical curriculum.

---

## 📌 Project Overview
Continuous Testing is a software testing practice where automated tests are executed as part of the software delivery pipeline to obtain immediate feedback on the business risks associated with a software release candidate.

In this project, whenever a developer makes changes and pushes code to GitHub (or creates a Pull Request), a GitHub Actions runner automatically spins up in the cloud, checks out the code, sets up the Python environment, installs dependencies, and runs the entire automated test suite.

---

## 🗂️ Project Directory Structure

```text
continuous-testing-pipeline/
├── .github/
│   └── workflows/
│       └── python-tests.yml   # GitHub Actions CI workflow definition
├── .gitignore                 # Files and folders to exclude from Git
├── calculator.py              # Application source code (Calculator logic)
├── test_calculator.py         # Automated test cases using pytest
├── requirements.txt           # Project dependencies (pytest)
└── README.md                  # Comprehensive project documentation
```

---

## ⚙️ Prerequisites & Tech Stack
- **Language:** Python 3.12+
- **Test Framework:** `pytest`
- **Version Control:** Git & GitHub
- **CI/CD Platform:** GitHub Actions
- **IDE:** Visual Studio Code
- **Operating System:** Windows

---

## 🚀 Local Setup and Execution

### 1. Open the Project in VS Code
Open VS Code, press `Ctrl + ~` to open the integrated terminal.

### 2. Create and Activate a Virtual Environment
```powershell
# Create a virtual environment named .venv
python -m venv .venv

# Activate the virtual environment on Windows PowerShell
.\.venv\Scripts\Activate.ps1
```

> **Note:** If PowerShell displays an `Execution_Policies` script restriction error, run:
> ```powershell
> Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
> ```
> and run the activate command again.

### 3. Install Dependencies
```powershell
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Run the Automated Tests Locally
```powershell
pytest -v
```

Expected output:
```text
============================= test session starts =============================
collected 12 items

test_calculator.py::test_add_positive_numbers PASSED                    [  8%]
test_calculator.py::test_add_negative_numbers PASSED                    [ 16%]
test_calculator.py::test_add_with_zero PASSED                           [ 25%]
test_calculator.py::test_add_floating_point PASSED                      [ 33%]
test_calculator.py::test_subtract_positive_numbers PASSED               [ 41%]
test_calculator.py::test_subtract_negative_numbers PASSED               [ 50%]
test_calculator.py::test_subtract_resulting_in_negative PASSED          [ 58%]
test_calculator.py::test_multiply_positive_numbers PASSED               [ 66%]
test_calculator.py::test_multiply_by_zero PASSED                        [ 75%]
test_calculator.py::test_multiply_negative_numbers PASSED               [ 83%]
test_calculator.py::test_divide_valid_numbers PASSED                    [ 91%]
test_calculator.py::test_divide_negative_numbers PASSED                 [100%]
test_calculator.py::test_divide_by_zero_raises_exception PASSED         [100%]

============================== 12 passed in 0.05s ==============================
```

---

## 🔄 GitHub Actions CI Pipeline Explanation

The workflow is defined in `.github/workflows/python-tests.yml`:
1. **Trigger (`on:`):** Activates on every `git push` to `main`, every `pull_request` to `main`, or manually via `workflow_dispatch`.
2. **Runner (`runs-on: ubuntu-latest`):** GitHub provisions an isolated cloud virtual machine running Ubuntu.
3. **Checkout (`actions/checkout@v4`):** Downloads the repository code onto the runner.
4. **Python Setup (`actions/setup-python@v5`):** Installs Python 3.12 and sets up pip caching.
5. **Install Dependencies:** Upgrades pip and runs `pip install -r requirements.txt`.
6. **Execute Tests:** Runs `pytest -v`. If all tests pass, the pipeline turns **Green (Success)**. If any test fails, it halts and marks the build **Red (Failure)**, alerting the team.

---

## 🧪 Experiments for Practical Evaluation

### Experiment A: Successful Pipeline Run
- Keep all tests valid in `test_calculator.py`.
- Push to GitHub: `git push origin main`.
- View the green checkmark under the **Actions** tab in GitHub.

### Experiment B: Failed Pipeline Run (Demonstrating Quality Gate)
- Modify `calculator.py` or `test_calculator.py` with an incorrect assertion (e.g. `assert add(2, 3) == 6`).
- Commit and push: observe GitHub Actions immediately flagging the failure and preventing broken code from slipping through.
- Revert the bug and push again to restore green status.
