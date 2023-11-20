import requests
from bs4 import BeautifulSoup
import csv

url = "https://en.wikipedia.org/wiki/List_of_U.S._states_and_territories_by_poverty_rate"
response = requests.get(url)
html_content = response.content
soup = BeautifulSoup(html_content, "html.parser")

tab = soup.find("table",{"class":"wikitable sortable mw-datatable static-row-numbers sticky-header"})

header = []
rows = []

for i, row in enumerate(tab('tr')):
    if i == 0:
        header = [el.text.strip() for el in row.find_all('th')]
    else:
        rows.append([el.text.strip() for el in row.find_all('td')])

# print(header)
# for row in rows:
#     print(row)

result = []
result.append(header)
for row in rows:
    result.append(row)

with open('Poverty_States.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(result)