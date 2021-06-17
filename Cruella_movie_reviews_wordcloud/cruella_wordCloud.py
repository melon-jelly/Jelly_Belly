from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()


text = open(path.join(d, '../크루엘라리뷰.csv'), encoding="utf-8").read()
cruella_coloring = np.array(Image.open(path.join(d, "../cruella_color.png")))

from matplotlib import rc
rc('font',family='NanumGothic')

wc = WordCloud('../data/a가위손M.ttf',
               background_color="black",
               max_words=2000,
               mask=cruella_coloring,
               stopwords = ["진짜", "그냥","없다","더", "영화","정말","이","굳이","잘","레알","ㅠ"\
                               ,"안","않는다","더구나","일단","이거","ㄹㅇ","그리고","다시","다","엠마","ㅎㅎ"\
                               ,"본","와","두","수"],
               max_font_size=40,
               random_state=42,
               relative_scaling=0.5
               )

wc.generate(text)
image_colors = ImageColorGenerator(cruella_coloring)

plt.figure(figsize=(12,12))
plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis("off")