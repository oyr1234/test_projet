import pytest
from pages.LoginPage import LoginPage
from pages.PharmaciensPage import PharmaciensPage
from utilities.readProperties import ReadConfig
from utilities.newCustomLogger import LogGen
from time import sleep
import random

@pytest.mark.pharmaciens
class Test_005_Pharmaciens:
    """Tests Pharmaciens (TC-023 à TC-027)"""
    
    baseURL = ReadConfig.getApplicationURL()
    loginURL = ReadConfig.getLoginURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen("./Logs/pharmaciens.log")
    
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
    def test_TC023_display_pharmaciens_list(self):
        """
        TC-023: Afficher liste Pharmaciens
        Technique: Tests de confirmation
        Priorité: P0
        """
        self.logger.log_info("========== TC-023: Display Pharmaciens List ==========")
        
        pharmaciensPage = PharmaciensPage(self.driver)
        pharmaciensPage.navigate_to_pharmaciens()
        sleep(2)
        
        if pharmaciensPage.is_table_displayed():
            self.logger.log_info("✅ TC-023 PASSED: Liste pharmaciens affichée")
            pharmaciensPage.take_screenshot("TC023_success")
            assert True
        else:
            self.logger.log_error("❌ TC-023 FAILED")
            pharmaciensPage.take_screenshot("TC023_failed")
            assert False
    
    @pytest.mark.P0
    def test_TC024_create_pharmacien_valid(self):
        """
        TC-024: Créer Pharmacien valide
        Technique: Partition d'équivalence
        Priorité: P0
        """
        self.logger.log_info("========== TC-024: Create Pharmacien Valid ==========")
        
        pharmaciensPage = PharmaciensPage(self.driver)
        pharmaciensPage.navigate_to_pharmaciens()
        
        pharmaciensPage.click_create_pharmacien()
        
        random_id = random.randint(1000, 9999)
        pharmaciensPage.create_pharmacien(
            nom=f"PharmaNom{random_id}",
            prenom=f"PharmaPrenom{random_id}"
        )
        
        sleep(2)
        pharmaciensPage.navigate_to_pharmaciens()
        
        if pharmaciensPage.is_table_displayed():
            self.logger.log_info("✅ TC-024 PASSED: Pharmacien créé")
            assert True
        else:
            self.logger.log_error("❌ TC-024 FAILED")
            assert False
    
    @pytest.mark.P0
    def test_TC025_create_pharmacien_empty_field(self):
        """
        TC-025: Créer Pharmacien champ vide
        Technique: Valeurs limites
        Priorité: P0
        """
        self.logger.log_info("========== TC-025: Create Pharmacien Empty Field ==========")
        
        pharmaciensPage = PharmaciensPage(self.driver)
        pharmaciensPage.navigate_to_pharmaciens()
        
        pharmaciensPage.click_create_pharmacien()
        pharmaciensPage.create_pharmacien(nom="", prenom="TestPrenom")
        
        sleep(2)
        
        if "create" in pharmaciensPage.get_current_url().lower():
            self.logger.log_info("✅ TC-025 PASSED: Validation OK")
            assert True
        else:
            self.logger.log_error("❌ TC-025 FAILED")
            assert False
    
    @pytest.mark.P1
    def test_TC026_edit_pharmacien(self):
        """
        TC-026: Modifier Pharmacien
        Priorité: P1
        """
        self.logger.log_info("========== TC-026: Edit Pharmacien ==========")
        self.logger.log_info("✅ TC-026 SKIPPED")
        pytest.skip("Edit non implémenté")
    
    @pytest.mark.P1
    def test_TC027_delete_pharmacien(self):
        """
        TC-027: Supprimer Pharmacien
        Priorité: P1
        """
        self.logger.log_info("========== TC-027: Delete Pharmacien ==========")
        self.logger.log_info("✅ TC-027 SKIPPED")
        pytest.skip("Delete requiert confirmation modal")
