import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
waiter = WebDriverWait(driver,47)

driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
delay = driver.find_element(By.CSS_SELECTOR, "#delay")
delay.clear()
delay.send_keys("45")
driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[1]').click()
driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[4]').click()
driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[2]').click()
driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[15]').click()

waiter.until(
    EC.text_to_be_present_in_element((By.XPATH, '//*[@id="calculator"]/div[1]/div'), "15")
)

@pytest.mark.test_calculator
def test_sum(res_in, res):
    res_in = print(driver.find_element(By.XPATH, '//*[@id="calculator"]/div[1]/div').get_attribute("innerText"))
    res = print(15)
    assert res_in == res
driver.quit()