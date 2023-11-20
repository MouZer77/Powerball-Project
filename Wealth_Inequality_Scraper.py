import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.statista.com/statistics/227249/greatest-gap-between-rich-and-poor-by-us-state/#:~:text=New%20York%20was%20the%20state,the%20United%20States%20that%20year."
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

with open('Wealth_Inequality.csv', 'w', newline='') as file:
    writer = csv.writer(file)