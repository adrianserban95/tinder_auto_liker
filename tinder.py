from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

# Create the web driver
driver = webdriver.Chrome(executable_path="/UPDATE_THIS/")

# Access tinder
driver.get("https://tinder.com/")
body = driver.find_element_by_tag_name('body')

# Ask user if he or she logged in
while True:
    logged = input("Did you login? y/n \n")

    if logged == "y":
        break

# Start liking
try:
    for i in range(99):
        # Open profile
        body.send_keys(Keys.ARROW_UP)
        time.sleep(2)

        # Next three photos
        for j in range(random.randint(0, 4)):
            body.send_keys(Keys.SPACE)
            time.sleep(2)

        # Swipe right
        body.send_keys(Keys.ARROW_RIGHT)
        time.sleep(1)
except:
    print(f"Some error occured.")

# Close web browser
driver.close()