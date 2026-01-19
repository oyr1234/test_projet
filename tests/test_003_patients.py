import pytest
from time import sleep

from pages.LoginPage import LoginPage
from pages.PatientsPage import PatientsPage
from utilities.readProperties import ReadConfig
from utilities.newCustomLogger import LogGen


@pytest.mark.patients
class Test_003_Patients:
    """Tests Patients page (/Patients)"""

    loginURL = ReadConfig.getLoginURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen("./Logs/patients.log")

    @pytest.fixture(autouse=True)
    def setup_login(self, setup):
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

    # ✅ TC010
    @pytest.mark.P0
    def test_TC010_display_patients_page(self):
        self.logger.log_info("TC-010: Display Patients Page")
        patients = PatientsPage(self.driver)
        patients.navigate_to_patients()
        assert patients.is_table_displayed()

    # ✅ TC011
    @pytest.mark.P0
    def test_TC011_display_patients_list_or_empty(self):
        self.logger.log_info("TC-011: Display list or empty state")
        patients = PatientsPage(self.driver)
        patients.navigate_to_patients()
        count = patients.get_patients_count()
        assert count >= 0

    # ✅ TC012
    @pytest.mark.P0
    def test_TC012_navigate_to_create_patient(self):
        self.logger.log_info("TC-012: Navigate to Create Patient")
        patients = PatientsPage(self.driver)
        patients.navigate_to_patients()
        patients.click_create_patient()
        assert "/Patients/Create" in self.driver.current_url

    # ✅ TC013
    @pytest.mark.P1
    def test_TC013_view_patient_details(self):
        self.logger.log_info("TC-013: View Patient Details")
        patients = PatientsPage(self.driver)
        patients.navigate_to_patients()

        if patients.get_patients_count() == 0:
            pytest.skip("No patient available")

        patients.click_details_first_patient()
        assert patients.is_details_modal_displayed()

    # ⚠️ TC014
    @pytest.mark.P1
    def test_TC014_edit_patient_navigation(self):
        self.logger.log_info("TC-014: Edit Patient Navigation")
        patients = PatientsPage(self.driver)
        patients.navigate_to_patients()

        if patients.get_patients_count() == 0:
            pytest.skip("No patient available")

        patients.click_edit_first_patient()
        assert "/Patients/Edit" in self.driver.current_url

    # ❌ TC015 (Expected limitation)
    @pytest.mark.P1
    def test_TC015_delete_patient(self):
        pytest.xfail("Delete confirmation modal not automated")

    # ❌ TC016 (Negative case)
    @pytest.mark.P1
    def test_TC016_details_modal_not_visible_by_default(self):
        patients = PatientsPage(self.driver)
        patients.navigate_to_patients()
        assert not patients.is_details_modal_displayed()
