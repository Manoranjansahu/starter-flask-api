from flask import Flask, render_template
from flask import Flask, render_template, request, redirect, url_for, jsonify
import urllib.request as rrequest
import json
import re
from time import sleep
import multiprocessing

app = Flask(__name__)
def schedule_task(delay):
    _data = {
            "chat_id": 1069737157,
            "text": "thread"
        }
    _request = rrequest.Request("https://api.telegram.org/bot6531655799:AAFuGpdFGZRfN7ndifFJwInv_rIPoyIa27s/sendMessage", data=json.dumps(_data).encode('utf8'), headers={"Content-Type": "application/json"})
    rrequest.urlopen(_request)
    sleep(5)
    _data = {
            "chat_id": 1069737157,
            "text": "thread"
        }
    _request = rrequest.Request("https://api.telegram.org/bot6531655799:AAFuGpdFGZRfN7ndifFJwInv_rIPoyIa27s/sendMessage", data=json.dumps(_data).encode('utf8'), headers={"Content-Type": "application/json"})
    rrequest.urlopen(_request)
    

@app.route('/')
def index():
    return render_template("publisher.html")

@app.route('/send/<msg>')
def send(msg):
    _data = {
            "chat_id": 1069737157,
            "text": str(msg)
        }
    _request = rrequest.Request("https://api.telegram.org/bot6531655799:AAFuGpdFGZRfN7ndifFJwInv_rIPoyIa27s/sendMessage", data=json.dumps(_data).encode('utf8'), headers={"Content-Type": "application/json"})
    rrequest.urlopen(_request)
    return "ok"

@app.route('/telegram')
def telegram():
    if __name__ == '__main__':
        p = multiprocessing.Process(daemon=False, target=schedule_task, args=(5,))
        p.start()
    _data = {
            "chat_id": 1069737157,
            "text": "hi"
        }
    _request = rrequest.Request("https://api.telegram.org/bot6531655799:AAFuGpdFGZRfN7ndifFJwInv_rIPoyIa27s/sendMessage", data=json.dumps(_data).encode('utf8'), headers={"Content-Type": "application/json"})
    rrequest.urlopen(_request)
    return "ok"

if __name__ == '__main__':
    app.run()
