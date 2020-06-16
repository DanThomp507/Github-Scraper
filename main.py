import requests
from bs4 import BeautifulSoup

github_page = requests.get('https://github.com/trending')

soup_object = BeautifulSoup(github_page.text, 'html.parser')

repo = soup_object.find(class_='explore-pjax-container container-lg p-responsive pt-6')

repo_list = repo.find_all(class_='Box-row')

print(len(repo_list))
