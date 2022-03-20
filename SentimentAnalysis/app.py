import tweepy

client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAALe2aQEAAAAA90C5FoIsZ%2BUS9iU1q4AHo4AApnw%3DOoZPqcsyR1qFEi9oH51Es3lkngN3wegmyY00LIB3KQOUme4nJv')

# Replace with your own search query
query = 'from:suhemparack -is:retweet'

tweets = client.search_all_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], max_results=100)

for tweet in tweets.data:
    print(tweet.text)
    if len(tweet.context_annotations) > 0:
        print(tweet.context_annotations)