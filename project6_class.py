import requests
from bs4 import BeautifulSoup

class WebDownloader:
    def __init__(self, url):
        self.url = url
        self.html = None

    def fetch(self):
        response = requests.get(self.url)
        response.encoding = "utf-8"
        self.html = response.text
        return self.html

    def get_title(self):
        if self.html is None:
            self.fetch()
        soup = BeautifulSoup(self.html, "html.parser")
        return soup.title.string

    def get_links(self):
        if self.html is None:
            self.fetch()
        soup = BeautifulSoup(self.html, "html.parser")
        all_a = soup.find_all("a")
        # 这一行是一个“列表推导式”，意思是：把所有 <a> 标签里的 href 拿出来，如果它存在的话
        links = [a.get("href") for a in all_a if a.get("href")]
        return links

# ---- 使用这个类 ----
downloader = WebDownloader("https://www.baidu.com")

# 1. 打印标题
print("标题:", downloader.get_title())

# 2. 打印前 5 个链接
all_links = downloader.get_links()
print("前 5 个链接:")
for link in all_links[:5]:
    print(link)