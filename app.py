import socket

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello %s, version 1.0' % (socket.gethostname())


if __name__ == '__main__':
    app.run(host='0.0.0.0')
