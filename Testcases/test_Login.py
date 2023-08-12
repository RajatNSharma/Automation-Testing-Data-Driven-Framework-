import time
import pytest
from PageObjects.LoginPage import Login
from Utilities import XLutils
from Utilities.Logger import LogGen
from Utilities.ReadConfigfile import ReadValue


class Test_Login:
    Url = ReadValue.getUrl()
    log = LogGen.loggen()
    path = "D:\\E\\IT\\Orangehrm Project DDT Framework\\TestData\\LoginData1.xlsx"

    def test_login001(self, setup):
        self.log.info("Opening Browser")
        self.driver = setup
        self.driver.get(self.Url)
        self.log.info("Going to Url")
        self.lp = Login(self.driver)
        self.rows = XLutils.getrowCount(self.path, 'Sheet1')
        print("Number of rows are --->", self.rows)
        login_stuats = []
        for r in range(2, self.rows + 1):
            self.username = XLutils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLutils.readData(self.path, 'Sheet1', r, 2)
            self.Exp_Stauts = XLutils.readData(self.path, 'Sheet1', r, 3)

            self.lp.Enter_Username(self.username)
            self.log.info("Enter UserName-->" + self.username)
            self.lp.Enter_Password(self.password)
            self.log.info("Enter Password-->" + self.password)
            self.lp.Click_Login()
            self.log.info("Click on login button")
            login_stauts = []
            if self.lp.login_status() == True:
                if self.Exp_Stauts == "Pass":
                    login_stauts.append("Pass")
                    self.driver.save_screenshot("D:\\E\\IT\\Orangehrm Project DDT Framework\\Screenshots\\test_login_001_pass.png")
                    self.lp.Click_Menu_Button()
                    self.log.info("Click on menu button")
                    self.lp.Click_logout_Button()
                    self.log.info("Click on logout button")
                    XLutils.writeData(self.path, 'Sheet1', r, 4, "Pass")
                elif self.Exp_Stauts == "Fail":
                    login_stauts.append("Fail")
                    self.driver.save_screenshot("D:\\E\\IT\\Orangehrm Project DDT Framework\\Screenshots\\test_login_001_fail.png")
                    self.lp.Click_Menu_Button()
                    self.log.info("Click on menu button")
                    self.lp.Click_logout_Button()
                    self.log.info("Click on logout button")
                    XLutils.writeData(self.path, 'Sheet1', r, 4, "Fail")

                # assert True
            else:
                if self.Exp_Stauts == "Fail":
                    login_stauts.append("Pass")
                    self.driver.save_screenshot("D:\\E\\IT\\Orangehrm Project DDT Framework\\Screenshots\\test_login_001_fail.png")
                    XLutils.writeData(self.path, 'Sheet1', r, 4, "Fail")
                elif self.Exp_Stauts == "Pass":
                    login_stauts.append("Fail")
                    self.driver.save_screenshot("D:\\E\\IT\\Orangehrm Project DDT Framework\\Screenshots\\test_login_001_fail.png")
                    XLutils.writeData(self.path, 'Sheet1', r, 4, "Fail")
            print(login_stauts)

        self.driver.close()

