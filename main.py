import requests
from bs4 import BeautifulSoup
import csv

github_page = requests.get('https://github.com/trending')

soup_object = BeautifulSoup(github_page.text, 'html.parser')

repo = soup_object.find(class_='explore-pjax-container container-lg p-responsive pt-6')

repo_list = repo.find_all(class_='Box-row')

print(len(repo_list))

# CSV functionality
file_name = 'github_trending_today.csv'

f = csv.writer(open(file_name, 'w', newline=''))

f.writerow(['Developer', 'Repo Name', 'Number of Stars'])

# iterate through repo list to get data points for csv, then write to file
for repo in repo_list:
    full_repo_name = repo.find(class_='h3 lh-condensed').text.split()

    developer = full_repo_name[0]

    repo_name = full_repo_name[2]

    stars = repo.find(class_='octicon octicon-star').parent.text.strip()
    
    f.writerow([developer, repo_name, stars])
