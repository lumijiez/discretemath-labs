import json
import nltk
import matplotlib.pyplot as plt
from nltk import TweetTokenizer


class Twt:
    def __init__(self, text, likes, retweets, date):
        self.text, self.likes, self.retweets, self.date = text, likes, retweets, date


checkedIDs, tod, word_counted_upper, word_counted_all_lowered, word_sliced_count, tt = [], {}, {}, {}, {}, TweetTokenizer()
nouns_counted_upper, popularity_nouns, filter_words, nouns_counted_lower = {}, {}, ["sure", "i"], {}
month_and_noun = {'2020-10': 0, '2020-11': 0, '2020-12': 0, '2022-01': 0, '2022-02': 0, '2022-03': 0, '2022-11': 0}
with open("tweets.json", "r", encoding="utf-8") as tweetJson:
    for tweet in json.load(tweetJson):
        if tweet["id"] not in checkedIDs:
            tod[tweet["id"]] = Twt([], tweet["likes"], tweet["retweets"], tweet["created_at"][:7])
            checkedIDs.append(tweet["id"])
            for word in tt.tokenize(tweet["text"]):
                if not any(c in "1234567890@.=?\",”$%^&’“*(…/[]):!><" for c in word):
                    tod[tweet["id"]].text.append(word)
                    if word.lower() not in word_counted_all_lowered:
                        word_counted_all_lowered[word.lower()] = 1
                    else:
                        word_counted_all_lowered[word.lower()] += 1
                    if word[0].isupper():
                        if word not in word_counted_upper:
                            word_counted_upper[word] = 1
                        else:
                            word_counted_upper[word] += 1
word_counted_all_lowered = dict(sorted(word_counted_all_lowered.items(), key=lambda item: item[1], reverse=True))
print("=========  TOP WORDS  =========")
[print(key, ' ', value) for key, value in list(word_counted_all_lowered.items())[:10]]

inpt = input("Write a word")
for id in tod:
    for word in tod[id].text:
        if word == inpt or word.lower() == inpt:
            month_and_noun[tod[id].date] += 1
x, y = list(month_and_noun.keys()), list(month_and_noun.values())
plt.bar(x, y, color='maroon', width=0.7)
plt.show()

for i in word_counted_all_lowered:
    ans = nltk.pos_tag([i])[0][1]
    if ans in ['NN', 'NNS', 'NNPS', 'NNP']:
        if i not in filter_words and not any(c in ["\'"] for c in i) and i[0].islower():
            nouns_counted_lower[i] = word_counted_all_lowered[i]
nouns_counted_lower = dict(sorted(nouns_counted_lower.items(), key=lambda item: item[1], reverse=True))
print("=========  TOP NOUNS  =========")
[print(key, ' ', value) for key, value in list(nouns_counted_lower.items())[:10]]

for i in word_counted_upper:
    ans = nltk.pos_tag([i])[0][1]
    if ans in ['NN', 'NNS', 'NNPS', 'NNP']:
        if i not in filter_words and not any(c in ["\'"] for c in i):
            nouns_counted_upper[i] = word_counted_upper[i]
nouns_counted_upper = dict(sorted(nouns_counted_upper.items(), key=lambda item: item[1], reverse=True))
print("=========  TOP PROPER NOUNS  =========")
[print(key, ' ', value) for key, value in list(nouns_counted_upper.items())[:10]]

for noun in nouns_counted_lower:
    like = [tod[id].likes for id in tod if noun in (x.lower() for x in tod[id].text)]
    retweet = [tod[id].retweets for id in tod if noun in (x.lower() for x in tod[id].text)]
    popularity_nouns[noun] = nouns_counted_lower[noun] * (1.4 + sum(retweet)) * (1.2 + sum(like))
popularity_nouns = dict(sorted(popularity_nouns.items(), key=lambda item: item[1], reverse=True))
print("=========  TOP NOUNS POPULARITY  =========")
[print(key, ' ', value) for key, value in list(popularity_nouns.items())[:10]]

word = input("Write word for suggestion")
for x in word_counted_all_lowered:
    if x not in word_sliced_count:
        word_sliced_count[x] = 0
for x in word_counted_all_lowered:
    if word == x[:len(word)] and word != x:
        word_sliced_count[x] += word_counted_all_lowered[x]
word_sliced_count = dict(sorted(word_sliced_count.items(), key=lambda item: item[1], reverse=True))
print("=========  TOP SUGGESTIONS  =========")
[print(key, ' ', value) for key, value in list(word_sliced_count.items())[:10]]

word = input("Write word for suggestion")
words_suggestion_counted = {}
for id in tod:
    for i in range(len(tod[id].text) - 1):
        if tod[id].text[i].lower() == word.lower():
            if tod[id].text[i + 1] not in words_suggestion_counted and len(tod[id].text[i + 1]) > 1:
                words_suggestion_counted[tod[id].text[i + 1]] = 1
            elif len(tod[id].text[i + 1]) > 1:
                words_suggestion_counted[tod[id].text[i + 1]] += 1
words_suggestion_counted = dict(sorted(words_suggestion_counted.items(), key=lambda item: item[1], reverse=True))
print("=========  TOP SUGGESTION OCCURRENCES  =========")
[print(key, ' ', value) for key, value in list(words_suggestion_counted.items())[:5] if value > 0]
