#Dynamic dropdowns
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver= webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID,"autosuggest").send_keys('ind')
time.sleep(4)
countries= driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item']")

print(len(countries))

for country in countries:
    if country.text=="India":
        country.click()
        break

print(driver.find_element(By.CSS_SELECTOR,"li[class='ui-menu-item']").get_attribute("value"))