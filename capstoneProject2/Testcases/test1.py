"""
Forgot Password link validation on login page
"""
from Data import data
from Locators import locator
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
# Explicit wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


# Defining a test class
class Test:
    dashboard = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

    # pytest fixture for setting up the test environment
    @pytest.fixture
    def boot(self):
        # Setting up Chrome WebDriver with the WebDriver Manager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        yield
        # implementation of explicit wait
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.quit()

    @pytest.mark.html
    def test_login(self, boot):
        try:
           # Opening the specified URL in the browser
            self.driver.get(data.WebData().url)
           # Maximizing the browser window
            self.driver.maximize_window()
            self.wait.until( EC.url_to_be(data.WebData().url) )
            self.wait.until( EC.presence_of_element_located(locator.WebLocators().entertext(self.driver, locator.WebLocators().usernameLocator, data.WebData().username)))
            self.wait.until( EC.presence_of_element_located(locator.WebLocators().clickbutton(self.driver, locator.WebLocators().forgotLocator)))
            self.wait.until( EC.presence_of_element_located(locator.WebLocators().x_path(self.driver, locator.WebLocators().username_Locator, data.WebData().username)))
            self.wait.until( EC.presence_of_element_located(locator.WebLocators().clickbutton(self.driver, locator.WebLocators().reset_Locator)))
            print("successful : A reset password link has been sent to you via email.")
         except NoSuchElementException as e:
             print("error")
