import pytest
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


# ================= Browser Setup ================= #

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser type")


@pytest.fixture()
def setup(request):
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--window-size=1920,1080")

        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=chrome_options
        )

    elif browser == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--headless")
        firefox_options.add_argument("--width=1920")
        firefox_options.add_argument("--height=1080")

        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=firefox_options
        )

    else:
        raise Exception("Browser not supported")

    driver.maximize_window()
    yield driver
    driver.quit()


# ================= HTML Report ================= #

def pytest_configure(config):
    report_dir = os.path.join(os.getcwd(), "reports")
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)

    # 🔥 FIX: static report name
    config.option.htmlpath = os.path.join(report_dir, "report.html")

    # 🔥 SAFE metadata handling (IMPORTANT)
    if hasattr(config, "_metadata"):
        config._metadata['Project Name'] = 'Opencart'
        config._metadata['Module Name'] = 'CustRegistration'
        config._metadata['Tester'] = 'Ahmad'


@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    if metadata:
        metadata.pop("JAVA_HOME", None)
        metadata.pop("Plugins", None)



# import pytest
# import os
# from datetime import datetime
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from selenium.webdriver.chrome.options import Options as ChromeOptions
# from selenium.webdriver.firefox.options import Options as FirefoxOptions
#
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
#
#
# # ================= Browser Setup ================= #
#
# def pytest_addoption(parser):
#     parser.addoption("--browser", action="store", default="chrome", help="browser type")
#
#
# @pytest.fixture()
# def setup(request):
#     browser = request.config.getoption("--browser")
#
#     if browser == "chrome":
#         chrome_options = ChromeOptions()
#         chrome_options.add_argument("--headless=new")
#         chrome_options.add_argument("--no-sandbox")
#         chrome_options.add_argument("--disable-dev-shm-usage")
#         chrome_options.add_argument("--window-size=1920,1080")
#
#         driver = webdriver.Chrome(
#             service=ChromeService(ChromeDriverManager().install()),
#             options=chrome_options
#         )
#
#     elif browser == "firefox":
#         firefox_options = FirefoxOptions()
#         firefox_options.add_argument("--headless")
#         firefox_options.add_argument("--width=1920")
#         firefox_options.add_argument("--height=1080")
#
#         driver = webdriver.Firefox(
#             service=FirefoxService(GeckoDriverManager().install()),
#             options=firefox_options
#         )
#
#     else:
#         raise Exception("Browser not supported")
#
#     driver.maximize_window()
#     yield driver
#     driver.quit()
#
#
# # ================= HTML Report ================= #
#
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'Opencart'
#     config._metadata['Module Name'] = 'CustRegistration'
#     config._metadata['Tester'] = 'Ahmad'
#
#     report_dir = os.path.join(os.getcwd(), "reports")
#     if not os.path.exists(report_dir):
#         os.makedirs(report_dir)
#
#     config.option.htmlpath = os.path.join(
#         report_dir,
#         datetime.now().strftime("%d-%m-%Y_%H-%M-%S") + ".html"
#     )
#
#
# @pytest.hookimpl(optionalhook=True)
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)


# import pytest
# import os
# from datetime import datetime
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.firefox.service import Service as FirefoxService
#
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
#
#
# # ================= Browser Setup ================= #
#
# def pytest_addoption(parser):
#     parser.addoption("--browser", action="store", default="chrome", help="browser type")
#
#
# @pytest.fixture()
# def setup(request):
#
#     browser = request.config.getoption("--browser")
#
#     if browser == "chrome":
#         driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#
#     elif browser == "firefox":
#         driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
#
#     else:
#         raise Exception("Browser not supported")
#
#     driver.maximize_window()
#
#     yield driver
#
#     driver.quit()
#
#
# # ================= HTML Report ================= #
#
# def pytest_configure(config):
#     # Add environment info
#     config._metadata['Project Name'] = 'Opencart'
#     config._metadata['Module Name'] = 'CustRegistration'
#     config._metadata['Tester'] = 'Ahmad'
#
#     # Create reports folder
#     report_dir = os.path.join(os.getcwd(), "reports")
#     if not os.path.exists(report_dir):
#         os.makedirs(report_dir)
#
#     # Set report path with timestamp
#     config.option.htmlpath = os.path.join(
#         report_dir,
#         datetime.now().strftime("%d-%m-%Y_%H-%M-%S") + ".html"
#     )
#
#
# @pytest.hookimpl(optionalhook=True)
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)

# import pytest
# import os
# from datetime import datetime
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.firefox.service import Service as FirefoxService
#
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
#
#
# # ================= Browser Setup ================= #
#
# def pytest_addoption(parser):
#     parser.addoption("--browser", action="store", default="chrome", help="browser type")
#
#
# @pytest.fixture()
# def setup(request):
#
#     browser = request.config.getoption("--browser")
#
#     if browser == "chrome":
#         driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#
#     elif browser == "firefox":
#         driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
#
#     else:
#         raise Exception("Browser not supported")
#
#     driver.maximize_window()
#
#     yield driver
#
#     driver.quit()
#
#
# # ================= HTML Report ================= #
#
# def pytest_configure(config):
#     # Add environment info
#     config._metadata['Project Name'] = 'Opencart'
#     config._metadata['Module Name'] = 'CustRegistration'
#     config._metadata['Tester'] = 'Ahmad'
#
#     # Create reports folder
#     report_dir = os.path.join(os.getcwd(), "reports")
#     if not os.path.exists(report_dir):
#         os.makedirs(report_dir)
#
#     # Set report path with timestamp
#     config.option.htmlpath = os.path.join(
#         report_dir,
#         datetime.now().strftime("%d-%m-%Y_%H-%M-%S") + ".html"
#     )
#
#
# @pytest.hookimpl(optionalhook=True)
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)

# import pytest
# from selenium import webdriver
# import os
# from datetime import datetime
# import pytest
#
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.firefox.service import Service as FirefoxService
#
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
#
#
# # ✅ Parametrize browser automatically
# def pytest_generate_tests(metafunc):
#     if "browser" in metafunc.fixturenames:
#         metafunc.parametrize("browser", ["chrome", "firefox"])
#
#
# @pytest.fixture()
# def setup(browser):
#
#     if browser == "chrome":
#         driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#
#     elif browser == "firefox":
#         driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
#
#     else:
#         raise Exception("Browser not supported")
#
#     driver.maximize_window()
#
#     yield driver
#
#     driver.quit()
#
# ########### pytest HTML Report ################
#
# # ✅ Combine BOTH configure functions
# def pytest_configure(config):
#     # Add environment info
#     config._metadata['Project Name'] = 'Opencart'
#     config._metadata['Module Name'] = 'CustRegistration'
#     config._metadata['Tester'] = 'Ahmad'
#
#     # Create reports folder if not exists
#     report_dir = os.path.join(os.getcwd(), "reports")
#     if not os.path.exists(report_dir):
#         os.makedirs(report_dir)
#
#     # Set report path with timestamp
#     config.option.htmlpath = os.path.join(
#         report_dir,
#         datetime.now().strftime("%d-%m-%Y_%H-%M-%S") + ".html"
#     )
#
#
# # ✅ Modify environment info
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)
#

# import pytest
# from selenium import webdriver
#
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from selenium.webdriver.edge.service import Service as EdgeService
#
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
#
#
# # Add browser option
# def pytest_addoption(parser):
#     parser.addoption("--browser", action="store", default="chrome", help="browser type")
#
#
# @pytest.fixture()
# def setup(request):
#
#     browser = request.config.getoption("--browser")
#
#     if browser == "chrome":
#         driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#
#     elif browser == "firefox":
#         driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
#
#     elif browser == "edge":
#         driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
#
#     else:
#         raise Exception("Browser not supported!")
#
#     driver.maximize_window()
#
#     yield driver
#
#     driver.quit()

# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
#
#
# @pytest.fixture()
# def setup():
#
#     service = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service)
#
#     yield driver
#
#     driver.quit()


# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
#
#
# @pytest.fixture()
# def setup():
#
#     service = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service)
#
#     yield driver
#
#     driver.quit()