import requests
import pandas as pd
from bs4 import BeautifulSoup

html=requests.get("https://www.rakuten-sec.co.jp/web/fx/RateData/SwapData.dat").text
soup=BeautifulSoup(html,"html.parser")
print(soup.prettify)



