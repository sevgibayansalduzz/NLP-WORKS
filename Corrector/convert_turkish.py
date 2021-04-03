import copy
import sys

def convert_to_english_letter(sentence):
    turkish_letters = {'ı': 'i', 'ö': 'o', 'ü': 'u', 'ş': 's', 'ç': 'c', 'ğ': 'g'}
    for index,i in enumerate(sentence):
        if i in turkish_letters:
            sentence=sentence[:index]+turkish_letters[i]+sentence[index+1:]
    return sentence



def convert_to_turkish_letter(sentence):
    turkish_letters={'i':'ı', 'o':'ö', 'u':'ü', 's': 'ş', 'c':'ç', 'g':'ğ'}
    possible_sentences=[sentence]

    for index,letter in enumerate(sentence):
        if letter in turkish_letters:
            i=0
            size=len(possible_sentences)
            while i < size:
                sentence=possible_sentences[i]
                possible_sentences.append(sentence[:index]+turkish_letters[sentence[index]]+sentence[index+1:])
                i += 1
    return possible_sentences

def highest_possible_sentence(ngram,n,possible_sentences):
    max_possible=-sys.maxsize-1
    max_possible_sentence=''

    for sentence in possible_sentences:
        prob=1/ngram.calc_probability_of(sentence)
        if prob > max_possible:
            max_possible=prob
            max_possible_sentence=copy.deepcopy(sentence)
    print("1",max_possible_sentence," n",n, "perplexity : ",ngram.calc_probability_of(max_possible_sentence))
    return max_possible_sentence

