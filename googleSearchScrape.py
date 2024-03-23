from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import random
import csv

# set up driver
path = r'C:\Program Files\chromedriver-win64\chromedriver-win64\chromedriver.exe'
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
data = []
current_height = 0
with open("googSearchlocations.txt", "r") as file:
            locations = file.readlines()

def scrape_google_search():  # Provide path to your ChromeDriver
    for location in locations:
        query = f'commercial "food waste" recycling in {location}'
        driver.get("https://www.google.com")  # Open Google
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "gLFyf")))
        search_box = driver.find_element(By.CLASS_NAME, "gLFyf")  # Name of the search box element
        time.sleep(random.randint(6,10))  # Wait for page to load
        search_box.send_keys(query)
        
        loc_data = []
        current_height = 0
        while len(loc_data) < 25:  # Limiting to n results
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "VuuXrf")))
            time.sleep(random.randint(2,6))  # Wait for page to load (random?)
            companies = driver.find_elements(By.CLASS_NAME, "GTRloc")
            
            for company in companies:
                company_name = company.text
                if company_name != '':
                    pass
                else:
                    continue
# remove unwanted websites
                if any(substring in company_name for substring in ['.gov', 'news', 'News', 'PDF', '.edu', 'muni', '.org']):
                    continue
                else:
                    pass
                loc_data.append((company_name, location))
            
            # Scroll to the bottom of the page to load more results
            time.sleep(random.randint(6,10))
            
            # make scrolling mechanism human-like
            pg_height = driver.execute_script("return document.body.scrollHeight") # total height
            # init scroll height outside of loop
            #execute script runs javascript code
            '''not working could just do 2 pages worth of results and then move on to the next location'''
            '''figure out variable initialization'''
            if current_height == 0:
                current_height = 0
            while current_height <= pg_height:
                time.sleep(random.uniform(1,2))  # Wait for page to load
                scroll_height = random.randint(500, 700)
                driver.execute_script(f"window.scrollBy(0, {scroll_height});")
                current_height += scroll_height
            # write to csv
        with open('google_search_results2.csv', "a", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(loc_data)
        scroll_height = 0
        data.extend(loc_data)
    return data

if __name__ == "__main__":
    search_results = scrape_google_search()
    driver.quit()
