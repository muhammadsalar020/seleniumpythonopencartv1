import os
import time
import pytest
from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from utilities.random_string import random_string_generator
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_AccountReg:

    baseURL = ReadConfig.getApplicationURL()

    @pytest.mark.regression
    def test_account_reg(self, setup):

        self.logger = LogGen.loggen()
        self.logger.info("**** test_account_reg started ****")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)

        self.hp.clickMyAccount()
        self.hp.clickRegister()

        self.regpage = AccountRegistrationPage(self.driver)

        self.regpage.setFirstName("John")
        self.regpage.setLastName("Kennedy")

        # self.email = random_string_generator() + "@gmail.com"
        # self.regpage.setEmail(self.email)
        self.email = f"test{int(time.time())}@gmail.com"
        self.regpage.setEmail(self.email)

        self.regpage.setTelephone("1234567890")
        self.regpage.setPassword("test123")
        self.regpage.setConfirmPassword("test123")

        self.regpage.setPrivacyPolicy()
        self.regpage.clickContinue()

        self.confmsg = self.regpage.get_confirmation_msg()

        print("CONF MSG:", self.confmsg)

        # ✅ FINAL ASSERTION FIX
        if self.confmsg and "Your Account Has Been Created!" in self.confmsg:
            self.logger.info("**** TEST PASSED ****")
            assert True
        else:
            self.logger.error("**** TEST FAILED ****")

            screenshot_dir = os.path.join(os.getcwd(), "screenshots")
            if not os.path.exists(screenshot_dir):
                os.makedirs(screenshot_dir)

            screenshot_path = os.path.join(screenshot_dir, "test_account_reg.png")
            self.driver.save_screenshot(screenshot_path)

            assert False

        self.logger.info("**** test_account_reg finished ****")

# import os
# from pageObjects.HomePage import HomePage
# from pageObjects.AccountRegistrationPage import AccountRegistrationPage
# from utilities.random_string import random_string_generator
# from utilities.readProperties import ReadConfig
# from utilities.customLogger import LogGen
#
#
# class Test_001_AccountReg:
#
#     baseURL = ReadConfig.getApplicationURL()
#
#     def test_account_reg(self, setup):
#
#         # Initialize logger
#         self.logger = LogGen.loggen()
#         self.logger.info("**** test_account_reg started ****")
#
#         self.driver = setup
#
#         self.logger.debug(f"Opening URL: {self.baseURL}")
#         self.driver.get(self.baseURL)
#
#         self.logger.debug("Maximizing window")
#         self.driver.maximize_window()
#
#         self.hp = HomePage(self.driver)
#
#         self.logger.debug("Clicking My Account")
#         self.hp.clickMyAccount()
#
#         self.logger.debug("Clicking Register")
#         self.hp.clickRegister()
#
#         self.regpage = AccountRegistrationPage(self.driver)
#
#         self.logger.debug("Entering First Name")
#         self.regpage.setFirstName("John")
#
#         self.logger.debug("Entering Last Name")
#         self.regpage.setLastName("Kennedy")
#
#         self.email = random_string_generator() + "@gmail.com"
#         self.logger.debug(f"Generated Email: {self.email}")
#
#         self.regpage.setEmail(self.email)
#
#         self.logger.debug("Entering Telephone")
#         self.regpage.setTelephone("1234567890")
#
#         self.logger.debug("Entering Password")
#         self.regpage.setPassword("test123")
#
#         self.regpage.setConfirmPassword("test123")
#
#         self.logger.debug("Accepting Privacy Policy")
#         # self.regpage.setPrivacyPolicy()
#         self.regpage.clickContinue()
#
#         # ✅ Handle alert (Firefox fix)
#         try:
#             alert = self.driver.switch_to.alert
#             print("ALERT BEFORE FIX:", alert.text)
#             alert.accept()
#         except:
#             pass
#
#         self.logger.debug("Clicking Continue")
#         self.regpage.clickContinue()
#
#         self.logger.debug("Fetching confirmation message")
#         self.confmsg = self.regpage.get_confirmation_msg()
#
#         print("CONF MSG:", self.confmsg)   # 🔥 Debug print
#
#         self.logger.debug(f"Confirmation message: {self.confmsg}")
#
#         # ✅ FIXED ASSERTION (CROSS-BROWSER SAFE)
#         if self.confmsg and "Your Account Has Been Created!" in self.confmsg:
#             self.logger.info("**** TEST PASSED ****")
#             assert True
#         else:
#             self.logger.error("**** TEST FAILED ****")
#
#             screenshot_dir = os.path.join(os.getcwd(), "screenshots")
#             if not os.path.exists(screenshot_dir):
#                 os.makedirs(screenshot_dir)
#
#             screenshot_path = os.path.join(screenshot_dir, "test_account_reg.png")
#             self.driver.save_screenshot(screenshot_path)
#
#             assert False
#
#         self.logger.info("**** test_account_reg finished ****")



# import sys
# import os
#
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#
# from pageObjects.HomePage import HomePage
# from pageObjects.AccountRegistrationPage import AccountRegistrationPage
# from utilities.random_string import random_string_generator
# from utilities.readProperties import ReadConfig
# from utilities.customLogger import LogGen
#
#
# class Test_001_AccountReg:
#
#     baseURL = ReadConfig.getApplicationURL()
#
#     def test_account_reg(self, setup):
#
#         # Initialize logger
#         self.logger = LogGen.loggen()
#         self.logger.info("**** test_account_reg started ****")
#
#         self.logger.debug("Launching browser")
#         self.driver = setup
#
#         self.logger.debug(f"Opening URL: {self.baseURL}")
#         self.driver.get(self.baseURL)
#
#         self.logger.debug("Maximizing window")
#         self.driver.maximize_window()
#
#         self.logger.debug("Initializing HomePage object")
#         self.hp = HomePage(self.driver)
#
#         self.logger.debug("Clicking My Account")
#         self.hp.clickMyAccount()
#
#         self.logger.debug("Clicking Register")
#         self.hp.clickRegister()
#
#         self.logger.debug("Initializing Registration Page")
#         self.regpage = AccountRegistrationPage(self.driver)
#
#         self.logger.debug("Entering First Name: John")
#         self.regpage.setFirstName("John")
#
#         self.logger.debug("Entering Last Name: Kennedy")
#         self.regpage.setLastName("Kennedy")
#
#         self.email = random_string_generator() + "@gmail.com"
#         self.logger.debug(f"Generated Email: {self.email}")
#
#         self.regpage.setEmail(self.email)
#
#         self.logger.debug("Entering Telephone")
#         self.regpage.setTelephone("1234567890")
#
#         self.logger.debug("Entering Password")
#         self.regpage.setPassword("test123")
#
#         self.regpage.setConfirmPassword("test123")
#
#         self.logger.debug("Accepting Privacy Policy")
#         self.regpage.setPrivacyPolicy()
#
#         self.logger.debug("Clicking Continue")
#         self.regpage.clickContinue()
#
#         self.logger.debug("Fetching confirmation message")
#         # self.confmsg = self.regpage.getconfirmationmsg()
#         self.confmsg = self.regpage.get_confirmation_msg()
#
#         self.logger.debug(f"Confirmation message: {self.confmsg}")
#
#         if self.confmsg == "Your Account Has Been Created!":
#             self.logger.info("**** TEST PASSED ****")
#             assert True
#         else:
#             self.logger.error("**** TEST FAILED ****")
#
#             screenshot_dir = os.path.join(os.getcwd(), "screenshots")
#             if not os.path.exists(screenshot_dir):
#                 os.makedirs(screenshot_dir)
#
#             screenshot_path = os.path.join(screenshot_dir, "test_account_reg.png")
#             self.driver.save_screenshot(screenshot_path)
#
#             assert False
#
#         self.logger.info("**** test_account_reg finished ****")



# from pageObjects.HomePage import HomePage
# from pageObjects.AccountRegistrationPage import AccountRegistrationPage
# from utilities import randomeString
# import os
# from utilities.readProperties import ReadConfig
# from utilities.customLogger import LogGen
#
#
# class Test_001_AccountReg:
#
#     baseURL = ReadConfig.getApplicationURL()
#
#     def test_account_reg(self, setup):
#
#         # Initialize logger HERE ✅
#         self.logger = LogGen.loggen()
#         self.logger.info("**** test_account_reg started ****")
#
#         self.driver = setup
#         self.driver.get(self.baseURL)
#         self.driver.maximize_window()
#
#         self.logger.info("Opening Home Page")
#
#         self.hp = HomePage(self.driver)
#
#         self.hp.clickMyAccount()
#         self.logger.info("Clicked My Account")
#
#         self.hp.clickRegister()
#         self.logger.info("Clicked Register")
#
#         self.regpage = AccountRegistrationPage(self.driver)
#
#         self.regpage.setFirstName("John")
#         self.regpage.setLastName("Kennedy")
#
#         self.email = randomeString.random_string_generator() + "@gmail.com"
#         self.regpage.setEmail(self.email)
#
#         self.regpage.setTelephone("1234567890")
#         self.regpage.setPassword("test123")
#         self.regpage.setConfirmPassword("test123")
#
#         self.regpage.setPrivacyPolicy()
#         self.regpage.clickContinue()
#
#         self.confmsg = self.regpage.getconfirmationmsg()
#
#         if self.confmsg == "Your Account Has Been Created!":
#             self.logger.info("**** TEST PASSED ****")
#             assert True
#         else:
#             self.logger.error("**** TEST FAILED ****")
#
#             screenshot_path = os.path.abspath(os.curdir) + "/Screenshots/test_account_reg.png"
#             self.driver.save_screenshot(screenshot_path)
#
#             assert False
#
#         self.logger.info("**** test_account_reg finished ****")


# from pageObjects.HomePage import HomePage
# from pageObjects.AccountRegistrationPage import AccountRegistrationPage
# from utilities import randomeString
# import os
# from utilities.readProperties import ReadConfig
# from utilities.customLogger import LogGen
#
#
#
# class Test_001_AccountReg:
#
#     baseURL = ReadConfig.getApplicationURL()
#     logger = LogGen.loggen() #logging
#
#     def test_account_reg(self, setup):
#         self.logger.info("**** test_account_reg started ****")
#
#         self.driver = setup
#         self.driver.get(self.baseURL)
#         self.driver.maximize_window()
#
#         self.hp = HomePage(self.driver)
#
#         self.hp.clickMyAccount()
#         self.hp.clickRegister()
#
#         self.regpage = AccountRegistrationPage(self.driver)
#
#         self.regpage.setFirstName("John")
#         self.regpage.setLastName("Kennedy")
#
#         self.email = randomeString.random_string_generator() + "@gmail.com"
#         self.regpage.setEmail(self.email)
#
#         self.regpage.setTelephone("1234567890")
#         self.regpage.setPassword("test123")
#         self.regpage.setConfirmPassword("test123")
#
#         self.regpage.setPrivacyPolicy()
#         self.regpage.clickContinue()
#
#         self.confmsg = self.regpage.getconfirmationmsg()
#
#         if self.confmsg == "Your Account Has Been Created!":
#             assert True
#             self.driver.close()
#         else:
#             # Screenshot folder
#             screenshot_path = os.path.abspath(os.curdir) + "/Screenshots/test_account_reg.png"
#
#             # Take Screenshot
#             self.driver.save_screenshot(screenshot_path)
#
#             self.driver.close()
#             assert False
#             self.logger.info("**** test_account_reg finished ****")



# from pageObjects.HomePage import HomePage
# from pageObjects.AccountRegistrationPage import AccountRegistrationPage
# from utilities import randomeString
#
#
# class Test_001_AccountReg:
#
#     baseURL = "https://naveenautomationlabs.com/opencart/"
#
#     def test_account_reg(self, setup):
#
#         self.driver = setup
#         self.driver.get(self.baseURL)
#         self.driver.maximize_window()
#
#         self.hp = HomePage(self.driver)
#
#         self.hp.clickMyAccount()
#         self.hp.clickRegister()
#
#         self.regpage = AccountRegistrationPage(self.driver)
#
#         self.regpage.setFirstName("John")
#         self.regpage.setLastName("Kennedy")
#
#         self.email = randomeString.random_string_generator() + "@gmail.com"
#         self.regpage.setEmail(self.email)
#
#         self.regpage.setTelephone("1234567890")
#         self.regpage.setPassword("test123")
#         self.regpage.setConfirmPassword("test123")
#
#         self.regpage.setPrivacyPolicy()
#         self.regpage.clickContinue()
#
#         self.confmsg = self.regpage.getconfirmationmsg()
#
#         if self.confmsg == "Your Account Has Been Created!":
#             assert True
#         else:
#             assert False




# from pageObjects.HomePage import HomePage
# from pageObjects.AccountRegistrationPage import AccountRegistrationPage
# from utilities import randomeString
#
#
# class Test_001_AccountReg:
#     baseURL = "https://demo.opencart.com/"
#
#     def test_account_reg(self, setup):
#
#         self.driver = setup
#         self.driver.get(self.baseURL)
#         self.driver.maximize_window()
#
#         # Home Page
#         self.hp = HomePage(self.driver)
#         self.hp.clickMyAccount()
#         self.hp.clickRegister()
#
#         # Registration Page
#         self.regpage = AccountRegistrationPage(self.driver)
#
#         self.regpage.setFirstName("John")
#         self.regpage.setLastName("Canedy")
#
#         self.email = randomeString.random_string_generator() + "@gmail.com"
#         self.regpage.setEmail(self.email)
#
#         self.regpage.setTelephone("65656565")
#         self.regpage.setPassword("abcxyz")
#         self.regpage.setConfirmPassword("abcxyz")
#
#         self.regpage.setPrivacyPolicy()
#         self.regpage.clickContinue()
#
#         self.confmsg = self.regpage.getconfirmationmsg()
#
#         self.driver.quit()
#
#         if self.confmsg == "Your Account Has Been Created!":
#             assert True
#         else:
#             assert False