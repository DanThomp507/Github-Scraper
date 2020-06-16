import requests
from bs4 import BeautifulSoup

github_page = requests.get('https://github.com/trending')
print(github_page)

soup_object = BeautifulSoup(github_page.text, 'html.parser')
print(soup_object)