import requests
from bs4 import BeautifulSoup
import csv

url = "https://worldpopulationreview.com/country-rankings/largest-countries-in-the-world"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

countries = soup.find_all("tr")

print(countries)