from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/voting', methods=['POST'])
def vote():
  data = request.json
  sender = data.get('sender')
  vote = data.get('vote')
  print(sender, vote)
  return jsonify({'result': 'sender({}) wants to vote for {}'.format(sender, vote), 'msg': 'POST 요청!'})

if __name__ == '__main__':
   app.run(debug=True)