#!flask/bin/python
from flask import Flask,request

app = Flask(__name__)

@app.route('/get_parameter_from_url', methods=['GET'])
def get_par01():
 user = request.args.get('user')
 return 'Hello, ' + user

if __name__ == '__main__':
 app.run(debug=True)
