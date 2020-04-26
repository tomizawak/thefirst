import requests
from bs4 import BeautifulSoup

def text_organizer(swap_text):
    print(swap_text)

if __name__ == "__main__":
    html=requests.get("https://www.rakuten-sec.co.jp/web/fx/RateData/SwapData.dat").text
    soup=BeautifulSoup(html,"html.parser")

    swap_text = soup.prettify
   
