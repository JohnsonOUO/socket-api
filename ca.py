#!flask/bin/python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
 return "Hello, World! (PYTHON+FLASK)"

@app.route('/', methods=['POST'])
def index_post():
 return "Hello, World! (This is POST method)"

if __name__ == '__main__':
 app.run(debug=True)
