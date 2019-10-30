import nltk
from nltk.corpus import brown

cfd = nltk.ConditionalFreqDist(
    (genre, word)
    for genre in brown.categories()
    for word in brown.words(categories=genre))
genres = ['religion', 'news', 'humor', 'reviews', 'adventure']
modals = ['who', 'what', 'when', 'where', 'why', 'how']
cfd.tabulate(conditions=genres, samples=modals)
