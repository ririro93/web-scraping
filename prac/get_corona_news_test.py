import requests
import re
from bs4 import BeautifulSoup

# get news
cnt = 1
URL = f"https://search.naver.com/search.naver?where=news&query=%EC%BD%94%EB%A1%9C%EB%82%98+%22%EA%B5%AD%EB%B0%A9%EB%B6%80%22+%2B%ED%99%95%EC%A7%84&sm=tab_arf&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=&mynews=0&refresh_start=1&related=0&refresh_cnt={cnt}"

headers = {"User-Agent":"mozilla/5.0 (windows nt 10.0; win64; x64; rv:80.0) gecko/20100101 firefox/80.0"}
res = requests.get(URL, headers=headers)
res.raise_for_status()

# return news if different with previous get result
soup = BeautifulSoup(res.text, 'lxml')

curr_articles = soup.find("ul", attrs={"class": "type01"}).find_all("li", attrs={"id":re.compile("^sp_nws")})
for curr_article in curr_articles:
    title = curr_article.find("a", attrs={"class": "_sp_each_title"})
    print(title['title'])
