# !/usr/bin/python3
def read_file_to_list(file_name):
    # read file lines to a list
    result = []
    with open(file_name, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            result.append(line.replace('\n', ''))
    return result


def extract_frequency_from_list(sentences_list, word_to_frequency_dict):
    # extract frequency of each token
    for sentence in sentences_list:
        words = sentence.split(' ')
        for i in range(0, len(words)):
            if words[i] not in word_to_frequency_dict.keys():
                word_to_frequency_dict[words[i]] = 0
            word_to_frequency_dict[words[i]] += 1


def add_count_for_UNK(word_to_frequency_dict):
    # add count for <UNK>
    word_to_frequency_dict['<UNK>'] = 0
    for word in word_to_frequency_dict.keys():
        if word_to_frequency_dict[word] == 1:
            word_to_frequency_dict['<UNK>'] += 1