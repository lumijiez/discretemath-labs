import json
import re
import nltk
from nltk import TweetTokenizer

hashtags = []
mapped_hashtags = dict()
emotional_values = dict()
tokenizer = TweetTokenizer()
final_emotional_data = {}

with open('AFINN-111.txt', encoding="utf-8") as file:
    for line in file:
        words = nltk.word_tokenize(line)
        nr = words[len(words) - 1]
        str = ""
        for x in range(len(words) - 1):
            str += words[x];
        emotional_values[str] = nr

with open('tweets.json', 'r', encoding='utf-8') as tweet_json:
    tweet_data = json.load(tweet_json)
    for i in range(len(tweet_data)):
        emotion_rating = 0
        words = tokenizer.tokenize(tweet_data[i]["text"])
        for x in words:
            if x[0] == '#' and len(x) > 1:
                hashtags.append(x)
            if re.sub("\s\s+", " ", x).lower() in emotional_values:
                emotion_rating += int(emotional_values[x.lower()])
        final_emotional_data[tweet_data[i]["id"]] = emotion_rating

for i in range(len(hashtags)):
    mapped_hashtags[hashtags[i]] = 0
for i in range(len(hashtags)):
    mapped_hashtags[hashtags[i]] += 1

sorted_dict = dict(sorted(mapped_hashtags.items(), key=lambda item: item[1], reverse=True))
counter = 10
x = 1
print("========================")
print("Top #10 Hashtags")
print("========================")
for i in sorted_dict:
    if x <= counter:
        print(x,'.', i, " ", sorted_dict[i])
    x += 1
x = 1
sorted_emotion_reverse = dict(sorted(final_emotional_data.items(), key=lambda item: item[1], reverse=True))
sorted_emotion = dict(sorted(final_emotional_data.items(), key=lambda item: item[1]))
print("========================")
print("Top #10 Positive Tweets")
print("=========================")
x = 1
for i in sorted_emotion_reverse:
    if x <= counter:
        print(i, " ", sorted_emotion_reverse[i])
    x += 1
print("========================")
print("Top #10 Negative Tweets")
print("========================")
x = 1
for i in sorted_emotion:
    if x <= counter:
        print(i, " ", sorted_emotion[i])
    x += 1
print("========================")
print("All Emotional Values per ID")
print("=========================")
for x in final_emotional_data:
    print(x, final_emotional_data[x])
