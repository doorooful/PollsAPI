from flask import Flask, jsonify, request
from heaan import Heaan
from option import Option
import random

app = Flask(__name__)

heaan = Heaan()
heaan.initialize()

initialVote = 0
setOption = 3 # numbers of options

option = Option(setOption, heaan)
option.initialize()

@app.route('/hello', methods=['GET'])
def hello():
  return "hello"

@app.route('/voting', methods=['POST'])
def voting():
  data = request.json
  vote = data.get('vote') # "Option1"
  option.vote(vote)
  return "voted!"

if __name__ == '__main__':
  app.run(debug=True)