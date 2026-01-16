from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from time import sleep

class DashboardPage(BasePage):
    """Page Object Model pour Dashboard Pharmacien"""
    
    MENU_DASHBOARD = (By.XPATH, "//h2[normalize-space()='Dashboard Pharmacien']")
    
    # Éléments statistiques (à adapter selon ton dashboard)
    STATS_PATIENTS = (By.CSS_SELECTOR, "body > div:nth-child(1) > div:nth-child(1) > main:nth-child(2) > article:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)")
    STATS_ORDONNANCES = (By.CSS_SELECTOR, "body > div:nth-child(1) > div:nth-child(1) > main:nth-child(2) > article:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1)")
    STATS_MEDICAMENTS = (By.CSS_SELECTOR, "div[class='row g-3 mb-4'] div:nth-child(3) div:nth-child(1) div:nth-child(1)")
    def __init__(self, driver):
        super().__init__(driver)
    
    def navigate_to_dashboard(self):
        self.click_element(self.MENU_DASHBOARD)
        sleep(1)
    
    def is_dashboard_displayed(self):
        # Vérifier si au moins un élément statistique est présent
        return self.is_element_present(self.STATS_PATIENTS, timeout=3) or \
               self.get_current_url().__contains__("dashboard")
    
    def is_stats_visible(self):

        try:
            patients_visible = self.is_element_present(self.STATS_PATIENTS, timeout=3)
            ordonnances_visible = self.is_element_present(self.STATS_ORDONNANCES, timeout=3)
            medicaments_visible = self.is_element_present(self.STATS_MEDICAMENTS, timeout=3)

            return patients_visible or ordonnances_visible or medicaments_visible

        except Exception as e:
            print(f"Erreur lors de la vérification des statistiques: {e}")
            return False

