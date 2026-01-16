from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from time import sleep

class MedecinsPage(BasePage):
    """Page Object Model pour Médecins"""
    
    # Navigation
    MENU_MEDECINS = (By.LINK_TEXT, "Médecins")
    
    # Liste
    TABLE_MEDECINS = (By.TAG_NAME, "table")
    TABLE_ROWS = (By.XPATH, "//table/tbody/tr")
    BUTTON_CREATE = (By.XPATH, "//button[contains(text(),'Créer')]")
    
    # Formulaire
    INPUT_NOM = (By.ID, "nom")
    INPUT_PRENOM = (By.ID, "prenom")
    INPUT_SPECIALITE = (By.ID, "specialite")
    INPUT_TELEPHONE = (By.ID, "telephone")
    INPUT_EMAIL = (By.ID, "email")
    BUTTON_SUBMIT = (By.XPATH, "//button[contains(text(),'Create') or contains(text(),'Créer')]")
    
    # Actions
    BUTTON_EDIT_FIRST = (By.XPATH, "(//button[contains(text(),'Edit')])[1]")
    BUTTON_DELETE_FIRST = (By.XPATH, "(//button[contains(text(),'Supprimer')])[1]")
    BUTTON_DETAILS_FIRST = (By.XPATH, "(//button[contains(text(),'Détails')])[1]")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def navigate_to_medecins(self):
        """Naviguer vers Médecins"""
        self.click_element(self.MENU_MEDECINS)
        sleep(1)
    
    def is_table_displayed(self):
        return self.is_element_present(self.TABLE_MEDECINS)
    
    def click_create(self):
        self.click_element(self.BUTTON_CREATE)
        sleep(1)
    
    def create_medecin(self, nom, prenom, specialite, telephone, email):
        """Créer un médecin"""
        self.send_keys_to_element(self.INPUT_NOM, nom)
        self.send_keys_to_element(self.INPUT_PRENOM, prenom)
        self.send_keys_to_element(self.INPUT_SPECIALITE, specialite)
        self.send_keys_to_element(self.INPUT_TELEPHONE, telephone)
        self.send_keys_to_element(self.INPUT_EMAIL, email)
        self.click_element(self.BUTTON_SUBMIT)
        sleep(2)
    
    def get_medecins_count(self):
        rows = self.driver.find_elements(*self.TABLE_ROWS)
        return len(rows)
    
    def click_edit_first(self):
        self.click_element(self.BUTTON_EDIT_FIRST)
        sleep(1)
    
    def click_delete_first(self):
        self.click_element(self.BUTTON_DELETE_FIRST)
        sleep(1)
