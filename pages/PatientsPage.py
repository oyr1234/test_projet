from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from time import sleep

class PatientsPage(BasePage):
    """
    Page Object Model pour Patients
    """
    
    # Navigation
    MENU_PATIENTS = (By.LINK_TEXT, "Patients")
    
    # Liste
    TABLE_PATIENTS = (By.TAG_NAME, "table")
    TABLE_ROWS = (By.XPATH, "//table/tbody/tr")
    BUTTON_CREATE = (By.XPATH, "//button[contains(text(),'Créer patient')]")
    
    # Formulaire création/modification
    INPUT_NOM = (By.ID, "nom")  # à adapter
    INPUT_PRENOM = (By.ID, "prenom")
    INPUT_CIN = (By.ID, "cin")
    INPUT_ADRESSE = (By.ID, "adresse")
    BUTTON_SUBMIT = (By.XPATH, "//button[contains(text(),'Create Patient')]")
    BUTTON_CANCEL = (By.XPATH, "//button[contains(text(),'Cancel')]")
    
    # Actions sur ligne
    BUTTON_EDIT_FIRST = (By.XPATH, "(//button[contains(text(),'Edit')])[1]")
    BUTTON_DELETE_FIRST = (By.XPATH, "(//button[contains(text(),'Supprimer')])[1]")
    BUTTON_DETAILS_FIRST = (By.XPATH, "(//button[contains(text(),'Détails')])[1]")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def navigate_to_patients(self):
        """Naviguer vers la page Patients"""
        self.click_element(self.MENU_PATIENTS)
        sleep(1)
    
    def is_table_displayed(self):
        """Vérifier si le tableau est affiché"""
        return self.is_element_present(self.TABLE_PATIENTS)
    
    def get_patients_count(self):
        """Compter le nombre de patients affichés"""
        rows = self.driver.find_elements(*self.TABLE_ROWS)
        return len(rows)
    
    def click_create_patient(self):
        """Cliquer sur bouton Créer patient"""
        self.click_element(self.BUTTON_CREATE)
        sleep(1)
    
    def create_patient(self, nom, prenom, cin, adresse):
        """Créer un patient complet"""
        self.send_keys_to_element(self.INPUT_NOM, nom)
        self.send_keys_to_element(self.INPUT_PRENOM, prenom)
        self.send_keys_to_element(self.INPUT_CIN, cin)
        self.send_keys_to_element(self.INPUT_ADRESSE, adresse)
        self.click_element(self.BUTTON_SUBMIT)
        sleep(2)
    
    def click_edit_first_patient(self):
        """Modifier le premier patient"""
        self.click_element(self.BUTTON_EDIT_FIRST)
        sleep(1)
    
    def click_delete_first_patient(self):
        """Supprimer le premier patient"""
        self.click_element(self.BUTTON_DELETE_FIRST)
        sleep(1)
