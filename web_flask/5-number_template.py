#!/usr/bin/python3
"""
Starts a flask web app with C page
"""
from flask import Flask, escape, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """root page"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """hbnb page"""
    return 'HBNB'


@app.route('/c/<text>')
def c(text):
    text = escape(text).replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python(text):
    text = escape(text.replace('_', ' '))
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    return render_template('5-number.html', number=n)


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
