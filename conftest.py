import pytest

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    if not config.option.htmlpath:
        config.option.htmlpath = 'report.html'  # Default report filename