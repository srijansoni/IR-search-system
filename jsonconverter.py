
from math import log
import sys
import math
import os
import codecs
from collections import defaultdict
import pickle
import  json

with open('./quotes.json') as json_data:
    document = json.load(json_data)

def jsonconverter():
    """
    Function for creating json files and then storing in json file for further usage
    """
    count = 0
    i = 0
    for index in document:
           count+=1

           if count%2 ==0 :

            dictt = dict()
            if len(index['Quote']) > 20 :
             i =  i+1
             dictt["Quote"] = index['Quote']
             dictt["Author"] =  index['Author']

             dictt["Category"]    = index['Category']

             file =  "jsonnn/" + str(i) + ".json"

             with open(file, 'w',encoding='utf8') as fp:
                 json.dump(dictt, fp, ensure_ascii=False)




jsonconverter()
