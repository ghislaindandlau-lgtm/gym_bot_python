import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from datetime import datetime, timedelta

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
email = "ghislain.dandlau@gmail.com"
password = "ghislain.dandlau@gmail.com"

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

# find correct courses
#dropdown = driver.find_element(By.ID, "type-filter")
#drop = Select(dropdown)
#class_wanted = "Spin"
#drop.select_by_visible_text(class_wanted)

# find the next tuesday
today_date = datetime.now()
weekday_idx = 1

days_delta = weekday_idx - today_date.weekday()
if days_delta <= 0:
    days_delta += 7

res = today_date + timedelta(days_delta)

#find one course for tuesday -- option 1

#next_course_button = driver.find_element(By.ID, f"book-button-{class_wanted.lower()}-{res.date()}-1800")
#print(next_course_button.is_displayed())
#next_course_button.click()

#find one course for tuesday -- option 2

#------ find tuesday in elements

days = driver.find_elements(By.CLASS_NAME, "Schedule_dayTitle__YBybs")
next_date = days[0]
print(next_date.text)


for item in days:
    if "Tue" in item.text:

        next_date = item

print(next_date.text)
#------ courses

list_of_items = driver.find_elements(By.CLASS_NAME, "Schedule_dayGroup__y79__")

for item in list_of_items:
    if item.find_element(By.CLASS_NAME, "Schedule_dayTitle__YBybs").text == next_date.text:

        classes_on_tuesday = item.find_elements(By.CLASS_NAME, "ClassCard_card__KpCx5")

        for class_t in classes_on_tuesday:
            tuesday_class = class_t.find_element(By.CLASS_NAME, "ClassCard_cardHeader__D9pf3").find_element(By.CLASS_NAME, "ClassCard_cardContent__WGvPp").find_element(By.CLASS_NAME, "ClassCard_classDetail__Z8Z8f")  #
            print(tuesday_class.text)
            if tuesday_class.text == "Time: 6:00 PM":
                elem = class_t.find_element(By.CLASS_NAME, "ClassCard_cardHeader__D9pf3").find_element(By.CLASS_NAME, "ClassCard_cardActions__tVZBm")
                print("yeah")

                if elem.text == "Book Class":
                    elem.click()
                    print(f"✓ Class booked for: Yoga Class on Tue, Aug 12")
                elif elem.text == "Join Waitlist":
                    elem.click()
                    print("✓ Joined waitlist for: Yoga Class on Tue, Aug 12")
                elif elem.text == "Booked":
                    print("✓ Already booked: Spin Class on Tue, Aug 12")
                elif elem.text == "Waitlisted":
                    print("✓ Already on waitlist: HIIT Class on Tue, Aug 12")




