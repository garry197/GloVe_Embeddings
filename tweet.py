# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 12:26:19 2019

@author: Garry
"""

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "950068921553465345-3GkWBmWhs5bcVPLxkguEluerBAayeF0"
access_token_secret = "Oju1k7qrBAEFtlDOBen31FXNGiuuUJppaXSSfw0403ycI"
consumer_key = "B9WgM0jU4049pJhWOwB8YTPLd"
consumer_secret = "8wK4LET5SpYpCpNhFD0OvVCwYCJweHkDW7yjQLA4qnUpvR3EwA"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    
    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(languages=["en"],track=["a", "the",",",".", "i", "you", "u","and","is","to","?","in","my","that","on","s","hi","hey","do","me","be","for","now","so","bc","we","will","can","time","am","by","today","rt","or","lol","did","had","he","she","thanks","1","2","3","4","5","6","7","8","9","0"])