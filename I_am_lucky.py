from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com/")

wait = WebDriverWait(driver, 10)

# Click on "I'm Feeling Lucky" button
button_lucky = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[2]')))
button_lucky.click()

# Click on "Library" 
library_icon = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="glue-drawer-2465973"]/div/div[2]/nav/ul/li[1]/a')))
library_icon.click()

# Enter "Cricket" in the search box
search_box = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/div/div[1]/form/div[1]/input')))
search_box.clear()
search_box.send_keys("Cricket")
time.sleep(5)

# Click on the search icon
search_icon = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/div/div[1]/form/div[1]/div[2]/button[1]')))
search_icon.click()
time.sleep(10)
print('CLicked search icon')


# Click on the first cricket image
image_elem = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/div/div[3]/div/div[1]/div[2]/a/div/div[2]')))
image_elem.click()

# Wait for 5 seconds to observe the click action
time.sleep(10)

driver.quit()



