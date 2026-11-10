import Naive_Bayesian_Luke_Michael as nbc
import numpy as np

email_count = nbc.number_of_training_emails
training_data = nbc.training_data
testing_data = nbc.testing_data
spam_training = training_data[email_count:]
ham_training = training_data[:email_count]

# COMPLETE (the count function): Count # occurences of a given word per email
spam_counts = {}
ham_counts = {}
for email in spam_training:
    for word in set(email.split()): # it is said words do not repeat in each email, but making a set to be sure
        spam_counts[word] = spam_counts.get(word, 0) + 1  
for email in ham_training:
    for word in set(email.split()): 
        ham_counts[word] = ham_counts.get(word, 0) + 1 

# COMPLETE (probability of a word): record the bernoulli distribution of each word in spam and ham 
spam_word_probability = {}
ham_word_probability = {}
for email in training_data:
    for word in set(email.split()):
        if word not in spam_word_probability:
            p = (spam_counts.get(word,0)+1)/(email_count+2) # laplace smooth  
            spam_word_probability[word] = p
        if word not in ham_word_probability: 
            p = (ham_counts.get(word,0)+1)/(email_count+2) # laplace smooth 
            ham_word_probability[word] = p

TP = 0
FP = 0
TN = 0
FN = 0

# COMPLETE (classifier)
for i, email in enumerate(testing_data): 
    spam_score = np.log(len(spam_training)/len(training_data))
    ham_score = np.log(len(ham_training)/len(training_data))

    for word in set(email.split()): 
  
        if word not in spam_word_probability: 
            spam_score += np.log(1/(email_count+2))
        else:
            spam_score += np.log(spam_word_probability[word])
        if word not in ham_word_probability:
            ham_score += np.log(1/(email_count+2))
        else:
            ham_score += np.log(ham_word_probability[word])

    if spam_score>ham_score: # spam predicted
        if i < 100: FP += 1 # actual ham
        if i >= 100: TP += 1 # actual spam
    else: # ham predicted
        if i < 100: TN += 1 # actual ham
        if i >= 100: FN += 1 # actual spam

precision = TP/(TP+FP)
recall = TP/(TP+FN)
print(f"Accuracy:  {(TP+TN)/(TP+TN+FP+FN)}")  
print(f"Precision: {precision}")  
print(f"Recall:    {recall}")
print(f"TN Rate:   {TN/(TN+FP)}")
print(f"F1:        {(2 * precision * recall)/(precision+recall)}") # 2 * precision * recall