from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



class Login:
    Text_username_Name = (By.NAME, "username")
    Text_Password_Name = (By.NAME,"password")
    Click_Login_Xpath = (By.XPATH, "//button[@type ='submit']")
    Click_menu_Xpath = (By.XPATH,"//p[@class='oxd-userdropdown-name']")
    Click_Logout_XPath = (By.XPATH,"//a[normalize-space()='Logout']")

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)


    def Enter_Username(self,username):
        self.wait.until(expected_conditions.presence_of_element_located(self.Text_username_Name))
        self.driver.find_element(*Login.Text_username_Name).clear()
        self.driver.find_element(*Login.Text_username_Name).send_keys(username)

    def Enter_Password(self,password):
        self.wait.until(expected_conditions.presence_of_element_located(self.Text_Password_Name))
        self.driver.find_element(*Login.Text_Password_Name).clear()
        self.driver.find_element(*Login.Text_Password_Name).send_keys(password)

    def Click_Login(self):
        self.driver.find_element(*Login.Click_Login_Xpath).click()

    def login_status(self):
        try:
            self.wait.until(expected_conditions.presence_of_element_located(self.Click_menu_Xpath))
            self.driver.find_element(*Login.Click_menu_Xpath)
            return True
        except (NoSuchElementException, TimeoutException):
            return False

    def Click_Menu_Button(self):
        self.wait.until(expected_conditions.presence_of_element_located(self.Click_menu_Xpath))
        self.driver.find_element(*Login.Click_menu_Xpath).click()

    def Click_logout_Button(self):
        self.driver.find_element(*Login.Click_Logout_XPath).click()







