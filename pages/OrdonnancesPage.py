from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.BasePage import BasePage
from time import sleep

class OrdonnancesPage(BasePage):
    """
    Page Object Model pour Ordonnances
    """
    
    # Navigation
    MENU_ORDONNANCES = (By.LINK_TEXT, "Ordonnances")
    
    # Liste
    TABLE_ORDONNANCES = (By.TAG_NAME, "table")
    TABLE_ROWS = (By.XPATH, "//table/tbody/tr")
    BUTTON_CREATE = (By.XPATH, "//button[contains(text(),'Créer une ordonnance')]")
    TABLE_HEADERS = (By.TAG_NAME, "th")
    
    # Formulaire création
    INPUT_DATE = (By.ID, "date")  # à adapter
    SELECT_PATIENT = (By.ID, "patient")
    SELECT_PHARMACIEN = (By.ID, "pharmacien")
    SELECT_MEDECIN = (By.ID, "medecin")
    TEXTAREA_COMMENTAIRE = (By.ID, "commentaire")
    
    # Lignes d'ordonnance
    SELECT_MEDICAMENT = (By.ID, "medicament")
    INPUT_QUANTITE = (By.ID, "quantite")
    INPUT_POSOLOGIE = (By.ID, "posologie")
    BUTTON_ADD_LINE = (By.XPATH, "//button[contains(text(),'Ajouter une ligne')]")
    BUTTON_REMOVE_LINE = (By.XPATH, "//button[@class='remove-line']")  # à adapter
    
    BUTTON_SUBMIT_ORDONNANCE = (By.XPATH, "//button[contains(text(),\"Créer l'ordonnance\")]")
    
    # Actions
    BUTTON_DETAILS_FIRST = (By.XPATH, "(//button[contains(text(),'Détails')])[1]")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def navigate_to_ordonnances(self):
        """Naviguer vers Ordonnances"""
        self.click_element(self.MENU_ORDONNANCES)
        sleep(1)
    
    def is_table_displayed(self):
        """Vérifier tableau affiché"""
        return self.is_element_present(self.TABLE_ORDONNANCES)
    
    def get_table_headers(self):
        """Récupérer les en-têtes"""
        headers = self.driver.find_elements(*self.TABLE_HEADERS)
        return [h.text for h in headers]
    
    def click_create_ordonnance(self):
        """Cliquer Créer ordonnance"""
        self.click_element(self.BUTTON_CREATE)
        sleep(1)
    
    def select_patient_by_index(self, index):
        """Sélectionner patient par index"""
        select = Select(self.find_element(self.SELECT_PATIENT))
        select.select_by_index(index)
    
    def select_pharmacien_by_index(self, index):
        """Sélectionner pharmacien"""
        select = Select(self.find_element(self.SELECT_PHARMACIEN))
        select.select_by_index(index)
    
    def select_medecin_by_index(self, index):
        """Sélectionner médecin"""
        select = Select(self.find_element(self.SELECT_MEDECIN))
        select.select_by_index(index)
    
    def enter_commentaire(self, commentaire):
        """Saisir commentaire"""
        self.send_keys_to_element(self.TEXTAREA_COMMENTAIRE, commentaire)
    
    def add_ligne_ordonnance(self, medicament_index, quantite, posologie):
        """Ajouter une ligne d'ordonnance"""
        select = Select(self.find_element(self.SELECT_MEDICAMENT))
        select.select_by_index(medicament_index)
        
        self.send_keys_to_element(self.INPUT_QUANTITE, str(quantite))
        self.send_keys_to_element(self.INPUT_POSOLOGIE, posologie)
        
        self.click_element(self.BUTTON_ADD_LINE)
        sleep(1)
    
    def submit_ordonnance(self):
        """Soumettre l'ordonnance"""
        self.click_element(self.BUTTON_SUBMIT_ORDONNANCE)
        sleep(2)
    
    def click_details_first(self):
        """Consulter détails première ordonnance"""
        self.click_element(self.BUTTON_DETAILS_FIRST)
        sleep(1)
