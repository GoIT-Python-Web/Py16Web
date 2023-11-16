from time import sleep

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service('chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_argument('--headless=chrome')


with webdriver.Chrome(service=service, options=options) as driver:
    driver.get("https://quotes.toscrape.com/login")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
    username = driver.find_element(by=By.ID, value="username")
    password = driver.find_element(by=By.ID, value="password")

    username.send_keys("admin")
    password.send_keys("admin")

    button = driver.find_element(by=By.XPATH, value="/html//input[@class='btn btn-primary']")
    button.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "footer")))
    html = driver.page_source  # -> Bs4
    links = driver.find_elements(by=By.TAG_NAME, value='a')
    [print(link.get_attribute('href')) for link in links]

    sleep(3)

# driver.quit()
