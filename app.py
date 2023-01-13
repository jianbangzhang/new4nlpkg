## 用Article爬取单条新闻
from newspaper import Article
# 目标新闻网址
url = 'https://news.southcn.com/node_179d29f1ce/8a88e7d28f.shtml'
news = Article(url, language='zh')
news.download()        # 加载网页
news.parse()           # 解析网页
print('题目：\n',news.title)       # 新闻题目
print('正文：\n',news.text)      # 正文内容


print(news.top_image) # 配图地址
print(news.movies)    # 视频地址
print(news.publish_date) # 发布日期
print(news.html)      # 网页源代码