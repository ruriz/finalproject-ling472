# !/usr/bin/python3
import helper
import math
import string

# TODO: Implement a Laplace-smoothed unigram model :)
class LanguageModel:

    def __init__(self):
        self.processed_text = []
        self.vocab = {} # {vocab;occurances}
        self.unigram = {} # {unigram = vocab;probability = occurances + 1/total + |V|
        self.sentences = {} # {test_sentence;probability = product of its unigrams}
        self.train_total = 0


    def train(self, train_corpus):
        self.processed_text = helper.preprocess(train_corpus, 1, True) # process raw text file into list of (sentences) lists of words
        self.vocab = helper.count_tokens(self.processed_text)[1] # Add each word(token) to vocab dictionary and its # of occurences
        self.train_total = helper.count_tokens(self.processed_text)[0] # Track N
        for token in self.vocab:
            probability = math.log2((self.vocab[token] + 1) / (self.train_total + len(self.vocab)))
            print(token + " " + str(round(probability, 3)))
            self.unigram[token] = math.log2((self.vocab[token] + 1) / (self.train_total + len(self.vocab))) # Store token into unigram dictionary with its probability



    def score(self, test_corpus):
        self.processed_text = helper.preprocess(test_corpus, 1, False)
        # process raw text file into list of (sentences) lists of words. [Hello, there, !] (punctuation preserved)
        probabilities = []
        for sentences in self.processed_text:
            test_sentence = ""
            probability = 0
            for token in sentences:
                test_sentence = test_sentence + token + " " # [Hello, there, !] -> "Hello " -> "Hello there " -> "Hello there ! "
                if token not in string.punctuation:
                    if token in self.vocab.keys():
                        probability += self.unigram[token]
                    else:
                        probability += (2 / (self.train_total + len(self.vocab)))
            probabilities.append(probability) # stores log_2(probabilities)
            print(test_sentence + str(round(probability, 3))) # print output "sentence | probability"
        # perplexity
        H = 0
        for probability in probabilities:
            H += probability # Sum of (log_2(P(s_i))); probabilities is stored as log_2(P(s_i))
        H = H * (-1 / self.train_total)
        print("Perplexity = " + str(round(2 ** H, 3)))
