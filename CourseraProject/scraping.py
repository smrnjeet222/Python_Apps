from urllib import request
from bs4 import BeautifulSoup

html = request.urlopen(
    'http://py4e-data.dr-chuck.net/comments_829839.html').read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('span')
sum = 0
for tag in tags:
    sum = sum+int(tag.contents[0])
print(sum)
