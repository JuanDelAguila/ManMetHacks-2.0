from Scraper import Scraper
from Data import Data
from Sentiment import Sentiment
from newspaper import Article

def main():
    myData = Data()
    evaluate = Sentiment()
    companies = myData.getCompanies()
    myScraper = Scraper(companies)
    url = str(input("Input a newspaper url: "))
    #url = "https://www.marketwatch.com/"
    #url = "https://www.cnbc.com/investing/"
    #url = "https://www.ccn.com/"
    myScraper.getArticleLinks(url)
    occurances = myScraper.filterByCompany()
    occurances = occurances[:5]
    while True:
        for occurance in occurances:
            name = occurance[0]
            num = occurance[1]
            if num > 0:
                print (name + " has " + str(num) + " articles")
        company = str(input ("Which company are you interested in: "))
        headlines = myScraper.findRelatedArticles(company)
        
        print ("We found these articles from the past 7 days: ")
        i = 1
        for headline in headlines:
            print (str (i) + " - " + headline)
            i += 1
        interest = int (input ("Which article would you like to analyze? "))
        article = myScraper.relatedArticles[interest-1]
        cleanArticle = myScraper.parseArticle(article.url)
        print ("The stats of the article are: ")
        evaluate.rankSentenceScores(cleanArticle, myData.getBasicDictionary())

main()
