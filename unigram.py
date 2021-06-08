# !/usr/bin/python3
import helper
import math
import string

# TODO: Implement a Laplace-smoothed unigram model :)
class LanguageModel:

# Pre-processing elements include: <UNK>ing, ignoring punctuation, laplace smoothing
    def __init__(self):
        self.processed_text = []
        self.vocab = {} # {vocab;occurances}
        self.unigram = {} # {unigram = vocab;probability = occurances + 1/total + |V|
        self.sentences = {} # {test_sentence;probability = product of its unigrams}
        self.train_total = 0


    def train(self, train_corpus):
        preUNK_text = helper.preprocess(train_corpus, 1, True)  # process raw text file into list of (sentences) lists of words
        preUNK_vocab = helper.count_tokens(preUNK_text)[1]  # Add each word(token) to vocab dictionary and its # of occurences
        self.vocab, self.processed_text = helper.convert_UNK(preUNK_vocab, preUNK_text)
        self.train_total = helper.count_tokens(self.processed_text)[0] # Track N
        for token in self.vocab:
            probability = math.log2(self.vocab[token] + 1) - math.log2(self.train_total + len(self.vocab))
            print(token + " " + str(round(probability, 3)))
            self.unigram[token] = probability # Store token into unigram dictionary with its probability



    def score(self, test_corpus):
        self.processed_text = helper.score_UNK(self.vocab, helper.preprocess(test_corpus, 1, False))
        n = helper.count_tokens(self.processed_text)[0]# process raw text file into list of (sentences) lists of words. [Hello, there, !] (punctuation preserved)
        probabilities = []
        for sentences in self.processed_text:
            test_sentence = ""
            probability = 0
            for token in sentences:
                test_sentence = test_sentence + token + " " # [Hello, there, !] -> "Hello " -> "Hello there " -> "Hello there ! "
                if token not in string.punctuation:
                    probability += self.unigram[token]
            probabilities.append(probability) # stores log_2(probabilities)
            print(test_sentence + str(round(probability, 3))) # print output "sentence | probability"
        # perplexity
        H = 0
        for probability in probabilities:
            H += probability # Sum of (log_2(P(s_i))); probabilities is stored as log_2(P(s_i))
        H = H * (-1 / n)
        print("Perplexity = " + str(round(2 ** H, 3)))
