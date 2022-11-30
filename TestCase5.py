#UI editor or dynamic checkbox
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver= webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#checkbox dynamic

checkboxes= driver.find_elements(By.XPATH,"//input[@type ='checkbox']")
print(len(checkboxes))

# for checkbox in checkboxes:
#     if checkbox.text == "option2":
#         checkbox.click()
#         time.sleep(3)
#         break

for checkbox in checkboxes:
    if checkbox.get_attribute("value")=="option2":
        checkbox.click()
        checkbox.is_selected()
        time.sleep(1)
        break
# driver.find_elements(By.ID,"checkBoxOption2").click()

#print(driver.find_element(By.CSS_SELECTOR,"input[type ='checkbox']")).get_attribute("value")


