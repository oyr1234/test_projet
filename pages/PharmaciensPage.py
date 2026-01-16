from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from time import sleep

class PharmaciensPage(BasePage):
    """Page Object Model pour Pharmaciens"""
    
    MENU_PHARMACIENS = (By.LINK_TEXT, "Pharmaciens")
    TABLE_PHARMACIENS = (By.TAG_NAME, "table")
    TABLE_ROWS = (By.XPATH, "//table/tbody/tr")
    BUTTON_CREATE = (By.XPATH, "//button[contains(text(),'Créer')]")
    
    INPUT_NOM = (By.ID, "nom")
    INPUT_PRENOM = (By.ID, "prenom")
    INPUT_TELEPHONE = (By.ID, "telephone")
    INPUT_EMAIL = (By.ID, "email")
    BUTTON_SUBMIT = (By.XPATH, "//button[contains(text(),'Create')]")
    
    BUTTON_EDIT_FIRST = (By.XPATH, "(//button[contains(text(),'Edit')])[1]")
    BUTTON_DELETE_FIRST = (By.XPATH, "(//button[contains(text(),'Supprimer')])[1]")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def navigate_to_pharmaciens(self):
        self.click_element(self.MENU_PHARMACIENS)
        sleep(1)
    
    def is_table_displayed(self):
        return self.is_element_present(self.TABLE_PHARMACIENS)
    
    def click_create(self):
        self.click_element(self.BUTTON_CREATE)
        sleep(1)
    
    def create_pharmacien(self, nom, prenom, telephone, email):
        self.send_keys_to_element(self.INPUT_NOM, nom)
        self.send_keys_to_element(self.INPUT_PRENOM, prenom)
        self.send_keys_to_element(self.INPUT_TELEPHONE, telephone)
        self.send_keys_to_element(self.INPUT_EMAIL, email)
        self.click_element(self.BUTTON_SUBMIT)
        sleep(2)
    
    def get_pharmaciens_count(self):
        rows = self.driver.find_elements(*self.TABLE_ROWS)
        return len(rows)
