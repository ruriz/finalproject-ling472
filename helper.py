import string
import re

def preprocess(filepath, n):
    with open(filepath, 'r') as f:

        sentences = f.readlines() # creates a list of lines from the from [line 1, line 2, ...]
        output = []
        for sentence in sentences: # for each sentence (line) in the list [line 1, The children are all fond of him ." \n, ...]
            sentence = sentence.strip("\n") # Gets rid \n characters [line 1, The children are all fond of him .", ...]
            sentence = sentence.translate(str.maketrans('', '', string.punctuation)) # remove punctuation [line 1, The children are all fond of him , ...]
            sentence = re.sub(pattern=r'[\s]+', repl = ' ', string=sentence) # remove extra white space [line 1, The children are all fond of him , ...]
            if n == 2:
                sentence = ("<s> " + sentence + " </s>")
            if n == 3:
                sentence = ("<s_1> <s_2> " + sentence + " </s>")
            output.append(sentence.split()) # splits sentence into a list of words [line 1, [The, children, are, all, fond, of, him] , ...]
    return (output)

def count_unigrams(sentences):
    # create a token dictionary
    token_dict = {}
    # count how many tokens are there in the entire text
    N = 0
    # for each sentence in the sentence list
    for sentence in sentences:
        # for each token in the sentence we are looking at
        for token in sentence:
            if token not in ["<s>", "<s_2>", "<s_1>"]:
                N += 1
                # if this is a new word
            if token not in token_dict.keys():
                # put this word into the key
                token_dict[token] = 0
            # add one count for the word
            token_dict[token] += 1
    return (N, token_dict)
    # token_dict = count_tokens(sentences)[1]

def count_bigrams(sentences):
    bigram_dictionary = {}
    for sentence in sentences: # {probability of bigram = counts of bigram + 1/ count of the first word + vocabulary size}
        prev = ""
        for token in sentence: # {remember the second word; i.e. "I"}
            if not prev == "":
                if prev + " " + token not in bigram_dictionary.keys():
                    # put this bigram into the key
                    bigram_dictionary[prev + " " + token] = 0
                bigram_dictionary[prev + " " + token] += 1 
            prev = token # {(remember first word) = first token; always used to keep track of the first "word" in the bigram}
    return bigram_dictionary 

# add counts for how many words have 1 occurrence(equals to counts of <UNK>),
# then process our processed texts convert the words to UNK
def convert_UNK(vocab, processed_text):
    # separate for loops implementation
    singulars = []

    for token in vocab.keys():
        if vocab[token] == 1:
            singulars.append(token)
    for token in singulars:
        if '<UNK>' not in vocab.keys():
            vocab['<UNK>'] = 0
        del vocab[token]
        vocab['<UNK>'] += 1
        # go through the preprocessed text and convert 1 occurence word(now not in voab dict)
    for sentences in processed_text:
        for i in range(0, len(sentences)):
            if sentences[i] not in vocab.keys():
                sentences[i] = "<UNK>"
    return vocab, processed_text

def score_UNK(vocab, processed_text):
    for sentences in processed_text:
        for i in range(0, len(sentences)):
            if sentences[i] not in string.punctuation:
                if sentences[i] not in vocab.keys() and sentences[i] not in ["<s>", "<s_2>", "<s_1>"]:
                    sentences[i] = "<UNK>"
    return processed_text