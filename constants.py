from selenium import webdriver
import yaml
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Constant URL's
LOGIN_URL="https://www.secura.e-sim.org"
WORK_URL="https://www.secura.e-sim.org/work.html"

# Constant HTML id's

SUBMIT_BTN="Submit"
WORK_BTN="workButton"

# reg button
REG_BTN="signIn3"