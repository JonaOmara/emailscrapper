# scraper/navigation.py

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_club_elements(driver):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//table[@id="tblClubs"]')))
    return driver.find_elements(By.XPATH, '//table[@id="tblClubs"]//a')

def go_to_next_page(driver):
    try:
        next_button = driver.find_element(By.ID, 'tblClubs_next')
        if "disabled" in next_button.get_attribute("class"):
            return False
        driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
        time.sleep(0.5)
        next_button.click()
        time.sleep(2)
        return True
    except Exception as e:
        print(f"⚠️ Error during next page click: {e}")
        return False
