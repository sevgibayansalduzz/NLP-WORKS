import pickle

from src.convert_turkish import highest_possible_sentence, convert_to_english_letter, convert_to_turkish_letter
from src.ngram import Ngram
from src.hecele import text_to_syllable

with open("input/tr_wiki_30.txt",encoding="utf8",errors='replace') as myfile:
    train_data=myfile.read()

train_data=text_to_syllable(train_data)

print("model is reading")
ngrams=[]
for i in range(5):
    ngrams.append(Ngram(i+1,train_data))
print("model is readed")


while True:
    sentence=input("Enter a sentece or exit with E.")
    sentence=convert_to_english_letter(sentence)
    possible_sentences=convert_to_turkish_letter(sentence)
    if sentence.lower()=='e':
        print("Program is finished.")
        break
    for i in range(5):
        highest_possible_sentence(ngrams[i],i+1,possible_sentences)


print("model is saving")
for i in range(5):
    file = open('model/'+str(i+1)+"gram.pickle", 'wb')
    pickle.dump(ngrams[i], file)
    file.close()
print("model is saved")








