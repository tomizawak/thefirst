import requests
from html.parser import HTMLParser

class RakutenParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("タグ開始:", tag)

    def handle_endtag(self, tag):
        print("タグ終了 :", tag)

    def handle_data(self, data):
        print("その他データ :", data)


if __name__ == "__main__":
 
    url = "https://www.rakuten-sec.co.jp/web/fx/RateData/SwapData.dat"
    r = requests.get(url)
    
    parser = RakutenParser()
    parser.feed('<title>タイトル</title>'
            '<h1>見出し1</h1>')
    
    