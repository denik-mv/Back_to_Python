import requests
from bs4 import BeautifulSoup

url = "https://int.soccerway.com/national/argentina/argentino-a/2022/north/r68086/"

agent = {"User-Agent": "Mozilla/5.0"}
req = requests.get(url, headers=agent)
# src = req.text
# print(src)

with open("index.html", "w") as file:
    file.write(req.content)
