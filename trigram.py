# !/usr/bin/python3
import helper
import math
import string


# TODO: Implement a Laplace-smoothed trigram model :)
class LanguageModel:
    # Pre-processing elements include: <UNK>ing, ignoring punctuation, laplace smoothing, 2 start tokens, 1 stop token
    def __init__(self):
        self.processed_text = []
        self.vocab = {} # {vocab;occurances}
        self.trigram_occurrences = {}
        self.trigram_prob = {} # {trigram probabilities for each trigram (wi wi−2 wi−1)
        self.scores = {} 
        self.bigram_dictionary = {}
        self.vocab_size = 0

    def train(self, train_corpus):
        # added start and stop tokens
        preUNK_text = helper.preprocess(train_corpus, 3) # process raw text file into list of (sentences) lists of words
        preUNK_vocab = helper.count_unigrams(preUNK_text)[1] # Add each word(token) to vocab dictionary and its # of occurences
        self.vocab, self.processed_text = helper.convert_UNK(preUNK_vocab, preUNK_text)
        self.vocab_size = len(self.vocab.keys()) - 2
        trigram_dictionary = {}
        # count bigram for denominator
        self.bigram_dictionary = helper.count_bigrams(self.processed_text)
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
            bigram_count = self.bigram_dictionary[' '.join(bigram_words)]
            self.trigram_prob[trigram] = math.log2(self.trigram_occurrences[trigram] + 1) - math.log2(bigram_count + self.vocab_size)
            print(trigram + " " + str(round(self.trigram_prob[trigram], 3)))





    def score(self, test_corpus):
        self.processed_text = helper.score_UNK(self.vocab, helper.preprocess(test_corpus, 3))
        n = helper.count_unigrams(self.processed_text)[0]# process raw text file into list of (sentences) lists of words. [Hello, there, !] (punctuation preserved)
        # store each sentence's prob into a list
        probabilities = []
        for sentences in self.processed_text:
            test_sentence = ""
            probability = 0
            # reconstruct the entire sentence, along the way store the sentence without punctuation for counting probability
            for i in range(2, len(sentences)):
                test_sentence = test_sentence + sentences[i] + " " # [<s2> <s1> Hello, there, ! <\s>] -> "Hello " -> "Hello there " -> "Hello there ! "
                prev2 = sentences[i - 2]
                prev1 = sentences[i - 1]
                this = sentences[i]
                key_to_search = prev2 + " " + prev1 + " " + this
                bigram_to_search = prev2 + " " + prev1
                if key_to_search in self.trigram_prob.keys():
                    probability += self.trigram_prob[key_to_search]
                else: 
                    this_prob = 0
                    if bigram_to_search in self.bigram_dictionary.keys(): 
                        count_bigram_to_search = self.bigram_dictionary[bigram_to_search]
                        this_prob = math.log2(1 / (count_bigram_to_search + self.vocab_size))    
                    else:
                        this_prob = math.log2(1/self.vocab_size)
                    probability += this_prob
                    
            probabilities.append(probability) # stores log_2(probabilities)
            print(test_sentence + str(round(probability, 3))) # print output "sentence | probability"
        # perplexity
        H = 0
        for probability in probabilities:
            H += probability # Sum of (log_2(P(s_i))); probabilities is stored as log_2(P(s_i))
        H = H * (-1 / n)
        print("Perplexity = " + str(round(2 ** H, 3)))

