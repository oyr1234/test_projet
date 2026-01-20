from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.BasePage import BasePage
from time import sleep

class StocksPage(BasePage):
    """Page Object Model pour Stocks Médicaments"""
    MENU_STOCKS = (By.XPATH, "//a[normalize-space()='Stocks médicaments']")
    TABLE_STOCKS = (By.TAG_NAME, "table")
    BUTTON_CREATE = (By.XPATH, "//button[normalize-space()='Créer Stock']") 
    SELECT_MEDICAMENT = (By.XPATH, "//div[@class='card-body']//div[2]//select[1]")
    SELECT_PHARMACIE = (By.XPATH, "//div[@class='card shadow-sm']//div[1]//select[1]")
    INPUT_QUANTITE = (By.XPATH, "//div[3]//input[1]")
    INPUT_SEUIL = (By.XPATH, "//div[4]//input[1]")
    BUTTON_SUBMIT = (By.XPATH, "//button[normalize-space()='Créer']")
    
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
    
    def create_stock(self, medicament_index, pharmacie_index, quantite, seuil):
        select_med = Select(self.find_element(self.SELECT_MEDICAMENT))
        select_med.select_by_index(medicament_index)
        
        select_pharma = Select(self.find_element(self.SELECT_PHARMACIE))
        select_pharma.select_by_index(pharmacie_index)
        
        self.send_keys_to_element(self.INPUT_QUANTITE, str(quantite))
        self.send_keys_to_element(self.INPUT_SEUIL, str(seuil))
        self.click_element(self.BUTTON_SUBMIT)
        sleep(2)
