from nltk import download
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer # Lemmatizer of coice
from nltk.stem import SnowballStemmer # Stemmer of choice

from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import matplotlib.pyplot as plt
import re

# Getting what we need from NLTK
download('punkt')
download('stopwords')
download('wordnet')

def clean_up(string):
    '''Removes punctuation from a string'''
    pattern="[.,:%-?()&$'\"!“”¯°–―—_\/|#\[\]…@ツ¡©\d]"
    return re.sub(pattern, '', string)

# Removing stopwords: common words that are less useful for detection (example:"the")
# Should be done before stemmeing, since some stop words might not be recognized
# after the stemmezation (doesnt happen if used lemmatization)
def stop_words(tokens):
    '''Removes stop words from a list of tokens preserving their order'''
    stop = set(stopwords.words('english'))
    tok_set = set()
    for t in tokens : tok_set.add(t)
    return list(tok_set-stop)

# Stemming words (brute reduction of words)
def stemming(tokens):
    '''Applies stemming to a list of tokens'''
    stemmer = SnowballStemmer('english')
    return list(map(stemmer.stem, tokens))

# Counting words (gives a matrix with the count of each word)
def count_words(tokens_list):
    '''Count number words in a list of tokens lists'''
    # Merge all tokens into a single string
    join = lambda words : " ".join(words)
    big_line =  " ".join(list(map(join, tokens_list)))
    counter = CountVectorizer()
    matrix = counter.fit_transform([big_line])
    words = counter.get_feature_names()
    counts = matrix.toarray()
    return words, counts

def show_wordcount(sentences, title=''):
    words, counts = count_words(sentences)
    if title: print(title)
    print(f"Amount of Words: {counts[0].sum()}")
    print(f"Amount of Distinct Words: {len(counts[0])}")

def onehotencoding(ids, size):
    '''One-hot encodes a list of labels (ids)'''
    hotencoded = np.zeros(shape=(size,))
    for x in ids : hotencoded[x] = 1
    return hotencoded

###############################################################

# Plot accuracy and loss graphs
def plot_graphs(history, title, key='accuracy'):
    # Plot training & validation accuracy values
    plt.plot(history.history[key])
    plt.plot(history.history['val_'+key])
    plt.title(title + ' accuracy')
    plt.ylabel('Accuracy')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Validation'], loc='upper left')
    plt.show()

    # Plot training & validation loss values
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title(title + ' loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Validation'], loc='upper left')
    plt.show()
