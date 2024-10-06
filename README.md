# 🌐 Web Scraping Tool with Selenium and BeautifulSoup

## 📖 Problem Statement

In today's data-driven world, businesses often need to collect and analyze information from various online sources to make informed decisions. However, manually gathering data from websites can be time-consuming and inefficient, especially when dealing with dynamic content that requires user interaction, such as scrolling and clicking.

This project aims to automate the process of extracting contact information from the **VATVA Association** website, which contains a list of chemicals and associated companies. The goal is to develop a web scraping tool that can seamlessly navigate the site, collect relevant data, and save it in a structured format for further analysis.

## 💡 Solution Overview

This solution utilizes **Selenium** to automate the web browser and **BeautifulSoup** to parse and extract the desired information. The main features of the tool include:

- 🖱️ **Automated Browser Navigation**: Using Selenium, the script opens the Brave browser and navigates to the specified URL.
- ⏳ **Dynamic Content Loading**: The script scrolls down the page to trigger loading additional content until all relevant data is loaded.
- 📊 **Data Extraction**: The HTML content is parsed using BeautifulSoup to extract company names, contact persons, email addresses, and mobile numbers from the loaded pages.
- 💾 **Data Storage**: The extracted data is stored in a CSV file for easy access and analysis.

## 📜 Code Walkthrough

### Dependencies

Ensure you have the following libraries installed:

- Selenium
- BeautifulSoup
- Pandas
- Requests
- Lxml

### ⚙️ Usage

To use this tool, simply run the script in your Python environment after modifying the paths for ChromeDriver, Brave, and the output CSV file as per your setup.

### 📥 Output

The output will be saved as `extracted_data.csv`, which contains the following fields:

- 🏢 Company_Name
- 👤 Contact_Person
- 📧 Contact_Email
- 📱 Mobile_Number

## 🎉 Conclusion

This web scraping tool effectively automates the data extraction process, saving time and effort while providing valuable insights into company information from the VATVA Association website. It can be easily adapted to scrape data from other similar websites by modifying the URL and extraction logic.

## 📫 Contact Me

- [LinkedIn](https://www.linkedin.com/in/animeshgarg153)
- [Email](mailto:animesh@jobemails.net)
- [Profile](https://animeshgarg.framer.ai)

---
