import json
import os

JSONS_DIR ="/home/kalyan32/news/corpus/"
TEXTS_DIR ="/home/kalyan32/news/corpus/"

for fn in os.listdir(JSONS_DIR):
    #print "Converting JSON: %s" % (fn)
    fjson=open(os.path.join(JSONS_DIR, fn), 'rb')
    #with open('items.json')as fjson:
    data=json.load(fjson)
    tfn = os.path.splitext(fn)[0] + ".txt"
    ftext = open(os.path.join(TEXTS_DIR, tfn), 'wb')
    ftext.write(data["text"].encode("utf-8"))
    ftext.close()
