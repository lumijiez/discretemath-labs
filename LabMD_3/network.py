import json

import nltk
from nltk import TweetTokenizer

tt = TweetTokenizer()
special_chars = "1234567890.=?\",”$%^&’*(…):!><"

words_tweet_tokenizer = []
words_per_tweet = {}
special_words = []
hashtags = []

# Handles the tweet json, separates words into needed categories, and extracts hashtags
with open("tweets.json", "r", encoding="utf-8") as tweetJson:
    tweetJsonData = json.load(tweetJson)
    for tweet in tweetJsonData:
        tempWords = tt.tokenize(tweet["text"])
        words_per_tweet[tweet["id"]] = tempWords
        for word in tempWords:
            if not any(c in special_chars for c in word) and len(word) > 1:
                words_tweet_tokenizer.append(word)
                if word[0] == '#':
                    hashtags.append(word)
            else:
                if len(word) > 1:
                    special_words.append(word)

# Counts hashtags and outputs the top
hashtag_dictionary = {x: 0 for x in hashtags}
for hashtag in hashtags:
    hashtag_dictionary[hashtag] += 1

hashtag_dictionary = dict(sorted(hashtag_dictionary.items(), key=lambda item: item[1], reverse=True))
print("===================")
print("Top 10 #hashtags:")
print("===================")
count = 0
for hashtag in hashtag_dictionary:
    if count < 10:
        print(hashtag, " ", hashtag_dictionary[hashtag])
    count += 1

# Analyzes each word
tweet_rated_emotion = {}
word_emotion_dict = {}
with open("AFINN-111.txt", "r", encoding="utf-8") as AFINNdict:
    for line in AFINNdict:
        words = nltk.word_tokenize(line)
        nr = words[len(words) - 1]
        str = ""
        for x in range(len(words) - 1):
            str += words[x]
        word_emotion_dict[str] = nr

for id in words_per_tweet:
    total_rating = 0
    for word in words_per_tweet[id]:
        if word.lower() in word_emotion_dict:
            total_rating += int(word_emotion_dict[word.lower()])
    tweet_rated_emotion[id] = total_rating
    
print("==========================")
print("Top 10 Positive :D Tweets:")
print("==========================")
tweet_rated_emotion = dict(sorted(tweet_rated_emotion.items(), key=lambda item: item[1], reverse=True))
count = 0
for tweet in tweet_rated_emotion:
    if count < 10:
        print(tweet, " ", tweet_rated_emotion[tweet])
    count += 1
print("===========================")
print("Top 10 Negative >:D Tweets:")
print("===========================")
tweet_rated_emotion = dict(sorted(tweet_rated_emotion.items(), key=lambda item: item[1], reverse=False))
count = 0
for tweet in tweet_rated_emotion:
    if count < 10:
        print(tweet, " ", tweet_rated_emotion[tweet])
    count += 1
print("=====================================")
print("All Tweets Rated by Emotional Damage:")
print("=====================================")
print(tweet_rated_emotion)
