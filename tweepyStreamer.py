import json
import tweepy

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        print(f"{tweet.user.name}:{tweet.text}")

    def on_error(self, status):
        print("Error Detected")

# Authenticate to Twitter
auth = tweepy.OAuthHandler("EWbFluEMqxINBbEWkQZn3KtLi", "EjcYcD5A877z88z5Wq2LxuPK33a8K2ZSbBA2UhysYy8qZOz195")
auth.set_access_token("41739520-9n4lkPzxcEPXGLVtsBOtt9FY8RXGk9xuyNjCNhn5h", "m2I8kqzxS5GdzN6MCsWvk1ErQTZpEySvdhdtFgj53I7m3")

try:
    # Create API Object
    api = tweepy.API(auth, wait_on_rate_limit=True, 
        wait_on_rate_limit_notify=True)
    print("Authentication OK")
except:
    print("Error during Authentication")

tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
stream.filter(track=["Python", "Django", "Tweepy"], languages=["en"])