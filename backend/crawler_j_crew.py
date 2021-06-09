from django.shortcuts import render
import requests, os, urllib.request, time, random, ssl
from urllib.parse import urlunparse
from bs4 import BeautifulSoup
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fashion.settings")
import django
django.setup()
from products.models import Product
ssl._create_default_https_context = ssl._create_unverified_context
from 
# short sleeve top
# long sleeve top
# short sleeve outwear
# long sleeve outwear
# vest
# sling
# shorts
# trousers
# skirt
# short sleeve dress
# long sleeve dress
# vest dress
# sling dress

kategorie_data = {
"coats": ["64892","long sleeve outwear"],
"dresses": ["15412","long sleeve dress"],
"jackets": ["64849","long sleeve outwear"],
"jeans": ["15382","trousers"],
"pants-leggings": ["15474","trousers"],
"shorts": ["15486","shorts"],
"skirts": ["15491","skirt"],
'sweaters-knits': ["15505","long sleeve top"],
"tops": ["15522","long sleeve top"]
}

color_data= ['white', 'grey', 'black', 'beige', 'brown',' blue', 'navy', 'purple', 'green', 'red', 'orange', 'yellow', 'pink']

start = time.time()
i = 0

# 전체 품목 개수
def total_num(all_item_url):
    custom_header = {
        'referer' : all_item_url,
        'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    req = requests.get(all_item_url, headers = custom_header)
    soup = BeautifulSoup(req.text, "html.parser")
    return int(soup.find("div", class_="pagination__item pagination__item--total-items").get_text().split(" ")[0])

# 크롤링
def crawling(soup):
    global i
    j = 0
    infos = soup.find_all("li", class_='c-product-tile')
    for info in infos:
        # # 제품이름 원가 할인가
        # info = info.find("div", class_='c-product-tile__details')
        # name = info.find("h3", class_='tile__detail tile__detail--name').get_text()
        # original_price = info.find("span", class_="strikethrough-price").get_text()
        # discount_price = info.find("span", class_="is-price").get_text()
        product_url = 'https://www.jcrew.com' + info.find("a")['href']
        url = product_url
        print(url)
        # 이미지
        req = requests.get(url, headers = custom_header)
        soup = BeautifulSoup(req.text, "lxml")
        print(soup.find('img')['src'])
        break
        # img_url = soup.find("picture").find("source")["srcset"]
        # result.append([name, "jcrew", original_price, discount_price, img_url, product_url, category])

        # 이미지 다운로드. 아래 주석해제하고 폴더위치 변경 후 사용.
        j += 1
        # urllib.request.urlretrieve(img_url, f"static/{category}/"+category +"_"+ str(j) + '.jpg' )

        # 진행률 체크
        # 한 품목이 여러 카테고리인 경우가 있어서 100% 가 조금 넘게 나옴!
        i += 1
        print(f"현재 {i}/{total_num} 진행중. {round(i / total_num * 100, 2)}%")

result = []
categories = [
    'blazers', 'coats_and_jackets', 'denim_jeans', 'dressesandjumpsuits', 'pants', 
    'shirts_tops', 'shorts', 'skirts', 'sweaters', 'sweatshirts_sweatpants', 'tshirts_tanktops'
]
all_item_url = "https://www.jcrew.com/kr/r/sale/women/sweaters/denim_jeans/skirts/shorts/blazers/coats_and_jackets/tshirts_tanktops/pants/sweatshirts_sweatpants/dressesandjumpsuits/shirts_tops?crawl=no"
total_num = total_num(all_item_url)

for category in categories:
    url = f'https://www.jcrew.com/kr/r/sale/women/{category}?crawl=no&Npge=1&Nrpp=120'
    custom_header = {
        'referer' : url,
        'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    req = requests.get(url, headers = custom_header)
    soup = BeautifulSoup(req.text, "html.parser")
    crawling(soup)


# 크롤링 결과 result에
# [[제품이름1, 브랜드, 원가1, 할인가1, 이미지url, 상품url, 카테고리1],
#  [제품이름2, 브랜드, 원가2, 할인가2, 이미지url2, 상품url2, 카테고리2],
#  [제품이름3, 브랜드, 원가3, 할인가3, 이미지url3, 상품url3, 카테고리3]]
# 이런식으로 저장되어있음.
# ex). print(result[0])
# ['Sommerset blazer in Italian stretch wool',
#   'jcrew',
#   'KRW 410,557',
#   'KRW 281,414–KRW 355,910',
#   'https://www.jcrew.com/s7-img-facade/AR127_RD0065_m?fmt=jpeg&qlt=90,0&resMode=sharp&op_usm=.1,0,0,0&crop=0,0,0,0&wid=500&hei=500',
#   'https://www.jcrew.com/kr/p/shops/reimagined/blazers/sommerset-blazer-in-italian-stretch-wool/AR127?sale=true&isFromSale=true&color_name=faded-poppy',
#   'blazers']

print("걸린시간: ", time.time() - start)

