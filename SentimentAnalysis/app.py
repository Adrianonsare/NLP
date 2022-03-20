#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#bearer_token="AAAAAAAAAAAAAAAAAAAAALe2aQEAAAAA90C5FoIsZ%2BUS9iU1q4AHo4AApnw%3DOoZPqcsyR1qFEi9oH51Es3lkngN3wegmyY00LIB3KQOUme4nJv"
consumer_key="f7Bm3Zi4eiN4O7QGzE0O6j1yT"
consumer_secret="dAUBbArJ3f2zJqQlMpFTVuJ8mON31AylmnRbJ2vl8ZasG4m3MX"
access_token="1683252618-Jc28x9poY0WQlOwlhfIDYYcDducDjrAmg0rr8pm"
access_token_secret="MnT2x5GRrLq7bRllhmSFOwsy3NiYpP8wsHOGCU7Ui5RhZ"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

def on_data(self, data):
    print data
    return True

def on_error(self, status):
    print status


if __name__ == '__main__':

#This handles Twitter authetification and the connection to Twitter 
Streaming API
l = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, l)

#This line filter Twitter Streams to capture data by the keywords: 'python', 
'javascript', 'ruby'
stream.filter(track=['python', 'javascript', 'ruby'])