#Twitter Application Tweeter
#By NeverLand
#MODIFY THIS TO SHOW TWEET
tweet = "Tweeting this from the tech shop. I guess the fridge is nice"
apikey = ""
apikeysecret = ""
#THIS IS CUSTOMER KEY / ACCESS KEY
accesskey = ""
accesskey_secret = ""
#DO NOT MODIFY THIS IF YOU DON'T KNOW WHAT YOU ARE DOING
import tweepy
print("TWITTER APPLICATION TWEETER BY NEVERLAND")
print("WELCOME")
print("")
twitterapiauth = tweepy.OAuthHandler(apikey, apikeysecret)
twitterapiauth.set_access_token(accesskey, accesskey_secret)

twitterapi = tweepy.API(twitterapiauth)
print("Attempting crendentials:")
try:
    twitterapi.verify_credentials()
    print("Success! Your crendentials work.")
except:
    print("Error during the authentication. Please check if your keys are right, or is Twitter down?")
print("")
print("Tweeting your tweet, the tweet is: " + tweet) 
print("")
twitterapi.update_status(tweet)
print("Successfully tweeted. Goodbye.")