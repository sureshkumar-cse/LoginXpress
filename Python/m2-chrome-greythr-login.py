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
ele_username = "username"
ele_password = "password"
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
WebDriverWait(browser, 6).until(EC.presence_of_element_located((By.ID, ele_username))).send_keys(username)
WebDriverWait(browser, 6).until(EC.presence_of_element_located((By.ID, ele_password))).send_keys(password)

# Check for Login in button
btn1 = WebDriverWait(browser, 6).until(EC.presence_of_element_located((By.TAG_NAME, "button")))

# Check if the button has type="submit" and contains "Log in" text
if btn1.get_attribute("type") == "submit" and "Log in" in btn1.text:
    WebDriverWait(browser, 6).until(EC.element_to_be_clickable(btn1)).click()

# Wait to load the dashboard
time.sleep(6)

# Check for Sign Out button
btn2 = WebDriverWait(browser, 6).until(EC.element_to_be_clickable((By.TAG_NAME, "gt-button")))
if btn2.get_attribute("class") == "hydrated":
    WebDriverWait(browser, 6).until(EC.element_to_be_clickable(btn2)).click()

# Wait for a Dropdown button element to appear
dropdown = WebDriverWait(browser, 6).until(EC.element_to_be_clickable((By.TAG_NAME, "gt-dropdown")))
if dropdown.get_attribute("class") == "hydrated":
    WebDriverWait(browser, 6).until(EC.element_to_be_clickable(dropdown)).click()

dropdown_item = WebDriverWait(browser, 6).until(EC.presence_of_element_located((By.CLASS_NAME, "item-label")))
if "Work from Home" in dropdown_item.text:
    WebDriverWait(browser, 6).until(EC.element_to_be_clickable(dropdown_item)).click()

# Check for Sign Out button
#btn2 = WebDriverWait(browser, 6).until(EC.element_to_be_clickable((By.TAG_NAME, "gt-button")))
#if btn2.get_attribute("class") == "hydrated":
#    WebDriverWait(browser, 6).until(EC.element_to_be_clickable(btn2)).click()

# Close the browser after a delay
#time.sleep(21)
browser.quit()