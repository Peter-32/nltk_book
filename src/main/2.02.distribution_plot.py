import nltk

from nltk.corpus import udhr
lang = 'English'
raw_text = udhr.raw(lang + '-Latin1')
nltk.FreqDist(raw_text).plot()
