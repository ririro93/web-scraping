import csv
import requests
from bs4 import BeautifulSoup

URL = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

FILENAME = "COSPI1-200.csv"

# encoding을 저렇게 하면 excel 에서 한글이 안깨짐
f = open(FILENAME, 'w', encoding='utf-8-sig', newline="") # newline 없으면 개행 이상해짐
writer = csv.writer(f)

for page in range(1, 5):
    res = requests.get(URL+str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')
    
    # 항목명 추가 
    if page == 1:
        heads = soup.find("thead").tr.find_all("th")
        heads_data = [head.get_text() for head in heads][:-1]
        writer.writerow(heads_data)
        print(heads_data)
    
    data_rows = soup.find("table", attrs={"class": "type_2"}).find("tbody").find_all("tr")
    
    for row in data_rows:
        cols = row.find_all("td")
        if len(cols) <= 1:
            continue
        data = [col.get_text().strip() for col in cols]
        writer.writerow(data)