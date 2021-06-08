# !/usr/bin/python3
import helper
import math
import string

# TODO: Implement a Laplace-smoothed bigram model :)
class LanguageModel:

    def __init__(self):
        self.processed_text = []
        self.vocab = {} # {vocab;occurances}
        self.bigram_occurrences = {} # {bigram; occurrences}
        self.bigram_probabilities = {} # {bigram = vocab; probability = occurances + 1/total + |V|}
        self.scores = {} # {test_sentence;probability = product of its bigrams}



    def train(self, train_corpus):
        self.processed_text = helper.preprocess(train_corpus, 2, True) # process raw text file into list of (sentences) lists of words
        self.vocab = helper.count_unigrams(self.processed_text)[1] # Add each word(token) to vocab dictionary and its # of occurences
        self.bigram_occurrences = helper.count_bigrams(self.processed_text)
        for bigram in self.bigram_occurrences:
        	self.bigram_probabilities[bigram] = math.log2(self.bigram_occurrences[bigram] + 1) - math.log2(self.vocab[bigram.split()[0]] + len(self.vocab)) # research scope within coding   
        	print (bigram + " " + str(round(self.bigram_probabilities[bigram], 3)))


    def score(self, test_corpus):
        self.processed_text = helper.preprocess(test_corpus, 2, False) # False is to preserve punctuation
        # process raw text file into list of bigrams lists of words. [Hello, there, !] (punctuation preserved)
        probabilities = []
        for sentences in self.processed_text:
            test_sentence = ""
            probability = 0
            for token in sentences:
                test_sentence = test_sentence + token + " " # [Hello, there, !] -> "Hello " -> "Hello there " -> "Hello there ! "
                if token not in string.punctuation:
                    if token in self.vocab.keys():
                    # if the word is in our list of bigrams, add the probability to the sentence probability
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
