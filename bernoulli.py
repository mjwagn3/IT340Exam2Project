import Naive_Bayesian_Luke_Michael as nbc

"""
Multi-variate Bernoulli Event Model
Luke Oess and Michael Wagner

notes (delete when finished):

take 500 ham, 500 spam for training set, rest for testing set 
for every training email X^i, there is a label y^i:
    X^i: a given email i in the training set 
    y^i: a label for the given email. (0=non-spam, 1=spam)

    X^j: a given email j in the testing set 


flow: 
    go through every email, count the occurences of each word
    num_occurences/total_word_count = probability of a given word 
"""

training_data = nbc.training_data
testing_data = nbc.testing_data

ham_word_occurences = {}
spam_word_occurences = {}

# add 1 to # occurences of a given word
for i in range(1000): 
    if i <= 500:
        words = training_data[i].split()
        for word in words: 
            ham_word_occurences[word] = ham_word_occurences.get(word, 0) + 1 
    else: 
        words = training_data[i].split()
        for word in words: 
            spam_word_occurences[word] = spam_word_occurences.get(word, 0) + 1

# total word count
ham_word_count = len(ham_word_occurences)
spam_word_count = len(spam_word_occurences)


        







