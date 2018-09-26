import socket

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    retrn 'hello %s' % (socket.gethostname())


if __name__ == '__main__':
    app.run(host='0.0.0.0')
