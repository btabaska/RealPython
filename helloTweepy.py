import tweepy

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

# Create a Tweet
#api.update_status("Hello Tweepy")

def printTimeline():
    #Print the author and text of the last tweets in timeline
    timeline = api.home_timeline()
    for tweet in timeline:
        print(f"{tweet.user.name} said {tweet.text}\n\n")

def updateStatus():
    api.update_status("Test tweet from Tweepy Python")

def userInformation():
    user = api.get_user("MikezGarcia")
    print("User details:")
    print(user.name)
    print(user.description)
    print(user.location)
    print("Last 20 Followers:")
    for follower in user.followers():
        print(follower.name)

def followUser():
    api.create_friendship("realpython")

def updateProfile():
    api.update_profile(description="I like Python")

def likeTweet():
    tweets = api.home_timeline(count=1)
    tweet = tweets[0]
    print(f"Liking tweet {tweet.id} {tweet.text} of {tweet.author.name}")
    api.create_favorite(tweet.id)

def seeBlocked():
    for block in api.blocks():
        print(block.name)

def searchTweet(searchterm):
    for tweet in api.search(q=searchterm, lang="en", rpp=10):
        print(f"{tweet.user.name}:{tweet.text}\n")

def trendsByLocation():
    trends_result = api.trends_place(90036018)
    for trend in trends_result[0]["trends"]:
        print(trend["name"])

def availableTrendLocations():
    trend_locations = api.trends_available()
    for trend in trend_locations:
        print(trend)
        print("\n")

