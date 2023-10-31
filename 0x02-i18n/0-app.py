#!/usr/bin/env python3
"""Sets up a basic Flask app"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('0-index.html')
