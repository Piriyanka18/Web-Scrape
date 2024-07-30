from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

# Install and get the path of the ChromeDriver
chrome_driver_path = ChromeDriverManager().install()

# Use the Service class to specify the path to the ChromeDriver
service = Service(chrome_driver_path)

# Initialize WebDriver with the service
driver = webdriver.Chrome(service=service)

# Navigate to the web page
driver.get("https://www.audible.com/search")

# Wait for the products to load
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//li[contains(@class,"productListItem")]'))
)

# Find all product list items
products = driver.find_elements(by=By.XPATH, value='//li[contains(@class,"productListItem")]')

# List to hold product details
product_details = []

# Loop through each product and extract the details
for product in products:
    try:
        title = product.find_element(by=By.XPATH, value='.//h3[contains(@class,"bc-heading")]').text
        author = product.find_element(by=By.XPATH, value='.//li[contains(@class,"authorLabel")]').text
        runtime = product.find_element(by=By.XPATH, value='.//li[contains(@class,"runtimeLabel")]').text
        product_details.append([title, author, runtime])
    except Exception as e:
        print(f"An error occurred: {e}")

# Define the CSV file path
csv_file_path = "audible_products.csv"

# Write the product details to a CSV file
with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(["Title", "Author", "Runtime"])
    # Write the product details
    writer.writerows(product_details)

# Close the browser
driver.quit()

print(f"Data has been written to {csv_file_path}")
