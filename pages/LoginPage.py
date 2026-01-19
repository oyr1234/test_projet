import os
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.BasePage import BasePage


class LoginPage(BasePage):
    """
    Page Object Model for Login - Pharmacie Management System
    """

    # Locators (update according to your HTML)
    USERNAME_INPUT = (By.XPATH, "//input[@placeholder='Enter your username']")
    PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='Enter your password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Logout')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # ---------------------------
    # Actions
    # ---------------------------
    def enter_username(self, username):
        """Enter username"""
        self.send_keys_to_element(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        """Enter password"""
        self.send_keys_to_element(self.PASSWORD_INPUT, password)

    def click_login(self):
        """Click Login button"""
        self.click_element(self.LOGIN_BUTTON)

    def login(self, username, password, screenshot_on_fail=True):
        """
        Full login method
        :param screenshot_on_fail: if True, take screenshot if login fails
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        sleep(2)  # wait for page to load

        # If login failed and screenshot_on_fail is True
        if screenshot_on_fail and self.is_error_displayed():
            self.take_screenshot(f"login_failed_{username}")

    def click_logout(self):
        """Click Logout"""
        self.click_element(self.LOGOUT_BUTTON)

    # ---------------------------
    # Checks
    # ---------------------------
    def is_error_displayed(self):
        """Check if error message is visible"""
        return self.is_element_present(self.ERROR_MESSAGE, timeout=3)

    # ---------------------------
    # Screenshots
    # ---------------------------
    def take_screenshot(self, filename):
        """Take a screenshot of current page"""
        # Ensure folder exists
        os.makedirs("./Screenshots", exist_ok=True)

        # Resize window so content is fully visible
        self.driver.set_window_size(1920, 1080)

        filepath = f"./Screenshots/{filename}.png"
        self.driver.save_screenshot(filepath)
        print(f"Screenshot saved: {filepath}")
