from difflib import restore
from venv import create
from requests import get
import random
import psycopg2
from bs4 import BeautifulSoup
import database
import requests
import datetime

db_url = "postgres://oxbvadmp:r5tJzuWI1-7XXKq1noJPVsoxFSQNfjG-@rogue.db.elephantsql.com/oxbvadmp"


fail = "Error - failed to scrape the text of this article from " 


papers = [
    [1, "https://www.mirror.co.uk/", "The Daily Mirror", "h2", "story__title"],
    [2, "https://www.theguardian.com/uk", "The Guardian", "span", "js-headline-text"],
    [3, "https://www.thesun.co.uk/", "The Sun", "p", "teaser__subdeck"],
    [4, "https://www.ft.com/world/uk", "The Financial Times", "div", "o-teaser__heading"],
    [5, "https://www.dailymail.co.uk/home/index.html", "The Daily Mail", "h2", "linkro-darkred"],
    [6, "https://www.thetimes.co.uk/", "The Times", "h3", "Headline--xl"]

]
scrape_results = []


def scrapeHeadlines():

    connection = psycopg2.connect(db_url)


    randomUrls = [ 
    "https://www.facebook.com/", 
    "https://www.google.co.uk", 
    "https://www.twitter.com"
    ]

    headers = {
        'User-Agent': 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
        'Referer': random.choice(randomUrls) 
        }

    fail = "Sorry but we could not get the headline for " + str(paper[2])
    timestamp = '{:%b-%d-%Y %H:%M:%S}'.format(datetime.datetime.now())
    id = paper[0]
    url = paper[1]
    newspaper = paper[2]

    results = requests.get(url, headers=headers)
    soup = BeautifulSoup(results.text, "html.parser")
    headline_html = soup.find(paper[3], class_=paper[4])

    if headline_html != None:
      headline = headline_html.text.strip()
    else:
      headline = fail 

    database.create_tables(connection)

    database.add_headline(connection, headline, url, newspaper, timestamp)
    
    # scrape_results.append({
    #                 'id': id,
    #                 'paper': newspaper,
    #                 'headline': headline
    #                 })



for paper in papers:
    scrapeHeadlines()

print(scrape_results)
