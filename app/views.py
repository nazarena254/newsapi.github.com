from app import app
from flask import Flask,render_template
from .request import businessArticles, entArticles, get_news_source, healthArticles, publishedArticles, randomArticles, scienceArticles, sportArticles, techArticles, topHeadlines

# we write the code that will handle users requests.
@app.route('/')
def home():
    articles = publishedArticles()
    return  render_template('home.html', articles = articles)