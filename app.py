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

# API test request.
# If you'd like to test the server is running,
# please find http://127.0.0.1:5000/hello
# If server is not running, please run this file. (`python app.py`)
@app.route('/hello', methods=['GET'])
def hello():
  return "hello"

# Voting request.
# Only returns "voted!" after succesful vote.
@app.route('/voting', methods=['POST'])
def voting():
  data = request.json
  vote = data.get('vote') # "Option1"
  option.vote(vote)
  return "voted!"

if __name__ == '__main__':
  app.run(debug=True)