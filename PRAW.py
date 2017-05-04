import praw

reddit = praw.Reddit('bot1')
sub = raw_input("Enter Subreddit Name: ")
subreddit = reddit.subreddit(sub)

for submission in subreddit.hot(limit=5):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------------------------------\n")
