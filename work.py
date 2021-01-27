from constants import *
from login import *


def work(url,work_buttonId):
    driver.find_element_by_id(work_buttonId)

login("https://www.secura.e-sim.org", "registeredPlayerLogin", myNick, "password", myPassword, "Submit")
work(WORK_URL,WORK_BTN)
