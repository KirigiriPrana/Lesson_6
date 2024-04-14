import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

    
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

first_name = driver.find_element(By.CSS_SELECTOR, "input[name='first-name']").send_keys("Иван")
last_name = driver.find_element(By.CSS_SELECTOR, "input[name='last-name']").send_keys("Петров")
address = driver.find_element(By.CSS_SELECTOR, "input[name='address']").send_keys("Ленина, 55-3")
email = driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']").send_keys("test@skypro.com")
phone_number = driver.find_element(By.CSS_SELECTOR, "input[name='phone']").send_keys("+7985899998787")
zip_code = driver.find_element(By.CSS_SELECTOR, "input[name='zip-code']").send_keys("")
city = driver.find_element(By.CSS_SELECTOR, "input[name='city']").send_keys("Москва")
country = driver.find_element(By.CSS_SELECTOR, "input[name='country']").send_keys("Россия")
job_position = driver.find_element(By.CSS_SELECTOR, "input[name='job-position']").send_keys("QA")
company = driver.find_element(By.CSS_SELECTOR, "input[name='company']").send_keys("SkyPro")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

waiter = WebDriverWait(driver,60)
waiter.until(
    EC.element_attribute_to_include((By.CSS_SELECTOR, "#first-name"), "background-color=#d1e7dd;")
)

ids = ["'#first-name'", "'#last-name'", "'#address'", "'#e-mail'", "'#phone'", "'#zip-code'",  "'#city'", "'#country'", "'#job-position'", "'#company'"]
for id in range(ids[0,9]):
    assert print(driver.find_element(By.CSS_SELECTOR, id).get_attribute("name")) == "alert py-2 alert-success"


driver.quit()