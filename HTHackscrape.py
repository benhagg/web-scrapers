from bs4 import BeautifulSoup
import requests
import csv

url ='https://www.kehe.com/locations/'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

data = soup.find_all('div', class_ = 'contact')

print(data)

with open('HTHackney.csv', 'w', newline = '\n') as file:
    writer = csv.writer(file)
    for element in data:
        writer.writerow([element])
