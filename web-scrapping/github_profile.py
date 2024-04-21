import requests
from bs4 import BeautifulSoup as bs

github_user = input("Input Github User: ")

try:
    url = 'https://github.com/'+github_user
    r = requests.get(url)
    soup = bs(r.content, 'html.parser')
    profile_image = soup.find('img', class_='avatar')['src']
    bio = soup.find('div', class_='p-note')['data-bio-text']
    print("Name: ",github_user)
    print("Profile IMG: ",profile_image)
    print("Bio: ",bio)

except:
    print("User not found")