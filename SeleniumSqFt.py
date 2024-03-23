import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import csv
from time import sleep
from random import randint

url = r'https://www.google.com/'
path = r'C:\Program Files\chromedriver-win64\chromedriver-win64\chromedriver.exe'
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
Ldata = []

with open("DCaddy.txt", 'r') as f:
    addresses = f.readlines()

batch_size = randint(35,70)
batch_size = min(batch_size, len(addresses))

for i in range(0, len(addresses), batch_size):
    batch = addresses[i:i+batch_size]
    print(f"Processing batch {i//batch_size + 1} of {len(addresses)//batch_size + 1}")
            
    for address in batch:
        pairs = {'TOTAL SQ FT': '\"not found\"', 'Land Use': '\"not found\"'}
        try:
            driver.get(url)
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "gLFyf")))
            inputElement = driver.find_element(By.CLASS_NAME, "gLFyf")
            inputElement.clear()
            inputElement.send_keys(f'sq footage of {address} ')
            sleep(randint(1,2))  # Introducing a sleep here to avoid overwhelming requests
            
            # Access property record then first link in search results
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "LoopNet")]')))
            button = driver.find_element(By.XPATH, '//span[contains(text(), "LoopNet")]')
            button.click()
            sleep(randint(3,6))  # Introducing a sleep here to avoid overwhelming requests
            # Extract data
            try:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="detailsInf"]')))
                data = driver.find_element(By.XPATH, '//*[@id="detailsInf"]').text
                lines = data.split('\n')
                pairs = {lines[i]:lines[i+1] for i in range(0, len(lines), 2)}
            except Exception as e:
                print(f"Error extracting data for {address}: {e}")

        except Exception as e:
            print(f"Error processing address {address}: {e}")
            
        # Write to CSV
        try:
            with open('DCOutput.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([address, pairs.get('TOTAL SQ FT', 'not found'), pairs.get('Land Use', 'not found')])
                print(address, pairs.get('TOTAL SQ FT', 'not found'), pairs.get('Land Use', 'not found'))
        except Exception as e:
            print(f"Error writing data for {address} to CSV: {e}")

    print("sleeping")        
    time.sleep(randint(900, 1500))           
       
driver.quit()




        
        