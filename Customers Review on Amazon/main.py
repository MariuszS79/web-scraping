import requests
from bs4 import BeautifulSoup
import csv
import lxml
from lxml import etree

# link to Amazon Fire HD 8 Tablet on amazon.co.uk
url = "https://tinyurl.com/3tcbjch4"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/98.0.4758.82 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
dom = etree.HTML(str(soup))

total_ratings = soup.find(id="acrCustomerReviewText").get_text()
total_ratings = total_ratings.split("ratings")
total_ratings = int(total_ratings[0].replace(",", ""))

print(total_ratings)

average_rating = soup.find(class_="a-icon-alt").get_text()
print(average_rating)

five_stars = soup.find(class_="a-link-normal 5star").get_text()
print(five_stars)


