import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
WebDriverWait(driver,10).until(expected_conditions.presence_of_element_located((By.NAME,"username")))
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type ='submit']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//p[@class='oxd-userdropdown-name']").click()
driver.find_element(By.XPATH,"//a[normalize-space()='Logout']").click()
time.sleep(5)
driver.close()

