import flask
import json
import os
import os
# import dialogflow
import requests
import json
# import pusher
from flask import Flask, request, jsonify, render_template

app = flask.Flask(__name__)


@app.route('/')
def home():
    return "Hello world"


@app.route('/', methods=['POST'])
def webhook():
    req = request.get_json(force=True)
    print(req)

    return {
        'fulfillmentText': 'Hello from the bot world'
    }


if __name__ == "__main__":
    # app.secret_key = 'ItIsASecret'
    app.debug = True
    app.run(debug=True, port=5000)
