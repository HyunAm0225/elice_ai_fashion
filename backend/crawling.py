from django.shortcuts import render
import requests, os, urllib.request, time, random, ssl
from urllib.parse import urlunparse
from bs4 import BeautifulSoup
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fashion.settings")
import django
django.setup()
from products.models import Product
ssl._create_default_https_context = ssl._create_unverified_context

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
"pants": ["15474","trousers"],
"shorts": ["15486","shorts"],
"skirts": ["15491","skirt"],
'sweaters-knits': ["15505","long sleeve top"],
"tops": ["15522","long sleeve top"]
}

color_data= ['white', 'grey', 'black', 'beige', 'brwon',' blue', 'navy', 'purple', 'green', 'red', 'orange', 'yellow', 'pink']

def get_cloth_data():
    number = [get_cloth_count(kategorie) for kategorie in kategorie_data]
    print(number)
    n = 1
    # test = 0
    for idx,kategorie in enumerate(kategorie_data):
        for i in range(number[idx]):
            result = requests.get(f"https://www.shopbop.com/sale-clothing-{kategorie}/br/v=1/{kategorie_data[kategorie][0]}.htm?baseIndex={i*100}")
            # Check for 200 OK response
            src = result.content
            soup = BeautifulSoup(src, 'lxml')
            ul = soup.find("ul", {'class': 'products'})
            for li in ul.find_all("li"):
                # print(li.find('div', class_='title').get_text().strip(), end=" ")
                # print(li.find('div', class_='title').get_text().strip(), end=" ")
                # print(li.find('span', class_='sale-price-low').get_text().strip())
                _brand = li.find('div', class_='brand').get_text().strip()
                _name = li.find('div', class_='title').get_text().strip().replace('/', '')
                _price = li.find('span', class_='retail-price').get_text().strip().split("$")[1].replace(',','')
                _sale_price = li.find('span', class_='sale-price-low').get_text().strip().split("$")[1].replace(',','')
                _thumnail = li.find('span', class_='productBrowseMainImage').find('img')['src'].strip()
                _url = f"https://www.shopbop.com/{li.find('a')['href']}"
                _feature = kategorie_data[kategorie][1]
                _color = random.choice(color_data)
                print(_price,_sale_price)
                _discount_rate = 100 - (int((float(_sale_price) / float(_price)) * 100))
                # 이미지 다운로드
                # urllib.request.urlretrieve(img, f"static/{kategorie}/{title}.jpg") # 이미지 다운로드
                # print(f"{n}/{number} 다운로드 중")
                n += 1
                Product(name = _name, brand = _brand, price = float(_price), sale_price = float(_sale_price), discount_rate= _discount_rate, url= _url, thumnail = _thumnail, category = _feature, color = _color).save()

def get_cloth_count(kategorie):
    result = requests.get(f"https://www.shopbop.com/sale-clothing-{kategorie}/br/v=1/{kategorie_data[kategorie][0]}.htm")
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    number = soup.find("div", class_="results").get_text()
    pagination = int(number.split()[0]) // 100 + 1
    return pagination

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
                price = int(re.findall("\d+", price.replace(",", ""))[0]) * 1600
                original_price = product.find(
                    "span", {"data-testid": "initialPrice"}
                ).get_text()
                original_price = int(re.findall("\d+", original_price.replace(",", ""))[0]) * 1600
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
    get_cloth_data()
    