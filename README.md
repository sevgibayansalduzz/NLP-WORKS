This repo includes following NLP projects :

-A simple FST that handles one Turkish morphological rule:
The Word Root mutates:
Words ending in -P -Ç -T -K change to -B -C -D -Ğ when suffixed with a vowel:
dolap → dolabı
kağıt → kağıdı

-A program to corrects Turkish sentences written using English letters only. For example, if the input sentence is “beklenen olumlu tepkiyi alamadi”, the output sentence will be “beklenen olumlu tepkiyi alamadı”. Note that “olumlu” could have been “ölümlü” but we did not choose it. Train data  is taken from the kaggle. Link: https://www.kaggle.com/mustfkeskin/turkish-wikipedia-dump
