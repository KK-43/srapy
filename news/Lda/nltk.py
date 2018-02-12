import nltk

nltk.download('all')
try:
    File = open("/home/kalyan32/news/items.csv","r")
except:
    print("File Opened")
    raise
          #open file
lines = File.read() #read all lin
sentences = nltk.sent_tokenize(lines) #tokenize sentences
nouns = [] #empty to array to hold all nouns

for sentence in sentences:
     for word,pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
         if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):
             nouns.append(word)

     print(word)
     print("\n")


