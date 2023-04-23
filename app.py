from flask import Flask, jsonify, request
from heaan import Heaan
import random

app = Flask(__name__)

heaan = Heaan()
heaan.initialize()

initialVote = 0

# TODO: apply random index(x duplicate)
optionDictionary = {
  "Option1": 1,
  "Option2": 2,
  "Option3": 3
}

# initial option list
optionList = [
  [heaan.encrypt(optionDictionary["Option1"]), heaan.encrypt(initialVote)],
  [heaan.encrypt(optionDictionary["Option2"]), heaan.encrypt(initialVote)],
  [heaan.encrypt(optionDictionary["Option3"]), heaan.encrypt(initialVote)]
]

@app.route('/hello', methods=['GET'])
def hello():
  return "hello"

@app.route('/voting', methods=['POST'])
def voting():
  data = request.json

  vote = data.get('vote') # "Option1"
  
  # get index from optionlist, update value
  for o in optionList:
    if heaan.isSame(heaan.encrypt(optionDictionary[vote]), o[0]):
      # Debugging purpose
      print(findOption(optionDictionary, heaan.pretty(heaan.decrypt(o[0]))))

      o[1] = heaan.add(o[1], heaan.encrypt(1))

  # shuffle optionList
  random.shuffle(optionList)

  # Debugging purpose
  get_pretty_result(optionList)
  
  return "voted!"


def get_pretty_result(list):
  pretty = []
  for l in list:
    dict_key = findOption(optionDictionary, heaan.pretty(heaan.decrypt(l[0])))
    dict_val = heaan.pretty(heaan.decrypt(l[1]))
    print(dict_key, dict_val)
  return dict(pretty)

# return string option name from optionindex
def findOption(dict, index):
  for key, value in dict.items():
    if value == index:
      return key

if __name__ == '__main__':
  app.run(debug=True)