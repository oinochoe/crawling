import requests

from bs4 import BeautifulSoup

source = requests.get("https://search.naver.com/search.naver").text
soup = BeautifulSoup(source, "html.parser")
hotKeys = soup.select("span.tit")


index = 0
for key in hotKeys:
    index += 1
    print(str(index) + ", " + key.text)
    if index >= 20:
        break