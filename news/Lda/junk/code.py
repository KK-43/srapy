import os
import random
import codecs
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer

# Function to remove stop words from sentences & lemmatize words.
def clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    normalized = " ".join(lemma.lemmatize(word,'v') for word in stop_free.split())
    x = normalized.split()
    y = [s for s in x if len(s) > 2]
    return y

# Remember this folder contains 72,000 articles extracted in Part-1 (previous post)
corpus_path = "articles-corpus/"
article_paths = [os.path.join(corpus_path,p) for p in os.listdir(corpus_path)]

# Read contents of all the articles in a list "doc_complete"
doc_complete = []
for path in article_paths:
    fp = codecs.open(path,'r','utf-8ontent = fp.read()
    doc_complete.append(doc_content)

# Randomly sample 70000 articles from the corpus created from wiki_parser.py
docs_all = random.sample(doc_complete, 70000)
docs = open("docs_wiki.pkl",'wbcPicklcPickle.dump(docs_all,docs)

# Use 60000 articles for training.
docs_train = docs_all[:60000]

# Cleaning all the 60,000 simplewiki articles
stop = set(stopwords.words('englishexclude = set(string.punctuation)
lemma = WordNetLemmatizer()
doc_clean = [clean(doc) for doc in docs_train]