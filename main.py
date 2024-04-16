import requests as req  # HTMLファイルを取得するためのライブラリ
from bs4 import BeautifulSoup as bs  # HTMLファイルを解析するためのライブラリ

url = "https://news.yahoo.co.jp/ranking/access/news"  # Yahoo!ニュースのランキングページのURL

response = req.get(url)  # Yahoo!ニュースのランキングページのHTMLファイルを取得
if response.status_code == 200:  # HTTPステータスコードが200(成功)の場合
    soup = bs(response.text, "html.parser")  # HTMLファイルを解析
    news_titles = soup.find_all(
        class_="newsFeed_item_title"
    )  # CSSセレクタでクラスが"newsFeed_item_title"の要素を取得
    news_titles = [
        news_title.get_text() for news_title in news_titles 
    ]  # ニュースのタイトルをリストに格納
    for i in range(len(news_titles)):
        news_titles[i] = (
            str(i + 1) + "位: " + news_titles[i]
        )  # ニュースのタイトルに順位を付与
    for news_title in news_titles:
        print(news_title)

else:
    print("HTMLファイルの取得に失敗しました。")
