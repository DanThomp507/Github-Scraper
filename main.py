import requests
from bs4 import BeautifulSoup

github_page = requests.get('https://github.com/trending')

soup_object = BeautifulSoup(github_page.text, 'html.parser')

repo = soup_object.find(class_='explore-pjax-container container-lg p-responsive pt-6')

repo_list = repo.find_all(class_='Box-row')

print(len(repo_list))

for repo in repo_list:
    full_repo_name = repo.find(class_='h3 lh-condensed').text.split()

    developer = full_repo_name[0]

    repo_name = full_repo_name[2]

    stars = repo.find(class_='octicon octicon-star').parent.text.strip()
