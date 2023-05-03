# Femicide Scraper

This is the first version of the web scraper for the Femicide project. 

It is deployed on Heroku and pushes the data to ElephantSQL - a cloud PostgreSQL database.

To run, open the terminal in the root folder of this project and type:

´´´
$ python3 app.py 
´´´

This will start the scrape and send the results to the cloud database.

# Things to note

The body of the article is not always available because the headline is sometimes linking to a living timeline, rather than an article. I'll see if this can be fixed, so the headline is always a story - maybe it isn't though.

