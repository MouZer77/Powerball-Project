import requests
from bs4 import BeautifulSoup

url = "https://www.powerball.net/winners"
response = requests.get(url)
html_content = response.content
soup = BeautifulSoup(html_content, "html.parser")
# find table object:
table = soup.find('table', id="table-winners")
# iterate through each row:
header = []
rows = []
for i, row in enumerate(soup.find_all('tr')):
    if i == 0:
        header = [el.text.strip() for el in row.find_all('th')]
    else:
        rows.append([el.text.strip() for el in row.find_all('td')])

divs = soup.find('div', text='')

for div in divs:
    div.extract()

print(header)
for row in rows:
    print(row)