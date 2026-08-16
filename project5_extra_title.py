import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.baidu.com")
response.encoding = "utf-8"

soup = BeautifulSoup(response.text, "html.parser")

title = soup.title.string

print("网页标题是：", title)