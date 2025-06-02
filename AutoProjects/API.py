## 06d21d403c344faaa0d60a56fe001ef9
import requests

r = requests.get("https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2025-5-27&to=2025-5-30&sortBy=popularity&language=en&apiKey=06d21d403c344faaa0d60a56fe001ef9")


def get_news(topic, from_date, to_date, language='en', api_key='06d21d403c344faaa0d60a56fe001ef9'):
    url = f'https://newsapi.org/v2/everything?qInTitle={topic}%20market&from={from_date}&to={to_date}&sortBy=popularity&language={language}&apiKey={api_key}'
    
    r = requests.get(url)
    content = r.json()
    articles = content['articles']

    #print(type(articles))
    results = []
    for article in articles:
        # print(f"Title\n, {article['title']}, \nDescription\n, {article['description']}")
        results.append(f"Title\n, {article['title']}, \nDescription\n, {article['description']}")
    return results

print(get_news(topic='stock', from_date='2025-5-30', to_date='2025-5-31'))

