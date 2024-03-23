# webscraping application
from bs4 import BeautifulSoup
import requests
import csv

url = 'https://apps.ams.usda.gov/dairy/ApprovedPlantList/'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
# column labels
column_labels = soup.find_all('th', attrs = {'scope' : 'col'})
column_labels = column_labels[:5]
column_labels_fr = [column.text.strip() for column in column_labels]

# rows of data (1608)
rows = [span for span in soup.find_all('span') if span.get('id', '').startswith('CHPublic')]
rows_fr = [row.text.strip() for row in rows]
for index, item in enumerate(rows_fr):
    if "Resident Plant" in item:
        print("found it ")
        rows_fr.pop(index)
# print column labels
csv_file = open('webscraper.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(column_labels_fr)
# remove unneeded item.
'''rows_fr.remove('* Resident Plant')'''

# iterate throug rows in groups of 5 append to csv file
for i in range(0, 1215, 5):
    csv_writer.writerow(rows_fr[i:i+5])
for i in range(1215, len(rows_fr), 4):
    csv_writer.writerow(rows_fr [i:i+4])

print("finshed running")
csv_file.close()

#pandas dataframe 
'''df = pd.DataFrame(columns = column_labels_fr)
print(df)'''

# other soup functions (practice)
'''result = soup.find("span", attrs={ 'id' : "CHPublic_Repeater2_Label19_21"})
print(result)
column_labels = soup.find_all('th', attrs = {'scope' : 'col'})
column_labels = pop.column_labels[]
print(column_labels[0:5])'''
