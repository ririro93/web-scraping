import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/"
res = requests.get(url)
res.raise_for_status()

# res.text 라는 내용을 lxml parser 를 통해서 BeautifulSoup라는 객체로 만든것
soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a)
# print(soup.a.attrs) # a element의 속성 정보 출력
# print(soup.a["class"]) # a element 의 class 속성 '값' 정보를 출력

print(soup.find("a", attrs = {"class": "grid--cell ml8 sm:ml0 sm:mt8 fc-white d:fc-black-900 bg-orange-400 py12 px24 bar-sm js-scroll-link js-gps-track"})) # 처음으로 이런 값을 갖는 element 를 가져올 수 있음

# next_sibling, previous_sibling, parent, find_next_sibling("li"), find_next_siblings("li") 다됨