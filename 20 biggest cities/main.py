import requests
import lxml
from bs4 import BeautifulSoup

url = "https://www.archdaily.com/906605/the-20-largest-cities-in-the-world-of-2018"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

cities = soup.find_all(name='h3')

for city in cities:
    print(city)

