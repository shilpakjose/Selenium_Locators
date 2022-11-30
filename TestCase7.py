#ALLERT HANDLING
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
name ="shilpa"
driver= webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,"#name").send_keys(name)
driver.find_element(By.ID,"alertbtn").click()
a=driver.switch_to.alert
alerttext=a.text
print(alerttext)
a.accept()
time.sleep(3)
assert name in alerttext

