from Counter import BernoulliCounter
import Naive_Bayesian_Luke_Michael as nbc

#Change the old implementation of bernoulli to incorrapte class

email_count = nbc.number_of_training_emails

training_data = nbc.training_data
testing_data = nbc.testing_data
spam_trd = training_data[:email_count]
ham_trd = training_data[email_count:]


#bernoulli counter train counter
bc_trc = BernoulliCounter()
bc_trc.count_spam(spam_trd)
bc_trc.count_ham(ham_trd)

# #multinomial counter train counter
# mc_trc = MultinomialCounter()
# mc_trc.count_spam(spam_trd)
# mc_trc.count_ham(ham_trd)
