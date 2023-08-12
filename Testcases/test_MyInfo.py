import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.LoginPage import Login
from PageObjects.MyInfo import MyInfo
from Utilities.Logger import LogGen
from Utilities.ReadConfigfile import ReadValue
import pytest

class Test_000_MyInfo_Pages():
    Url = ReadValue.getUrl()
    log = LogGen.loggen()
    username = ReadValue.getusername()
    password = ReadValue.getpassword()

    #Function to check Every Category Page using an existing element
    def checkifPageWorks(self,categoryname):
        ele = By.XPATH,"//span[normalize-space()='My Info']"
        WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(ele))
        if self.driver.find_element(By.XPATH,"//span[normalize-space()='My Info']").is_displayed() != True:
            self.log.error("***MyInfo Test Failed ***")
            self.log.error("*** {0} Category Failed to load ***").format(categoryname)
            self.driver.save_screenshot("D:\\E\\IT\\Orangehrm Project DDT Framework\\Screenshots\\test_MyInfo.png")
            assert False

    #@pytest.mark.sanity
    def test_MyInfo(self,setup):
        self.log.info("Test_000_MyInfo_Page_Categories")
        self.log.info("Opening Browser")
        self.driver = setup
        self.driver.get(self.Url)
        self.log.info("Going to Url")
        self.lp = Login(self.driver)
        self.lp.Enter_Username(self.username)
        self.lp.Enter_Password(self.password)
        self.lp.Click_Login()
        self.log.info("***Successfully Logged***")
        self.myinfo = MyInfo(self.driver)

        #verifying pages
        self.myinfo.ClickOnMyInfo()
        self.checkifPageWorks("My Info")
        self.log.info("***Verified MyInfo***")

        self.myinfo.ClickOnPhotoChange()
        self.checkifPageWorks("Profile Picture")
        self.log.info("***Verified Profile Picture***")

        self.myinfo.ClickOnContactDetails()
        self.checkifPageWorks("Contact Details")
        self.log.info("***Verified Contact Details***")

        self.myinfo.ClickOnEmergencyDetails()
        self.checkifPageWorks("Emergency Details")
        self.log.info("***Verified Emergency Details***")

        self.myinfo.ClickOnDependents()
        self.checkifPageWorks("Dependents")
        self.log.info("***Verified Dependents***")

        self.myinfo.ClickOnImmigration()
        self.checkifPageWorks("Immigrations")
        self.log.info("***Verified Immigrations***")

        self.myinfo.ClickOnJob()
        self.checkifPageWorks("Job")
        self.log.info("***Verified Job***")

        self.myinfo.ClickOnSalary()
        self.checkifPageWorks("Salary")
        self.log.info("***Verified Salary***")

        self.myinfo.ClickOnTaxExemption()
        self.checkifPageWorks("Tax Exemptions")
        self.log.info("***Verified Tax Exemptions***")

        self.myinfo.ClickOnReportTo()
        self.checkifPageWorks("Report To")
        self.log.info("***Verified Report To***")

        self.myinfo.ClickOnQualifications()
        self.checkifPageWorks("Qualifications")
        self.log.info("***Verified Qualifications***")

        self.myinfo.ClickOnMembership()
        self.checkifPageWorks("Memberships")
        self.log.info("***Verified Memberships***")


        self.driver.close()
        self.log.info("***MyInfo Test Passed***")
        self.log.info("***All Categories Successfully Loaded***")
        self.log.info("***Ending MyInfo Test***")
        assert True

