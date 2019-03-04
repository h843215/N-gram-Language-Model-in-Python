#This is the user interface of n-gram language model. You could run this script by using python shell.
#First, it will show up the small window where you can upload and save your text file which you're going to analyze. 
#Then, you can close the window and typing the fuctions from corpus.py and lm.py on the python shell to examine the text.
#From the corpus.py, you could use tokenize and detokenize functions to inspect the text.
#For tokenizing the text, you could first type "from corpus import tokenize" on the python shell then type "print(tokenize(your filename))". After that you would get the result you want.
#For detokenizing, you could follow the same instructions above just change "tokenize" to "detokenize".
#For the functions from lm.py, for example you would like to get n-grams, you could type "from lm import get_ngrams" on python shell
#then type "print(get_ngrams(your tokens, number of n-gram))". Then you would get the n-grams you want.
#For other functions, you could just change the name of function then you could get what you want.

from tkinter import filedialog
from tkinter import *
 
#Create the window
root = Tk()

#modify root window
root.title("Language Model")
root.geometry("200x200")

root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))    #Open the file
root.filename =  filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))  #Save the file
print(root.filename)

#Kick off the events loop
root.mainloop()


