import pytest
import random
from time import sleep
from pages.LoginPage import LoginPage
from pages.MedecinsPage import MedecinsPage
from utilities.readProperties import ReadConfig
from utilities.newCustomLogger import LogGen

@pytest.mark.medecins
class Test_004_Medecins:
    """Tests Médecins page (/Medecins)"""

    loginURL = ReadConfig.getLoginURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen("./Logs/medecins.log")

    @pytest.fixture(autouse=True)
    def setup_login(self, setup):
        """Auto-login before each test"""
        self.driver = setup
        self.driver.get(self.loginURL)
        LoginPage(self.driver).login(self.username, self.password)
        sleep(2)
        yield
        self.driver.quit()
    @pytest.hookimpl(tryfirst=True, hookwrapper=True)
    def pytest_runtest_makereport(self, item, call):
        outcome = yield
        rep = outcome.get_result()
        if rep.when == "call" and rep.failed:
            test_name = item.name
            filepath = f"./Screenshots/{test_name}.png"
            self.driver.save_screenshot(filepath)
            print(f"💾 Screenshot saved: {filepath}")

    # ✅ TC017 - Display Medecins List
    @pytest.mark.P0
    def test_TC017_display_medecins_list(self):
        self.logger.log_info("TC-017: Display Medecins List")
        medecins = MedecinsPage(self.driver)
        medecins.navigate_to_medecins()
        sleep(1)
        if medecins.is_table_displayed():
            count = medecins.get_medecins_count()
            self.logger.log_info(f"✅ TC-017 PASSED: {count} médecins affichés")
            assert True
        else:
            self.logger.log_error("❌ TC-017 FAILED: Table not displayed")
            assert False

    # ✅ TC018 - Create Medecin Valid
    @pytest.mark.P0
    def test_TC018_create_medecin_valid(self):
        self.logger.log_info("TC-018: Create Medecin Valid")
        medecins = MedecinsPage(self.driver)
        medecins.navigate_to_medecins()
        count_before = medecins.get_medecins_count()

        medecins.click_create_medecin()
        rid = random.randint(1000, 9999)
        medecins.create_medecin(
            nom=f"DrNom{rid}",
            prenom=f"DrPrenom{rid}",
            specialite="Cardiologue",
            telephone="+21620123456",
            email=f"dr{rid}@example.com"
        )

        medecins.navigate_to_medecins()
        count_after = medecins.get_medecins_count()

        if count_after > count_before:
            self.logger.log_info("✅ TC-018 PASSED: Médecin créé")
            assert True
        else:
            self.logger.log_error("❌ TC-018 FAILED: Médecin non créé")
            assert False

    # ✅ TC019 - Create Medecin Empty Nom
    @pytest.mark.P0
    def test_TC019_create_medecin_empty_nom(self):
        self.logger.log_info("TC-019: Create Medecin Empty Nom")
        medecins = MedecinsPage(self.driver)
        medecins.navigate_to_medecins()

        medecins.click_create_medecin()
        medecins.create_medecin(
            nom="",
            prenom="TestPrenom",
            specialite="Dermatologue"
        )

        # Check validation: should stay on form page
        if medecins.is_element_present(medecins.INPUT_NOM):
            self.logger.log_info("✅ TC-019 PASSED: Validation bloque nom vide")
            assert True
        else:
            self.logger.log_error("❌ TC-019 FAILED: Form submitted with empty nom")
            assert False

    # ⚠️ TC020 - Edit Medecin
    @pytest.mark.P1
    def test_TC020_edit_medecin(self):
        self.logger.log_info("TC-020: Edit Medecin SKIPPED")
        pytest.skip("Edit non implémenté")

    # ⚠️ TC021 - Delete Medecin
    @pytest.mark.P1
    def test_TC021_delete_medecin(self):
        self.logger.log_info("TC-021: Delete Medecin SKIPPED")
        pytest.skip("Delete requiert modal confirmation")

    # ⚠️ TC022 - View Medecin Details
    @pytest.mark.P1
    def test_TC022_view_medecin_details(self):
        self.logger.log_info("TC-022: View Medecin Details SKIPPED")
        pytest.skip("Détails non implémentés")
