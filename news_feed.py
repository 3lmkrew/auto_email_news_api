# Get top-headline new's articles

import requests


class NewsFeed:
    """ Creates a news feed object that holds API key, URL and requires interest parameter"""
    api_key = "7d0cf35cf6cc4dbeaad6ef23f2238f3b"
    url = f"https://newsapi.org/v2/top-headlines?"

    def __init__(self, interest, message=""):
        self.interest = interest
        self.message = message

    def get(self):
        parameters = {"q": self.interest, "searchIn": "title", "sortBy": "publishedAt", "language": "en",
                      "apikey": NewsFeed.api_key}
        response = requests.get(url=NewsFeed.url, params=parameters)
        content = response.json()
        articles = content["articles"]
        try:
            for data in articles:
                titles = data["title"]
                links = data["url"]
                self.message += f"{titles} \n\n {links}\n\n"
            return self.message

        except IndexError:
            print("No Articles Found.")