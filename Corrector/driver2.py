import pickle
import time

from src.convert_turkish import highest_possible_sentence, convert_to_english_letter, convert_to_turkish_letter

st=time.time()
print("model are loading")
ngrams=[]
for i in range(5):
    file = open('model/30mb' + str(i + 1) + "gram.pickle", 'rb')
    ngrams.append(pickle.load(file))
    file.close()
print("models are loaded.Loaded in ",time.time()-st," seconds")


while True:
    sentence=input("Enter a sentece or exit with E.")
    sentence=convert_to_english_letter(sentence)
    possible_sentences=convert_to_turkish_letter(sentence)
    if sentence.lower()=='e':
        print("Program is finished.")
        break
    for i in range(5):
        highest_possible_sentence(ngrams[i],i+1,possible_sentences)

