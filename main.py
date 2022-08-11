from bs4 import BeautifulSoup
import requests

# with open('index.html', 'r') as f:
html_site = requests.get(
    'https://www.marocannonces.com/categorie/315/Vente-immobilier/Appartements.html').text
soup = BeautifulSoup(
    html_site, 'html.parser')

appartements = soup.find('ul', class_='cars-list')
for _ in appartements.findAll('li'):
    if _.h3:
        print(_.h3.text)
        print('************************************************************************')
