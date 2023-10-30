import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.powerball.net/winners"
response = requests.get(url)
html_content = response.content
soup = BeautifulSoup(html_content, "html.parser")
# find table object:
tab = soup.find("table",{"class":"table-winners"})

header = []
rows = []

for i, row in enumerate(tab('tr')):
    if i == 0:
        header = [el.text.strip() for el in row.find_all('th')]
    else:
        rows.append([el.text.strip() for el in row.find_all('td')])

result = []
result.append(header)
for row in rows:
    result.append(row)

with open('State_Powerball.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(result)