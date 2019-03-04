#Import the tools
import nltk.data
import codecs
import os

#Import tool for detokenizer
from nltk.tokenize.treebank import TreebankWordDetokenizer

#Tokenizing
def tokenize(filename):
    
    #Read the text
    read = codecs.open(filename).read()

    #Tokenizing text into words
    tokenized_text = nltk.word_tokenize(read)
    return tokenized_text


#Detokenizing
def detokenize(tokens):

    #Detokenizing tokens into sentence
    detokenized_text = TreebankWordDetokenizer().detokenize(tokens)
    detokenized_text = detokenized_text.replace(" .", ".") #Remove the space before period
    detokenized_text = detokenized_text.replace(" ,", ",") #Remove the space before comma 
    detokenized_text = detokenized_text.replace(" :", ":") #Remove the space before colon
    return detokenized_text
    
    
    
