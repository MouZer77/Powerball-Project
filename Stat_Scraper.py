import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.statista.com/statistics/388238/sales-of-lotteries-by-state-us/"
response = requests.get(url)
html_content = response.content
soup = BeautifulSoup(html_content, "html.parser")

tab = soup.find("table",{"class":"table hidden"})

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

with open('Lottery_Sales_Stats.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(result)