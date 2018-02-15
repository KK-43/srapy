import json
import os

JSONS_DIR ="/home/kalyan32/news/corpus/"
TEXTS_DIR ="/home/kalyan32/news/corpus/"
# Source: gensim_preprocess.py
JSONS_DIR = "/path/to/jsons/dir"
TEXTS_DIR = "/path/to/texts/dir"

for fn in os.listdir(JSONS_DIR):
    print "Converting JSON: %s" % (fn)
    fjson = open(os.path.join(JSONS_DIR, fn), 'rb')
    data = json.load(fjson)
    fjson.close()
    tfn = os.path.splitext(fn)[0] + ".txt"
    ftext = open(os.path.join(TEXTS_DIR, tfn), 'wb')
    ftext.write(data["text"].encode("utf-8"))
    ftext.close()