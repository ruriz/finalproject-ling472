import string
import re


def preprocess(filepath):
    with open(filepath, 'r') as f:
        sentences = f.readlines()
        for sentence in sentences:
            sentence = sentence.strip("\n")
            sentence = sentence.translate(str.maketrans('', '', string.punctuation))
            sentence = re.sub(pattern=r'[\s]+', repl = ' ', string=sentence)
        

def sen_to_tokens(sentences):
    for sentence in sentences:
        pass