import requests
from bs4 import BeautifulSoup
import csv

# target url for scraping
URL = "http://www.values.com/inspirational-quotes"

# create a response object
r = requests.get(URL)

# parse the content of the response
soup = BeautifulSoup(r.content, 'html5lib')

quotes = []

# extract all divs with specific id
table = soup.find('div', attrs={'id': 'all_quotes'})

for row in table.findAll(
        'div',
        attrs={
            'class':
            'col-6 col-lg-4 text-center margin-30px-bottom sm-margin-30px-top'
        }):

    # build a quote dict
    quote = {}
    quote['theme'] = row.h5.text
    quote['url'] = row.a['href']
    quote['img'] = row.img['src']
    quote['lines'] = row.img['alt'].split(" #")[0]
    quote['author'] = row.img['alt'].split(" #")[1]

    # Add a quote to the list
    quotes.append(quote)

# saving filename
filename = 'inspirational_quotes.csv'

# write all quotes to the csv file
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f, ['theme', 'url', 'img', 'lines', 'author'])
    w.writeheader()

    for quote in quotes:
        w.writerow(quote)
