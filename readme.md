# Create a Security Newspaper Content Aggregator

import newspaper
import nltk
from newspaper import Article

def summerize_article(url):
    article = Article(url)

    article.download()
    article.parse()

    nltk.download('punkt')
    nltk.nlp()
