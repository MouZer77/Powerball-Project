import requests
from bs4 import BeautifulSoup
import csv

url = "https://powerball.us.org/lottery-powerball-jackpot-winners-list-by-state"
response = requests.get(url)
html_content = response.content
soup = BeautifulSoup(html_content, "html.parser")
# find table object:
table = soup.find('table', id="winnerstable")
# iterate through each row:
header = [] #Gives Headers a place to be placed for organization
rows = [] #Gives Rows a place to be placed for organization

for i, row in enumerate(table.find_all('tr')):
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

with open('Powerball.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(result)