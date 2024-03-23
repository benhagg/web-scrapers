import requests
from bs4 import BeautifulSoup
import re
import csv

url = 'https://performancefoodservice.com/Our-Locations#locations-C'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')


data = soup.find_all('address')
print(data)

cleanData = re.sub('<[^>]+>', '', str(data))
print(cleanData)

# put clean data into a csv file
with open ('PFG.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([cleanData])