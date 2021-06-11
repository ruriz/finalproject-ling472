# finalproject-ling472

We have implemented 3 types of N-gram models (unigram, bigram, and trigram) under the LanguageModel class that contains a train() and score() method. train() calculates n-gram probabilities through maximum likelihood estimation (MLE) of a user-specified .txt file (whitespace separated with each sentence taking up a single line). Said method outputs each possible n-gram found in the training corpus and its probability in log_2 space to the terminal. 

The previous n-gram probabilities from train() then are utilized in the score() method to provide both sentence probabilities and model perplexity based on a test set, once again in log_2 space.

We used a helper function for all models to count n-grams by type and to preprocess the text. The preprocessing steps taken for both train() and score() include: punctuation scrubbing, <UNK>ing and token insertion when necessary (start and stop tokens for bigrams and trigrams). The calculation methods used are based on MLE with Laplace Smoothing (add-1 smoothing). 

The primary dataset used to train and test the model is based on a collection of sentences from 3 Jane Austen novels: Emma, Persuasion, and Sense and Sensibility. 80% of the total sentences were assigned to the Training set, while 10% were assigned to the Development set and another 10% to the Test set.


Perplexity Table
In the format:

n-gram
PP(Train set)
PP(Development set)
PP(Test set)

Unigram
582.655
555.179
559.895
  
Bigram
633.546
765.956
779.626
  
Trigram
1913.09
3154.311
3180.776



