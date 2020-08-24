import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_serial_killers_in_the_United_States'

req = requests.get(url)

soup = BeautifulSoup(req.text, 'html.parser')
print(soup)