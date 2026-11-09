#this is the counter class
#this is desine to count the number of times
from abc import ABC, abstractmethod
class Counter(ABC):
    def __init__(self):
        self._words_appear=set()
        self._spam_counts = {}
        self._ham_counts = {}
        self._has_count_spam = False
        self._has_count_ham = False
        self._num_of_ham_emails= 0
        self._num_of_spam_emails = 0
    @property
    def vocab_size(self):
        if not self._has_count_spam:
            raise RuntimeError("Spam counting has not been counted")
        if not self._has_count_ham:
            raise RuntimeError("Ham counting has not been counted")
        return len(self._words_appear)
        
    @property
    def words_appear(self):
        if not self._has_count_spam:
            raise RuntimeError("Spam counting has not been counted")
        if not self._has_count_ham:
            raise RuntimeError("Ham counting has not been counted")
        return self._words_appear
    @property
    def num_of_spam(self):
        if not self._has_count_spam:
            raise RuntimeError("Spam counting has not been counted")
        return self._num_of_spam_emails
    @property
    def num_of_ham(self):
        if not self._has_count_ham:
            raise RuntimeError("Ham counting has not been counted")
        return self._num_of_ham_emails
    def allow_counting_spam(self):
        self._has_count_spam = False
    def allow_counting_ham(self):
        self._has_count_ham = False
    @abstractmethod
    def count_spam(self,data):
        pass
    @abstractmethod
    def count_ham(self,data):
        pass

    @property
    def spam_counts(self):
        if not self._has_count_spam:
            raise RuntimeError("Spam counting has not been counted")
            raise RuntimeWarning("Ham counting has not been counted")
        return self._spam_counts
    @property
    def ham_counts(self):
            
        if not self._has_count_ham:
            raise RuntimeError("Ham counting has not been counted")
        return self._ham_counts
        

class BernoulliCounter(Counter):
    def __init__(self):
        super().__init__()

    def count_spam(self,data):
        if self._has_count_spam:
            raise RuntimeError("Spam instances has been counted")
        for email in data:
            email_tok = email.split()
            appear = {word:False for word in email_tok}
            self._num_of_spam_emails+=1
            for word in email_tok:
                if appear[word] == True:
                    continue
                appear[word] = True 
                if word not in self._spam_counts:
                    self._spam_counts[word] = 0
                self._words_appear.add(word)
                self._spam_counts[word] += 1
        self._has_count_spam = True      
    def count_ham(self,data):
        if self._has_count_ham:
            raise RuntimeError("Ham instances has been counted")
        for email in data:
            email_tok = email.split()
            appear = {word:False for word in email_tok}
            self._num_of_ham_emails += 1 
            for word in email_tok:
                if appear[word] == True:
                    continue
                appear[word] = True 
                if word not in self._ham_counts:
                    self._ham_counts[word] = 0
                self._words_appear.add(word)
                self._ham_counts[word] += 1 
        self._has_count_ham = True
        
        

# class MultinomialCounter(Counter):
#     def __init__(self):
#         super().__init__()

#     def count_spam(self,data):
#         if self._has_count_spam:
#             raise RuntimeError("Spam instances has been counted")
#         for email in data:
#             email_tok = email.split()
#             self._num_of_spam_emails+=1
#             for word in email_tok:
#                 if word not in self._spam_counts:
#                     self._spam_counts[word] = 0
#                 self._spam_counts[word] += 1
#                 self._words_appear.add(word)
#         self._has_count_spam = True
#     def count_ham(self,data):
#         if self._has_count_ham:
#             raise RuntimeError("Ham instances has been counted")
#         for email in data:
#             email_tok = email.split()
#             self._num_of_ham_emails += 1 
#             for word in email_tok:
#                 if word not in self._ham_counts:
#                     self._ham_counts[word] = 0
#                 self._ham_counts[word] += 1 
#                 self._words_appear.add(word)
#         self._has_count_ham = True
