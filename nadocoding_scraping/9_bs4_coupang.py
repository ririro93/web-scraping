import requests
from bs4 import BeautifulSoup

############# 아마 파이썬 버전 업그레이드 해야되는듯!
URL = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&eventCategory=SRP&sorter=scoreDesc&listSize=36&isPriceRange=false&rating=0&page=1"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0", 
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
"Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3",
"Accept-Encoding": "gzip, deflate, br", 
"Referer": "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=2&rocketAll=false&searchIndexingToken=1=4&backgroundColor=", 
"Connection": "keep-alive", 
"Upgrade-Insecure-Requests": "1",
"Cache-Control": "max-age=0",
"TE": "Trailers"}

res = requests.get(URL, headers=headers)
res.raise_for_status()

print(res.text)
# soup = BeautifulSoup(res.text, 'lxml')
# print(soup)