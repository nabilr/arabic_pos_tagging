import json
import dynet as dy
import numpy as np
import sys
import nltk
from collections import defaultdict
import random


HID = 10
WDIM = 200
CDIM = 10
TDIM = 20

tags = ['pos', 'prc3', 'prc2', 'prc1', 'prc0', 'per', 'asp', 'vox', 'mod', 'stt', 'cas', 'enc0',
'form_gen', 'form_num',  'gen', 'num', 'stemcat']

tagSet = sys.argv[1]


def extract_word_hidden_features(coded_word, cf_init, cb_init):    
    char_embs = [C[c2i[c]] for c in i2w[coded_word]]
    # print('aaaa',len(char_embs[0].value()))
    fw_exps = cf_init.transduce(char_embs)
    bw_exps = cb_init.transduce(reversed(char_embs))
    char_emb = dy.concatenate([fw_exps[-1], bw_exps[-1]])

    
    word_emb = W[coded_word]
    wemb = dy.concatenate([word_emb, char_emb])
    # print(len(wemb.value()), )
    return wemb

fd = open('data/preprocess_5253.json')
training_set = json.load(fd)

# Data structure to construct Bag of word
w2i = defaultdict(lambda: len(w2i))
t2i = defaultdict(lambda: len(t2i))
c2i = defaultdict(lambda: len(c2i))


# Extract feature curresponding to tagSet values. 
for each_sent in training_set:
    for word, tag in each_sent:

        # print(word, tag)
        word = word.lower()
        w2i[word]
        t2i[tag[tagSet]]
        for c in word:
            c2i[c]


i2w = {i:w for w,i in w2i.items()}
i2t = {i:w for w,i in t2i.items()}
i2c = {i:w for w,i in c2i.items()}



# Convert the text into numerical value

coded_sents = []
for each_sent in training_set:
    coded_sent = []
    for word, tag in each_sent:
        word = word.lower()
        coded_sent.append((w2i[word], t2i[tag[tagSet]]))

    coded_sents.append(coded_sent)



# print(coded_sents)


Vsize = len(w2i)
Tsize = len(t2i)
Csize = len(c2i)


m = dy.ParameterCollection()
trainer = dy.AdamTrainer(m)

W = m.add_lookup_parameters((Vsize, WDIM))
C = m.add_lookup_parameters((Csize, CDIM))
# T = m.add_lookup_parameters((Tsize, TDIM))

pW1 = m.add_parameters((HID,WDIM+10))
pb1 = m.add_parameters(HID)

pW2 = m.add_parameters((Tsize,HID))
pb2 = m.add_parameters(Tsize)


n_layer = 2
fwdRNN = dy.VanillaLSTMBuilder(n_layer, WDIM, 4, m)
bwdRNN = dy.VanillaLSTMBuilder(n_layer, WDIM, 4, m)

cfwdRNN = dy.VanillaLSTMBuilder(n_layer, CDIM, 5, m)
cbwdRNN = dy.VanillaLSTMBuilder(n_layer, CDIM, 5, m)

f_init = fwdRNN.initial_state()
b_init = bwdRNN.initial_state()

cf_init = cfwdRNN.initial_state()
cb_init = cbwdRNN.initial_state()

total_sentences = len(coded_sents)


index = int(total_sentences * 0.10)
test_sentences = coded_sents[0:index]
training_sentences =  coded_sents[index:]

train_loss=0
for i in range(1):
    for code_sent in training_sentences:
        dy.renew_cg()
        cf_init = cfwdRNN.initial_state()
        cb_init = cbwdRNN.initial_state()
        for w_c, t_c in code_sent:
            
            wemb = extract_word_hidden_features(w_c, cf_init, cb_init)
            y = pW2*(dy.tanh(pW1 * wemb + pb1)) + pb2
            # y = dy.tanh(pW1 * W[w_c] + pb1
            # y = pW2 * (pW1 * W[w_c] + pb1) + pb2
            # print(dy.softmax(y).value())
            # print(t_c, Tsize)
            loss = dy.pickneglogsoftmax(y, t_c)
            loss.backward()
            trainer.update()
            train_loss = loss.scalar_value()
            # print(loss.value())

            # print(y.value())
            # sys.exit(0)

print(train_loss)

TP =  0

total = 0
# F1 = 2 * precision * recall/ (precision + recall)

for each_sent in test_sentences:
    dy.renew_cg()
    cf_init = cfwdRNN.initial_state()
    cb_init = cbwdRNN.initial_state()

    for w_c, t_c in each_sent:

        wemb = extract_word_hidden_features(w_c, cf_init, cb_init)
        y = pW2*(dy.tanh(pW1 * wemb + pb1)) + pb2

        predict_c = np.argmax(y.value())

        if t_c == predict_c:
            TP += 1

        
        total += 1
            

        
        # print(w_c, t_c, )


print('Tag', tagSet, 'accuracy', TP/total)
# print(w2i)



# print(training_set[0][0][0], training_set[0][0][1]['form_num'])

print(len(training_set))