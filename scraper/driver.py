# scraper/driver.py

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def setup_driver(headless=True):
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-notifications")
    return webdriver.Chrome(options=chrome_options)
