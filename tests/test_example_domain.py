"""A first custom-code browser test: verify the Example Domain page."""

import os
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_example_domain_title_and_content():
    options = webdriver.ChromeOptions()
    if os.environ.get("HEADLESS", "0") == "1":
        options.add_argument("--headless=new")

    # Selenium Manager locates the matching Chrome driver automatically.
    driver = webdriver.Chrome(options=options)
    try:
        driver.set_page_load_timeout(30)
        driver.get("https://example.com/")

        description = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'p[lang="en"]'))
        )
        assert driver.title == "Example Domain", "Unexpected page title"
        assert "This domain is for use in documentation examples" in description.text
        learn_more = driver.find_element(By.LINK_TEXT, "Learn more")
        assert learn_more.is_displayed(), "Learn more link is not visible"
        assert learn_more.get_attribute("href") == "https://iana.org/help/example-domains"
    except Exception:
        # Keep the original failure even if Chrome cannot provide diagnostics.
        reports = Path(__file__).resolve().parents[1] / "reports"
        reports.mkdir(exist_ok=True)
        for name, capture in (
            ("page-info.txt", lambda: f"URL: {driver.current_url}\nTitle: {driver.title}\n"),
            ("page.html", lambda: driver.page_source),
        ):
            try:
                value = capture()
                (reports / name).write_text(value, encoding="utf-8")
                if name == "page-info.txt":
                    print(value)
            except Exception as diagnostic_error:
                print(f"Could not capture {name}: {diagnostic_error}")
        try:
            driver.save_screenshot(str(reports / "failure.png"))
        except Exception as diagnostic_error:
            print(f"Could not capture screenshot: {diagnostic_error}")
        print(f"Failure diagnostics: {reports}")
        raise
    finally:
        driver.quit()
