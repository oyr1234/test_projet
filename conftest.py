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


@pytest.fixture(autouse=True)
def screenshot_on_failure(request, setup):
    """
    Prendre automatiquement un screenshot si le test échoue,
    similaire à ce que tu faisais en appelant save_screenshot dans test_002/test_003. [file:15][file:16]
    """
    yield
    driver = setup
    if request.node.rep_call.failed:
        screenshots_dir = os.path.join("tests", "screenshots")
        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        test_name = request.node.name
        file_path = os.path.join(screenshots_dir, f"{test_name}_{timestamp}.png")
        driver.save_screenshot(file_path)
        print(f"\n📸 Screenshot enregistré : {file_path}")
