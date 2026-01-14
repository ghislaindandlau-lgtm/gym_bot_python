import os
from selenium import webdriver
from selenium.webdriver.common.by import By


# So window is always open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create profile -- this I am not 100% sure
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

# Open the tab
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://appbrewery.github.io/gym/")

#user details
email = "student@test.com"
password = "password123"

#login
login_button = driver.find_element(By.ID, "login-button")
login_button.click()

driver.implicitly_wait(2)

email_input = driver.find_element(By.ID, "email-input")
email_input.send_keys(email)

password_input = driver.find_element(By.ID, "password-input")
password_input.send_keys(password)

submit_button = driver.find_element(By.ID, "submit-button")
submit_button.click()

logged_in = driver.find_element(By.ID, "schedule-page").is_displayed()
print(logged_in)

