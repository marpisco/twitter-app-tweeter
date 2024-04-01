#------------------------------
# X (formely Twitter) Application Poster
#
# This code is absolutely legacy and does not properly work.
# I will not be updating this any time soon
#------------------------------

tweet = "Tweeting this from the tech shop. I guess the fridge is nice"
apikey = ""
apikeysecret = ""
#THIS IS CUSTOMER KEY / ACCESS KEY
accesskey = ""
accesskey_secret = ""

#DO NOT MODIFY THIS IF YOU DON'T KNOW WHAT YOU ARE DOING
import tweepy
print("X (formely Twitter) Aplication Poster")
print("Welcome.")
print("")
twitterapiauth = tweepy.OAuthHandler(apikey, apikeysecret)
twitterapiauth.set_access_token(accesskey, accesskey_secret)

twitterapi = tweepy.API(twitterapiauth)
print("Attempting crendentials:")
try:
    twitterapi.verify_credentials()
    print("Success! Your crendentials work.")
except:
    print("Error during the authentication. Please check if your keys are right, or is X (formely Twitter) down?")
print("")
print("Posting your tweet, the tweet is: " + tweet) 
print("")
twitterapi.update_status(tweet)
print("Successfully posted. Goodbye.")