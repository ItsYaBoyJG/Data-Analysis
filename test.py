from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import requests


URL = 'https://www.scrapethissite.com/pages/forms/'

BASE_HEADERS = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
                "accept": 
                    "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "accept-langauge": "en-US",
                "accept-encoding": "gzip,deflate,br,zstd"
                }

page = requests.get(URL)
html = page.content
soup = BeautifulSoup(html, "html.parser")

table = soup.find("table",class_="table")


def remove_html_tags(text):
    clean = re.compile('<.*?>')
    print(re.sub(clean, '',text))
    #return re.sub(clean, '',text)


columns = soup.find_all('th')

titles = ()

for i in columns:
    x = remove_html_tags(str(i))
    l = list(titles)
    if i != "None":
        l.append(x)
        

print(titles)
    
    
    
    
    


#for t in soup.find_all('table'):