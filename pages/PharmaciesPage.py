from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from time import sleep

class PharmaciesPage(BasePage):
    """Page Object Model pour Pharmacies"""
    
    MENU_PHARMACIES = (By.LINK_TEXT, "Pharmacies")
    TABLE_PHARMACIES = (By.TAG_NAME, "table")
    BUTTON_CREATE = (By.XPATH, "//button[contains(text(),'Créer')]")
    
    INPUT_NOM = (By.ID, "nom")
    INPUT_ADRESSE = (By.ID, "adresse")
    INPUT_TELEPHONE = (By.ID, "telephone")
    INPUT_EMAIL = (By.ID, "email")
    BUTTON_SUBMIT = (By.XPATH, "//button[contains(text(),'Create')]")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def navigate_to_pharmacies(self):
        self.click_element(self.MENU_PHARMACIES)
        sleep(1)
    
    def is_table_displayed(self):
        return self.is_element_present(self.TABLE_PHARMACIES)
    
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
