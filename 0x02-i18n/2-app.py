#!/usr/bin/env python3
"""Sets up a basic Flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Configuration of babel"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Gets the locale"""
    return request.accept_languages.best_match(Config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def home() -> str:
    """Serves the index.html file for home"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
