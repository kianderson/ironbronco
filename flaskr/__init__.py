#!/usr/bin/env python

import os

from flask import Flask, render_template#, request, redirect, url_for
#from static import functions as f
#import static/functions
#from static import functions.py

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # home page
    @app.route('/')
    @app.route('/index.html')
    def home():
        f.hello()
        return render_template('index.html')

    # create team
    @app.route('/createTeam')
    @app.route('/createTeam.html')
    def createTeam():
        return render_template('createTeam.html')

    # login
    @app.route('/login')
    @app.route('/login.html')
    def login():
        return render_template('login.html')

    # login
    @app.route('/profileBoard')
    @app.route('/profileBoard.html')
    def profileBoard():
        return render_template('profileBoard.html')

    # login
    @app.route('/register')
    @app.route('/register.html')
    def register():
        return render_template('register.html')

    return app
