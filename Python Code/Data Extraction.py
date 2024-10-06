import time
import re
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# ------------------- Configuration -------------------
# Set the path to ChromeDriver and Brave browser executable
chrome_driver_path = "YOUR_CHROME_DRIVER_PATH"  # Replace with your actual ChromeDriver path
brave_path = "YOUR_CHROME_PATH"  # Replace with your actual Brave executable path

# ------------------- Set Up WebDriver -------------------
# Configure options for Brave browser
options = Options()
options.binary_location = brave_path
options.add_argument('--ignore-certificate-errors')  # Ignore SSL certificate errors
options.add_argument('--allow-insecure-localhost')   # Allow insecure localhost
options.add_argument('--headless')                   # Run browser in headless mode

# Initialize the ChromeDriver service and create a WebDriver instance
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

# ------------------- Load the Target URL -------------------
url = "http://www.vatvaassociation.org/search/chemicals"  # Replace with your URL
driver.get(url)

# Wait for the page to load
time.sleep(3)

# Scroll to the bottom of the page to load additional content
previous_height = driver.execute_script('return document.body.scrollHeight')
while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(3)  # Wait for new content to load
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height == previous_height:  # Exit if no more content is loaded
        break
    previous_height = new_height

# ------------------- Extract Page Source -------------------
page_source = driver.page_source
driver.quit()  # Close the driver after page source is collected

# ------------------- Parse HTML with BeautifulSoup -------------------
soup = BeautifulSoup(page_source, 'lxml')  # Parse HTML content

# Extract links to individual company pages
a_tags = soup.find_all('a', class_='result-name')
list_of_links = [i['href'] for i in a_tags if 'href' in i.attrs]  # List comprehension for links

# Initialize lists to store extracted data
companies, contact_persons, contact_emails, mobile_numbers = [], [], [], []

# ------------------- Extract Data from Company Links -------------------
for link in list_of_links:
    response = requests.get(link)
    soup_temp = BeautifulSoup(response.content, 'lxml')

    # Extract company name
    com_name = soup_temp.find('li', class_='active', id='breadcrumb_keyword').text.strip()
    companies.append(com_name)

    # Extract additional information
    temp_list = [str(i.text).replace('\t', '').replace('\n', ' ') for i in soup_temp.find_all('div', class_='flex_single_i')]
    output = "\n".join(temp_list)

    # Use regular expressions to extract contact information
    con_name = re.search(r'Contact Person (.+)', output)
    mob_no = re.search(r'Mobile\s+([\d\s/]+)', output)
    con_email = re.search(r'Email\s+(.+)', output)

    # Get matched groups or set to empty string if not found
    contact_persons.append(con_name.group(1).strip() if con_name else 'N/A')
    mobile_numbers.append(mob_no.group(1).strip() if mob_no else 'N/A')
    contact_emails.append(con_email.group(1).strip() if con_email else 'N/A')

# ------------------- Create DataFrame and Save to CSV -------------------
data = {
    'Company_Name': companies,
    'Contact_Person': contact_persons,
    'Contact_Email': contact_emails,
    'Mobile_Number': mobile_numbers
}
df = pd.DataFrame(data)
df.to_csv("PATH_TO_SAVE_EXTRACTED_CSV", index=False)  # Save DataFrame to CSV

print("Data extraction complete. CSV file saved successfully.")

