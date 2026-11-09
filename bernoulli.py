# Multi-variate Bernoulli Event Model
# Luke Oess and Michael Wagner


"""
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

ham_word_occurences = {}
spam_word_occurences = {}





