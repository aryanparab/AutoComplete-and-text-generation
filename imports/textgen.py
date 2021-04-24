from keras.models import load_model
import pickle
import numpy as np
import msvcrt
from keras.preprocessing.sequence import pad_sequences

model = load_model('model_autocomplete.h5')
tokenizer = pickle.load(open('tokenizer_autocomplete.pickle','rb'))


def generate_text_seq(seed_text,nwords,model=model,tokenizer=tokenizer,text_seq_length = 20):
  text = []
  for _ in range(nwords):
    encoded = tokenizer.texts_to_sequences([seed_text])[0]
    encoded = pad_sequences([encoded],maxlen=text_seq_length,truncating='pre')

    y_pred = model.predict_classes(encoded)
    predicted_word = ''
    for word , index in tokenizer.word_index.items() : 
      if index== y_pred :
        predicted_word = word
        break
    seed_text = seed_text + ' '+predicted_word
    text.append(predicted_word)
  return ' '.join(text)
