import flask
import json
import os
import os

import requests
import json
# import pusher
from flask import request

app = flask.Flask(__name__)


@app.route('/')
def home():
    return "Hello world"


@app.route('/', methods=['POST'])
def webhook():
    req = request.get_json(force=True)
    print("hello world")
    print(req)
    try:
        if req:
            print('The response Id ,{}'.format(req['responseId']))
            print('Text received from User: ,{}'.format(req['queryResult']['queryText']))
            intent_name = req['queryResult']['intent']['displayName']
            print('The intent discovered, {}'.format(req['queryResult']['intent']['displayName']))
        if intent_name == "Enzo_navigate":
            return {
                'fulfillmentText': 'Do you want to make sure?'
            }
        else:
            return {
                'fulfillmentText': 'I need more training to reply you better'
            }

    except:
        print("Error")
        return {
            'fulfillmentText': 'Sorry , I could not understand. Please try again'
        }


if __name__ == "__main__":
    app.run(debug=True, port=5000)
