import requests
from bs4 import BeautifulSoup

URL = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(URL)
res.raise_for_status()

with open("naver_webtoon.html", 'w', encoding='utf8') as f:
    f.write(res.text)
    

soup = BeautifulSoup(res.text, 'lxml')
rank01 = soup.find(attrs={"class":"rank01"})
rankings = [rank01] + rank01.find_next_siblings('li')

for i, rank in enumerate(rankings):
    print(i+1, "등: ", rank.find("a").text)

