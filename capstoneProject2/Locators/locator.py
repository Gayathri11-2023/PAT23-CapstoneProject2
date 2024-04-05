from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



class WebLocators:

    usernameLocator = "username"
    passwordLocator = "password"
    buttonLocator = "//button[@type='submit']"
    emp_fn_Locator = "//input[@name='firstName']"
    emp_ln_locator = "//input[@name='lastName']"
    emp_id_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input'
    pimLocator = "PIM"
    addLocator = "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']"
    saveLocator = "//button[@type='submit']"
    emplistLocator = "Employee List"
    editLocator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[10]/div/div[9]/div/button[2]'
    deleteLocator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[18]/div/div[9]/div/button[1]'
    yesbuttonLocator = '//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]'
    forgotLocator = "//p[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']"
    username_Locator = "//input[@class='oxd-input oxd-input--active']"
    reset_Locator = "//button[@type='submit']"
    adminLocator = "//a[@class='oxd-main-menu-item active']"
    employeefirstnamelocator ="//input[@name='firstName']"
    employeelastnamelocator ="//input[@name='lastName']"
    empidlocator ='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[1]/div/div[2]/input'
    savebuttonLocator = "//button[@type='submit']"
    def entertext(self, driver, locator, textvalue):
        driver.find_element(by=By.NAME, value=locator).send_keys(textvalue)

    def clickbutton(self, driver, locator):
        driver.find_element(by=By.XPATH, value=locator).click()
    def link_text(self, driver, locator):
        driver.find_element(by=By.LINK_TEXT, value=locator).click()


    def x_path(self, driver, locator, textvalue):
         driver.find_element(by=By.XPATH, value=locator).send_keys(textvalue)
