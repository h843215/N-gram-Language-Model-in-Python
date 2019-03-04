#Functions for LanguageModel
from nltk.util import ngrams
from corpus import tokenize

from functools import partial #Function for get_ngrams

def get_ngrams(tokens, n):

        #Convert the token sequences to ngrams
        result = ngrams(tokens, n, pad_left=True, pad_right=True, left_pad_symbol='None', right_pad_symbol='None')
        result = list(result) #Change the result to list
        return result

def normalize(word_counts):
        
        probability = {}   #Dictioanry for adding probability of words
        for word in word_counts: #Words are list of tokens
                word_counts[word] = word_counts.setdefault(word, 0) #Adding counted words in dictionary
                
        sumwords = sum(word_counts.values()) #Sum the total words

        #Calculate the probability of words
        for word in word_counts:
                probability[word] = word_counts[word]/sumwords #Addin the probability of words in dictionary
        return probability
