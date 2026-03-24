from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
import utilities.XLUtils as XLUtils
import os
import pytest
import time   # 🔥 IMPORTANT (added)


class Test_003_Login_DDT:

    baseURL = ReadConfig.getApplicationURL()

    path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "testdata", "LoginData.xlsx")
    )

    @pytest.mark.regression
    def test_login_ddt(self, setup):

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickLogin()

        self.lp = LoginPage(self.driver)

        rows = XLUtils.getRowCount(self.path, 'Sheet1')

        lst_status = []

        for r in range(2, rows + 1):

            user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            pwd = XLUtils.readData(self.path, 'Sheet1', r, 2)
            exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            print("Running row:", r, user, pwd, exp)

            self.lp.setEmail(user)
            self.lp.setPassword(pwd)
            self.lp.clickLogin()

            time.sleep(2)   # 🔥 FIX FOR HEADLESS STABILITY

            act_status = self.lp.isMyAccountPageExists()

            # ✅ PASS CASE
            if act_status == True and exp == "Pass":
                self.lp.clickLogout()

                time.sleep(1)   # 🔥 small wait before next login

                self.hp.clickMyAccount()
                self.hp.clickLogin()

                XLUtils.writeData(self.path, 'Sheet1', r, 4, "Pass")
                XLUtils.fillGreenColor(self.path, 'Sheet1', r, 4)

                lst_status.append("Pass")

            # ✅ FAIL EXPECTED CASE
            elif act_status == False and exp == "Fail":
                XLUtils.writeData(self.path, 'Sheet1', r, 4, "Pass")
                XLUtils.fillGreenColor(self.path, 'Sheet1', r, 4)

                lst_status.append("Pass")

            # ❌ WRONG RESULT
            else:
                XLUtils.writeData(self.path, 'Sheet1', r, 4, "Fail")
                XLUtils.fillRedColor(self.path, 'Sheet1', r, 4)

                lst_status.append("Fail")

        print("Final Status:", lst_status)

        assert "Fail" not in lst_status

        self.driver.quit()

# from pageObjects.HomePage import HomePage
# from pageObjects.LoginPage import LoginPage
# from utilities.readProperties import ReadConfig
# import utilities.XLUtils as XLUtils
# import os
# import pytest
#
# class Test_003_Login_DDT:
#
#     baseURL = ReadConfig.getApplicationURL()
#
#     path = os.path.abspath(
#         os.path.join(os.path.dirname(__file__), "..", "testdata", "LoginData.xlsx")
#     )
#
#     @pytest.mark.regression
#     def test_login_ddt(self, setup):
#
#         self.driver = setup
#         self.driver.get(self.baseURL)
#         self.driver.maximize_window()
#
#         self.hp = HomePage(self.driver)
#         self.hp.clickMyAccount()
#         self.hp.clickLogin()
#
#         self.lp = LoginPage(self.driver)
#
#         rows = XLUtils.getRowCount(self.path, 'Sheet1')
#
#         lst_status = []
#
#         for r in range(2, rows + 1):
#
#             user = XLUtils.readData(self.path, 'Sheet1', r, 1)
#             pwd = XLUtils.readData(self.path, 'Sheet1', r, 2)
#             exp = XLUtils.readData(self.path, 'Sheet1', r, 3)
#
#             print("Running row:", r, user, pwd, exp)
#
#             self.lp.setEmail(user)
#             self.lp.setPassword(pwd)
#             self.lp.clickLogin()
#
#             act_status = self.lp.isMyAccountPageExists()
#
#             # ✅ PASS CASE
#             if act_status == True and exp == "Pass":
#                 self.lp.clickLogout()
#                 self.hp.clickMyAccount()
#                 self.hp.clickLogin()
#
#                 XLUtils.writeData(self.path, 'Sheet1', r, 4, "Pass")
#                 XLUtils.fillGreenColor(self.path, 'Sheet1', r, 4)
#
#                 lst_status.append("Pass")
#
#             # ✅ FAIL EXPECTED CASE
#             elif act_status == False and exp == "Fail":
#                 XLUtils.writeData(self.path, 'Sheet1', r, 4, "Pass")
#                 XLUtils.fillGreenColor(self.path, 'Sheet1', r, 4)
#
#                 lst_status.append("Pass")
#
#             # ❌ WRONG RESULT
#             else:
#                 XLUtils.writeData(self.path, 'Sheet1', r, 4, "Fail")
#                 XLUtils.fillRedColor(self.path, 'Sheet1', r, 4)
#
#                 lst_status.append("Fail")
#
#         print("Final Status:", lst_status)
#
#         assert "Fail" not in lst_status
#
#         self.driver.quit()