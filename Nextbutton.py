from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time

# Install and get the path of the ChromeDriver
chrome_driver_path = ChromeDriverManager().install()

# Use the Service class to specify the path to the ChromeDriver
service = Service(chrome_driver_path)

# Initialize WebDriver with the service
driver = webdriver.Chrome(service=service)

# Navigate to the web page
driver.get("https://www.amazon.fr/s?k=Phones&__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2J3RH0DZXNA51&sprefix=phones%2Caps%2C410&ref=nb_sb_noss_1")

# List to hold product details
product_details = []

# Function to extract product details from the current page
def extract_products():
    # Wait for the products to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class,"puis-card-border")]'))
    )

    # Find all product list items
    products = driver.find_elements(by=By.XPATH, value='//div[contains(@class,"puis-card-border")]')

    # Loop through each product and extract the details
    for product in products:
        try:
            Product = product.find_element(by=By.XPATH, value='.//span[contains(@class,"a-text-normal")]').text
            product_details.append([Product])
        except Exception as e:
            print(f"An error occurred: {e}")

# Extract products from the first page
extract_products()

# Loop through the next 6 pages
for _ in range(6):
    try:
        # Wait for the next button to be clickable and click it
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[contains(@class,"s-pagination-next")]'))
        )
        next_button.click()

        # Wait for the page to load
        time.sleep(2)

        # Extract products from the current page
        extract_products()
    except Exception as e:
        print(f"An error occurred while navigating to the next page: {e}")
        break

# Define the CSV file path
csv_file_path = "Amazon_products_1.csv"

# Write the product details to a CSV file
with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(["Product"])
    # Write the product details
    writer.writerows(product_details)

driver.quit()

print(f"Data has been written to {csv_file_path}")
