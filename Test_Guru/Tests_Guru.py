from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.maximize_window()
driver.get("https://demo.guru99.com/insurance/v1/index.php")

driver.find_element(By.XPATH, "//a[@class='btn btn-default']").click()
Select(driver.find_element(By.ID, "user_title")).select_by_visible_text('Captain')

driver.find_element(By.XPATH, '//*[@name="firstname"]').send_keys("Sergio")
driver.find_element(By.XPATH, '//*[@name="lastname"]').send_keys("Nas")
driver.find_element(By.XPATH, '//*[@name="phone"]').send_keys("1234-3210")

Select(driver.find_element(By.ID, 'user_dateofbirth_1i')).select_by_visible_text('1983')
Select(driver.find_element(By.ID, 'user_dateofbirth_2i')).select_by_visible_text('March')
Select(driver.find_element(By.ID, 'user_dateofbirth_3i')).select_by_visible_text('3')

driver.find_element(By.XPATH, '//*[@value="Provisional"]').click()

Select(driver.find_element(By.ID, 'user_licenceperiod')).select_by_visible_text('9')
Select(driver.find_element(By.ID, 'user_occupation_id')).select_by_visible_text('Engineer')

driver.find_element(By.XPATH, '//*[@name="street"]').send_keys("R.abaddia, 100")
driver.find_element(By.XPATH, '//*[@name="city"]').send_keys("Parnaida")
driver.find_element(By.XPATH, '//*[@name="county"]').send_keys("Brasil")
driver.find_element(By.XPATH, '//*[@name="post_code"]').send_keys("58075-120")
driver.find_element(By.XPATH, '//*[@name="email"]').send_keys("asdasd@gmail.com")
driver.find_element(By.XPATH, '//*[@name="password"]').send_keys("1234")
driver.find_element(By.XPATH, '//*[@name="c_password"]').send_keys("1234")
driver.find_element(By.XPATH, '//*[@name="submit"]').click()

driver.find_element(By.ID, 'email').send_keys("asdasd@gmail.com")
driver.find_element(By.ID, 'password').send_keys("1234")
driver.find_element(By.XPATH, '//input[@name="submit"]').click()

assert driver.find_element(By.XPATH, '//h2[text() = "Broker Insurance WebPage"]').is_displayed()
