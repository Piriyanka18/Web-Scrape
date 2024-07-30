from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Install and get the path of the ChromeDriver
chrome_driver_path = ChromeDriverManager().install()

# Use the Service class to specify the path to the ChromeDriver
service = Service(chrome_driver_path)

# Initialize WebDriver with the service
driver = webdriver.Chrome(service=service)

# Open the website
driver.get("https://google.com")

WebDriverWait(driver,5).until(
  EC.presence_of_element_located((By.CLASS_NAME,"gLFyf"))
)


input_element =driver.find_element(By.CLASS_NAME,"gLFyf")
input_element.clear()
input_element.send_keys(" tech with tim" + Keys.ENTER)

link =driver.find_element(By.PARTIAL_LINK_TEXT,"Tech with Tim")
link.click()

time.sleep(10)

driver.quit()
