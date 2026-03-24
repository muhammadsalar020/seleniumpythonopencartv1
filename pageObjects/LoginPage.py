from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    txt_email = (By.ID, "input-email")
    txt_password = (By.ID, "input-password")
    btn_login = (By.XPATH, "//input[@value='Login']")
    txt_myaccount = (By.XPATH, "//h2[text()='My Account']")

    # Logout elements
    lnk_myaccount_menu = (By.XPATH, "//span[text()='My Account']")
    lnk_logout = (By.XPATH, "//a[text()='Logout']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)   # increased wait

    def setEmail(self, email):
        element = self.wait.until(
            EC.presence_of_element_located(self.txt_email)
        )
        element.clear()
        element.send_keys(email)

    def setPassword(self, password):
        element = self.wait.until(
            EC.presence_of_element_located(self.txt_password)
        )
        element.clear()
        element.send_keys(password)

    def clickLogin(self):
        element = self.wait.until(
            EC.presence_of_element_located(self.btn_login)
        )
        self.driver.execute_script("arguments[0].click();", element)

    def login(self, email, password):
        self.setEmail(email)
        self.setPassword(password)
        self.clickLogin()

    def isMyAccountPageExists(self):
        try:
            return self.wait.until(
                EC.presence_of_element_located(self.txt_myaccount)
            ).is_displayed()
        except:
            return False

    # 🔥 FINAL FIXED LOGOUT METHOD
    def clickLogout(self):
        # Step 1: Open My Account dropdown
        my_account = self.wait.until(
            EC.presence_of_element_located(self.lnk_myaccount_menu)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", my_account)
        self.driver.execute_script("arguments[0].click();", my_account)

        # Step 2: Click Logout
        logout = self.wait.until(
            EC.presence_of_element_located(self.lnk_logout)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", logout)
        self.driver.execute_script("arguments[0].click();", logout)


# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# class LoginPage:
#
#     txt_email = (By.ID, "input-email")
#     txt_password = (By.ID, "input-password")
#     btn_login = (By.XPATH, "//input[@value='Login']")
#     txt_myaccount = (By.XPATH, "//h2[text()='My Account']")
#
#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, 10)
#
#     def setEmail(self, email):
#         self.wait.until(
#             EC.visibility_of_element_located(self.txt_email)
#         ).clear()
#         self.driver.find_element(*self.txt_email).send_keys(email)
#
#     def setPassword(self, password):
#         self.driver.find_element(*self.txt_password).clear()
#         self.driver.find_element(*self.txt_password).send_keys(password)
#
#     def clickLogin(self):
#         self.driver.find_element(*self.btn_login).click()
#
#     def login(self, email, password):
#         self.setEmail(email)
#         self.setPassword(password)
#         self.clickLogin()
#
#     def isMyAccountPageExists(self):
#         try:
#             self.wait.until(
#                 EC.visibility_of_element_located(self.txt_myaccount)
#             )
#             return True
#         except:
#             return False


# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# class LoginPage:
#
#     # Locators
#     txt_email = (By.ID, "input-email")
#     txt_password = (By.ID, "input-password")
#     btn_login = (By.XPATH, "//input[@value='Login']")
#     txt_myaccount = (By.XPATH, "//h2[text()='My Account']")
#
#     def __init__(self, driver):
#         self.driver = driver
#
#     # Actions
#     def setEmail(self, email):
#         self.driver.find_element(*self.txt_email).clear()
#         self.driver.find_element(*self.txt_email).send_keys(email)
#
#     def setPassword(self, password):
#         self.driver.find_element(*self.txt_password).clear()
#         self.driver.find_element(*self.txt_password).send_keys(password)
#
#     def clickLogin(self):
#         self.driver.find_element(*self.btn_login).click()
#
#     # Combined method (Best Practice)
#     def login(self, email, password):
#         self.setEmail(email)
#         self.setPassword(password)
#         self.clickLogin()
#
#     # Verification
#     def isMyAccountPageExists(self):
#         try:
#             WebDriverWait(self.driver, 10).until(
#                 EC.visibility_of_element_located(self.txt_myaccount)
#             )
#             return True
#         except:
#             return False