from unicodedata import category
import requests
from bs4 import BeautifulSoup
import math
import re
import urllib.request
import time
import random
code_code_to_category = {
        # "니트웨어": "136245",
        "136043" : "Denim",
        "135979" : "Dresses",
        "136045" : "Shorts",
        "135985" : "Skirts",
        "136253" : "Jumpsuits",
        "136226" : "Jackets",
        "136227" : "Coats",
        "135983" : "Tops",
        "135981" : "Trousers",
    }

#웹사이트 의류 크롤링 
def crawl_website():
    for code in code_code_to_category.keys():
        get_clothes_data(code)

    return "finish"


# 카테고리별 크롤링
def get_clothes_data(code):
    # 페이지 수 아직 오류가 있어 / MVP 이후 새로 구현필요
    last_page_number = count_page(code)
    data = []
    category = code_code_to_category[code]
    print(category)

    # 페이지별 크롤링
    for i in range(last_page_number):
        print(f"page - start: {i} / {last_page_number}")
        url = f"https://www.farfetch.com/uk/shopping/women/sale/all/items.aspx?page={i}&view=90&code={code}"
        soup = crawl_page(url)

        product_grid = soup.find("ul", {"data-testid": "product-card-list"})
        products = product_grid.find_all("li", {"data-testid": "productCard"})
        cnt = 0

        # 상품별 크롤링
        for product in products:
            cnt += 1
            len_product = len(products)
            #페이지당 상품개수 및 크롤링중인 아이템 확인
            print(f"item start: {cnt} / {len_product}")
            if cnt % 39 == 0:
                time.sleep(0.002)
            else:
                time.sleep(random.random() / 1000)

            brand = product.find(
                "h3", {"data-testid": "productDesignerName"}
            ).get_text()
            item_detail = product.find(
                "p", {"data-testid": "productDescription"}
            ).get_text()


            #영국 파운드화 기준으로 크롤링됨, 한국 환율 기준으로 변동 필요
            price = product.find("span", {"data-testid": "price"}).get_text()
            price = int(re.findall("\d+", price.replace(",", ""))[0])*1600
            original_price = product.find(
                "span", {"data-testid": "initialPrice"}
            ).get_text()
            original_price = int(re.findall("\d+", original_price.replace(",", ""))[0])*1600
            sale = math.floor((original_price - price) / original_price * 100)

            product_url = (
                "https://www.farfetch.com" + product.find("a")["href"].lstrip()
            )

            image_url = product.find("meta")["content"]
            #이미지 크롤링 실패서, continue
            try:
                image_url = product.find("meta")["content"]
                image_static_url = download_image(image_url, brand, item_detail)
            except:
                continue
            data.append(
                {
                    "category": category,
                    "brand": brand,
                    "item_detail": item_detail,
                    "price(KWR)": price,
                    "original_price(KWR)": original_price,
                    "sale": sale,
                    "product_url": product_url,
                    "image_url": image_url,
                }
            )
            print(data)
        return data


def crawl_page(url):
    custom_header = {
        "referer": url,
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    }

    req = requests.get(url, headers=custom_header)
    req.raise_for_status()
    soup = BeautifulSoup(req.content, "lxml")

    return soup


def count_page(code):
    url = f"https://www.farfetch.com/uk/shopping/women/sale/all/items.aspx?page=1&view=90&code={code}"
    soup = crawl_page(url)
    try:
        max_page = max(
            re.find(
                "\d+", (soup.find("div", {"data-testid": "page-number"}).get_text())
            )
        )
        print(max_page)
        return int(max_page)
    except:
        return 1


def download_image(img_url, str_brand, str_item_detail):
    dir = "/Users/sangjoon/Downloads/crawling/"
    static_url = dir + str_brand.replace(" ", "") + str_item_detail.replace(" ", "") + ".jpg"
    urllib.request.urlretrieve(img_url, static_url)

    return static_url


crawl_website()