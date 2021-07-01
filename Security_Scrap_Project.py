import newspaper
import nltk
from newspaper import Article

def summerize_article(url):
    article = Article(url)

    article.download()
    article.parse()

    nltk.download('punkt')
    nltk.nlp()
#
#     print("Author" + str(article.authors) )
#
#     date = article.publish_date
#     print("Publish Date" + str(article.publish_date))
#
# summerize_article("https://www.sans.org/blog/top-5-ics-incident-response-tabletops-and-how-to-run-them/")
#
# # from bs4 import BeautifulSoup as soup
# # import  requests
# # import sys
# #
# # from datetime import date
# # today = date.today()
# # d = today.strftime('%m-%d-%y')
# # print('date =', d)
