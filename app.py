
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Hello, my name is David Roland Gnimpieba Zanfack My Company Id: 101037638 </h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
