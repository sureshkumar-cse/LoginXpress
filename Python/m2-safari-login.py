from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import yaml
import time

###########################################################

def load_credentials(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

# Load credentials from YAML file
credentials = load_credentials('h-input.yaml')

###########################################################

# Website and Credentials
website_link = credentials["website_link"]
username = credentials["username"]
password = credentials["password"]

# Element Selectors
ele_username = "member[email]"
ele_password = "member[password]"
ele_rememberMe = "member_remember_me"
ele_submit = "form-button"

###########################################################

# Initialize Safari WebDriver (Optimized for Mac M2 Pro)
options = webdriver.safari.options.Options()
options.automatic_inspection = False
options.automatic_profiling = False

browser = webdriver.Safari(options=options)

# Open the website
browser.get(website_link)

# Wait for the input fields to be present and interact safely
WebDriverWait(browser, 6).until(EC.presence_of_element_located((By.NAME, ele_username))).send_keys(username)
WebDriverWait(browser, 6).until(EC.presence_of_element_located((By.NAME, ele_password))).send_keys(password)

# Click Remember Me checkbox (if it exists)
try:
    WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.ID, ele_rememberMe))).click()
except:
    print("Remember Me checkbox not found, continuing...")

# Wait for the submit button to be clickable and click it
WebDriverWait(browser, 6).until(EC.element_to_be_clickable((By.CLASS_NAME, ele_submit))).click()

# Add any additional steps after login if necessary

# Close the browser after a delay
time.sleep(6)
browser.quit()
