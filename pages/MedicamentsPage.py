from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from time import sleep

class MedicamentsPage(BasePage):
    """Page Object Model pour Médicaments"""
    
    MENU_MEDICAMENTS = (By.LINK_TEXT, "Médicaments")
    TABLE_MEDICAMENTS = (By.TAG_NAME, "table")
    TABLE_ROWS = (By.XPATH, "//table/tbody/tr")
    BUTTON_CREATE = (By.XPATH, "//button[contains(text(),'Créer')]")
    
    INPUT_NOM = (By.ID, "nom")
    INPUT_DESCRIPTION = (By.ID, "description")
    INPUT_PRIX = (By.ID, "prix")
    INPUT_REFERENCE = (By.ID, "reference")
    BUTTON_SUBMIT = (By.XPATH, "//button[contains(text(),'Create')]")
    
    BUTTON_EDIT_FIRST = (By.XPATH, "(//button[contains(text(),'Edit')])[1]")
    BUTTON_DELETE_FIRST = (By.XPATH, "(//button[contains(text(),'Supprimer')])[1]")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def navigate_to_medicaments(self):
        self.click_element(self.MENU_MEDICAMENTS)
        sleep(1)
    
    def is_table_displayed(self):
        return self.is_element_present(self.TABLE_MEDICAMENTS)
    
    def click_create(self):
        self.click_element(self.BUTTON_CREATE)
        sleep(1)
    
    def create_medicament(self, nom, description, prix, reference):
        self.send_keys_to_element(self.INPUT_NOM, nom)
        self.send_keys_to_element(self.INPUT_DESCRIPTION, description)
        self.send_keys_to_element(self.INPUT_PRIX, str(prix))
        self.send_keys_to_element(self.INPUT_REFERENCE, reference)
        self.click_element(self.BUTTON_SUBMIT)
        sleep(2)
    
    def get_medicaments_count(self):
        rows = self.driver.find_elements(*self.TABLE_ROWS)
        return len(rows)
