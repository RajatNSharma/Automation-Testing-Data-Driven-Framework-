from selenium.common import ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class MyInfo():
    linkMyInfo_Xpath = (By.XPATH,"//span[normalize-space()='My Info']")
    linkPhotoChange_Xpath  = (By.XPATH,"//div[@class='orangehrm-edit-employee-image']//img[@alt='profile picture']")
    linkContactDetails_Xpath = (By.XPATH,"//a[normalize-space() = 'Contact Details']")
    linkEmergencyDetails_Xpath = (By.XPATH,"//a[normalize-space() = 'Emergency Contacts']")
    linkDependents_Xpath = (By.XPATH,"//a[normalize-space() = 'Dependents']")
    linkImmigration_Xpath = (By.XPATH,"//a[normalize-space() = 'Immigration']")
    linkJob_Xpath = (By.XPATH,"//a[normalize-space() = 'Job']")
    linkSalary_Xpath = (By.XPATH,"//a[normalize-space() = 'Salary']")
    linkTaxExemption_Xpath = (By.XPATH, "//a[normalize-space() = 'Tax Exemptions']")
    linkReport_to_Xpath = (By.XPATH, "//a[normalize-space() = 'Report-to']")
    linkQualifications_Xpath = (By.XPATH, "//a[normalize-space() = 'Qualifications']")
    linkMemberships_Xpath = (By.XPATH, "//a[normalize-space() = 'Memberships']")

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    def ClickOnMyInfo(self):
        self.wait.until(expected_conditions.presence_of_element_located(self.linkMyInfo_Xpath)).click()

    def ClickOnPhotoChange(self):
        try:
            self.wait.until(expected_conditions.presence_of_element_located(self.linkPhotoChange_Xpath)).click()

        except:
            ElementNotInteractableException

    def ClickOnContactDetails(self):
        self.wait.until(expected_conditions.presence_of_element_located(self.linkContactDetails_Xpath)).click()

    def ClickOnEmergencyDetails(self):
        self.wait.until(expected_conditions.presence_of_element_located(self.linkEmergencyDetails_Xpath)).click()

    def ClickOnDependents(self):
        self.wait.until(expected_conditions.presence_of_element_located(self.linkDependents_Xpath)).click()
        
    def ClickOnImmigration(self):
        self.wait.until(expected_conditions.presence_of_element_located(self.linkImmigration_Xpath)).click()

    def ClickOnJob(self):
        self.wait.until(expected_conditions.presence_of_element_located(self.linkJob_Xpath)).click()

    def ClickOnSalary(self):
        self.wait.until(expected_conditions.presence_of_element_located(self.linkSalary_Xpath)).click()

    def ClickOnTaxExemption(self):
        self.wait.until(expected_conditions.presence_of_element_located(self.linkTaxExemption_Xpath)).click()

    def ClickOnReportTo(self):
        self.wait.until(expected_conditions.presence_of_element_located(self.linkReport_to_Xpath)).click()

    def ClickOnQualifications(self):
        self.wait.until(expected_conditions.presence_of_element_located(self.linkQualifications_Xpath)).click()

    def ClickOnMembership(self):
        self.wait.until(expected_conditions.presence_of_element_located(self.linkMemberships_Xpath)).click()


