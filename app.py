#!/usr/bin/python3

from difflib import restore
from venv import create
import requests
from requests import get
import random
import psycopg2
from bs4 import BeautifulSoup
import database
from papers import papers
import datetime
import time
from pprint import pprint
import os
from dotenv import load_dotenv

load_dotenv()

MY_DB_URL = os.getenv('MY_DB_URL')

scrape_results = []

def scrapeHeadlines():

    connection = psycopg2.connect(MY_DB_URL)
    randomUrls = [ 
    "https://www.facebook.com/", 
    "https://www.google.co.uk", 
    "https://www.twitter.com"
    ]

    headers = {
        'User-Agent': 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
        'Referer': random.choice(randomUrls) 
        }

    fail = "Sorry but we cannot currently get the headline for " + str(paper[1])
    timestamp = '{:%b-%d-%Y %H:%M:%S}'.format(datetime.datetime.now())
    url = paper[0]
    newspaper = paper[1]
    paper_id = paper[4]
    css_name = paper[5]

    results = requests.get(url, headers=headers)
    soup = BeautifulSoup(results.text, "html.parser")


    if paper[5] == "indy":
      headline_html = soup.findAll('h2')[3]
    else:
      headline_html = soup.find(paper[2], class_=paper[3])

    if (headline_html != None or headline_html != ""):
      headline = headline_html.text.strip()
    else:
      headline = fail 

    database.create_tables(connection)
    database.add_headline(connection, headline, url, newspaper, timestamp, paper_id, css_name)
    
    # this is just to print out stuff in the terminal
    scrape_results.append({
                    'paper': newspaper,
                    'headline': headline,
                    'css name': css_name
                    })

for paper in papers:
  scrapeHeadlines()

# pprint(scrape_results)
