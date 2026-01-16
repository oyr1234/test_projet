from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from time import sleep

class LoginPage(BasePage):
    """
    Page Object Model pour Login - Pharmacie Management System
    """
    
    # Locators (à adapter selon ton HTML)
    USERNAME_INPUT = (By.XPATH, "//input[@placeholder='Enter your username']")  # ou "Input.Email"
    PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='Enter your password']")  # ou "Input.Password"
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message")  # à adapter
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Logout')]")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def enter_username(self, username):
        """Saisir le nom d'utilisateur"""
        self.send_keys_to_element(self.USERNAME_INPUT, username)
    
    def enter_password(self, password):
        """Saisir le mot de passe"""
        self.send_keys_to_element(self.PASSWORD_INPUT, password)
    
    def click_login(self):
        """Cliquer sur Login"""
        self.click_element(self.LOGIN_BUTTON)
    
    def login(self, username, password):
        """Méthode complète de login"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        sleep(2)
    
    def is_error_displayed(self):
        """Vérifier si un message d'erreur est affiché"""
        return self.is_element_present(self.ERROR_MESSAGE, timeout=3)
    
    def click_logout(self):
        """Déconnexion"""
        self.click_element(self.LOGOUT_BUTTON)
