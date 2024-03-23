from selenium import webdriver
from selenium.webdriver.common.keys import Keys # allows you to push keys like enter, esc, etc.
from selenium.webdriver.chrome.service import Service # allows you to use the chromedriver
from selenium.webdriver.support.ui import WebDriverWait # allows you to wait for the page to load
from selenium.webdriver.support import expected_conditions as EC # allows you to wait for the page to load
from selenium.webdriver.common.by import By # by element
import time
from bs4 import BeautifulSoup
import requests

path = r'C:\Users\thagg\Downloads\Code extension apps\chromedriver-win64\chromedriver-win64\chromedriver.exe'
service = Service(path)
driver = webdriver.Chrome(service=service)

driver.get("https://www.unfi.com/west-locations-mobile")
print(driver.title) # title of the webpage

# 
# search = driver.find_element('id', 'edit-search-block-form--2') # navigate to the search bar
# search.send_keys('locations') # input text into search bar
# search.send_keys(Keys.RETURN) # hit enter
# time.sleep(5) 

# function to navigate to link based on displayed text and click
def click_link(text):
    try:
        link = driver.find_element_by_xpath("//a[@text]='{text}]")
        link.click()
        time.sleep(5)
    except:
        print(f'could not find {text} link')

links_to_click = ['East Coast', 'West Coast', 'Central']
cleanData = []
for link in links_to_click:
    click_link(link)
    extracted_html = driver.page_source
    soup = BeautifulSoup(extracted_html, 'html.parser')
    
    data = soup.get_text(strip=True)
    cleanData.append(data)
print(cleanData)

# explicit wait
# try:
#     data = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located('class_', 'sc-1w24qwn-1 cpEnwH'))
#     print(data)
# except:
#     print('did not load')


