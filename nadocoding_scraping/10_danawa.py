import requests
import re
from bs4 import BeautifulSoup

URL = "http://prod.danawa.com/list/?cate=11337803&searchOption=/innerSearchKeyword="
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0"}

res = requests.get(URL, headers=headers)
res.raise_for_status()

# with open("danawa.html", 'w', encoding="utf8") as f:
#     f.write(res.text)

soup = BeautifulSoup(res.text, 'lxml')

products = soup.find_all("li", attrs={"class":re.compile("^prod_item")})
print(products[0])