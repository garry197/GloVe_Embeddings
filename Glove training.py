# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 01:48:57 2019

@author: Garry
"""

import os
import nltk
import most_Similar


from nltk.tokenize import sent_tokenize

raw=[]


from nltk.corpus import brown,reuters,comtrans,gutenberg
r=gutenberg.sents()
for i in r:
  j=' '.join(i)
  raw.append(j)


r=brown.sents()
for i in r:
  j=' '.join(i)
  raw.append(j)
  

r=reuters.sents()
for i in r:
  j=' '.join(i)
  raw.append(j)


r=comtrans.sents()
for i in r:
  j=' '.join(i)
  raw.append(j)


from nltk.corpus import stopwords 
data=[]
stop_words = set(stopwords.words('english')) 
for i in raw:
  wordlist=nltk.word_tokenize(i)
  wordsList = [w for w in wordlist if not w in stop_words]
  data.append(' '.join(wordsList))



data=[]
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import word_tokenize
lmtzr = WordNetLemmatizer()
raw = [[lmtzr.lemmatize(word) for word in word_tokenize(s)]
              for s in raw]



import glove
from glove import  Corpus,Glove
corpus=Corpus()


corpus.fit(raw, window=10)

glove = Glove(no_components=100, learning_rate=0.05)
   
glove.fit(corpus.matrix, epochs=100, no_threads=4, verbose=True)

glove.add_dictionary(corpus.dictionary)

glove.save('glove1.model')








