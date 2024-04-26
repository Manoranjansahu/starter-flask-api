from flask import Flask, render_template
from flask import Flask, render_template, request, redirect, url_for, jsonify
import urllib.request as rrequest
import json
import re
from time import sleep
import multiprocessing
# import paho.mqtt.client as mqtt
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("publisher.html")

@app.route('/mqtt')
def mqtt():
    # client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    # client.connect("broker.emqx.io")
    # client.loop_start()
    # client.publish("topic/to/publish", "data")
    # time.sleep(0.5)
    return "success"

@app.route('/test')
def test():
    return render_template("publisher_.html")

if __name__ == '__main__':
    app.run()
