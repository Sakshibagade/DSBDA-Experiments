import nltk
nltk.download()
import os
import nltk.corpus
text = "Tokenization is the first step in the text analysis. The process of breaking down a text paragraph into smaller chunks such as words or sentences is called tokenization."
type(text)
from nltk.tokenize import word_tokenize, sent_tokenize
z = word_tokenize(text)
y = sent_tokenize(text)
print(z)
print(y)
print(os.listdir(nltk.data.find('corpora')))

from nltk.corpus import stopwords
stop_words = set(stopwords.words("english"))
print(stop_words)

from nltk.corpus import brown
brown.words()
print(os.listdir(nltk.data.find('corpora')))
nltk.corpus.gutenberg.fileids()
bible = nltk.corpus.gutenberg.words('bible-kjv.txt')
bible

tokens = word_tokenize(text.lower())
filtered_text=[]
for w in tokens:
    if w not in stop_words: filtered_text.append(w)
print("Tokenized Sentence:",tokens)
print("Filtered Sentences:",filtered_text)

from nltk.stem import PorterStemmer
e_words = ['wait', 'warning','waited','waits']
ps=PorterStemmer()
for w in e_words:
    rootWord = ps.stem(w)
    print(rootWord)


