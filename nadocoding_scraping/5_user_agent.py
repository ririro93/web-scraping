import requests

url = "https://nadocoding.tistory.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0"}
res = requests.get(url, headers=headers)
res = requests.get(url)

res.raise_for_status() # 문제 있으면 바로 코드 종료 됨
# 이거 에러 핸들링 안하면 파일 생기긴 하는데 문자 깨짐
with open("nadocoding1.html", "w", encoding="utf8") as f:
    f.write(res.text)
