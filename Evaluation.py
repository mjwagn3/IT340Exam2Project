#this is the evaluation code
#postive class (0) is email is spam
#negative class (1) is email is not spam
#We are assuming the spam_classifer_function will return 1 or 0
#create by michael wagner
#
class Evaluation:
  #confusion_matrix holds the number of instance of actual vs true, confusion_matrix[actual][predict],
  #confusion_matrix[0][0] is the number of times the classifer predicted as spam a but was actual spam; tp
  #confusion_matrix[0][1] is the number of times the classifer predicted as not spam but was actual spam; fp
  #confusion_matrix[1][0] is the number of times the classifer predicted as spam a but was actual not spam; fn
  #confusion_matrix[1][1] is the number of times the classifer predicted as not spam but was actual not spam; tn
  #results = [0,0,0,0,0]
  #results[0] = "acc"
  #results[1] = "pre"
  #results[2] = "rec"
  #results[3] = "tnr"
  #results[4] = "fls"
  #it also takes the classifer function, has this was the first thing that was built, and also gives more autominy for the classifer function and for this class to run
  def __init__(self,spam_classifer_function):
    self.__confusion_matrix = [[0,0],[0,0]]
    self.__allow_new_instance = True
    self.__can_get_results = False
    self.__can_set_results = False
    self.__spam_classifer_function = spam_classifer_function
    self.__results = [0,0,0,0,0]
  #you passed in the argances for the classifer instance, and what the data you are classifying should be
  #it can only run if you all the program to read new instances, other wise adding new data to a calculated CM
  #will result in data that is not matching what was calucated vs wwhat was classified
  def classify_instance(self,args,actual):
    if not self.__allow_new_instance:
      raise RuntimeError("You have already set your stats; adding a new instance will chance the model\'s stats")
    if actual > 1 or actual < 0 and not isinstance(actual,int):
      raise ValueError(f"actual must an integer value that is either 1 or 0 not {actual}")
    predict = self.__spam_classifer_function(*args)
    self.__confusion_matrix[actual][predict] += 1
    return True
  #this disallows the ability to add new instances and allows the ability to set the results
  def disallow_instances(self):
    self.__allow_new_instance = False
    self.__can_set_results = True
  #this allows the ability to get the results, only if the you don't allow new instances to be added and the data has been calculated
  def can_retrieve_results(self):
    if self.__allow_new_instance == False and self.__can_set_results==False:
      self.__can_get_results = True
  #this allows the ability to add new instances to the data but it resets the results and disallows the ability to set and retrieved the results
  def allow_instances(self):
    self.__can_get_results = False
    self.__allow_new_instance = True 
    self.__can_set_results = False
    self.__results = [0,0,0,0,0]
  #this calculates
  def calculate_results(self):
    if self.__allow_new_instance == False and self.__can_get_results == False and self.__can_set_results==True:
      tp = self.__results[0][0]
      fp = self.__results[0][1]
      fn = self.__results[1][0]
      fp = self.__results[1][1]
      def cal_acc():
        acc = (tp+tn)/(tp+tn+fp+fn)
        return acc
      def cal_pre():
        pre = tp/(tp+fp)
        return pre
      def cal_rec():
        rec = tp/(tp+fn)
        return rec
      def cal_tnr():
        tnr = tn/(tn+fp)
        return tnr
      def cal_f1s():
        pre = cal_pre()
        rec = cal_rec()
        f1s = (2*pre*rec)/(pre+rec)
        return f1s
      self.__results = [cal_acc(),cal_pre(),cal_rec(),cal_tnr(),cal_f1s()]
      self.__can_set_results = False
      return True
    if self.__allow_new_instance:
      raise RuntimeError("You must no longer allow new instances to be added to the matrix before you can calculated the results")
    if self.__can_get_results:
      raise RuntimeError("The results have been calculated")
    raise RuntimeError("Unable to set results")

  # this gets the reulst, you can do, Evaluation.results
  #you can only get the results if you are allowed to meaning you no longer allow new instances and you have set the resul;t
  @property
  def results(self):
    if self.__can_get_results:
      return self.__results
    if self.__allow_new_instance:
      raise RuntimeError("You must no longer allow new instances to be add and then calculate the results before you can get the results")
    if self.__can_set_results:
      raise RuntimeError("You must calculate the results before you can get the results")
    raise RuntimeError("There was an issue retrieving the results")
