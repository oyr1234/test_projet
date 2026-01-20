from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from time import sleep

class PharmaciesPage(BasePage):

    MENU_PHARMACIES = (By.XPATH, "//a[normalize-space()='Pharmacies']")
    TABLE_PHARMACIES = (By.XPATH, "//div[@class='container mt-4']")

    BUTTON_CREATE = (By.XPATH, "//button[normalize-space()='Creer Pharmacie']")
    INPUT_NOM = (By.XPATH, "//input[@name='nom']")
    INPUT_ADRESSE = (By.XPATH, "//input[@name='adresse']")
    INPUT_TELEPHONE = (By.XPATH, "//input[@name='telephone']")
    BUTTON_SUBMIT = (By.XPATH, "//button[normalize-space()='Create Pharmacie']")

    def navigate_to_pharmacies(self):
        self.click_element(self.MENU_PHARMACIES)
        sleep(1)

    def click_create_pharmacie(self):
        self.click_element(self.BUTTON_CREATE)
        sleep(1)

    def create_pharmacie(self, nom, adresse, telephone=""):
        self.send_keys_to_element(self.INPUT_NOM, nom)
        self.send_keys_to_element(self.INPUT_ADRESSE, adresse)
        if telephone:
            self.send_keys_to_element(self.INPUT_TELEPHONE, telephone)
        self.click_element(self.BUTTON_SUBMIT)
        sleep(2)

    def is_table_displayed(self):
        return self.is_element_present(self.TABLE_PHARMACIES)
