from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.BasePage import BasePage
from time import sleep

class StocksPage(BasePage):
    """Page Object Model pour Stocks Médicaments"""
    
    MENU_STOCKS = (By.LINK_TEXT, "Stocks médicaments")
    TABLE_STOCKS = (By.TAG_NAME, "table")
    BUTTON_CREATE = (By.XPATH, "//button[contains(text(),'Créer')]")
    
    SELECT_MEDICAMENT = (By.ID, "medicament")
    SELECT_PHARMACIE = (By.ID, "pharmacie")
    INPUT_QUANTITE = (By.ID, "quantite")
    INPUT_DATE_EXPIRATION = (By.ID, "dateExpiration")
    BUTTON_SUBMIT = (By.XPATH, "//button[contains(text(),'Create')]")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def navigate_to_stocks(self):
        self.click_element(self.MENU_STOCKS)
        sleep(1)
    
    def is_table_displayed(self):
        return self.is_element_present(self.TABLE_STOCKS)
    
    def click_create(self):
        self.click_element(self.BUTTON_CREATE)
        sleep(1)
    
    def create_stock(self, medicament_index, pharmacie_index, quantite, date_expiration):
        select_med = Select(self.find_element(self.SELECT_MEDICAMENT))
        select_med.select_by_index(medicament_index)
        
        select_pharma = Select(self.find_element(self.SELECT_PHARMACIE))
        select_pharma.select_by_index(pharmacie_index)
        
        self.send_keys_to_element(self.INPUT_QUANTITE, str(quantite))
        self.send_keys_to_element(self.INPUT_DATE_EXPIRATION, date_expiration)
        self.click_element(self.BUTTON_SUBMIT)
        sleep(2)
