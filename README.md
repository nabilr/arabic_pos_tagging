# arabic_pos_tagging
Arabic Parts Of Speech Tagging

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

Read all the files and construct a sentence structure and associated word information from PATB file


### Extract morphological information using camel tool

camel tool: https://github.com/CAMeL-Lab/camel_tools


#### Sample out from camel_morphology analyze 

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





