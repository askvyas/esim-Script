# Automating Login task using python and Selenium
from selenium import webdriver
import yaml
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


conf = yaml.load(open('loginDetails.yml'))
myNick = conf['user']['email']
myPassword = conf['user']['password']

driver = webdriver.Chrome(executable_path='/Users/askvyas/Desktop/esim-Script/chromedriver')
driver.get("https://secura.e-sim.org/")
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "// div[@id='sectionContainer']//div[@id='login_section_btn']"))
).click()

def login(url, usernameId, username, passwordId, password, submit_buttonId):

    driver.find_element_by_id(usernameId).send_keys(username)
    driver.find_element_by_name(passwordId).click()
    driver.find_element_by_name(passwordId).send_keys(password)
    driver.find_element_by_id(submit_buttonId).click()



login("https://www.secura.e-sim.org", "registeredPlayerLogin", myNick, "password", myPassword, "Submit")

