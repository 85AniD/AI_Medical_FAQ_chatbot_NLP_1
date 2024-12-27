'''
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def tokenize_input(user_input):
    tokens = word_tokenize(user_input)
    tokens = [t for t in tokens if t not in stopwords.words('english')]
    return tokens
'''

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def tokenize_input(user_input):
    """
    Tokenize the user input string into words using NLTK's word_tokenize.
    """
    if not isinstance(user_input, str):
        raise ValueError("Input to tokenize_input must be a string.")
    return nltk.word_tokenize(user_input)
