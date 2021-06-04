import pytest
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime

driver = webdriver.Chrome()
driver.get("https://www.allmovie.com")
driver.implicitly_wait(1)
dt = str(datetime.now())
driver.get_screenshot_as_file("before_login"+dt+".png")
login = WebDriverWait(driver,2).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".open-login-modal")))
#driver.find_element_by_css_selector(".open-login-modal")
login.click()
driver.implicitly_wait(1)
iframe = WebDriverWait(driver,2).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body > div.login-modal > iframe")))
driver.switch_to.frame(iframe)
dt = str(datetime.now())
driver.get_screenshot_as_file("after_login"+dt+".png")
driver.implicitly_wait(1)

username = WebDriverWait(driver,4).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body > form > fieldset > p:nth-child(1) > input[type='email']")))
#driver.find_element_by_css_selector("[name=email]")
password =  WebDriverWait(driver,4).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body > form > fieldset > p:nth-child(2) > input[type='password']")))
#driver.find_element_by_css_selector("[name=password]")
username.send_keys("<enterusername>")
password.send_keys("<enterpassword>")
dt = str(datetime.now())
driver.get_screenshot_as_file("after_creds"+dt+".png")
