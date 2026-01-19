from selenium.webdriver.common.by import By
from time import sleep


class PatientsPage:

    # Navigation
    MENU_PATIENTS = (By.XPATH, "//a[normalize-space()='Patients']")

    # Page
    TITLE = (By.XPATH, "//h3[normalize-space()='Patients']")
    CREATE_BUTTON = (By.XPATH, "//button[normalize-space()='Créer patient']")

    # Table
    TABLE = (By.XPATH, "//table")
    EMPTY_ROW = (By.XPATH, "//td[contains(text(),'Aucun patient')]")
    TABLE_ROWS = (By.XPATH, "//table/tbody/tr")

    # Row actions
    DETAILS_BTN = (By.XPATH, "(//button[normalize-space()='Détails'])[1]")
    EDIT_BTN = (By.XPATH, "(//button[normalize-space()='Edit'])[1]")
    DELETE_BTN = (By.XPATH, "(//button[normalize-space()='Supprimer'])[1]")

    # Modal
    MODAL = (By.XPATH, "//div[contains(@class,'modal-content')]")
    MODAL_CLOSE = (By.XPATH, "//button[contains(@class,'btn-close') or text()='Fermer']")

    def __init__(self, driver):
        self.driver = driver

    # Navigation
    def navigate_to_patients(self):
        self.driver.find_element(*self.MENU_PATIENTS).click()
        sleep(1)

    # Page checks
    def is_table_displayed(self):
        return self.driver.find_element(*self.TABLE).is_displayed()

    # Patients count
    def get_patients_count(self):
        if self.driver.find_elements(*self.EMPTY_ROW):
            return 0
        return len(self.driver.find_elements(*self.TABLE_ROWS))

    # Create
    def click_create_patient(self):
        self.driver.find_element(*self.CREATE_BUTTON).click()

    # Details
    def click_details_first_patient(self):
        self.driver.find_element(*self.DETAILS_BTN).click()
        sleep(1)

    def is_details_modal_displayed(self):
        return self.driver.find_element(*self.MODAL).is_displayed()

    def close_details_modal(self):
        self.driver.find_element(*self.MODAL_CLOSE).click()

    # Edit
    def click_edit_first_patient(self):
        self.driver.find_element(*self.EDIT_BTN).click()

    # Delete
    def click_delete_first_patient(self):
        self.driver.find_element(*self.DELETE_BTN).click()
