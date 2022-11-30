import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver= webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

radiobutton=driver.find_elements(By.XPATH,"//input[@type='radio']")
print(len(radiobutton))

for radio in radiobutton:
    if radio.get_attribute("value")=="radio2":
        radio.click()
        radio.is_selected()
        time.sleep(3)
        break

d=driver.find_element(By.ID,"displayed-text")
assert d.is_displayed()
driver.find_element(By.ID,"hide-textbox")
assert d.is_displayed()