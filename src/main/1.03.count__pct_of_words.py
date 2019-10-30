from nltk.book import *

occurrences = text5.count("lol")
word_count = len(text5)
print("%.1f pct" % (100*occurrences/word_count))
