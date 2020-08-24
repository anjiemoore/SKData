import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_serial_killers_in_the_United_States'

req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')

sk_table = soup.find('table', class_ = 'wikitable')

for skill in sk_table.find_all('tbody'):
    rows = skill.find_all('tr')
    for row in rows:
        names = row.find('td')
        if names:
            print(names.text)