from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')  # 创建对象
print(soup.prettify())  # 格式化输出

# 获取所有文字内容
print(soup.get_text)

# 获取title信息
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.parent.name)

# 获取p
print(soup.p)
print(soup.p['class'])

# 获取a
print(soup.a)
print(soup.a['class'])
print(soup.find(id="link3"))

# 找到所有a标签
for link in soup.find_all('a'):
    print(link)







