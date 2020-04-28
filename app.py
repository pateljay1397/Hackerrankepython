# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 16:06:02 2020

@author: Jay Patel
"""

# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world!\n'

if __name__ == '__main__':
    app.run()