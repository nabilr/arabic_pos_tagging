import os
import sys
import json
from camel_tools.morphology.database import MorphologyDB
from camel_tools.morphology.analyzer import Analyzer

base_dir = 'data/atb1_v4_1/data/pos/after/'


def get_tag(tagset):
    s = ''

    for t in tagset.split('+'):
        if t == '':
            continue
        i = t.index('/') + 1
        t = t[i:]
        s += '+' + t
    
    return s.strip('+')


files = os.listdir(base_dir)

sentence_size = 0
min_sentence = 1000
max_sentence = 0

# Construct sentence from the PATB file format
sentences = []
for f in files:

    path = base_dir + '/' + f
    # print(path)
    fd = open(path)

    lines = fd.readlines()
    pairs = [[item[0].strip(), item[1].strip()] for item in [t.strip().split(':')  for t in lines if t.strip() != '']]
    
    sentence = []
    for i in range(0, len(pairs), 9):
        k_v = {item[0]:item[1] for item in   pairs[i: i + 9]}
        # print(k_v)
        
        if int(k_v['INDEX'].split('W')[1]) == 1:
            # print(k_v['INDEX'], k_v['INDEX'].split('W')[1])
            sentence = []
            sentences.append(sentence)
             
        sentence.append(k_v)

    if len(sentence) != 0:
        sentences.append(sentence)

    s_size = len(sentences[-1])
    if s_size < min_sentence:
        min_sentence = s_size

    if s_size > max_sentence:
        max_sentence = s_size

    sentence_size += s_size
    

    fd.close()
    


print(min_sentence, max_sentence, sentence_size/len(sentences))

# Extract Morphological properties of every word from corpus

db = MorphologyDB.builtin_db()
analyzer = Analyzer(db)

# # Create analyzer with NOAN_PROP backoff
# analyzer = Analyzer(db, 'NOAN_PROP')

training_set = []

for sentence in sentences:
    s = []
    for word in sentence:
        
        analyses = analyzer.analyze(word['INPUT STRING'])
        # print(word, analyses)
        for d in analyses:
            # print(get_tag(d['bw']) == sentences[0][0]['POS'])
            tag = get_tag(d['bw'])
            if  tag == word['POS']:

                tag_set =[[k,d[k]] for  k in d]
                s.append([word['IS_TRANS'], d])
                break
                # print(d)


        i += 1    

    training_set.append(s)  



# print(training_set[0])

print(len(sentences), len(training_set))


with open('data/preprocess_5253.json', 'w') as outfile:
    json.dump(training_set, outfile)

# for d in analyses:
#     print(get_tag(d['bw']) == sentences[0][0]['POS'])
    





