from bs4 import BeautifulSoup
import requests
import csv

url = 'https://gfs.com/en-us/our-markets/locations/'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

data = soup.find_all('div', class_='elementor-post__excerpt') # change to 'elementor-post__title' for more data

cleanData = []
for element in data:
    clean = element.get_text().strip()
    clean = clean.replace('\n', ' ')
    cleanData.append(clean)

print(data)

# add to csv
# with open('GFS.csv', 'w', encoding = 'utf-8', newline = '') as file:
#         writer = csv.writer(file)
#         for element in cleanData:
#             writer.writerow([element])

print('done')