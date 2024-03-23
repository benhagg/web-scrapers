import requests
from bs4 import BeautifulSoup
import json
import re

url = 'https://vistar.com/About/Page#Map'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')


data = soup.find_all('script', id = 'MapLocations')

cleanData = re.sub('<[^>]+>', '', str(data))

# put data in a json file
with open ('Vistar.json', 'w') as f:
    json.dump(cleanData, f)