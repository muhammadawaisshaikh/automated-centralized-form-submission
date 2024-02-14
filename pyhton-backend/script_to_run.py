from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import time

def process_data(data):
    print(data)

    # Launch Chrome browser (you'll need to have chromedriver installed and in your PATH)
    driver = webdriver.Chrome()

    # Navigate to the page with the form
    driver.get("http://localhost:3000/test-form-01")

    # Wait for the page to load
    time.sleep(2)

    try:
        # Find the form elements and fill them out
        name = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "firstName"))
        )
        name.send_keys(data.firstName)

        email = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "lastName"))
        )
        email.send_keys(data.lastName)

        street = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "street"))
        )
        street.send_keys(data.street)

        housenr = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "housenr"))
        )
        housenr.send_keys(data.housenr)

        zipcode = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "zipcode"))
        )
        zipcode.send_keys(data.zipcode)

        city = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "city"))
        )
        city.send_keys(data.city)

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