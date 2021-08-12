import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0'}

url = "https://Madrika.ir"

r = requests.get(url, headers=headers)
print(r.text)

soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())