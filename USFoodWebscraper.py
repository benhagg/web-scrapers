from bs4 import BeautifulSoup as bs4
import requests
import csv
import html
import json

'''url = 'https://www.usfoods.com/locations.html'
page = requests.get(url)
soup = bs4(page.text, 'html.parser')
# write soup to txt file
with open('USFood.xt', 'w') as file:
    file.write(str(soup))'''
# write soup to json file
with open('USFood.txt', 'r') as file:
    jsonsoup = file.read()
    decoded_json = json.loads(jsonsoup)


with open ('USFood.json', 'w') as file:
    json.dump(decoded_json, file, indent = 2, sort_keys=True)

print('done')

    