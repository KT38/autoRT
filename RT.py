#!/usr/bin/python
# -*- coding:utf-8 -*-

import tweepy
import datetime

# 各種キーを認証
CK = ""
CS = ""
AT = ""
AS = ""


#　対象となるアカウントのリスト
RtList = []


# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)
 
api = tweepy.API(auth)
 
class Listener(tweepy.StreamListener):
    def on_status(self, status):
        status.created_at += datetime.timedelta(hours=9)
 
	if (status.user.screen_name in RtList) and (status.in_reply_to_screen_name == None):
		tweetID = status.id
		api.retweet(tweetID)
		api.create_favorite(tweetID)

		print(status.created_at)
		print('@' + status.user.screen_name)
		print(status.text)
		print('------------------------------------------')


	return True
     
    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True
     
    def on_timeout(self):
        print('Timeout...')
        return True
 
# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)
 
listener = Listener()
stream = tweepy.Stream(auth, listener)
stream.userstream()