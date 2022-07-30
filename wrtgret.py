from bs4 import BeautifulSoup  
import requests               
from requests import get
import time
import random

url = 'https://www.avito.ru/sankt-peterburg/kvartiry/sdam/na_dlitelnyy_srok-ASgBAgICAkSSA8gQ8AeQUg?cd=1&p='
houses = []
count = 1
while count <= 1:
    url = 'https://www.avito.ru/sankt-peterburg/kvartiry/sdam/na_dlitelnyy_srok-ASgBAgICAkSSA8gQ8AeQUg?cd=1&p=' + str(count)
    print(url)
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')

    house_data = html_soup.find_all('div', class_="iva-item-root-_lk9K photo-slider-slider-S15A_ iva-item-list-rfgcH iva-item-redesign-rop6P iva-item-responsive-_lbhG items-item-My3ih items-listItem-Gd1jN js-catalog-item-enum")
    if house_data != []:
        houses.extend(house_data)
        value = random.random()
        scaled_value = 1 + (value * (6 - 5))
        print(scaled_value)
        time.sleep(scaled_value)
    else:
        print('empty')
        break
    count += 1
    
print(len(houses))
print(houses[0])
print()
n = int(len(houses)) - 1
count = 0
while count <= 1:  # count <= n
    info = houses[int(count)]
    price = info.find ('span',{"class":"price-text-_YGDY text-text-LurtD text-size-s-BxGpL"}).text
    title = info.find ('a',{"class":"link-link-MbQDP link-design-default-_nSbv title-root-zZCwT iva-item-title-py3i_ title-listRedesign-_rejR title-root_maxHeight-X6PsH"}).text
    print(title, ' ', price)
    count += 1
