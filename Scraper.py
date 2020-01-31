import html2text
import requests
from bs4 import BeautifulSoup
import string
import newspaper
from newspaper import Article
import datetime
from datetime import timezone
from newspaper import news_pool

class Scraper ():
    def __init__(self, companies):
        self.companies = companies
    def parseArticle (self, url):
        article = Article(url)
        article.download()
        article.parse()
        text = article.text.replace("\n", " ").split(" ")
        cleanText = list(filter (lambda x: len(x) != 0, text))
        return cleanText

    def getArticleLinks(self, url):
        paper = newspaper.build(url, memoize_articles=False)
        paper.articles = paper.articles[:100]
        #news_pool.set([paper], threads_per_source = 2)
        #news_pool.join()
        today = datetime.datetime.now()
        today = today.replace(tzinfo=None)
        recentArticles = []
        headlines = []
        for article in paper.articles:
            article.download()
            article.parse()
            publication = article.publish_date
            if publication != None:
                publication = publication.replace(tzinfo=None)
                distance = today - publication
                if distance.days < 8:
                    recentArticles += [article]
                    headlines += [article.title]
        self.recentArticles = recentArticles
        self.headlines = headlines

    def filterByCompany(self):
        tracker = []
        for company in self.companies:
            counter = 0
            for headline in self.headlines:
                if company in headline:
                    counter += 1
            tracker += [[company, counter]]
        tracker.sort(key = lambda x: -x[1])
        return tracker[:5]

    def findRelatedArticles(self, company):
        self.relatedArticles = []
        self.relatedHeadlines = []
        for index in range (0, len(self.headlines)):
            headline = self.headlines[index]
            if (company in headline):
                self.relatedArticles += [self.recentArticles[index]]
                self.relatedHeadlines += [self.headlines[index]]
        return self.relatedHeadlines

            



        



