#   Author: Jessica Valenzuela
#   Assignment 7

#  This Program starts by prompting the user for a Twitter User Screen Name. If the user enters STOP, the program ends with an appropriate message and stop. Else it will display the following in the console:
# o User Screen Name
# o User Name
# o User ID
# o User Description
# o Location
# o Number of Friends
# o Number of Followers
# o The screen names of the most recent 5 followers of the Twitter User Account
# o The text of the Twitter User Account's most recent 5 tweets. 
# then it will prompt the user for the next Twitter User Screen Name to search, unless they enter STOP.

#  To run in a terminal window:   python3  twitter_data.py


import tweepy

### PUT AUTHENTICATOIN KEYS HERE ###
CONSUMER_KEY = "w2XyzCegeF59pf7NT9aRFcjmi"
CONSUMER_KEY_SECRET = "732m807zWYcbDqMVGBdYkliScWcMqlxMSQbqSlYYSCDnrdhKue"
ACCESS_TOKEN = "1388155758-67iqU84nVfCT2ZIkNp3O46JGPLGzlpr6eE6sQsN"
ACCESS_TOKEN_SECRET = "3XbqEoLZC4MEy10h8a8fXscYxkkuBijruOFJmBht4paVG"

# Authentication

authenticate = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_KEY_SECRET)
authenticate.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

#  use wait_on_rate_limit to avoid going over Twitter's rate limits
api = tweepy.API(authenticate, wait_on_rate_limit=True, 
                 wait_on_rate_limit_notify=True)
                 
# Get Information About a Twitter User Account

twitter_user = api.get_user('FollowStevens')

#intro statement
print('Hello! This program will retrieve and display twitter data based on your input.\n')

# Prompt the user for a Twitter User Screen Name. 
print('Please enter in a Twitter User Screen Name to search for. If you would like to end the program enter "STOP"')
#declare variable user_input that takes in the input the user enters in
user_input = input()

#while the user doesn't enter "STOP".
while user_input != "STOP":
    #if the screen name exist 
    try: 
        #declare variable user that gets user info w the input user provided
        user = api.get_user(user_input)
        #print the screen name, name, id, description, location, number of friends and number of followers
        print("========RESULT=========")
        print("Screen Name: ", user.screen_name)
        print("Name: ", user.name)
        print("ID: ", user.id)
        print("Description: ", user.description)
        print("Location: ", user.location)
        print("Number of Friends: ", user.friends_count )
        print("Number of Followers: ", user.followers_count)
        
        #print the screen names of the most recent 5 followers of Twitter User Account with appropriate label
        print("\n5 most recent followers:")

        #I followed the example provided for getting 5 friends to help me with this part.

        #create a cursor
        cursor = tweepy.Cursor(api.followers,  screen_name=user.screen_name)

        #for each follower in the cursor with 5 items print each screen name
        for follower in cursor.items(5):
            print(follower.screen_name)

        #print the text of the Twitter User Account's most recent 5 tweets. 
        print("\n5 most recent tweets:")
        # I followed this tutorial to help me with this part: https://www.geeksforgeeks.org/python-api-user_timeline-in-tweepy/

        #create variable for number of tweets you want to recieve (in our case it is 5)
        numTweets = 5

        #create variable that retrieves user timeline that takes in the inputed screen name and the amount of tweets to show
        
        tweets = api.user_timeline(user.screen_name, count = numTweets)

        #for each tweet Label each as TWEET 1, TWEET 2 etc with a blank line between tweets
        for tweet in range(numTweets):
            print(f'TWEET #{tweet+1}: {tweets[tweet].text}\n')

    #if the screen name does not exist display error
    except:
        print("ERROR: This Screen Name does not exist...")

    #after result is gathered and displayed, prompt user for screen name again.
    print('\nPlease enter in a Twitter User Screen Name to search for. If you would like to end the program enter "STOP"')
    user_input = input()

# If the user enters STOP, end the program with an appropriate message and stop
if user_input == "STOP":
    print("\nending program...")
    exit()


#===================CODE PROVIDED======================

# # Get Basic Account Information
# print("twitter_user id: ", twitter_user.id)

# print("twitter_user name: ", twitter_user.name)

# # Determine an Account’s Friends 
# friends = []

# print("\nFirst 5 friends:")

# # Creating a Cursor
# cursor = tweepy.Cursor(api.friends, screen_name='FollowStevens')

# # Get and print 5 friends
# for account in cursor.items(5):
#     print(account.screen_name)
    