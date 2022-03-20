import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("qkwnE4vowlKsHX0C3cogh8umD", 
    "HVC35mHAKomL2uJs7NYKcjcjVowu2Rnv8X1RzgadqhsNWtQz6n")
auth.set_access_token("1683252618-bPpnrFb1uutWLGvQbLvS6X4l0UcpND8ZWJy7EGC", 
    "0uJrTlNqza9NopJOekA2TX3T9kqBNmswgPZNJ93xLwgAm")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")
