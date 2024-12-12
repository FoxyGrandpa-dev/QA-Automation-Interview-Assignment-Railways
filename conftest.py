import pytest
import pytest_html
from pytest_html import extras
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))


def pytest_html_report_title(report):
    report.title = "My Selenium Test Report"


def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([extras.html("<span style='color:blue;font-weight:bold;'>Custom Summary</span>")])


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to capture test status and include additional information in the report.
    """
    outcome = yield
    report = outcome.get_result()
    if report.when == "call":
        report.extra = getattr(report, "extra", [])
        # Add screenshot for failed tests
        if report.failed:
            driver = getattr(item.instance, 'driver', None)
            if driver:
                screenshot_path = f"screenshots/{item.name}.png"
                driver.save_screenshot(screenshot_path)
                report.extra.append(pytest_html.extras.image(screenshot_path))
