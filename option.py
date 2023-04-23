from heaan import Heaan
import random

class Option():
    def __init__(self, options, heaan:Heaan):
        self.optionDict=None # Option indicies reference dictionary
        self.optionList=None # Option list
        self.options=options # Number of options (i.e. if a,b,c then 3)
        self.heaan=heaan
        self.initialVote=0
    
    def initialize(self):
        self.setOptionDict()
        self.setOptionList()

    # TODO: change indices in random numbers
    def setOptionDict(self):
        self.optionDict = {
            "Option1": 1,
            "Option2": 2,
            "Option3": 3
            }

    # TODO: change option name from option dictionary
    # Create optionlist which has encrypted data from option dictionary
    def setOptionList(self):
        self.optionList = [
        [self.heaan.encrypt(self.optionDict["Option1"]), self.heaan.encrypt(self.initialVote)],
        [self.heaan.encrypt(self.optionDict["Option2"]), self.heaan.encrypt(self.initialVote)],
        [self.heaan.encrypt(self.optionDict["Option3"]), self.heaan.encrypt(self.initialVote)]
        ]

    def vote(self, vote):
        for o in self.optionList:
            if self.heaan.isSame(self.heaan.encrypt(self.optionDict[vote]), o[0]):
                # Debugging purpose
                print(self.findOption(self.heaan.pretty(self.heaan.decrypt(o[0]))))

                o[1] = self.heaan.add(o[1], self.heaan.encrypt(1))
        random.shuffle(self.optionList)
        # Debugging purpose
        self.get_pretty_result()

    # From reference index to get exact option name as String
    def findOption(self, reference_index):
        for key, value in self.optionDict.items():
            if value == reference_index:
                return key
    
    # print optionList in plaintext
    # This function is for debugging purpose
    def get_pretty_result(self):
        pretty = []
        for l in self.optionList:
            dict_key = self.findOption(self.heaan.pretty(self.heaan.decrypt(l[0])))
            dict_val = self.heaan.pretty(self.heaan.decrypt(l[1]))
            print(dict_key, dict_val)
        return dict(pretty)
