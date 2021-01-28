# Automating Login task using python and Selenium
from constants import *

conf = yaml.load(open('loginDetails.yml'))
myNick = conf['user1']['email']
myPassword = conf['user1']['password']
# Testura Chages added
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


login(LOGIN_URL, "registeredPlayerLogin", myNick, "password", myPassword,SUBMIT_BTN)
# defining signup function
def signup(url, usernameId, username, passwordId, password, submit_buttonId):
    driver.find_element_by_id(usernameId).send_keys(username)
    driver.find_element_by_name(passwordId).click()
    driver.find_element_by_name(passwordId).send_keys(password)
    driver.find_element_by_id(submit_buttonId).click()