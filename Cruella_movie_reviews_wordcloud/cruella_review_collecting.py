from urllib.request import urlopen
from bs4 import BeautifulSoup

count = 0
comments = []
basic_url = "https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=187322&target=after&page="

for i in range(1, 51):
    url = basic_url + str(i)
    page = urlopen(url)
    soup = BeautifulSoup(page, "html.parser")

    comment_all = soup.find_all('td', class_='title')

    for comment in comment_all:
        temp = list(comment.children)
        count += 1
        result = temp[6].strip()
        comments.append(result)

import pandas as pd
dict_doc = {"text": comments}
doc = pd.DataFrame(dict_doc)
doc.to_csv("크루엘라리뷰.csv", index = False)
doc