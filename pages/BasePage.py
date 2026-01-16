from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    """
    Classe de base pour tous les Page Objects
    """
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def find_element(self, locator):
        """Trouver un élément avec attente"""
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def click_element(self, locator):
        """Cliquer sur un élément avec attente"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    def send_keys_to_element(self, locator, text):
        """Saisir du texte dans un élément"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def is_element_present(self, locator, timeout=5):
        """Vérifier si un élément est présent"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False
    
    def get_current_url(self):
        """Obtenir l'URL actuelle"""
        return self.driver.current_url
    
    def get_page_title(self):
        """Obtenir le titre de la page"""
        return self.driver.title
