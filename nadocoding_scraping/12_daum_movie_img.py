import requests
from bs4 import BeautifulSoup

# get movie images
for year in range(2019, 2014, -1):
    URL = f"https://search.daum.net/search?w=tot&q={year}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
    
    res = requests.get(URL)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, 'lxml')
    images = soup.find_all("img", attrs={'class': "thumb_img"})
    
    for i, image in enumerate(images):
        src = image["src"]
        if src.startswith('//'):
            img_URL = "https:" + src
            res_img = requests.get(img_URL)
            res_img.raise_for_status()

            with open(f"img/movie_{year}_{i+1}.jpg", 'wb') as f:
                f.write(res_img.content)
        if i == 4: 
            break