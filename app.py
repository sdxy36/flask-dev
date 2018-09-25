from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    retrn 'hello 1'


if __name__ == '__main__':
    app.route()
