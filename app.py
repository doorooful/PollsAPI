from flask import Flask, jsonify, request
from heaan import Heaan
from option import Option

# This is flask api server file.
# To run the api,
# 1. Activate python environment
# 2. run app.py(`python app/py`)
# 3. send POST request to http://127.0.0.1:5000/voting
# body sample is:
# {
#   "sender": "sendername",
#   "vote": "Option1"
# }

app = Flask(__name__)

# Create heaan object
heaan = Heaan()
heaan.initialize()

# User must provide any of these option name to use our api.
# If you'd like to change options names, change names here.
# If the option name has been changed,
# please kindly provide changed name for the API usage.
setOption = ["Option1", "Option2", "Option3"] # list of options, this should be provided for voting

# Create option object with option names.
option = Option(heaan)
option.initialize(setOption)

# Result dictionary object
result = {}

# API test request.
# If you'd like to test the server is running,
# please find http://127.0.0.1:5000/hello
# If server is not running, please run this file. (`python app.py`)
@app.route('/hello', methods=['GET'])
def hello():
  return "hello"

# Setting option list with user defined lists
# Sample body is:
# {
#   "1": "yes",
#   "2": "no"
# }
@app.route('/setOptionList', methods=['POST'])
def setOptionList():
  global setOption
  global option
  global heaan
  data = request.json
  setOption = list(data.values())
  option = Option(heaan)
  option.initialize(setOption)
  return "Given options are {}".format(setOption)

# Voting request.
# Only returns "voted!" after succesful vote.
# You should provide the voting with the key "vote",
# and the value which can be matched from optionList
# Default optionList has "Option1", "Option2", "Option3",
# If you set your own optionList, 
# then the values are from your own optionList(i.e. "yes" or "no")
@app.route('/voting', methods=['POST'])
def voting():
  global vote
  global option
  data = request.json
  vote = data.get('vote') # "Option1"
  option.vote(vote)
  return "voted!"

# Returns voting result in readable format.
# If the server hasn't got the result from option object, it tries to get the result.
# Else, just refer to the global variable to return result multiple times.
@app.route('/result', methods=['GET'])
def finish():
  global result
  if(result == {}):
    result = option.get_result()
  return jsonify(result)

if __name__ == '__main__':
  app.run(debug=True)