import numpy as np
import jieba
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
with open(r"H:\示例\第9章\影评.txt", "rb") as f:
    text = f.read()
words = jieba.cut(text)
wordstr = " ".join(words)
wordcloud = WordCloud(font_path='H:\示例\第9章\msyh.ttf', 
    mask=np.array(Image.open(r'H:\示例\第9章\background.png')),
    width=600, height=600, max_words=100, max_font_size=80,
    stopwords=set(STOPWORDS),scale=4,background_color='white')
wordcloud.generate(wordstr)
wordcloud.to_file(r'H:\示例\第9章\wordcloud.png')
