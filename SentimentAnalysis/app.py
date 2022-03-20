

import tweepy

auth = tweepy.OAuth1UserHandler(
   "yCNiXLDzpkAmcDlX0J3TgWEbP", "nftIllHjeJbUNonzCFhPOV4JaKCy6GXn2IHeqYDSCABKItAltz", 
   "1683252618-Xvu4ARYu6wp4jaEejhXoBngcU3VPuC2DGOGQc8y", "xzVh1UhtlbAJ1UG1sfSb32Q0q8OshyjuAJQsjz0rRFbVQ"
)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)