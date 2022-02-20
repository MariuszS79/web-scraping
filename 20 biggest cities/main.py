import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.archdaily.com/906605/the-20-largest-cities-in-the-world-of-2018"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

cities = soup.find_all("h3")

city_list_raw = [city.getText() for city in cities]
city_list_raw = city_list_raw[0:20]

position = []
city = []
country = []
population = []

for i in range(len(city_list_raw)):
    splitted = city_list_raw[i].split()
    position.append(splitted[0])
    position[i] = position[i].replace("-", "")
    city.append(splitted[1])
    city[i] = city[i].replace(",", "")
    country.append(splitted[2])

pop = soup.find_all(lambda tag: tag.name == "p" and "Population:" in tag.text)
pop_list_raw = [p.getText() for p in pop]
pop_list_raw = pop_list_raw[::2]


for i in range(len(pop_list_raw)):
    splitted = pop_list_raw[i][12:]
    population.append(splitted)
    population[i] = population[i].replace(" ", "")
    population[i] = population[i].replace(",", "")
    population[i] = int(population[i])


fields = ["Position", "City", "Country", "Population"]

rows = []

for i in range(len(population)):
    row = [position[i], city[i], country[i], population[i]]
    rows.append(row)


with open('20 biggest cities', 'w') as f:
    write = csv.writer(f)
    write.writerow(fields)
    write.writerows(rows)
