import requests
from bs4 import BeautifulSoup

url = "https://powerball.us.org/lottery-powerball-jackpot-winners-list-by-state"
response = requests.get(url)
html_content = response.content
soup = BeautifulSoup(html_content, "html.parser")
# find table object:
table = soup.find('table', id="winnerstable")
# iterate through each row:
header = []
rows = []
for i, row in enumerate(table.find_all('tr')):
    if i == 0:
        header = [el.text.strip() for el in row.find_all('th')]
    else:
        rows.append([el.text.strip() for el in row.find_all('td')])

print(header)
for row in rows:
    print(row)