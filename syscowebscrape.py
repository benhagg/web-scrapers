from bs4 import BeautifulSoup
from pandas import json_normalize
import pandas as pd
import csv
import requests


url = 'https://www.sysco.com/Contact/Contact/Our-Locations.html'

page = requests.get(url, timeout=5)
soup = BeautifulSoup(page.text, 'html.parser')

with open('sysco.txt', 'w') as txt_file:
    txt_file.write(str(soup))
# print column labels
'''csv_file = open('webscrapersysco.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(loction_data)'''


print("finshed running")