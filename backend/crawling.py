from django.shortcuts import render
import requests
import os
import urllib.request
from urllib.parse import urlunparse
from bs4 import BeautifulSoup
import time
import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fashion.settings")
import django
django.setup()
from products.models import Product

def get6pmCrawler():
    categorys= {
        "women-shirts-tops":["DL1w", "Top" ],
        "women-coats-outerwear" : ["DH1w", "Outer"],
        "women-dresses" : ["DE1w", "Dress"],
        "women-pants" : ["DK1w", "Pants"],
        "women-sweaters" : ["DQ1w", "Sweater"],
        "women-hoodies-sweatshirts" : ["DF1w", "Hoodie"],
        "women-jeans" : ["DI1w", "Jeans"],
        "women-shorts" : ["DM1w", "Shorts"],
        "women-skirts" : ["DN1w", "Skirts"],
        "women-jumpsuits-rompers" : ["CN3Q", "Jumpsuits"],
        "women-suits" : ["Cu4A", "Outer"]
    }

    color= ['white', 'grey', 'black', 'beige', 'brwon',' blue', 'navy', 'purple', 'green', 'red', 'orange', 'yellow', 'pink']
    
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}

    url_home = "https://www.6pm.com"
    for category in categorys:
        time.sleep(10)
        url = f"https://www.6pm.com/{category}/CKvXAR{categorys[category][0]}HAAQHiAgMBAhg.zso?s=isNew/desc/goLiveDate/desc/recentSalesStyle/desc/"
        res = requests.get(url, headers = headers)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'html.parser')
        products = soup.find_all("article") 

        for product in products:
            img = product.figure.meta["content"]
            _thumnail = img
            _url = url_home + product.a["href"] 
            _brand = product.find("dd",attrs={"itemprop":"brand"}).get_text()
            _name = product.find("dd",attrs={"itemprop":"name"}).get_text()
            _sale_price = product.find("span")
            _sale_price_text = _sale_price.get_text().split("$")[1]
            _price = _sale_price.find_next_sibling("span")
            _feature = categorys[category][1]
            _color = random.choice(color)

            if _price:
                _price = _price.get_text().split("$")[1]
                if ',' in _price:
                    _price = _price.replace(',','')

                if ',' in _sale_price_text:
                    _sale_price_text = _sale_price_text.replace(',','')

                _discount_rate = 100 - (int((float(_sale_price_text) / float(_price)) * 100))

            else:
                _price = "0"
                _discount_rate = "0"
  
            Product(name = _name, brand = _brand, price = float(_price), sale_price = float(_sale_price_text), discount_rate= _discount_rate, url= _url, thumnail = _thumnail, category = _feature, color = _color).save()
            
            
def getFarfetchCrawler():
    category_to_code = {
    "Denim": "136043",
    "Dresses": "135979",
    "Shorts": "136045",
    "Skirts": "135985",
    "Jumpsuits": "136253",
    "Jackets": "136226",
    "Coats": "136227",
    "Tops": "135983",
    "Trousers": "135981",
    }

    custom_header = {
        "referer": "https://www.farfetch.com/uk",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    }


    def check_last_page(amount_item: int):
        if amount_item != 90:
            return True
        else:
            return False


    def download_product_image(image_url: str, item_detail: str):
        static_url = "/" + item_detail + ".jpg"
        urllib.request.urlretrieve(image_url, static_url)
        return static_url


    def get_category_data(category_name: str, category_code: int):
        pagination = 1
        last_page = False
        category_data = []

        while not last_page:
            url = f"https://www.farfetch.com/uk/shopping/women/sale/all/items.aspx?page={pagination}&view=90&code={category_code}"
            req = requests.get(url, headers=custom_header)
            soup = BeautifulSoup(req.content, "lxml")
            products = soup.find_all("li", {"data-testid": "productCard"})
            amount_item = len(products)

            if check_last_page(amount_item):
                last_page = True

            for product in products:
                product_brand = product.find("h3", {"data-testid": "productDesignerName"}).get_text()
                product_detail = product.find("p", {"data-testid": "productDescription"}).get_text()
                product_sale_price = product.find("span", {"data-testid": "price"}).get_text()
                product_sale_price = int(product_sale_price[1:].replace(",", ""))
                product_original_price = product.find(
                    "span", {"data-testid": "initialPrice"}
                ).get_text()
                product_original_price = int(product_original_price[1:].replace(",", ""))
                product_sale_rate = (
                    (product_original_price - product_sale_price) / product_sale_price * 100
                )
                adjusted_sale_rate = math.floor(product_sale_rate)
                product_url = "https://www.farfetch.com" + product.find("a")["href"].lstrip()
                product_image_url = product.find("meta")["content"]

                # download_product_image(product_image_url, product_detail)
                category_data.append(
                    [
                        category_name,
                        product_brand,
                        product_detail,
                        product_sale_price,
                        product_original_price,
                        adjusted_sale_rate,
                        product_url,
                        product_image_url,
                    ]
                )

            pagination += 1

        return category_data

    def main():
        for category, code in category_to_code.items():
            category_data = get_category_data(category, code)
            print(category, category_data)


def getJcrewCrawler():
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
            # 제품이름 원가 할인가
            info = info.find("div", class_='c-product-tile__details')
            name = info.find("h3", class_='tile__detail tile__detail--name').get_text()
            original_price = info.find("span", class_="strikethrough-price").get_text()
            discount_price = info.find("span", class_="is-price").get_text()
            product_url = 'https://www.jcrew.com' + info.find("a")['href']
            url = product_url

            # 이미지
            req = requests.get(url, headers = custom_header)
            soup = BeautifulSoup(req.text, "html.parser")
            img_url = soup.find("picture").find("source")["srcset"]
            result.append([name, "jcrew", original_price, discount_price, img_url, product_url, category])

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


if __name__=='__main__':
    get6pmCrawler()
    