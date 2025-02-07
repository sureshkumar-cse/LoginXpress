from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import yaml
import time

###########################################################

def load_credentials(file_path):
    with open(file_path, 'r') as file:
        credentials = yaml.safe_load(file)
    return credentials

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

# Initialize Chrome WebDriver (Optimized for Mac M2 Pro)
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # Open browser in full screen
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-notifications")  # Block popups/alerts
options.add_argument("--no-sandbox")  # M2 Optimization
options.add_argument("--disable-dev-shm-usage")  # Fix crashes on macOS

# Initialize the browser
browser = webdriver.Chrome(service=service, options=options)

# Open the website
browser.get(website_link)

# Wait for the input fields to be present and interact safely
WebDriverWait(browser, 6).until(EC.presence_of_element_located((By.NAME, ele_username))).send_keys(username)
WebDriverWait(browser, 6).until(EC.presence_of_element_located((By.NAME, ele_password))).send_keys(password)
WebDriverWait(browser, 6).until(EC.presence_of_element_located((By.ID, ele_rememberMe))).click()

# Wait for the submit button to be clickable and click it
WebDriverWait(browser, 6).until(EC.element_to_be_clickable((By.ID, ele_submit))).click()

# Add any additional steps after login if necessary

# Close the browser after a delay
time.sleep(6)
browser.quit()