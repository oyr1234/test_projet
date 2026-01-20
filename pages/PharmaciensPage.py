from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from time import sleep


class PharmaciensPage(BasePage):
    """Page Object Model pour Pharmaciens"""

    # ✅ Locators (ALL must be tuples: (By.X, "value"))
    MENU_PHARMACIENS = (By.XPATH, "//a[normalize-space()='Pharmaciens']")
    TABLE_PHARMACIENS = (By.XPATH, "//div[@class='container mt-4']")
    TABLE_ROWS = (By.XPATH, "//table/tbody/tr")

    BUTTON_CREATE = (By.XPATH, "//button[normalize-space()='Creer Pharmacien']")
    INPUT_NOM = (By.XPATH, "//div[@class='card shadow-sm']//div[1]//input[1]")
    INPUT_PRENOM = (By.XPATH, "//div[@class='card-body']//div[2]//input[1]")
    INPUT_TELEPHONE = (By.XPATH, "//div[3]//input[1]")
    INPUT_EMAIL = (By.XPATH, "//main//div[5]//input")
    INPUT_INSCRIPTION = (By.XPATH, "//div[4]//input[1]")
    BUTTON_SUBMIT = (By.XPATH, "//button[normalize-space()='Create Pharmacien']")

    BUTTON_EDIT_FIRST = (By.XPATH, "(//button[contains(text(),'Edit')])[1]")
    BUTTON_DELETE_FIRST = (By.XPATH, "(//button[contains(text(),'Supprimer')])[1]")

    def __init__(self, driver):
        super().__init__(driver)

    # -----------------------
    # Actions
    # -----------------------
    def navigate_to_pharmaciens(self):
        self.click_element(self.MENU_PHARMACIENS)
        sleep(1)

    def click_create(self):
        self.click_element(self.BUTTON_CREATE)
        sleep(1)

    def create_pharmacien(self, nom, prenom, telephone, email, inscription):
        self.send_keys_to_element(self.INPUT_NOM, nom)
        self.send_keys_to_element(self.INPUT_PRENOM, prenom)
        self.send_keys_to_element(self.INPUT_TELEPHONE, telephone)
        self.send_keys_to_element(self.INPUT_EMAIL, email)
        self.send_keys_to_element(self.INPUT_INSCRIPTION, inscription)
        self.click_element(self.BUTTON_SUBMIT)
        sleep(2)

    # -----------------------
    # Checks
    # -----------------------
    def is_table_displayed(self):
        return self.is_element_present(self.TABLE_PHARMACIENS)

    def get_pharmaciens_count(self):
        rows = self.driver.find_elements(*self.TABLE_ROWS)
        return len(rows)
