import requests
from bs4 import BeautifulSoup

headers = {'Accept': 'text/html', 
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36'}


URL = 'https://pizzasushiwok.ru'

res = []

response = requests.get(URL, headers = headers)

if response.status_code != 200:
    print(f'Error: {response.status_code}')
    print(response.text[:500])
else:
    print('OK')

html = response.text

soup = BeautifulSoup(html, 'lxml')

#Вариант 1
#pizza_block = soup.find('div', {'alias': 'assorti'})

#Если использууете первый вариант, то измените soup на pizza_block 
pizza_names = soup.find_all('span', itemprop='name')

for span in pizza_names:
    #Вариант 1
    #print(span.get_text(strip=True))
    res.append(span.get_text(strip=True))

#Второй вариант через список 
pizza_only = [item for item in res if 'Пицца' in item]
for pizza in pizza_only:
    print(pizza)

