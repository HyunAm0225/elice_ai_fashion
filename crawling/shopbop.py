import requests
from bs4 import BeautifulSoup
import urllib.request
import ssl  # ssl Error 발생 시
ssl._create_default_https_context = ssl._create_unverified_context

kategorie_data = {
    "coats": 64892,
    "dresses": 15412,
    "jackets": 64849,
    "jeans": 15382,
    "jumpsuits-rompers": 15451,
    "pants": 15474,
    "shorts": 15486,
    "skirts": 15491,
    'sweaters-knits': 15505,
    "tops": 15522
}


def get_cloth_data(kategorie):
    number = get_cloth_count(kategorie)
    n = 1
    data = []
    # test = 0
    page = number // 100
    for i in range(page+1):
        result = requests.get(f"https://www.shopbop.com/sale-clothing-{kategorie}/br/v=1/{kategorie_data[kategorie]}.htm?baseIndex={i*100}")
        # Check for 200 OK response
        src = result.content
        soup = BeautifulSoup(src, 'lxml')
        ul = soup.find("ul", {'class': 'products'})

        for li in ul.find_all("li"):
            # print(li.find('div', class_='title').get_text().strip(), end=" ")
            # print(li.find('div', class_='title').get_text().strip(), end=" ")
            # print(li.find('span', class_='sale-price-low').get_text().strip())
            brand = li.find('div', class_='brand').get_text().strip()
            title = li.find('div', class_='title').get_text().strip().replace('/', '')
            high_price = li.find('span', class_='retail-price').get_text().strip()
            low_price = li.find('span', class_='sale-price-low').get_text().strip()
            img = li.find('span', class_='productBrowseMainImage').find('img')['src'].strip()
            url = f"https://www.shopbop.com/{li.find('a')['href']}"

            # 이미지 다운로드
            # urllib.request.urlretrieve(img, f"static/{kategorie}/{title}.jpg") # 이미지 다운로드
            # print(f"{n}/{number} 다운로드 중")
            n += 1
            data.append((title, brand, high_price, low_price, img, url))
    return data


def get_cloth_count(kategorie):
    result = requests.get(f"https://www.shopbop.com/sale-clothing-{kategorie}/br/v=1/{kategorie_data[kategorie]}.htm")
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    number = soup.find("div", class_="results").get_text()
    pagination = int(number.split()[0])
    return pagination


print(get_cloth_data(input()))
