#!/usr/bin/env python3
"""Sets up a basic Flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home() -> str:
    """Serves the index.html file for home"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
