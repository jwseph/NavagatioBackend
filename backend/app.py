from flask import Flask, render_template
from base.util import *

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Welcome To Wanderlag!</h1>'


if __name__ == '__main__':
    app.run()
