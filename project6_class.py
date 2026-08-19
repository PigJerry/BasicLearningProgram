import requests
from bs4 import BeautifulSoup

class WebDownloader:
    def __init__(self, url):
        self.url = url
        self.html = None

    def fetch (self):
        response = requests.get(self.url)
        response.encoding = "utf-8"
        self.html = response.text
        return self.html

    def get_title(self):
        if self.html is None:
            self.fetch()
        soup = BeautifulSoup(self.html, "html.parser")
        return soup.title.string

Downloader = WebDownloader("https://www.baidu.com")
print(Downloader.get_title())
