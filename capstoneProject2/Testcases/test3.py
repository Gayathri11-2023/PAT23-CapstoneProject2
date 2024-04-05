"""
Main menu validation on Admin page
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


class Test_case3:
    dashboard = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

    # pytest fixture for setting up the test environment

    @pytest.fixture
    def boot(self, loginpage_title="OrangeHRM"):
        self.loginpage_title = loginpage_title
        # Setting up Chrome WebDriver with the WebDriver Manager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        yield
       # implementation of explicit wait
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.quit()

    @pytest.mark.html
    def test_mainmenu_validation(self, boot):
        try:
           # Opening the specified URL in the browser
           self.driver.get(data.WebData().url)
           # Maximizing the browser window
           self.driver.maximize_window()
           self.wait.until( EC.url_to_be(self.url) )
           self.wait.until( EC.presence_of_element_located(locator.WebLocators().entertext(self.driver, locator.WebLocators().usernameLocator, data.WebData().username)))
           self.wait.until( EC.presence_of_element_located(locator.WebLocators().entertext(self.driver, locator.WebLocators().passwordLocator,
                                        data.WebData().password)))
           self.wait.until( EC.presence_of_element_located(locator.WebLocators().clickbutton(self.driver, locator.WebLocators().buttonLocator)))
           assert (self.driver.current_url == self.dashboard)
           print("Successfully logged into the webpage of OrangeHRM")
           self.wait.until( EC.presence_of_element_located(locator.WebLocators().clickbutton(self.driver, locator.WebLocators().adminLocator)))

           # Validate Menu options on the admin page
           menu_options = ["Admin", "PIM", "Leave", "Time", "Recruitment",
                        "My Info", "Performance", "Dashboard", "Directory", "Maintenance", "Buzz"]
           for option in menu_options:
              try:
                 self.driver.find_element_by_link_text(option)
                 print(f"{option} option is displayed.")
              except:
                print(f"{option} option is not displayed.")
        
        except NoSuchElementException as e:
              print("error")
