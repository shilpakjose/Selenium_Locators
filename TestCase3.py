#client page forget password :extendeted locators

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver= webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://rahulshettyacademy.com/client")
driver.find_element(By.LINK_TEXT,"Forgot password?").click()
driver.find_element(By.XPATH,"//form/div[1]/input").send_keys("demo@gmail.com")
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(2) input").send_keys("ABC123")
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(3) input").send_keys("ABC123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()

