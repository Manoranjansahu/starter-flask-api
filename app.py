from flask import Flask, render_template
from flask import Flask, render_template, request, redirect, url_for, jsonify
import urllib.request as rrequest
import json
import re
from time import sleep
import multiprocessing

app = Flask(__name__)

def func(data):
    return redirect(url_for('test'))

@app.route('/')
def index():
    return render_template("publisher.html")

@app.route('/mqtt')
def mqtt():
    i = 10
    func(i)

@app.route('/test')
def test():
    return render_template("publisher_.html")

if __name__ == '__main__':
    app.run()
