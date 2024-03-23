from bs4 import BeautifulSoup
import requests
import csv

url = 'https://www.unfi.com/locations'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

data = soup.find_all('div', class_='streetAddress') # change to 'elementor-post__title' for more data

data1 = []

for i in soup:
    soup1 = soup.get_text().strip()
    data1.append(soup1)

cleanData = []
for element in data:
    clean = element.get_text().strip()
    clean = clean.replace('\n', ' ')
    cleanData.append(clean)

# add to csv
'''with open('UNFI.csv', 'w', encoding = 'utf-8', newline = '') as file:
        writer = csv.writer(file)
        for element in cleanData:
            writer.writerow([element])'''

print(data1)

print('done')