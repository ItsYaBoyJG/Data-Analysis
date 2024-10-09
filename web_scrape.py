from bs4 import BeautifulSoup
from urllib.request import urlopen


url = "https://weather.com/weather/today/l/17057"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")


print(soup.get_text())
