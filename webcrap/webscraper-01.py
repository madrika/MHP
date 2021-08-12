from urllib.request import urlopen
from bs4 import BeautifulSoup


url = urlopen('https://digikala.com')
# print(html.read())
bs = BeautifulSoup(url, 'html.parser')
print(bs.h1)


# import requests
# from bs4 import BeautifulSoup
#
# headers = {'User-Agent': 'Mozilla/5.0'}
#
# url = "https://linkedin.com/company/1005"
#
# r = requests.get(url, headers=headers)
# print(r.text)
#
# soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())

