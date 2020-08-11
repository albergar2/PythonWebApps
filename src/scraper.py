__author__ = 'albergar2'

import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.johnlewis.com/kettler-palma-4-seater-garden-cube-table-and-chairs-set/p2255253")
soup = BeautifulSoup(r.content, "html.parser")
element = soup.find("p", {"class": "price price--large"})

string_value = element.text.strip() 
print(string_value)
price = float(string_value[1:])


if price < 100:
    print("Buy the chair!")
elif price == 100:
    print("Buy at your own peril!")
else:
    print("Definitely don't buy.")


#<p class="price price--large">£599.00</p>