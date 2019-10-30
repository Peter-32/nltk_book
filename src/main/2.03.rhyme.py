import nltk
entries = nltk.corpus.cmudict.entries()

for word, pron in entries:
    if word == "orange":
        print(pron)

syllable = ['R', 'IH0', 'N', 'JH']
print([word for word, pron in entries if pron[-4:] == syllable])
