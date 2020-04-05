from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("タグ開始:", tag)

    def handle_endtag(self, tag):
        print("タグ終了 :", tag)

    def handle_data(self, data):
        print("その他データ :", data)

parser = MyHTMLParser()
parser.feed('<title>タイトル</title>'
            '<h1>見出し</h1>')
