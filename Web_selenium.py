import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Firefox options
options = Options()
options.headless = True  # Optional: run in headless mode

# Initialize the WebDriver
driver = webdriver.Firefox(options=options)

def main():
    try:
        # Open the webpage
        driver.get('https://wiki.erepublik.com/index.php/List_of_cities_and_regions')

        # Wait for the table body to be present
        wait = WebDriverWait(driver, 10)
        tbody = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="mw-content-text"]/div[1]/table/tbody'))
        )

        # Extract data
        data = []
        rows = tbody.find_elements(By.XPATH, './/tr')
        for tr in rows:
            row = [item.text for item in tr.find_elements(By.XPATH, './/td')]
            data.append(row)

        # Save data to CSV
        with open('cities_and_regions.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(data)

        print("Data saved to 'cities_and_regions.csv'.")

    finally:
        driver.quit()

if __name__ == '__main__':
    main()
