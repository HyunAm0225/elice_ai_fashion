from django.shortcuts import render
import requests
import os
import urllib.request
from urllib.parse import urlunparse
from bs4 import BeautifulSoup
import time

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fashion.settings")
import django
django.setup()
from crawling.models import Crawl_data

def getDataCrawler():
    categorys= {
        "women-shirts-tops":"DL1w" ,
        "women-coats-outerwear" : "DH1w",
        "women-dresses" : "DE1w",
        "women-pants" : "DK1w",
        "women-sweaters" : "DQ1w",
        "women-hoodies-sweatshirts" : "DF1w",
        "women-jeans" : "DI1w",
        "women-shorts" : "DM1w",
        "women-skirts" : "DN1w",
        "women-jumpsuits-rompers" : "CN3Q",
        "women-suits" : "Cu4A" 
    }
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}

    url_home = "https://www.6pm.com"
    for category in categorys:
        time.sleep(10)
        url = f"https://www.6pm.com/{category}/CKvXAR{categorys[category]}HAAQHiAgMBAhg.zso?s=isNew/desc/goLiveDate/desc/recentSalesStyle/desc/"
        res = requests.get(url, headers = headers)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'html.parser')
        products = soup.find_all("article") 

        for product in products:    
            img = product.figure.meta["content"]
            _img_url = "../static/"+img+".jpg"
            # urllib.request.urlretrieve(img, _img_url)
            _url = url_home + product.a["href"] 
            _brand = product.find("dd",attrs={"class":"RN-z"}).get_text()
            _name = product.find("dd",attrs={"class":"SN-z"}).get_text()
            _sale_price = product.find("span")
            _sale_price_text = _sale_price.get_text().split("$")[1]
            _price = _sale_price.find_next_sibling("span")

            if _price:
                _price = _price.get_text().split("$")[1]
                if ',' in _price:
                    _price = _price.replace(',','')

                if ',' in _sale_price_text:
                    _sale_price_text = _sale_price_text.replace(',','')

                _discount_rate = str(int(( float(_sale_price_text) / float(_price) ) * 100))

            else:
                _price = "0"
                _discount_rate = "0"
                
            Crawl_data(name = _name, brand = _brand, price = _price, sale_price = _sale_price_text, discount_rate= _discount_rate + "%", url= _url, img_url = _img_url).save()
            


if __name__=='__main__':
    getDataCrawler()
    