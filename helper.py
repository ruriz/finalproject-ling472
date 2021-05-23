import string
import re


def preprocess(filepath):
    with open(filepath, 'r') as f:
        sentences = f.readlines()
        output = []
        for sentence in sentences:
            sentence = sentence.strip("\n")
            sentence = sentence.translate(str.maketrans('', '', string.punctuation))
            # set 1+whitespace to only one whitespace for split
            sentence = re.sub(pattern=r'[\s]+', repl = ' ', string=sentence)
            # sentence here becomes a list of tokens
            output.append(sentence.split())
    return output
