import string
import re

def preprocess(filepath, n, train):
    with open(filepath, 'r') as f:

        sentences = f.readlines() # creates a list of lines from the from [line 1, line 2, ...]
        output = []
        for sentence in sentences: # for each sentence (line) in the list [line 1, The children are all fond of him ." \n, ...]
            sentence = sentence.strip("\n") # Gets rid \n characters [line 1, The children are all fond of him .", ...]
            if train:
                sentence = sentence.translate(str.maketrans('', '', string.punctuation)) # remove punctuation [line 1, The children are all fond of him , ...]
            sentence = re.sub(pattern=r'[\s]+', repl = ' ', string=sentence) # remove extra white space [line 1, The children are all fond of him , ...]
            if n == 2:
                sentence = ("<s> " + sentence + " </s>")
            if n == 3:
                sentence = ("<s_1> <s_2> " + sentence + " </s>")
            output.append(sentence.split()) # splits sentence into a list of words [line 1, [The, children, are, all, fond, of, him] , ...]
    return (output)

def count_tokens(sentences):
    # create a token dictionary
    token_dict = {}
    # count how many tokens are there in the entire text
    N = 0
    # for each sentence in the sentence list
    for sentence in sentences:
        # for each token in the sentence we are looking at
        for token in sentence:
            N += 1
            # if this is a new word
            if token not in token_dict.keys():
                # put this word into the key
                token_dict[token] = 0
            # add one count for the word
            token_dict[token] += 1
    return (N, token_dict)
    # token_dict = count_tokens(sentences)[1]
