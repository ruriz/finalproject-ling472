# !/usr/bin/python3


# TODO: Implement a Laplace-smoothed bigram model :)
import math
from util import *


class LanguageModel:

    def __init__(self):
        self._sentences_list = []
        self._word_to_frequency_dict = {}
        self._bigram_dict = {}
        self._result_dict = {}

    def train(self, train_corpus):
        self._sentences_list = read_file_to_list(train_corpus)
        extract_frequency_from_list(self._sentences_list, self._word_to_frequency_dict)
        add_count_for_UNK(self._word_to_frequency_dict)

        # add count for <s> and </s>
        self._word_to_frequency_dict['<s>'] = len(self._sentences_list)
        self._word_to_frequency_dict['</s>'] = len(self._sentences_list)

        # iterate the list and extract tokens
        for sentence in self._sentences_list:
            words = sentence.split(' ')
            for i in range(-1, len(words)):
                # start token <s>
                if i == -1:
                    w1 = '<s>'
                    w2 = words[i + 1]
                elif i == len(words) - 1:
                    w1 = words[i]
                    w2 = '</s>'
                else:
                    w1 = words[i]
                    w2 = words[i + 1]
                    if self._word_to_frequency_dict[words[i]] == 1:
                        w1 = '<UNK>'
                    if self._word_to_frequency_dict[words[i + 1]] == 1:
                        w2 = '<UNK>'
                w1_w2 = w1 + " " + w2
                if w1_w2 not in self._bigram_dict.keys():
                    self._bigram_dict[w1_w2] = 0
                self._bigram_dict[w1_w2] += 1
        V = len(self._word_to_frequency_dict.keys())
        # Compute logged maximum likelihood
        # P(w2|w1)=count(w1 w2)/count(w1)
        for key in self._bigram_dict.keys():
            w1 = key.split(' ')[0]
            p = (self._bigram_dict[key] + 1) / (self._word_to_frequency_dict[w1] + V)
            self._result_dict[key] = math.log2(p)
        result_dict = {k: v for k, v in
                       sorted(self._result_dict.items(), key=lambda item: (item[1], item[0]), reverse=True)}
        i = 0
        for key in result_dict.keys():
            if i == 100:
                break
            i += 1
            print(key + ': ' + str(result_dict[key]))

    def score(self, test_corpus):
        test_sentences_list = read_file_to_list(test_corpus)
        pp = 0
        for sentence in test_sentences_list:
            words = sentence.split(' ')
            p = 0
            for i in range(0, len(words) - 1):
                w1 = words[i]
                w2 = words[i + 1]
                if w1 not in self._word_to_frequency_dict.keys():
                    w1 = '<UNK>'
                if w2 not in self._word_to_frequency_dict.keys():
                    w2 = '<UNK>'
                w1_w2 = w1 + ' ' + w2
                if w1_w2 not in self._result_dict.keys():
                    p += 1
                else:
                    p += self._result_dict[w1_w2]
            print(sentence + ' ' + str(p))
            pp += p
        print("Perplexity: " + str(pp / len(test_sentences_list)))
