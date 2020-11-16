# arabic_pos_tagging
Arabic Parts of Speech Taging

## Down load Arabic Corpus from https://catalog.ldc.upenn.edu/LDC2010T13
- Name of the file download atb1_v4_1_LDC2010T13.tgz
- Copy th extracted folder atb1_v4_1 into flder data/
- Follder used to train the model: atb1_v4_1/data/pos/after/


## PATB file format 
```
 INPUT STRING: الولايات
     IS_TRANS: AlwlAyAt
      COMMENT: []
        INDEX: P1W4
      OFFSETS: 12,21
  UNVOCALIZED: AlwlAyAt
    VOCALIZED: Al+wilAy+At+u
          POS: DET+NOUN+NSUFF_FEM_PL+CASE_DEF_NOM
        GLOSS: the + states/provinces + [fem.pl.] + [def.nom.]
```
Every word is described in 9 lines.
```
IS_TRANS:   Arabic pronounciation
INDEX:      Number after P show, sentance index and number after w indicates word position
OFFSETS:    It idicates the length and word index position in the document.
```


## Stage 1: Preprocess the data:
```
Min sentence size: 7 
Max sentence size: 134 
Avg sentence size: 4.774033885398819
Total number of sentence to train: 5253
```
### Construct sentence structure.

Read all the files and construct a sentance structure and associated word information from PATB file


### Run


