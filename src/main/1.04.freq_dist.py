from nltk.book import *

fdist1 = FreqDist(text5)
print(fdist1.most_common(50))
print(fdist1['lol'])

print(sorted(item for item in set(text5) if item.istitle()))
