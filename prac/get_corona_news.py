import requests
import re
from bs4 import BeautifulSoup

def get_corona_news(prev_titles, cnt):
    # get news
    URL = f"https://search.naver.com/search.naver?where=news&query=%EC%BD%94%EB%A1%9C%EB%82%98+%22%EA%B5%AD%EB%B0%A9%EB%B6%80%22+%2B%ED%99%95%EC%A7%84&sm=tab_arf&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=&mynews=0&refresh_start=1&related=0&refresh_cnt={cnt}"

    headers = {"User-Agent":"mozilla/5.0 (windows nt 10.0; win64; x64; rv:80.0) gecko/20100101 firefox/80.0"}
    res = requests.get(URL, headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, 'lxml')
    
    # return news if different with previous get result
    curr_titles = prev_titles
    new_articles = []

    curr_articles = soup.find("ul", attrs={"class": "type01"})
    curr_articles = curr_articles.find_all("li", attrs={"id":re.compile("^sp_nws")})
    for curr_article in curr_articles:
        title = curr_article.find("a", attrs={"class": "_sp_each_title"})["title"]
        if title not in prev_titles:
            new_articles.append(curr_article)
            curr_titles.append(title)
    
    return new_articles, curr_titles
            

    

                   
    

    