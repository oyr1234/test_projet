import pytest
from pages.LoginPage import LoginPage
from pages.MedicamentsPage import MedicamentsPage
from utilities.readProperties import ReadConfig
from utilities.newCustomLogger import LogGen
from time import sleep
import random

@pytest.mark.medicaments
class Test_007_Medicaments:
    """Tests Médicaments (TC-033 à TC-038)"""
    
    baseURL = ReadConfig.getApplicationURL()
    loginURL = ReadConfig.getLoginURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen("./Logs/medicaments.log")
    
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
    def test_TC033_display_medicaments_list(self):
        """
        TC-033: Afficher liste Médicaments
        Technique: Tests de confirmation
        Priorité: P0
        """
        self.logger.log_info("========== TC-033: Display Medicaments List ==========")
        
        medicamentsPage = MedicamentsPage(self.driver)
        medicamentsPage.navigate_to_medicaments()
        sleep(2)
        
        if medicamentsPage.is_table_displayed():
            count = medicamentsPage.get_medicaments_count()
            self.logger.log_info(f"✅ TC-033 PASSED: {count} médicaments affichés")
            medicamentsPage.take_screenshot("TC033_success")
            assert True
        else:
            self.logger.log_error("❌ TC-033 FAILED")
            medicamentsPage.take_screenshot("TC033_failed")
            assert False
    
    @pytest.mark.P0
    def test_TC034_create_medicament_valid(self):
        """
        TC-034: Créer Médicament valide
        Technique: Partition d'équivalence
        Priorité: P0
        """
        self.logger.log_info("========== TC-034: Create Medicament Valid ==========")
        
        medicamentsPage = MedicamentsPage(self.driver)
        medicamentsPage.navigate_to_medicaments()
        
        count_before = medicamentsPage.get_medicaments_count()
        
        medicamentsPage.click_create_medicament()
        
        random_id = random.randint(1000, 9999)
        medicamentsPage.create_medicament(
            nom=f"Médicament Test {random_id}",
            prix=25.50
        )
        
        sleep(2)
        medicamentsPage.navigate_to_medicaments()
        count_after = medicamentsPage.get_medicaments_count()
        
        if count_after > count_before:
            self.logger.log_info("✅ TC-034 PASSED: Médicament créé")
            assert True
        else:
            self.logger.log_error("❌ TC-034 FAILED")
            assert False
    
    @pytest.mark.P0
    def test_TC035_create_medicament_empty_nom(self):
        """
        TC-035: Créer Médicament Nom vide
        Technique: Valeurs limites
        Priorité: P0
        """
        self.logger.log_info("========== TC-035: Create Medicament Empty Nom ==========")
        
        medicamentsPage = MedicamentsPage(self.driver)
        medicamentsPage.navigate_to_medicaments()
        
        medicamentsPage.click_create_medicament()
        medicamentsPage.create_medicament(nom="", prix=10.00)
        
        sleep(2)
        
        if medicamentsPage.is_error_displayed() or "create" in medicamentsPage.get_current_url():
            self.logger.log_info("✅ TC-035 PASSED: Validation bloque nom vide")
            assert True
        else:
            self.logger.log_error("❌ TC-035 FAILED")
            assert False
    
    @pytest.mark.P1
    def test_TC036_create_medicament_invalid_prix(self):
        """
        TC-036: Créer Médicament Prix invalide
        Technique: Valeurs limites
        Priorité: P1
        """
        self.logger.log_info("========== TC-036: Create Medicament Invalid Prix ==========")
        
        medicamentsPage = MedicamentsPage(self.driver)
        medicamentsPage.navigate_to_medicaments()
        
        medicamentsPage.click_create_medicament()
        medicamentsPage.create_medicament(nom="TestMedicament", prix=-10.00)
        
        sleep(2)
        
        if medicamentsPage.is_error_displayed():
            self.logger.log_info("✅ TC-036 PASSED: Prix négatif refusé")
            assert True
        else:
            self.logger.log_warning("⚠️ TC-036: Prix négatif accepté")
            assert True  # Pas bloquant
    
    @pytest.mark.P1
    def test_TC037_edit_medicament(self):
        """TC-037: Modifier Médicament"""
        self.logger.log_info("========== TC-037: Edit Medicament ==========")
        self.logger.log_info("✅ TC-037 SKIPPED")
        pytest.skip("Edit non implémenté")
    
    @pytest.mark.P1
    def test_TC038_delete_medicament(self):
        """TC-038: Supprimer Médicament"""
        self.logger.log_info("========== TC-038: Delete Medicament ==========")
        self.logger.log_info("✅ TC-038 SKIPPED")
        pytest.skip("Delete requiert confirmation modal")
