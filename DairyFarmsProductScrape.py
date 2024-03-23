import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time

# Set up the Chrome driver
driver = webdriver.Chrome()
path = r'C:\Program Files\chromedriver-win64\chromedriver-win64\chromedriver.exe'
service = Service(executable_path=path)
url = 'https://www.dairyfoods.com/directories/7376-dairy-plants-usa'

# create dairyname.txt file
with open("python/DairyName.txt", 'r') as f:
    names = f.readlines()
# create list for csv file
Ltext = []
# loop through names from txt file and imput to search bar
for name in names:
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "search-directories__field")))
        inputElement = driver.find_element(By.CLASS_NAME, "search-directories__field")
        inputElement.clear()
        inputElement.send_keys(name)
        # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "commit")))
        # button = driver.find_element(By.NAME, "commit")
        # button.click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Read More")))
        button = driver.find_element(By.PARTIAL_LINK_TEXT, "Read More")
        button.click()
        time.sleep(1)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "directory-categories-tree__category-link")))
        data = driver.find_elements(By.CLASS_NAME, "directory-categories-tree__category-link")
        for element in data:
            text = element.text
            Ltext.append(text)
        with open('DairyPlantProduct.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([name, Ltext])
            Ltext.clear()

    except:
        text = 'did not find'
        with open('DairyPlantProduct.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([name, text])