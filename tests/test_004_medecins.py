import pytest
from pages.LoginPage import LoginPage
from pages.MedecinsPage import MedecinsPage
from utilities.readProperties import ReadConfig
from utilities.newCustomLogger import LogGen
from time import sleep
import random

@pytest.mark.medecins
class Test_004_Medecins:
    """Tests Médecins (TC-017 à TC-022)"""
    
    baseURL = ReadConfig.getApplicationURL()
    loginURL = ReadConfig.getLoginURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen("./Logs/medecins.log")
    
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
    def test_TC017_display_medecins_list(self):
        """
        TC-017: Afficher liste Médecins
        Technique: Tests de confirmation
        Priorité: P0
        """
        self.logger.log_info("========== TC-017: Display Medecins List ==========")
        
        medecinsPage = MedecinsPage(self.driver)
        medecinsPage.navigate_to_medecins()
        sleep(2)
        
        if medecinsPage.is_table_displayed():
            count = medecinsPage.get_medecins_count()
            self.logger.log_info(f"✅ TC-017 PASSED: {count} médecins affichés")
            medecinsPage.take_screenshot("TC017_success")
            assert True
        else:
            self.logger.log_error("❌ TC-017 FAILED: Tableau non affiché")
            medecinsPage.take_screenshot("TC017_failed")
            assert False
    
    @pytest.mark.P0
    def test_TC018_create_medecin_valid(self):
        """
        TC-018: Créer Médecin valide
        Technique: Partition d'équivalence
        Priorité: P0
        """
        self.logger.log_info("========== TC-018: Create Medecin Valid ==========")
        
        medecinsPage = MedecinsPage(self.driver)
        medecinsPage.navigate_to_medecins()
        
        count_before = medecinsPage.get_medecins_count()
        
        medecinsPage.click_create_medecin()
        
        random_id = random.randint(1000, 9999)
        medecinsPage.create_medecin(
            nom=f"DrNom{random_id}",
            prenom=f"DrPrenom{random_id}",
            specialite="Cardiologue",
            telephone="+216 20 123 456",
            email=f"dr{random_id}@example.com"
        )
        
        sleep(2)
        medecinsPage.navigate_to_medecins()
        count_after = medecinsPage.get_medecins_count()
        
        if count_after > count_before:
            self.logger.log_info("✅ TC-018 PASSED: Médecin créé")
            assert True
        else:
            self.logger.log_error("❌ TC-018 FAILED")
            assert False
    
    @pytest.mark.P0
    def test_TC019_create_medecin_empty_nom(self):
        """
        TC-019: Créer Médecin Nom vide
        Technique: Valeurs limites
        Priorité: P0
        """
        self.logger.log_info("========== TC-019: Create Medecin Empty Nom ==========")
        
        medecinsPage = MedecinsPage(self.driver)
        medecinsPage.navigate_to_medecins()
        
        count_before = medecinsPage.get_medecins_count()
        
        medecinsPage.click_create_medecin()
        medecinsPage.create_medecin(
            nom="",
            prenom="TestPrenom",
            specialite="Dermatologue"
        )
        
        sleep(2)
        
        if medecinsPage.is_error_displayed() or "create" in medecinsPage.get_current_url():
            self.logger.log_info("✅ TC-019 PASSED: Validation bloque nom vide")
            assert True
        else:
            self.logger.log_error("❌ TC-019 FAILED")
            assert False
    
    @pytest.mark.P1
    def test_TC020_edit_medecin(self):
        """
        TC-020: Modifier Médecin
        Technique: Tests de confirmation
        Priorité: P1
        """
        self.logger.log_info("========== TC-020: Edit Medecin ==========")
        self.logger.log_info("✅ TC-020 SKIPPED: Modification non testée")
        pytest.skip("Edit non implémenté dans ce test")
    
    @pytest.mark.P1
    def test_TC021_delete_medecin(self):
        """
        TC-021: Supprimer Médecin
        Technique: Tests de confirmation
        Priorité: P1
        """
        self.logger.log_info("========== TC-021: Delete Medecin ==========")
        self.logger.log_info("✅ TC-021 SKIPPED: Suppression requiert confirmation modal")
        pytest.skip("Delete requiert interaction modal")
    
    @pytest.mark.P1
    def test_TC022_view_medecin_details(self):
        """
        TC-022: Consulter Détails Médecin
        Technique: Tests de confirmation
        Priorité: P1
        """
        self.logger.log_info("========== TC-022: View Medecin Details ==========")
        self.logger.log_info("✅ TC-022 SKIPPED")
        pytest.skip("Détails non implémentés")
