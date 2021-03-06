from pytwitterscraper import TwitterScraper
from tqdm import tqdm

import pandas as pd
from p_tqdm import p_map

tw = TwitterScraper()

def get_data(tweet):
    tweetID = tweet['id']
    twcomments = tw.get_tweetcomments(tweetID)
    tData = {
        'id':tweetID,
        'date':tweet['created_at'],
        'text':tweet['text'],
        'likes':tweet['likes'],
        'retweet':tweet['retweet'],
        'comments':len(twcomments.contents),
        'urls': tweet['urls']
    }

    return tData

if __name__ == '__main__':
    
    profile = tw.get_profile(name="McDonalds")

    print('Following: {}'.format(profile.__dict__['following']))
    print('Follower: {}'.format(profile.__dict__['follower']))


    twitterID = profile.__dict__['id']

    tweets = tw.get_tweets(twitterID, count=50)
    
    tList = p_map(get_data,tweets.contents)

    tDF = pd.DataFrame(tList)
    tDF.to_csv('mcd.csv')