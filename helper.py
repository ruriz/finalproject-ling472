import string
import re

def preprocess(filepath):
    with open(filepath, 'r') as f:
        sentences = f.readlines() # creates a list of lines from the from [line 1, line 2, ...]
        for sentence in sentences: # for each sentence (line) in the list [line 1, The children are all fond of him ." \n, ...]
            sentence = sentence.strip("\n") # Gets rid \n characters [line 1, The children are all fond of him .", ...]
            sentence = sentence.translate(str.maketrans('', '', string.punctuation)) # remove punctuation [line 1, The children are all fond of him , ...]
            sentence = re.sub(pattern=r'[\s]+', repl = ' ', string=sentence) # remove extra white space [line 1, The children are all fond of him , ...]
            sentence = sentence.split() # splits sentence into a list of words [line 1, [The, children, are, all, fond, of, him] , ...]
        print (sentences)

preprocess("C:\\Users\\nguye\\Documents\\LING 472\\Term Project\\finalproject-ling472\\data")
