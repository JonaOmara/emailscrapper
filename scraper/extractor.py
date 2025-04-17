# scraper/extractor.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

def scrape_club_details(driver, club_element):
    club_name = club_element.text
    url = club_element.get_attribute("href")

    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(url)

    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//div[contains(@class,"profile-info")]')))
        email_element = driver.find_element(By.XPATH, '//div[contains(@class,"profile-info")]//li[2]')
        club_email = email_element.text
    except (NoSuchElementException, TimeoutException):
        club_email = "Not available"

    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    return {"Club name": club_name, "club_email": club_email}
