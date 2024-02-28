from Osaka.api import Twitter_API

twitter_api = Twitter_API(
    api_key="03d7f2d9ccmsha129b9e62cdf9fap153f12jsn0c736f818bc6",
    api_host="twitter154.p.rapidapi.com",
)
# call data hastag
hastag_twitter = twitter_api.hashtag(hashtag="#Prabowo-Gibran", limit=20)
print(hastag_twitter.head(5))
hastag_twitter.to_csv("hastag_twitter.csv")
