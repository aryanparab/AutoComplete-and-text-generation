from keras.models import load_model
import pickle
import numpy as np
import msvcrt
from keras.preprocessing.sequence import pad_sequences

model = load_model('model_autocomplete.h5')
tokenizer = pickle.load(open('tokenizer_autocomplete.pickle','rb'))


def get_words(text):
    text = tokenizer.texts_to_sequences([text])[0]
    text = pad_sequences([text],maxlen=20,truncating='pre')
    ypred = model.predict(text)
    top_3  = np.argpartition(ypred,-4)[0][-4:-1]
    suggestions = []
    for word, item in tokenizer.word_index.items():
        if item in top_3:
            suggestions.append(word)
        if len(suggestions) == 3:
            break
    return suggestions
    
def main(): 
    c= ''
    prev = ''
    sent = ''
    last_suggestion = []
    while(c != b'\r'):  
        prev = sent 
        if(c!=b'\t'):
            c = msvcrt.getch()
        else:
            c = b' '
        if (c != b'\t'):
            print(str(c.decode('utf-8')),end='',flush=True)
        sent = sent + str(c.decode('utf-8'))  #create word on space
        if(c == b' '):
            tkns = sent.split()
            last_suggestion = get_words(sent.lower())
            print(last_suggestion, end='  ', flush=True)

        if(c == b'\b'):
            sent = prev
            
        if (c == b'\t' and len(last_suggestion) > 0):   #print last suggestion on tab
            print(last_suggestion[0], end='  ', flush=True)
            sent = sent + " " + last_suggestion[0]

if __name__ == "__main__":
    main()