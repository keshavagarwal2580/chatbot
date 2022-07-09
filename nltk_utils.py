import numpy as np
import nltk
from nltk.stem import SnowballStemmer
sStemmer= SnowballStemmer('english')

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return sStemmer.stem(word.lower())
# list of all words after tokenizing ,stemming and lowering   
def bag_of_words(tokenized_sentence, words):
    # stem each word
    sentence_words = [stem(word) for word in tokenized_sentence]
    # initialize bag with 0 for each word
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words: 
            bag[idx] = 1
    return bag