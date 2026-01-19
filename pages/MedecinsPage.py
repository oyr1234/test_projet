from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from time import sleep

class MedecinsPage(BasePage):
    """Page Object Model pour Médecins (/Medecins)"""

    # Navigation
    MENU_MEDECINS = (By.XPATH, "//a[normalize-space()='Médecins']")

    # Table container
    TABLE_MEDECINS = (By.XPATH, "//div[@class='container mt-4']//table")
    TABLE_ROWS = (By.XPATH, "//div[@class='container mt-4']//table/tbody/tr")

    # Buttons
    BUTTON_CREATE = (By.XPATH, "//button[normalize-space()='Creer Medecin']")
    BUTTON_EDIT_FIRST = (By.XPATH, "(//button[contains(text(),'Edit')])[1]")
    BUTTON_DELETE_FIRST = (By.XPATH, "(//button[contains(text(),'Supprimer')])[1]")
    # Formulaire (Create/Edit)
    INPUT_NOM = (By.XPATH, "//div[@class='card shadow-sm']//div[1]//input[1]")
    INPUT_PRENOM = (By.XPATH, "//div[@class='card-body']//div[2]//input[1]")
    INPUT_SPECIALITE = (By.XPATH, "//div[3]//input[1]")
    INPUT_TELEPHONE = (By.XPATH,"//div[5]//input[1]")
    INPUT_TELEPHONE_pro = (By.XPATH, "//div[4]//input[1]")
    BUTTON_SUBMIT = (By.XPATH, "//button[normalize-space()='Create Medecin']")
    def __init__(self, driver):
        super().__init__(driver)

    # Navigation
    def navigate_to_medecins(self):
        self.click_element(self.MENU_MEDECINS)
        sleep(1)

    # Table
    def is_table_displayed(self):
        return self.is_element_present(self.TABLE_MEDECINS)

    def get_medecins_count(self):
        rows = self.driver.find_elements(*self.TABLE_ROWS)
        return len(rows)

    # Create
    def click_create_medecin(self):
        self.click_element(self.BUTTON_CREATE)
        sleep(1)

    def create_medecin(self, nom, prenom, specialite, telephone="",telephone_pro="", email=""):
        self.send_keys_to_element(self.INPUT_NOM, nom)
        self.send_keys_to_element(self.INPUT_PRENOM, prenom)
        self.send_keys_to_element(self.INPUT_SPECIALITE, specialite)
        if telephone:
            self.send_keys_to_element(self.INPUT_TELEPHONE, telephone)
        if telephone_pro:
            self.send_keys_to_element(self.INPUT_TELEPHONE_pro, telephone)
        if email:
            self.send_keys_to_element(self.INPUT_EMAIL, email)
        self.click_element(self.BUTTON_SUBMIT)
        sleep(2)

    # Actions on first row
    def click_edit_first(self):
        self.click_element(self.BUTTON_EDIT_FIRST)
        sleep(1)

    def click_delete_first(self):
        self.click_element(self.BUTTON_DELETE_FIRST)
        sleep(1)
