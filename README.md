# Scrape a subreddit for videos

## Set up

Install praw using pip
```bash
pip install praw
```

Change 'Your subreddit here' in scrap.py to the subreddit you want

Go to reddit and create a new app: https://www.reddit.com/prefs/apps/
Change it to a script, and set the redirect uri to http://localhost:8080

Create a setUp.py that looks something similar to this:
Replace the clientId, clientSecret, password and username

```bash
import praw
def setUp():
	clientId = 'your client id'
	clientSecret = 'your client secret'
	raw = praw.Reddit(user_agent='You',
	                  client_id=clientId,
	                  client_secret=clientSecret,
	                  password = "redditpassword",
	                  username = 'redditusername')
	return raw
```

## Usage

Run the scrap.py
It'll attempt to scrape all possible reddit videos from the subreddit (currently set to nothing)