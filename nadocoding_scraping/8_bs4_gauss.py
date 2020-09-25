import requests
from pprint import pprint
from bs4 import BeautifulSoup

URL = "https://comic.naver.com/webtoon/list.nhn?titleId=675554"
res = requests.get(URL)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

# 제목, 링크 구하기
cartoons = soup.find_all("td", attrs={"class":"title"})
for cartoon in cartoons:
    title = cartoon.a.get_text()
    link = "https://comic.naver.com" + cartoon.a["href"]
    # rating = cartoon.find_next_sibling("td").div.strong.get_text()
    print(title, link)

    
# 평점 구하기
cartoon_ratings = soup.find_all("div", attrs={"class":"rating_type"})
for cartoon_rating in cartoon_ratings:
    rating = cartoon_rating.find("strong").get_text()
    print(rating)
