# !/usr/bin/python3
import helper
import math
import string


# TODO: Implement a Laplace-smoothed trigram model :)
class LanguageModel:

    def __init__(self):
        self.processed_text = []
        self.vocab = {} # {vocab;occurances}
        self.trigram_occurrences = {}
        self.trigram_prob = {} # {trigram probabilities for each trigram (wi wi−2 wi−1)
        self.scores = {} 

    def train(self, train_corpus):
        # added start and stop tokens
        preUNK_text = helper.preprocess(train_corpus, 3, True) # process raw text file into list of (sentences) lists of words
        preUNK_vocab = helper.count_tokens(preUNK_text)[1] # Add each word(token) to vocab dictionary and its # of occurences
        self.vocab, self.processed_text = helper.convert_UNK(preUNK_vocab, preUNK_text)
        trigram_dictionary = {}
        # count bigram for denominator
        bigram_dictionary = helper.count_bigrams(self.processed_text)
        # count trigram occurrences
        for sentence in self.processed_text:
            for i in range(2, len(sentence)):
                wi = sentence[i]
                wi_1 = sentence[i - 1]
                wi_2 = sentence[i - 2]
                key = wi_2 + " " + wi_1 + " " + wi
                if key not in trigram_dictionary.keys():
                    trigram_dictionary[key] = 0
                trigram_dictionary[key] += 1
        self.trigram_occurrences = trigram_dictionary
        for trigram in self.trigram_occurrences.keys(): 
            bigram_words = trigram.split()[:2]
            bigram_count = bigram_dictionary[' '.join(bigram_words)]
            self.trigram_prob[trigram] = math.log2(self.trigram_occurrences[trigram] + 1) - math.log2(bigram_count + len(self.vocab))
            print(trigram + " " + str(self.trigram_prob[trigram]))
   



    def score(self, test_corpus):
        print('I am an unimplemented TRIGRAM score() method.')  # delete this!
