"""
conftest.py - Shared Fixtures and Configuration
This file is automatically discovered by pytest
"""

import pytest
from selenium import webdriver
from datetime import datetime
import os

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    
    # Give driver to test
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):

    outcome = yield
    report = outcome.get_result()
    if report.when == 'call':
        driver = item.funcargs.get('driver')
        if driver:
            os.makedirs('screenshots', exist_ok=True)
            
            # Generate filename
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            test_name = item.name
            filename = f'screenshots/{test_name}_{timestamp}.png'
            driver.save_screenshot(filename)
            print(f"\nScreenshot saved: {filename}")