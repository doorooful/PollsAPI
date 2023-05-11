from heaan import Heaan
import random

# Option class which provides voting function which uses heaan object to use heaan function.
class Option():
    def __init__(self, heaan:Heaan):
        self.optionDict={}  # Option indicies reference dictionary
        self.optionList=[]  # Option list
        self.options=[]     # List of options(i.e. ["Option1", "Option2", "Option3"])
        self.heaan=heaan    # Heaan object
        self.initialVote=0  # Before vote, score is 0
    
    # Initialize the instance with given options.
    # Here option dictionary gets random indicies for all options.
    # Then option list will created with encrypted indicies and score(initially 0)
    def initialize(self, options):
        self.options=options
        self.setOptionDict(self.select_rand(len(options)))
        self.setOptionList()

    # Input: how many numbers do you want
    # Output: random number list with no duplicates
    # |index| <= 54 (due to discrete equal function)
    def select_rand(self, length):
        rands = random.sample(range(-54, 54), length)
        return rands

    # Sets option dictionary with given options and random indicies
    def setOptionDict(self, rand_nums):
        length = len(self.options)
        for i in range(length):
            self.optionDict[self.options[i]]=self.heaan.encrypt(rand_nums[i])

    # Sets option list which has encrypted sets of values of each options' indices and vote score(initially 0 score)
    def setOptionList(self):
        for key, val in self.optionDict.items():
            self.optionList.append([val, self.heaan.encrypt(self.initialVote)])

    # By using heaan module, optionList would be updated.
    def vote(self, vote):
        self.optionList = self.heaan.updateVote(self.optionList, self.optionDict[vote])
        self.get_pretty_result()

    # From reference index to get exact option name as String
    # We assume there's no duplicates in the option index.
    def findOption(self, reference_index):
        for key, value in self.optionDict.items():
            if value == reference_index:
                return key
    
    # print optionList in plaintext
    # This function is for debugging purpose
    def get_pretty_result(self):
        pretty = []
        for l in self.optionList:
            dict_key = self.findOption(l[0])
            dict_val = self.heaan.pretty(self.heaan.decrypt(l[1]))
            print(dict_key, dict_val)
        return dict(pretty)
