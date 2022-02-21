import requests
from bs4 import BeautifulSoup
import csv
import lxml

# link to Amazon Fire HD 8 Tablet on amazon.co.uk
url = "https://tinyurl.com/3tcbjch4"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/98.0.4758.82 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")

total_ratings = soup.find(id="acrCustomerReviewText").get_text()
total_ratings = total_ratings.split("ratings")
total_ratings = int(total_ratings[0].replace(",", ""))






print(five_stars)

