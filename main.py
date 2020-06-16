import requests
from bs4 import BeautifulSoup

github_page = requests.get('https://github.com/trending')
# print(github_page)

soup_object = BeautifulSoup(github_page.text, 'html.parser')
# print(soup_object)

repo = soup_object.find(class_='explore-pjax-container container-lg p-responsive pt-6')
# print(repo)

repo_list = repo.find_all(class_='Box-row')

print(len(repo_list))
