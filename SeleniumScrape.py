import selenium
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



url = "https://www.gps-coordinates.net/gps-coordinates-converter"
path = r'C:\Program Files\chromedriver-win64\chromedriver-win64\chromedriver.exe'
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
Latitude =[]
Longitude =[]
#loop through addresses from txt file
with open("DCaddy.txt", 'r') as f:
    addresses = f.readlines()
driver.get(url)
time.sleep(5)
for address in addresses:
    try:
        time.sleep(.5)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "address")))
        inputElement = driver.find_element(By.ID, "address")
        inputElement.clear()
        inputElement.send_keys(address)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary")))
        button = driver.find_element(By.CLASS_NAME, "btn-primary")
        button.click()
        time.sleep(1)
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element(By.ID, "latitude").get_attribute('value') != '')
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element(By.ID, "longitude").get_attribute('value') != '')
        sLatitude = driver.find_element(By.ID, "latitude").get_attribute('value')
        sLongitude = driver.find_element(By.ID, "longitude").get_attribute('value')
        Latitude.append(sLatitude)
        Longitude.append(sLongitude)
        # write address lat long to csv
        with open('DairyPlantOutput.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for lat, lon in zip(Latitude, Longitude):
                writer.writerow([address, lat, lon])

            # Clear lists
        Latitude.clear()
        Longitude.clear()
            
    except:
        print('not found for ' + address)
        Latitude.append("")
        Longitude.append("")
        continue

   
    
# get latitude and longitude
    
    

    '''try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h3')))

        link = driver.find_element(By.CSS_SELECTOR, 'h3')
        link.click()
    except:
        sqFeet.append((address + '*' + ""))
        continue
        '''
    '''try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '//div[@id="nationwide/lot_and_building_info_content"]/div[@class="cols"]/div[@class="cols21"]/table[@class="data"]/tr[1]/td[@class="r_align"]')))

        square_footage = driver.find_element(By.CSS_SELECTOR, '//div[@id="nationwide/lot_and_building_info_content"]/div[@class="cols"]/div[@class="cols21"]/table[@class="data"]/tr[1]/td[@class="r_align"]')
        print(square_footage)
        squareFootageText = square_footage.text
        sqFeet.append((address + '*' + squareFootageText))
    except:
        sqFeet.append((address + '*' + ""))
        continue'''

time.sleep(3)
driver.quit()

#write to csv file
# with open('DairyLatLong.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(['Address', 'Latitude', 'Longitude'])
#     writer.writerows(zip(addresses, Latitude, Longitude,))
#     f.close()
