#fiiling the form
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)
driver.find_element(By.NAME,"name").send_keys("shilpa")
driver.find_element(By.NAME,"email").send_keys("shilpakjose90@gmail")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("abcd")
driver.find_element(By.ID,"exampleCheck1").click()
dropdown= Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_index(1)
driver.find_element(By.XPATH,"//input[@type='submit']").click()
m1= driver.find_element(By.CLASS_NAME,'alert-success').text
print(m1)
assert 'Success' in m1

driver.find_element(By.CSS_SELECTOR,"#inlineRadio2").click()
driver.find_element(By.CSS_SELECTOR,".ng-pristine").send_keys("hello")

driver.close()