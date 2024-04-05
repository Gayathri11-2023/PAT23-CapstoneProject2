"""
Forgot Password link validation on login page
"""
from Data import data
from Locators import locator
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pytest
from time import sleep


# Defining a test class
class Test_case1:
    dashboard = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

    # pytest fixture for setting up the test environment
    @pytest.fixture
    def boot(self):
        # Setting up Chrome WebDriver with the WebDriver Manager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        yield
        self.driver.quit()

    @pytest.mark.html
    def test_forgotpassword_link(self, boot):
        # Opening the specified URL in the browser
        self.driver.get(data.WebData().url)
        # Maximizing the browser window
        self.driver.maximize_window()
        # Introducing a sleep delay for 7 seconds
        sleep(7)
        locator.WebLocators().entertext(self.driver, locator.WebLocators().usernameLocator, data.WebData().username)
        sleep(2)
        locator.WebLocators().clickbutton(self.driver, locator.WebLocators().forgotLocator)
        sleep(2)
        locator.WebLocators().x_path(self.driver, locator.WebLocators().username_Locator, data.WebData().username)
        sleep(2)
        locator.WebLocators().clickbutton(self.driver, locator.WebLocators().reset_Locator)
        sleep(5)
        print("successful : A reset password link has been sent to you via email.")

