#!/usr/bin/env python3
"""Sets up a basic Flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext


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
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def home() -> str:
    """Serves the index.html file for home"""
    home_title = gettext("Welcome to Holberton")
    home_header = gettext("Hello world!")
    
    return render_template('3-index.html',
                        home_title=home_title,
                        home_header=home_header
                        )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
