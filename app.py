from flask import Flask, jsonify, request
from heaan import Heaan
from option import Option

app = Flask(__name__)

heaan = Heaan()
heaan.initialize()

initialVote = 0
setOption = ["Option1", "Option2", "Option3"] # list of options, this should be provided for voting

option = Option(heaan)
option.initialize(setOption)

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