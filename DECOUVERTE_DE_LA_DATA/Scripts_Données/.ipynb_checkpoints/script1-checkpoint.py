import requests
from bs4 import BeautifulSoup

url = 'https://www.zalando.fr/mode-femme/'

requete = requests.get(url)
soup = BeautifulSoup(requete.text, 'html.parser')

tableau = []

produits = soup.find_all('div', {'class': 'L5YdXz _0xLoFW _7ckuOK mROyo1'})
for produit in produits:
    nom = produit.find('h3',{'class': 'KxHAYs lystZ1 FxZV-M _4F506m ZkIJC- r9BRio qXofat EKabf7 nBq1-s _2MyPg2'}).text
    prix = produit.find('span', {'class': 'KxHAYs lystZ1 dgII7d _3SrjVh'}).text
    
    tableau.append([nom, prix])

    if len(tableau) >= 1000:
        break
    
print(tableau)
