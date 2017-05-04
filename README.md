# redditmonitor
------------------------------------------------------------------NOTE------------------------------------------------------------------

In order to get the script to work, you will need to: import PRAW (Reddit's scraping libary), create a Reddit app, and edit praw.ini. First you will need to pip install Praw. Afterwards, go to https://www.reddit.com/prefs/apps/ and create an app. You will need to save the strings after "personal use script" (this is the client_id) and "secret" (this is the client_secret) for latter use. Then go to praw.ini, which is located in PythonXX\Lib\site-packages\praw\. Add the following:

[bot1]

client_id = XXXXXXXXXXXXXX

client_secret = XXXXXXXXXXXXXXXXXXXXXXXXXX

user_agent = PyEng Bot 0.1 #this is just a version number its not really needed


Afterwards, the script will run.


----------------------------------------------------------------CHANGELOG----------------------------------------------------------------

5/3/2017 - Added Reddit Scraper that scrapes for top 5 on r/funny

5/3/2017 - Allows user to input which subreddit they wish to scrape

5/3/2017 - Changed name of .py file to appropriate name
