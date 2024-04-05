"""
Main menu validation on Admin page
"""
from Data import data
from Locators import locator
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pytest
from time import sleep


# Defining a test class


class Test:
    dashboard = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

    # pytest fixture for setting up the test environment

    @pytest.fixture
    def boot(self, loginpage_title="OrangeHRM"):
        self.loginpage_title = loginpage_title
        # Setting up Chrome WebDriver with the WebDriver Manager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        yield
        self.driver.quit()

    @pytest.mark.html
    def test_login(self, boot):
        # Opening the specified URL in the browser
        self.driver.get(data.WebData().url)
        # Maximizing the browser window
        self.driver.maximize_window()
        # Introducing a sleep delay for 7 seconds
        sleep(7)
        locator.WebLocators().entertext(self.driver, locator.WebLocators().usernameLocator, data.WebData().username)
        locator.WebLocators().entertext(self.driver, locator.WebLocators().passwordLocator,
                                        data.WebData().password)
        locator.WebLocators().clickbutton(self.driver, locator.WebLocators().buttonLocator)
        sleep(2)
        assert (self.driver.current_url == self.dashboard)
        print("Successfully logged into the webpage of OrangeHRM")
        locator.WebLocators().clickbutton(self.driver, locator.WebLocators().adminLocator)
        sleep(3)

        # Validate Menu options on the admin page
        menu_options = ["Admin", "PIM", "Leave", "Time", "Recruitment",
                        "My Info", "Performance", "Dashboard", "Directory", "Maintenance", "Buzz"]
        for option in menu_options:
            try:
                self.driver.find_element_by_link_text(option)
                print(f"{option} option is displayed.")
            except:
                print(f"{option} option is not displayed.")
