from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import requests
import pandas as pd
import time


URL = 'https://www.scrapethissite.com/pages/forms/'

BASE_HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
                "Accept": 
                    "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Accept-Langauge": "en-US",
                "Accept-Encoding": "gzip,deflate,br,zstd"
                }

page = requests.get(URL)
html = page.content
soup = BeautifulSoup(html, "html.parser")


table = soup.find("table",class_="table")


def remove_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '',text)
    


columns = soup.find_all('th')

titles = ()

for i in columns:
    x = remove_html_tags(str(i))
    l = list(titles)
    if x != "None":
        t = x.replace('\n', '')
        l.append(t)
        titles = tuple(l)
         
    
teams = soup.find_all('tr', class_="team")
    

df = pd.DataFrame(columns=['Team Name','Year','Wins','Losses','OT Losses','Win %','Goals For','Goals Against','+/-'])

for r in table.find_all('tr'):
     cols = r.find_all('td')
     
     
     if (cols != []):
         name = remove_html_tags(str(cols[0])).replace('\n','').replace(' ','')
         year = remove_html_tags(str(cols[1])).replace('\n','')
         wins = remove_html_tags(str(cols[2])).replace('\n','')
         losses = remove_html_tags(str(cols[3])).replace('\n','')
         ot = remove_html_tags(str(cols[4])).replace('\n','')
         winPerc = remove_html_tags(str(cols[5])).replace('\n','')
         gf = remove_html_tags(str(cols[6])).replace('\n','')
         ga = remove_html_tags(str(cols[7])).replace('\n','')
         over_under = remove_html_tags(str(cols[8])).replace('\n','')
         
         df = pd.concat([df, pd.DataFrame.from_records([{'Team Name': name, 'Year': year, 'Wins': wins, 'Losses': losses, 'OT Losses': ot, 'Win %': winPerc, 'Goals For': gf, 'Goals Against': ga, '+/-':over_under}])], ignore_index=True)
         
         


#df.to_csv('test.csv')


new = df[(df['Win %'].astype(float) >= 0.50).all()]