from dotenv import load_dotenv
import os
from tweepy import TweepError

from iepy import getTodayEvents, tweetEvent

load_dotenv()

for e in getTodayEvents():
    for a in e:
        if a.language == "cz":
            try:
                tweetEvent(
                    a,
                    os.environ["consumerKey"],
                    os.environ["consumerSecret"],
                    os.environ["accessToken"],
                    os.environ["accessTokenSecret"]
                )
            except TweepError as e:
                if e.api_code == 187:
                    pass
                else:
                    raise
