from http import client
from flask import Flask, send_from_directory, render_template
from random import randint


app = Flask(__name__, template_folder='templates/')

@app.route('/home')
def base():
    return send_from_directory('templates/', 'index.html' )

@app.route('/static/<path:path>')
def home(path):
    return send_from_directory('', path)

@app.route('/rand')
def rand():
    return str(randint(0,100))

if __name__ == '__main__':
    app.run(debug=True)
