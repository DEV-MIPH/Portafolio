import requests
from bs4 import BeautifulSoup

def get_price(url):
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text,'html.parser')
    price_with_eur = soup.find('span', {"class":"tvcurrent-price"}).contents[0]
    
    return price_with_eur

while True:
    url = input("Introduce la url: ")
    if url == "":
        break
    print(get_price(url))