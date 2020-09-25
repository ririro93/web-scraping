import requests
from bs4 import BeautifulSoup

URL = "https://search.daum.net/search?w=tot&q=2019%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"

res = requests.get(URL)
res.raise_for_status()

## saving html to a file
# with open("daum_movies.html", 'w', encoding='utf8') as f:
#     f.write(res.text)
    
soup = BeautifulSoup(res.text, 'lxml')

# get movies info
items = soup.find_all("div", attrs={"class": "wrap_cont cont_type2"})

for i, item in enumerate(items):
    rank = i+1
    title = item.find('a', attrs={"class": "tit_main"}).get_text()
    rate = item.find('em', attrs={"class": "rate"}).get_text()
    rate_cnt = item.find('a', attrs={"class": "link_count"}).get_text()
    print("//////////////////////////////")
    print(f"{rank}위")
    print(f"제목 : {title}")
    print(f"평점 : {rate}")
    print(f"{rate_cnt}")

