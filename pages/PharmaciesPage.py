from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from time import sleep


class PharmaciesPage(BasePage):
    """Page Object Model pour Pharmacies"""

    # ✅ Locators (must be tuples)
    MENU_PHARMACIES = (By.XPATH, "//a[normalize-space()='Pharmacies']")
    TABLE_PHARMACIES = (By.XPATH, "//div[@class='container mt-4']")

    BUTTON_CREATE = (By.XPATH, "//button[normalize-space()='Creer Pharmacie']")
    INPUT_NOM = (By.XPATH, "//div[@class='card shadow-sm']//div[1]//input[1]")
    INPUT_ADRESSE = (By.XPATH, "//div[@class='card shadow-sm']//div[2]//input[1]")
    INPUT_TELEPHONE = (By.XPATH, "//div[3]//input[1]")
    INPUT_EMAIL = (By.ID, "email")
    BUTTON_SUBMIT = (By.XPATH, "//button[normalize-space()='Create Pharmacie']")

    def __init__(self, driver):
        super().__init__(driver)

    # -----------------------
    # Actions
    # -----------------------
    def navigate_to_pharmacies(self):
        self.click_element(self.MENU_PHARMACIES)
        sleep(1)

    def click_create(self):
        self.click_element(self.BUTTON_CREATE)
        sleep(1)

    def create_pharmacie(self, nom, adresse, telephone, email):
        self.send_keys_to_element(self.INPUT_NOM, nom)
        self.send_keys_to_element(self.INPUT_ADRESSE, adresse)
        self.send_keys_to_element(self.INPUT_TELEPHONE, telephone)
        self.send_keys_to_element(self.INPUT_EMAIL, email)
        self.click_element(self.BUTTON_SUBMIT)
        sleep(2)

    # -----------------------
    # Checks
    # -----------------------
    def is_table_displayed(self):
        return self.is_element_present(self.TABLE_PHARMACIES)
