from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/evan')
def evan():
    return 'Hello Evan'

@app.route('/six')
def plus():
    return str(3 + 3)

if __name__ == '__main__':
    app.run()