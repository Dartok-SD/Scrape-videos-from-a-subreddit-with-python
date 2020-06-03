import setUp
import time
from urllib.request import urlretrieve
reddit = setUp.setUp()
# Change the subreddit you want
posts = reddit.subreddit('Your subreddit here').top(limit=None)
vids = []
for hot in posts:
    time.sleep(1)
    if(hot.secure_media != None):
        try:
            url = hot.media['reddit_video']['fallback_url']
            url = url.split("?")[0]
            name = hot.title + ".mp4"
            vids.append((url, name))
            urlretrieve(url,name)
        except:
            pass
    elif(hot.url != None and hot.url[0:9] == "https://v"):
        try:
            urlretrieve(hot.url+"/DASH_720",hot.title+".mp4")
        except:
            try:
                urlretrieve(hot.url+"/DASH_480",hot.title+".mp4")
            except:
                pass
