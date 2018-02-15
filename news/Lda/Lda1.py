import logging
import os
import gensim
from string import maketrans

MODELS_DIR = "/home/kalyan32/news/corpus/"
NUM_TOPICS = 5

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',
                    level=logging.INFO)

dictionary = gensim.corpora.Dictionary.load(os.path.join(MODELS_DIR,
                                            "mtsamples.dict"))
corpus = gensim.corpora.MmCorpus(os.path.join(MODELS_DIR, "mtsamples.mm"))
print("X1")
# Project to LDA space
lda = gensim.models.LdaModel(corpus, id2word=dictionary, num_topics=NUM_TOPICS)
for i in  lda.show_topics(num_words=5):
    #print (i[0], i[1])
    x=0
s=str(lda.show_topics(num_words=5)[1][1])
#print(s)
x=str(lda.show_topics(num_words=5)[3][1])
z=str(lda.show_topics(num_words=5)[3][1])
#print(x)
x=x.translate(maketrans('',''),'1234567890+*.')
z=z.translate(maketrans('',''),'abcdefghijklmnopqrstuvwxyz+*"')
#print(z)
omega=z.split(" ")
#print(omega[2])
numero=float(omega[2])
print(numero)
x=x.replace('"','')
y=x.split(" ")
#print(y[1])
#print(x)
s=s.replace("0","")
s=s.replace("1","")
s=s.replace("2","")
s=s.replace("3","")
s=s.replace("4","")
s=s.replace("5","")
s=s.replace("6","")
s=s.replace("7","")
s=s.replace("8","")
s=s.replace("9","")
s=s.replace(".","")
s=s.replace("+","")
s=s.replace("*","")
s=s.replace('"','')
#print(s)
#s=str(lda.print_topic(gensim.models.LdaModel,1))
#print(s)