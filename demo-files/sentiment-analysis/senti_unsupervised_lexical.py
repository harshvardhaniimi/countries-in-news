# -*- coding: utf-8 -*-
"""
Lexicon-Based Sentiment
"""

# we will use this small sample
text = '''I begin this story with a neutral statement.  
  Basically this is a very silly test.  
  You are testing the Syuzhet package using short, inane sentences.  
  I am actually very happy today. 
  I have finally finished writing this package.  
  Tomorrow I will be very sad. 
  I won't have anything left to do. 
  I might get angry and decide to do something horrible.  
  I might destroy the entire package and start from scratch.  
  Then again, I might find it satisfying to have completed my first R package. 
  Honestly this use of the Fourier transformation is really quite elegant.  
  You might even say it's beautiful!
'''

# you may optionally split it into sentences if you would like more detail
import nltk
sentences = nltk.sent_tokenize(text.lower())
sentences

#%% AFINN
# pip install afinn
from afinn import Afinn
afn = Afinn(emoticons=True) 
print(afn.score('I really hated the plot of this movie'))
print(afn.score('I really hated the plot of this movie :('))

# apply to text
afn.score(text)
[afn.score(sentence) for sentence in sentences]

import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0, len(sentences))
y = [afn.score(sentence) for sentence in sentences]
plt.plot(x, y)
plt.xlabel("Sentence ID")
plt.ylabel("Sentiment Score")

# you can apply it to each review comment in movie

# similar idea for Bing Liu 

#%% VADER
# pip install vaderSentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

# it returns 4 scores: 
#     positive, negative, neutral, and compound.
vs = analyzer.polarity_scores(text)
vs

pos = 0
neg = 0
neu = 0
compound = 0
for sentence in sentences:
    vs = analyzer.polarity_scores(sentence)
    pos += vs["pos"]/len(sentences)
    neg += vs["neg"]/len(sentences)
    neu += vs["neu"]/len(sentences)
    compound += vs["compound"]/len(sentences)

pos
neg
neu
compound
