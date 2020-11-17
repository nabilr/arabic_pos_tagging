
# tags=['pos', 'prc3', 'prc2', 'prc1', 'prc0', 'per', 'asp', 'vox', 'mod', 'stt', 'cas', 'enc0', 'form_gen', 'form_num',  'gen', 'num', 'stemcat'

# echo $tags
tags=(pos prc3 prc2 prc1 prc0 per asp vox mod stt cas enc0 form_gen form_num gen num stemcat)
i=0
while [ $i -lt 17 ]
do
    python train.py "${tags[i]}"
    i=$(( $i + 1 ))

done