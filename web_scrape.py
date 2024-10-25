from bs4 import BeautifulSoup
import pandas as pd
from urllib.request import urlopen
import re


url = "https://www.nfl.com/stats/team-stats/"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

team_names = soup.find_all("div", class_="d3-o-club-info")

print(team_names)


