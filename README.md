# First Python browser test

This learning project uses Selenium and pytest to open https://example.com/
and verify the page title, visible English description, and Learn more link.
It opens a separate Chrome session and closes that session after the test.

## Set up in VS Code

Install Python 3.11 or later and Chrome. Open this folder in VS Code.
In the VS Code PowerShell terminal, run:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pytest
```

For VS Code's Testing panel, use the Microsoft Python extension and select
`.venv\Scripts\python.exe` with **Python: Select Interpreter**.

To run without a visible browser window and produce a JUnit report:

```powershell
$env:HEADLESS = '1'
.\.venv\Scripts\python.exe -m pytest --junitxml=reports/results.xml
Remove-Item Env:HEADLESS
```

The first run needs network access for packages and the matching Chrome driver.
If `py` refers to a missing Python installation, repair Python or use the full
path to a working Python executable in place of `py -3`.

## How to read the test

Open `tests/test_example_domain.py`. `driver.get` opens the page,
`WebDriverWait` waits for the description, and the `assert` statements check
the expected results. The `finally` block closes the test browser even if a check fails.

## Skye status

This project includes a draft `.skye-runner.yml` for the general **From Repo**
test-suite workflow. It creates a Linux virtual environment, installs the pinned
dependencies and runs pytest in headless Chrome, producing `reports/results.xml`.
It has not yet been uploaded or registered in Skye.

The selected Skye image must provide Python 3.12 or later, the `venv` module,
Chrome and the required Linux browser libraries. Package installation, driver
resolution and example.com also require network access. The pipeline does not
install operating-system packages or bypass browser security checks.

The observed image list included `Python_DEPRECATED` and `No Code Python
Playwright`; neither has been confirmed compatible with this Selenium project.
Select a supported image before executing the suite. JUnit XML is generated,
but automatic ingestion into Skye's reports has not been verified.

To connect the repository, use **Custom Code > Test Suite > Create Test Suite**,
select the intended customer and region, enter the repository clone URL and
branch, choose the supported image, and use the repository's runner file.
Skye must have repository access as described in the runbook. Access grants
should be made by the repository owner using the approved service account.

Runbook: [CSS Regression Testing Platform](https://confluence.oraclecorp.com/confluence/display/ACSI/CSS+Regression+Testing+Platform+-+Runbook).

References: [Selenium Chrome documentation](https://www.selenium.dev/documentation/webdriver/browsers/chrome/?tab=python)
and [pytest getting started](https://docs.pytest.org/en/stable/getting-started.html).

## Validation on this computer

A Python 3.12 virtual environment was created in `.venv` using the bundled
runtime because the system `py` launcher points to a missing installation.
Selenium and pytest are installed; exact versions are in `requirements-lock.txt`.

Initial restricted runs crashed Chrome. A normal desktop run revealed that
example.com's current page has no h1 heading, so the original heading check
was replaced with checks of the visible English description and Learn more link.
The corrected test passed: **1 passed in 6.74s** on 19 November 2026.
The latest result is recorded in `reports/results.xml`.
pytest caching is disabled to avoid the observed cache permission warnings.
On failure, the test attempts to save page details, HTML and a screenshot under
`reports/`; these diagnostics are available only while the browser remains connected.

To rerun from this folder with the existing environment:

```powershell
.\.venv\Scripts\python.exe -m pytest --tb=short --junitxml=reports/results.xml
```
