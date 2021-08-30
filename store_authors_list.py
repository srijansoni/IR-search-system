from math import log
import nltk
from nltk import word_tokenize
from nltk import FreqDist
import sys
import math
import os
from nltk.stem.snowball import SnowballStemmer
from collections import OrderedDict
from collections import defaultdict
import pickle
import  json

nltk.download('punkt')
nltk.download('stopwords')
authors_list= []
temp_authors_list = []
docFiles = [f for f in os.listdir('./jsonnn') if f.endswith(".json")]

for i in range(len(docFiles)):

    docFiles[i] = int(docFiles[i].split(".")[0])
    # print(docFiles[i])

docFiles.sort()
 # print(docFiles)

def create_authors_list():
    """
    Function for creating authors_list and then storing in json file for further usage
    """
    count=0
    for file in docFiles :
        document =  dict()
        with open("./jsonnn/"+ str(file) + ".json") as json_data:
         document = json.load(json_data)

        count+=1
        words = document["Author"]
        if len(words)<20:
            authors_list.append(words)

    #storing in json file
    a = set(authors_list)
    a=list(set(a))
    a.sort()
    print ('\n'.join(a))
    with open('savers/authors_list.json', 'w') as fp:
        json.dump(a, fp)


#caling function
create_authors_list()
