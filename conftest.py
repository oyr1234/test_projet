import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import os


@pytest.fixture()
def setup(request):
    """
    Fixture d'initialisation du driver (comme dans tes anciens tests test_002/test_003). [file:15][file:16]
    Utilise Chrome + webdriver_manager.
    """
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook pour savoir si un test a échoué (pour les screenshots automatiques).
    """
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # run all other hooks to get the report object
    outcome = yield
    rep = outcome.get_result()

    # Only take screenshot on failure of the test itself (not setup/teardown)
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("setup")  # get the fixture driver
        if driver:
            os.makedirs("./Screenshots", exist_ok=True)
            test_name = item.name
            filepath = f"./Screenshots/{test_name}.png"
            driver.save_screenshot(filepath)
            print(f"💾 Screenshot saved: {filepath}")

