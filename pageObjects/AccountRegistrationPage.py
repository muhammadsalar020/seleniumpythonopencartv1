from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AccountRegistrationPage:

    txt_firstname_name = "firstname"
    txt_lastname_name = "lastname"
    txt_email_name = "email"
    txt_telephone_name = "telephone"
    txt_password_name = "password"
    txt_confirm_password_name = "confirm"
    chk_policy_name = "agree"
    btn_continue_xpath = "//input[@value='Continue']"

    # ✅ Stable locator
    txt_confirmation_xpath = "//div[@id='content']/h1"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def setFirstName(self, fname):
        self.wait.until(EC.presence_of_element_located((By.NAME, self.txt_firstname_name))).send_keys(fname)

    def setLastName(self, lname):
        self.wait.until(EC.presence_of_element_located((By.NAME, self.txt_lastname_name))).send_keys(lname)

    def setEmail(self, email):
        self.wait.until(EC.presence_of_element_located((By.NAME, self.txt_email_name))).send_keys(email)

    def setTelephone(self, tel):
        self.wait.until(EC.presence_of_element_located((By.NAME, self.txt_telephone_name))).send_keys(tel)

    def setPassword(self, pwd):
        self.wait.until(EC.presence_of_element_located((By.NAME, self.txt_password_name))).send_keys(pwd)

    def setConfirmPassword(self, pwd):
        self.wait.until(EC.presence_of_element_located((By.NAME, self.txt_confirm_password_name))).send_keys(pwd)

    # ✅ FIXED checkbox (Firefox issue)
    def setPrivacyPolicy(self):
        checkbox = self.wait.until(
            EC.presence_of_element_located((By.NAME, self.chk_policy_name))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)
        self.driver.execute_script("arguments[0].click();", checkbox)

    # def clickContinue(self):
    #     self.wait.until(EC.element_to_be_clickable((By.XPATH, self.btn_continue_xpath))).click()
    def clickContinue(self):
        button = self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.btn_continue_xpath))
        )

        # Scroll into view
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)

        # Click using JS (important for Firefox)
        self.driver.execute_script("arguments[0].click();", button)

    # ✅ FIXED confirmation
    # def get_confirmation_msg(self):
    #     try:
    #         # Handle alert (Firefox issue)
    #         try:
    #             alert = self.driver.switch_to.alert
    #             print("ALERT FOUND:", alert.text)
    #             alert.accept()
    #         except:
    #             pass
    #
    #         element = self.wait.until(
    #             EC.visibility_of_element_located((By.XPATH, self.txt_confirmation_xpath))
    #         )
    #         return element.text.strip()
    #     except Exception as e:
    #         print("ERROR fetching confirmation message:", e)
    #         return None

    def get_confirmation_msg(self):
        try:
            element = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self.txt_confirmation_xpath))
            )
            return element.text.strip()
        except Exception as e:
            print("ERROR fetching confirmation message:", e)
            return None


# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# class AccountRegistrationPage:
#
#     txt_firstname_name = "firstname"
#     txt_lastname_name = "lastname"
#     txt_email_name = "email"
#     txt_telephone_name = "telephone"
#     txt_password_name = "password"
#     txt_confirm_password_name = "confirm"
#     chk_policy_name = "agree"
#     btn_continue_xpath = "//input[@value='Continue']"
#
#     # ✅ UPDATED (more stable locator)
#     txt_confirmation_xpath = "//div[@id='content']/h1"
#
#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, 10)
#
#     def setFirstName(self, fname):
#         self.wait.until(EC.presence_of_element_located((By.NAME, self.txt_firstname_name))).send_keys(fname)
#
#     def setLastName(self, lname):
#         self.wait.until(EC.presence_of_element_located((By.NAME, self.txt_lastname_name))).send_keys(lname)
#
#     def setEmail(self, email):
#         self.wait.until(EC.presence_of_element_located((By.NAME, self.txt_email_name))).send_keys(email)
#
#     def setTelephone(self, tel):
#         self.wait.until(EC.presence_of_element_located((By.NAME, self.txt_telephone_name))).send_keys(tel)
#
#     def setPassword(self, pwd):
#         self.wait.until(EC.presence_of_element_located((By.NAME, self.txt_password_name))).send_keys(pwd)
#
#     def setConfirmPassword(self, pwd):
#         self.wait.until(EC.presence_of_element_located((By.NAME, self.txt_confirm_password_name))).send_keys(pwd)
#
#     # def setPrivacyPolicy(self):
#     #     self.wait.until(EC.element_to_be_clickable((By.NAME, self.chk_policy_name))).click()
#
#     # def setPrivacyPolicy(self):
#     #     checkbox = self.wait.until(
#     #         EC.presence_of_element_located((By.NAME, self.chk_policy_name))
#     #     )
#     #     self.driver.execute_script("arguments[0].click();", checkbox)
#     def setPrivacyPolicy(self):
#         checkbox = self.wait.until(
#             EC.presence_of_element_located((By.NAME, self.chk_policy_name))
#         )
#
#         # scroll into view (important for Firefox)
#         self.driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)
#
#         # click using JS (stable across browsers)
#         self.driver.execute_script("arguments[0].click();", checkbox)
#
#     def clickContinue(self):
#         self.wait.until(EC.element_to_be_clickable((By.XPATH, self.btn_continue_xpath))).click()
#
#     # ✅ FINAL FIXED METHOD
#     # def get_confirmation_msg(self):
#     #     try:
#     #         element = self.wait.until(
#     #             EC.visibility_of_element_located((By.XPATH, self.txt_confirmation_xpath))
#     #         )
#     #         return element.text.strip()
#     #     except Exception as e:
#     #         print("ERROR fetching confirmation message:", e)
#     #         return None
#
#     def get_confirmation_msg(self):
#         try:
#             # ✅ HANDLE ALERT FIRST (important for Firefox)
#             try:
#                 alert = self.driver.switch_to.alert
#                 print("ALERT FOUND:", alert.text)
#                 alert.accept()
#             except:
#                 pass  # no alert
#
#             # ✅ Now wait for confirmation message
#             element = self.wait.until(
#                 EC.visibility_of_element_located((By.XPATH, self.txt_confirmation_xpath))
#             )
#             return element.text.strip()
#
#         except Exception as e:
#             print("ERROR fetching confirmation message:", e)
#             return None


# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# class AccountRegistrationPage:
#
#     txt_firstname_name = "firstname"
#     txt_lastname_name = "lastname"
#     txt_email_name = "email"
#     txt_telephone_name = "telephone"
#     txt_password_name = "password"
#     txt_confirm_password_name = "confirm"
#     chk_policy_name = "agree"
#     btn_continue_xpath = "//input[@value='Continue']"
#     txt_confirmation_xpath = "//h1[text()='Your Account Has Been Created!']"
#
#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, 10)
#
#     def setFirstName(self, fname):
#         self.driver.find_element(By.NAME, self.txt_firstname_name).send_keys(fname)
#
#     def setLastName(self, lname):
#         self.driver.find_element(By.NAME, self.txt_lastname_name).send_keys(lname)
#
#     def setEmail(self, email):
#         self.driver.find_element(By.NAME, self.txt_email_name).send_keys(email)
#
#     def setTelephone(self, tel):
#         self.driver.find_element(By.NAME, self.txt_telephone_name).send_keys(tel)
#
#     def setPassword(self, pwd):
#         self.driver.find_element(By.NAME, self.txt_password_name).send_keys(pwd)
#
#     def setConfirmPassword(self, pwd):
#         self.driver.find_element(By.NAME, self.txt_confirm_password_name).send_keys(pwd)
#
#     def setPrivacyPolicy(self):
#         self.driver.find_element(By.NAME, self.chk_policy_name).click()
#
#     def clickContinue(self):
#         self.driver.find_element(By.XPATH, self.btn_continue_xpath).click()
#
#     # def getconfirmationmsg(self):
#     #     try:
#     #         return self.wait.until(
#     #             EC.visibility_of_element_located((By.XPATH, self.txt_confirmation_xpath))
#     #         ).text
#     #     except:
#     #         return None
#     def get_confirmation_msg(self):
#         try:
#             element = self.wait.until(
#                 EC.visibility_of_element_located((By.XPATH, self.txt_confirmation_xpath))
#             )
#             return element.text.strip()
#         except:
#             return None



# from selenium.webdriver.common.by import By
#
#
# class AccountRegistrationPage():
#     txt_firstname_name = "firstname"
#     txt_lastname_name = "lastname"
#     txt_email_name = "email"
#     txt_telphone_name = "telephone"
#     txt_password_name = "password"
#     txt_confpassword_name = "confirm"
#     chk_policy_name = "agree"
#     btn_cont_xpath="//input[@value='Continue']"
#     text_msg_conf_xpath="//h1[normalize-space()='Your Account Has Been Created!']"
#
#     def __init__(self, driver):
#         self.driver = driver
#
#     def setFirstName(self,fname):
#       self.driver.find_element(By.NAME,self.txt_firstname_name).send_keys(fname)
#
#     def setLastName(self,lname):
#         self.driver.find_element(By.NAME,self.txt_lastname_name).send_keys(lname)
#
#     def setEmail(self,email):
#         self.driver.find_element(By.NAME,self.txt_email_name).send_keys(email)
#
#     def setTelephone(self,tel):
#        self.driver.find_element(By.NAME,self.txt_telphone_name).send_keys(tel)
#
#     def setPassword(self,pwd):
#         self.driver.find_element(By.NAME,self.txt_password_name).send_keys(pwd)
#
#     def setConfirmPassword(self,cnfpwd):
#         self.driver.find_element(By.NAME,self.txt_confpassword_name).send_keys(cnfpwd)
#
#     def setPrivacyPolicy(self):
#         self.driver.find_element(By.NAME,self.chk_policy_name).click()
#
#     def clickContinue(self):
#         self.driver.find_element(By.XPATH,self.btn_cont_xpath).click()
#
#     def getconfirmationmsg(self):
#         try:
#             return  self.driver.find_element(By.XPATH,self.text_msg_conf_xpath).text
#         except:
#             None