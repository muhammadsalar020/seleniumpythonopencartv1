from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    lnk_myaccount_xpath = "//span[text()='My Account']"
    lnk_register_xpath = "//a[text()='Register']"
    lnk_login_xpath = "//a[text()='Login']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def clickMyAccount(self):
        element = self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.lnk_myaccount_xpath))
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.execute_script("arguments[0].click();", element)

    def clickRegister(self):
        element = self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.lnk_register_xpath))
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.execute_script("arguments[0].click();", element)

    def clickLogin(self):
        element = self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.lnk_login_xpath))
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.execute_script("arguments[0].click();", element)

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# class HomePage:
#
#     lnk_myaccount = (By.XPATH, "//span[text()='My Account']")
#     lnk_register = (By.LINK_TEXT, "Register")
#     lnk_login = (By.LINK_TEXT, "Login")
#
#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, 10)
#
#     def clickMyAccount(self):
#         self.wait.until(
#             EC.element_to_be_clickable(self.lnk_myaccount)
#         ).click()
#
#     def clickRegister(self):
#         self.wait.until(
#             EC.element_to_be_clickable(self.lnk_register)
#         ).click()
#
#     def clickLogin(self):
#         self.wait.until(
#             EC.element_to_be_clickable(self.lnk_login)
#         ).click()



# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# class HomePage:
#
#     lnk_myaccount_xpath = "//span[text()='My Account']"
#     lnk_register_linktext = "Register"
#     lnk_login_linktext = "Login"
#
#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, 10)
#
#     def clickMyAccount(self):
#         self.wait.until(
#             EC.element_to_be_clickable((By.XPATH, self.lnk_myaccount_xpath))
#         ).click()
#
#     def clickRegister(self):
#         self.wait.until(
#             EC.element_to_be_clickable((By.LINK_TEXT, self.lnk_register_linktext))
#         ).click()
#
#     def clickLogin(self):
#         self.wait.until(
#             EC.element_to_be_clickable((By.LINK_TEXT, self.lnk_login_linktext))
#         ).click()


# from selenium.webdriver.common.by import By
#
#
# class HomePage():
#     lnk_myaccount_xpath = "//a[@title='My Account']"
#     lnk_register_linktext = "Register"
#     lnk_login_linktext = "Login"
#
#     def __init__(self, driver):
#         self.driver = driver
#
#     def clickMyAccount(self):
#         self.driver.find_element(By.XPATH, self.lnk_myaccount_xpath).click()
#
#     def clickRegister(self):
#         self.driver.find_element(By.LINK_TEXT,self.lnk_register_linktext).click()
#
#     def clickLogin(self):
#         self.driver.find_element(By.LINK_TEXT,self.lnk_login_linktext).click()
