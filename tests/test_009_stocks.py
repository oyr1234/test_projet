import pytest
from pages.LoginPage import LoginPage
from pages.StocksPage import StocksPage
from utilities.readProperties import ReadConfig
from utilities.newCustomLogger import LogGen
from time import sleep


@pytest.mark.stocks
class Test_009_Stocks:
    """Tests Stocks (TC-049 à TC-053)"""

    loginURL = ReadConfig.getLoginURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen("./Logs/stocks.log")

    @pytest.fixture(autouse=True)
    def setup_login(self, setup):
        self.driver = setup
        self.driver.get(self.loginURL)

        loginPage = LoginPage(self.driver)
        loginPage.login(self.username, self.password)
        sleep(2)

        yield

        self.driver.close()

    @pytest.mark.P0
    def test_TC049_display_stocks_list(self):
        self.logger.log_info("========== TC-049: Display Stocks List ==========")

        stocksPage = StocksPage(self.driver)
        stocksPage.navigate_to_stocks()
        sleep(2)

        assert stocksPage.is_table_displayed(), "Stocks table not displayed"

    @pytest.mark.P0
    def test_TC050_create_stock_valid(self):
        self.logger.log_info("========== TC-050: Create Stock Valid ==========")

        stocksPage = StocksPage(self.driver)
        stocksPage.navigate_to_stocks()
        stocksPage.click_create_stock()

        stocksPage.create_stock(
            medicament_index=1,
            pharmacie_index=1,
            quantite=100,
            seuil=10
        )

        assert not stocksPage.is_error_displayed(), "Error message displayed"

    @pytest.mark.P0
    def test_TC051_create_stock_negative_quantity(self):
        self.logger.log_info("========== TC-051: Create Stock Negative Quantity ==========")

        stocksPage = StocksPage(self.driver)
        stocksPage.navigate_to_stocks()
        stocksPage.click_create_stock()

        stocksPage.create_stock(
            medicament_index=1,
            pharmacie_index=1,
            quantite=-50,
            seuil=10
        )

        assert stocksPage.is_error_displayed() or "create" in stocksPage.get_current_url().lower()

    @pytest.mark.P1
    def test_TC052_edit_stock(self):
        pytest.skip("Edit non implémenté")

    @pytest.mark.P1
    def test_TC053_delete_stock(self):
        pytest.skip("Delete requiert confirmation modal")
