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
        self.vocab_size = 0



    def train(self, train_corpus):
        # self.processed_text = helper.preprocess(train_corpus, 2, True) # process raw text file into list of (sentences) lists of words
        # self.vocab = helper.count_unigrams(self.processed_text)[1] # Add each word(token) to vocab dictionary and its # of occurences
        preUNK_text = helper.preprocess(train_corpus, 2)  # process raw text file into list of (sentences) lists of words
        preUNK_vocab = helper.count_unigrams(preUNK_text)[1]  # Add each word(token) to vocab dictionary and its # of occurences
        self.vocab, self.processed_text = helper.convert_UNK(preUNK_vocab, preUNK_text)
        self.vocab_size = len(self.vocab.keys()) - 1
        self.bigram_occurrences = helper.count_bigrams(self.processed_text)
        for bigram in self.bigram_occurrences:
        	self.bigram_probabilities[bigram] = math.log2(self.bigram_occurrences[bigram] + 1) - math.log2(self.vocab[bigram.split()[0]] + self.vocab_size) # research scope within coding   
        	print (bigram + " " + str(round(self.bigram_probabilities[bigram], 3)))


    def score(self, test_corpus):
        # UNK any words not encountered
        self.processed_text = helper.score_UNK(self.vocab, helper.preprocess(test_corpus, 2)) # includes punctuation
        n = helper.count_unigrams(self.processed_text)[0]# process raw text file into list of (sentences) lists of words. [Hello, there, !] (punctuation preserved)
        # process raw text file into list of bigrams lists of words. [Hello, there, !] (punctuation preserved)
        probabilities = []
        for sentences in self.processed_text:
            test_sentence = ""
            probability = 0
            for i in range(1, len(sentences)):
                # reconstruct the sentence for print
                test_sentence = test_sentence + sentences[i] + " " # [<s2> <s1> Hello, there, ! <\s>] -> "Hello " -> "Hello there " -> "Hello there ! "                
                # store prev = wi-1, this = wi
                prev = sentences[i - 1]
                this = sentences[i]
                key_to_search = prev + " " + this
                # if this bigram is known from train set, then get its probability from bigram_probabilites
                if key_to_search in self.bigram_probabilities.keys():
                    probability += self.bigram_probabilities[key_to_search]
                # if the bigram is not known, calculate it as 1/(count(wi-1) + |V|)
                else: 
                    count_prev = self.vocab[prev]
                    this_prob = math.log2(1 / (count_prev + self.vocab_size))
                    probability += this_prob
            probabilities.append(probability) # stores log_2(probabilities)
            print(test_sentence + str(round(probability, 3))) # print output "sentence | probability"
        # perplexity
        H = 0
        for probability in probabilities:
            H += probability # Sum of (log_2(P(s_i))); probabilities is stored as log_2(P(s_i))
        H = H * (-1 / n)
        print("Perplexity = " + str(round(2 ** H, 3)))
