import json 
import numpy as np
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder
import colorama 
colorama.init()
from colorama import Fore, Style, Back

import random
import pickle

from flask import Flask,request
from flask_cors import CORS,cross_origin

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config['CORS_HEADERS']='Content-Type'

with open("intents.json") as file:
        data = json.load(file)
     # load tokenizer object
with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    # load label encoder object
with open('label_encoder.pickle', 'rb') as enc:
        lbl_encoder = pickle.load(enc)
        max_len = 20
    # parameters

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
@app.route("/user",methods=['POST'])
@cross_origin()
def user():
    jsony=request.json
    dataValue=jsony['message']
    responseMessage=''
    model = keras.models.load_model('chat_model')
    
    result = model.predict(keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences([dataValue]),
                                             truncating='post', maxlen=max_len))
    tag = lbl_encoder.inverse_transform([np.argmax(result)])
    for i in data['intents']:
            if i['tag'] == tag:
                responseMessage=np.random.choice(i['responses'])
        
    return  str(responseMessage)



""" def chat():
    # load trained model
    model = keras.models.load_model('chat_model')

    # load tokenizer object
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    # load label encoder object
    with open('label_encoder.pickle', 'rb') as enc:
        lbl_encoder = pickle.load(enc)

    # parameters
    max_len = 20
    
    while True:
        print(Fore.LIGHTBLUE_EX + "User: " + Style.RESET_ALL, end="")
        inp = input()
        if inp.lower() == "quit":
            break
        result = model.predict(keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences([inp]),
                                             truncating='post', maxlen=max_len))
        tag = lbl_encoder.inverse_transform([np.argmax(result)])

        for i in data['intents']:
            if i['tag'] == tag:
                print(Fore.GREEN + "ChatBot:" + Style.RESET_ALL , np.random.choice(i['responses']))

        # print(Fore.GREEN + "ChatBot:" + Style.RESET_ALL,random.choice(responses))
 """
""" print(Fore.YELLOW + "Start messaging with the bot (type: ""quit"" to stop)!" + Style.RESET_ALL)
chat()
 """