#browser invoke
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://rahulshettyacademy.com/")
driver.maximize_window()

# https://rahulshettyacademy.com/angularpractice/


print(driver.title)
print(driver.current_url)

driver.get("https://rahulshettyacademy.com/lifetime-access")
driver.back()
driver.forward()
driver.refresh()
# driver.close()