import requests  # HTMLファイルを取得するためのライブラリ
from bs4 import BeautifulSoup  # HTMLファイルを解析するためのライブラリ

# Yahoo!ニュースのランキングページから、タイトルの順位順のリストを取得する
def fetch_news_titles():
    # HTMLファイルを取得
    response = requests.get("https://news.yahoo.co.jp/ranking/access/news")
    response.raise_for_status()
    # HTMLファイルを解析
    soup = BeautifulSoup(response.text, "html.parser")
    # CSSセレクタでクラスが"newsFeed_item_title"の要素を取得
    news_titles = soup.find_all(class_="newsFeed_item_title")
    return [news_title.get_text() for news_title in news_titles]

news_titles = fetch_news_titles()
for i, title in enumerate(news_titles):
    print(f"{i + 1}位: {title}")
