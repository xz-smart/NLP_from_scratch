import numpy as np
import pandas as pd
import nltk
import string
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

class TextProcessor():
    def __init__(self,):
        self.lem = nltk.stem.wordnet.WordNetLemmatizer() 
        self.stem = nltk.stem.porter.PorterStemmer()
        self.stop_words = set(nltk.corpus.stopwords.words("english"))
        self.punctuations = list(string.punctuation)
    def clean(self, text):
        """
        tokenize a paragraph of text
        remove the handles, URL, stop words
        stem and lemmatize the words
        convert words into lower cases
        """
        tokens=nltk.tokenize.word_tokenize(text)
        output = []
        for token in tokens:
            if (token not in self.stop_words) and ("@" not in token) and ("//" not in token) and (token not in self.punctuations):
                
                output.append(self.lem.lemmatize(self.stem.stem(token)).lower())
        return output



