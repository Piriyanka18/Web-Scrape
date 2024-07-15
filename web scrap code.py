from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.timesjobs.lk/Vacancy/showVacancies?location=Location&title=Job%20Title,%20Keywords,%20or%20Company&category=All%20Categories%20And%20Sub%20Categories&start=0&per_page=0'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    html_text = response.text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='careerfy-column-12 mobile-view')

    data = []
    for job in jobs:
        published_date = job.find('ul', class_='job-lst').text.strip()
        company_name = job.find('h2').text.strip()
        # skills = job.find('span', class_='srp-skills').text.strip()
        more_info = job.find('div', class_="careerfy-list-option").a['href']

        data.append({
            "Published Date": published_date,
            "Company Name": company_name,
            # "Skills": skills,
            "More Info": more_info
        })

    # Convert data to DataFrame
    df = pd.DataFrame(data)

    # Save DataFrame to Excel
    output_file = r'C:\Users\Lenovo\Desktop\webscraping\job_listings.xlsx'  # Use raw string literal (r'') for file paths
    df.to_excel(output_file, index=False)
    
    print(f"Data saved to {output_file}")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
