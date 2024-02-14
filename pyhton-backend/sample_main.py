from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import time

# Launch Chrome browser (you'll need to have chromedriver installed and in your PATH)
driver = webdriver.Chrome()

# Navigate to the page with the form
driver.get("http://localhost:3000/test-form-01")

# Wait for the page to load
time.sleep(2)  # You may need to adjust the wait time depending on the page load speed

try:
    # Find the form elements and fill them out
    name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "name"))
    )
    name.send_keys("John BOT")

    email = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "email"))
    )
    email.send_keys("john@email.com")

    message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "message"))
    )
    message.send_keys("john@email.com")

    # Submit the form
    submit_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "submit_button"))
    )
    submit_button.click()

    # Wait for a few seconds to see the result
    time.sleep(10)

except:
    driver.quit()
    print("Error")
