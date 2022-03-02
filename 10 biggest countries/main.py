import requests
from bs4 import BeautifulSoup
import csv
from lxml import html

url = "https://www.worlddata.info/the-largest-countries.php"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# tree = html.fromstring(response.content)
# number_one = tree.xpath('//*[@id="example2"]/tbody/tr[1]/td[2]')
# print(number_one)

test = soup.find(class_="std100 hover")
print(test.text)
lista = [i.getText() for i in test]
print(lista)



