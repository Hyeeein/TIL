from wordcloud import WordCloud
import json

# word cloud 설치
# pip install wordcloud
# conda install -c conda-forge wordcloud

# word-cloud는 한글을 표시하지 못함 그래서 cloud에 font_path 추가해주기
cloud = WordCloud(font_path='Goyang.ttf', background_color='white', max_words=30, width=400, height=300)

with open('webtoons.json', encoding='utf-8') as f:
    webtoons = json.load(f)

# print(webtoons)
res = dict()
for webtoon in webtoons['webtoons']:
    res[webtoon['title']] = int(float(webtoon['star']) * 100)

visual = cloud.fit_words(res)
visual.to_image()
visual.to_file('cloud01.png')

