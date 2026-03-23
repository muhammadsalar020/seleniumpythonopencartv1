from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import os
import pytest


class Test_002_Login:

    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    user = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    @pytest.mark.smoke
    def test_login(self, setup):

        self.logger.info("******** Starting Login Test ********")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        # ✅ Navigate to login page
        self.hp = HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickLogin()

        # ✅ Perform login
        self.lp = LoginPage(self.driver)
        self.lp.login(self.user, self.password)

        # ✅ Validation
        if self.lp.isMyAccountPageExists():
            self.logger.info("******** Login Test Passed ********")
            assert True
        else:
            self.driver.save_screenshot(
                os.path.join(os.getcwd(), "screenshots", "test_login.png")
            )
            self.logger.error("******** Login Test Failed ********")
            assert False

        self.driver.quit()
        self.logger.info("******** End of Login Test ********")