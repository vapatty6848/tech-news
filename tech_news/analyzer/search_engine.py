from tech_news.database import search_news
import datetime


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    titles = search_news({"title": {"$regex": title, "$options": "i"}})

    if titles:
        for title in titles:
            return [(title["title"], title["url"])]
    else:
        return []


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
        news_date = search_news({"timestamp": {"$regex": date}})
        if news_date:
            for new in news_date:
                return [(new["title"], new["url"])]
        else:
            return []
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
