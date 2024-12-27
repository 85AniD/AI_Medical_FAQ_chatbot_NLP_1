import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def tokenize_input(user_input):
    tokens = word_tokenize(user_input)
    tokens = [t for t in tokens if t not in stopwords.words('english')]
    return tokens
