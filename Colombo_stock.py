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
driver.get("https://www.cse.lk/")

# Wait for the table to load
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//table[contains(@class,"table-striped")]'))
)

# Find all tables with class 'table-striped'
tables = driver.find_elements(by=By.XPATH, value='//table[contains(@class,"table-striped")]')

# List to hold all data
data = []

# Extract data from each table
for table in tables:
    rows = table.find_elements(By.XPATH, './/tr')
    for tr in rows:
        cells = tr.find_elements(By.XPATH, './/td')
        row = [cell.text for cell in cells]
        if row:  # Avoid adding empty rows
            data.append(row)

# Save data to CSV
csv_file_path = 'CSE.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the header row (adjust if needed based on the table structure)
    writer.writerow(['Date', 'Company_Name', 'Announcement'])
    # Write the data rows
    writer.writerows(data)

print(f"Data saved to '{csv_file_path}'.")

# Close the browser
driver.quit()
