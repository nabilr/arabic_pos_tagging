
# Arabic Parts Of Speech Tagging

## Download Arabic Corpus from https://catalog.ldc.upenn.edu/LDC2010T13
- Name of the file downloaded: atb1_v4_1_LDC2010T13.tgz
- Copy the extracted folder atb1_v4_1 into flder data/
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
IS_TRANS:   Arabic pronunciation
INDEX:      Number after P show, sentence index and number after w indicates word position
OFFSETS:    It indicates the length and word index position in the document.
```


## Stage 1: Preprocess the data:
```
Vocabulary Size   : 10612
Min sentence size : 7 
Max sentence size : 134 
Avg sentence size : 4.774033885398819
Sentence count    : 5253
```
### Construct sentence structure.

Read all the files and construct a sentence structure and associated word information from PATB file


### Extract morphological information using camel tool

camel tool: https://github.com/CAMeL-Lab/camel_tools


#### Sample out from camel_morphology analyzer

```                          
الولايات
#WORD: الولايات
diac:الوِلاياتِ lex:وِلايَة_1 caphi:2_a_l_w_i_l_aa_y_aa_t_i gloss:the+state;province+[fem.pl.] bw:ال/DET+وِلاي/NOUN+ات/NSUFF_FEM_PL+ِ/CASE_DEF_ACC pos:noun catib6:PRT+NOM ud:DET+NOUN root:#.ل.# pattern:الوِ2اياتِ prc3:0 prc2:0 prc1:0 prc0:Al_det per:na asp:na vox:na mod:na form_gen:f gen:f form_num:p num:p stt:d cas:a enc0:0 rat:i source:lex stem:وِلاي stemcat:NapAt stemgloss:state;province d1seg:الوِلايات d2seg:الوِلايات d3seg:ال+_وِلايات atbseg:الوِلايات d1tok:الوِلاياتِ d2tok:الوِلاياتِ d3tok:ال+_وِلاياتِ atbtok:الوِلاياتِ bwtok:ال+_وِلاي_+ات_+ِ pos_logprob:-0.4344233 lex_logprob:-2.91554 pos_lex_logprob:-2.91554
```
```
diac:الوِلاياتِ lex:وِلايَة_1 caphi:2_a_l_w_i_l_aa_y_aa_t_i gloss:the+state;province+[fem.pl.] bw:ال/DET+وِلاي/NOUN+ات/NSUFF_FEM_PL+ِ/CASE_DEF_GEN pos:noun catib6:PRT+NOM ud:DET+NOUN root:#.ل.# pattern:الوِ2اياتِ prc3:0 prc2:0 prc1:0 prc0:Al_det per:na asp:na vox:na mod:na form_gen:f gen:f form_num:p num:p stt:d cas:g enc0:0 rat:i source:lex stem:وِلاي stemcat:NapAt stemgloss:state;province d1seg:الوِلاياتِ d2seg:الوِلاياتِ d3seg:ال+_وِلاياتِ atbseg:الوِلاياتِ d1tok:الوِلاياتِ d2tok:الوِلاياتِ d3tok:ال+_وِلاياتِ atbtok:الوِلاياتِ bwtok:ال+_وِلاي_+ات_+ِ pos_logprob:-0.4344233 lex_logprob:-2.91554 pos_lex_logprob:-2.91554
```
```
diac:الوِلايات lex:وِلايَة_1 caphi:2_a_l_w_i_l_aa_y_aa_t gloss:the+state;province+[fem.pl.] bw:ال/DET+وِلاي/NOUN+ات/NSUFF_FEM_PL pos:noun catib6:PRT+NOM ud:DET+NOUN root:#.ل.# pattern:الوِ2ايات prc3:0 prc2:0 prc1:0 prc0:Al_det per:na asp:na vox:na mod:na form_gen:f gen:f form_num:p num:p stt:d cas:u enc0:0 rat:i source:lex stem:وِلاي stemcat:NapAt stemgloss:state;province d1seg:الوِلايات d2seg:الوِلايات d3seg:ال+_وِلايات atbseg:الوِلايات d1tok:الوِلايات d2tok:الوِلايات d3tok:ال+_وِلايات atbtok:الوِلايات bwtok:ال+_وِلاي_+ات pos_logprob:-0.4344233 lex_logprob:-2.91554 pos_lex_logprob:-2.91554
```
```
diac:الوِلاياتُ lex:وِلايَة_1 caphi:2_a_l_w_i_l_aa_y_aa_t_u gloss:the+state;province+[fem.pl.] bw:ال/DET+وِلاي/NOUN+ات/NSUFF_FEM_PL+ُ/CASE_DEF_NOM pos:noun catib6:PRT+NOM ud:DET+NOUN root:#.ل.# pattern:الوِ2اياتُ prc3:0 prc2:0 prc1:0 prc0:Al_det per:na asp:na vox:na mod:na form_gen:f gen:f form_num:p num:p stt:d cas:n enc0:0 rat:i source:lex stem:وِلاي stemcat:NapAt stemgloss:state;province d1seg:الوِلاياتُ d2seg:الوِلاياتُ d3seg:ال+_وِلاياتُ atbseg:الوِلاياتُ d1tok:الوِلاياتُ d2tok:الوِلاياتُ d3tok:ال+_وِلاياتُ atbtok:الوِلاياتُ bwtok:ال+_وِلاي_+ات_+ُ pos_logprob:-0.4344233 lex_logprob:-2.91554 pos_lex_logprob:-2.91554

```
```
diac:الوِلاياتِ lex:وِلايات_1 caphi:2_a_l_w_i_l_aa_y_aa_t_i gloss:the+States+[fem.pl.] bw:ال/DET+وِلاي/NOUN_PROP+ات/NSUFF_FEM_PL+ِ/CASE_DEF_ACC pos:noun_prop catib6:PRT ud:DET root:ل pattern:الوِ1اياتِ prc3:0 prc2:0 prc1:0 prc0:Al_det per:na asp:na vox:na mod:na form_gen:f gen:f form_num:p num:p stt:d cas:a enc0:0 rat:y source:lex stem:وِلاي stemcat:NAt stemgloss:States d1seg:الوِلايات d2seg:الوِلايات d3seg:ال+_وِلايات atbseg:الوِلايات d1tok:الوِلاياتِ d2tok:الوِلاياتِ d3tok:ال+_وِلاياتِ atbtok:الوِلاياتِ bwtok:ال+_وِلاي_+ات_+ِ pos_logprob:-99.0 lex_logprob:-99.0 pos_lex_logprob:-99.0
```
```
diac:الوِلاياتِ lex:وِلايات_1 caphi:2_a_l_w_i_l_aa_y_aa_t_i gloss:the+States+[fem.pl.] bw:ال/DET+وِلاي/NOUN_PROP+ات/NSUFF_FEM_PL+ِ/CASE_DEF_GEN pos:noun_prop catib6:PRT ud:DET root:ل pattern:الوِ1اياتِ prc3:0 prc2:0 prc1:0 prc0:Al_det per:na asp:na vox:na mod:na form_gen:f gen:f form_num:p num:p stt:d cas:g enc0:0 rat:y source:lex stem:وِلاي stemcat:NAt stemgloss:States d1seg:الوِلاياتِ d2seg:الوِلاياتِ d3seg:ال+_وِلاياتِ atbseg:الوِلاياتِ d1tok:الوِلاياتِ d2tok:الوِلاياتِ d3tok:ال+_وِلاياتِ atbtok:الوِلاياتِ bwtok:ال+_وِلاي_+ات_+ِ pos_logprob:-99.0 lex_logprob:-99.0 pos_lex_logprob:-99.0

```
```
diac:الوِلايات lex:وِلايات_1 caphi:2_a_l_w_i_l_aa_y_aa_t gloss:the+States+[fem.pl.] bw:ال/DET+وِلاي/NOUN_PROP+ات/NSUFF_FEM_PL pos:noun_prop catib6:PRT ud:DET root:ل pattern:الوِ1ايات prc3:0 prc2:0 prc1:0 prc0:Al_det per:na asp:na vox:na mod:na form_gen:f gen:f form_num:p num:p stt:d cas:u enc0:0 rat:y source:lex stem:وِلاي stemcat:NAt stemgloss:States d1seg:الوِلايات d2seg:الوِلايات d3seg:ال+_وِلايات atbseg:الوِلايات d1tok:الوِلايات d2tok:الوِلايات d3tok:ال+_وِلايات atbtok:الوِلايات bwtok:ال+_وِلاي_+ات pos_logprob:-99.0 lex_logprob:-99.0 pos_lex_logprob:-99.0
```
```
diac:الوِلاياتُ lex:وِلايات_1 caphi:2_a_l_w_i_l_aa_y_aa_t_u gloss:the+States+[fem.pl.] bw:ال/DET+وِلاي/NOUN_PROP+ات/NSUFF_FEM_PL+ُ/CASE_DEF_NOM pos:noun_prop catib6:PRT ud:DET root:ل pattern:الوِ1اياتُ prc3:0 prc2:0 prc1:0 prc0:Al_det per:na asp:na vox:na mod:na form_gen:f gen:f form_num:p num:p stt:d cas:n enc0:0 rat:y source:lex stem:وِلاي stemcat:NAt stemgloss:States d1seg:الوِلاياتُ d2seg:الوِلاياتُ d3seg:ال+_وِلاياتُ atbseg:الوِلاياتُ d1tok:الوِلاياتُ d2tok:الوِلاياتُ d3tok:ال+_وِلاياتُ atbtok:الوِلاياتُ bwtok:ال+_وِلاي_+ات_+ُ pos_logprob:-99.0 lex_logprob:-99.0 pos_lex_logprob:-99.0
```




Evaluation.

```
Tag             pos   gen   num   cas   mod   asp     per   vox   stt   prc0  prc1  prc2  prc3  enc0    Avg
JoinPrediction  97.21 99.50 99.59 94.76 99.41 99.44   99.47 99.25 98.24 99.71 99.81 99.73 99.96 99.71   98.99
CamelParser     96.78 99.41 99.43 92.68 99.13 99.27   99.23 99.08 97.54 99.67 99.63 99.59 99.90 99.61   98.64
LSTM            96.00 99.36 99.21 87.30 100   99.78   99.99 100   96.88 99.81 99.23 99.23 99.19 99.10   98.22
NO-LSTM         95.69 98.62 98.80 86.42 100   99.78   99.99 100   95.05 99.11 99.12 99.12 99.12 99.12   97.85
bag-of-word     95.67 98.54 98.77 85.71 100   99.79   99.99 100   94.98 98.10 99.13 99.13 99.13 99.13   97.719  

```

Tag pos accuracy 0.9567236375362786
Tag prc3 accuracy 0.9912931312479846
Tag prc2 accuracy 0.9912931312479846
Tag prc1 accuracy 0.9912931312479846
Tag prc0 accuracy 0.9809738793937439
Tag per accuracy 0.999935504675911
Tag asp accuracy 0.9978716543050629
Tag vox accuracy 1.0
Tag mod accuracy 1.0
Tag stt accuracy 0.9498226378587552
Tag cas accuracy 0.8571428571428571
Tag enc0 accuracy 0.9912931312479846
Tag form_gen accuracy 0.9869719445340213
Tag form_num accuracy 0.9901322154143825
Tag gen accuracy 0.9854885520799742
Tag num accuracy 0.9876813930990003
Tag stemcat accuracy 0.9568526281844566
##The result shows

### Case category
### Nominative Case
The nominative case is the case used for a noun or pronoun which is the subject of a verb. For example (nominative case shaded):

### Accusative Case
The accusative case's main function is to show the direct object of a verb.

### Genitive Case
The genitive case is predominantly used for showing possession. With nouns, it is usually created by adding 's to the word or by preceding it with "of."

