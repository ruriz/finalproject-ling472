# !/usr/bin/python3


# TODO: Implement a Laplace-smoothed unigram model :)
class LanguageModel:

    def __init__(self):
        self.processed_text = []
        self.vocab = {} # {vocab;occurances}
        self.unigram = {} # {unigram = vocab;probability = occurances + 1/total + |V|}


    def train(self, train_corpus):
        self.processed_text = preprocess(train_corpus, 1) # process raw text file into list of (sentences) lists of words
        self.vocab = count_tokens(self.processed_text)[1] # Add each word(token) to vocab dictionary and its # of occurences
        total = count_tokens(self.processed_text)[0]
        for token in self.vocab:
            self.unigram[token] = (self.vocab[token] + 1) / (total + len(self.vocab)) # Store token into unigram dictionary with its probability
        print(self.unigram)


    def score(self, test_corpus):
        print('I am an unimplemented UNIGRAM score() method.')  # delete this!
