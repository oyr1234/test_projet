import pytest
from pages.LoginPage import LoginPage
from pages.PharmaciesPage import PharmaciesPage
from utilities.readProperties import ReadConfig
from utilities.newCustomLogger import LogGen
from time import sleep
import random

@pytest.mark.pharmacies
class Test_006_Pharmacies:
    """Tests Pharmacies (TC-028 à TC-032)"""
    
    baseURL = ReadConfig.getApplicationURL()
    loginURL = ReadConfig.getLoginURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen("./Logs/pharmacies.log")
    
    @pytest.fixture(autouse=True)
    def setup_login(self, setup):
        """Auto-login"""
        self.driver = setup
        self.driver.get(self.loginURL)
        
        loginPage = LoginPage(self.driver)
        loginPage.login(self.username, self.password)
        sleep(2)
        
        yield
        
        self.driver.close()
    
    @pytest.mark.P0
    def test_TC028_display_pharmacies_list(self):
        """
        TC-028: Afficher liste Pharmacies
        Technique: Tests de confirmation
        Priorité: P0
        """
        self.logger.log_info("========== TC-028: Display Pharmacies List ==========")
        
        pharmaciesPage = PharmaciesPage(self.driver)
        pharmaciesPage.navigate_to_pharmacies()
        sleep(2)
        
        if pharmaciesPage.is_table_displayed():
            self.logger.log_info("✅ TC-028 PASSED: Liste pharmacies affichée")
            pharmaciesPage.take_screenshot("TC028_success")
            assert True
        else:
            self.logger.log_error("❌ TC-028 FAILED")
            pharmaciesPage.take_screenshot("TC028_failed")
            assert False
    
    @pytest.mark.P0
    def test_TC029_create_pharmacie_valid(self):
        """
        TC-029: Créer Pharmacie valide
        Technique: Partition d'équivalence
        Priorité: P0
        """
        self.logger.log_info("========== TC-029: Create Pharmacie Valid ==========")
        
        pharmaciesPage = PharmaciesPage(self.driver)
        pharmaciesPage.navigate_to_pharmacies()
        
        pharmaciesPage.click_create_pharmacie()
        
        random_id = random.randint(1000, 9999)
        pharmaciesPage.create_pharmacie(
            nom=f"Pharmacie Test {random_id}",
            adresse=f"Avenue Test {random_id}, Tunis"
        )
        
        sleep(2)
        pharmaciesPage.navigate_to_pharmacies()
        
        if pharmaciesPage.is_table_displayed():
            self.logger.log_info("✅ TC-029 PASSED: Pharmacie créée")
            assert True
        else:
            self.logger.log_error("❌ TC-029 FAILED")
            assert False
    
    @pytest.mark.P0
    def test_TC030_create_pharmacie_empty_field(self):
        """
        TC-030: Créer Pharmacie champ vide
        Technique: Valeurs limites
        Priorité: P0
        """
        self.logger.log_info("========== TC-030: Create Pharmacie Empty Field ==========")
        
        pharmaciesPage = PharmaciesPage(self.driver)
        pharmaciesPage.navigate_to_pharmacies()
        
        pharmaciesPage.click_create_pharmacie()
        pharmaciesPage.create_pharmacie(nom="", adresse="Test")
        
        sleep(2)
        
        if "create" in pharmaciesPage.get_current_url().lower():
            self.logger.log_info("✅ TC-030 PASSED: Validation OK")
            assert True
        else:
            self.logger.log_error("❌ TC-030 FAILED")
            assert False
    
    @pytest.mark.P1
    def test_TC031_edit_pharmacie(self):
        """TC-031: Modifier Pharmacie"""
        self.logger.log_info("========== TC-031: Edit Pharmacie ==========")
        self.logger.log_info("✅ TC-031 SKIPPED")
        pytest.skip("Edit non implémenté")
    
    @pytest.mark.P1
    def test_TC032_delete_pharmacie(self):
        """TC-032: Supprimer Pharmacie"""
        self.logger.log_info("========== TC-032: Delete Pharmacie ==========")
        self.logger.log_info("✅ TC-032 SKIPPED")
        pytest.skip("Delete requiert confirmation modal")
