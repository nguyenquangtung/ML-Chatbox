from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
from chatbox import get_response
import subprocess
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT_DIR)

# Check if intents change
size = os.path.getsize("intents.json")
check = ""

with open('intent_size.txt', 'r') as temp_file:
    check = temp_file.readline()

if str(size) == check:
    print(" No changes in Intents file")
else:
    open('intent_size.txt', 'w').close()
    with open('intent_size.txt', 'w') as temp_file:
        temp_file.write(str(size))
    subprocess.run(["python training.py"])

#########################################################

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.get("/")
def index_get():
    return render_template("base.html")


@app.post("/predict")
def userchat():
    text = request.get_json().get("message")  # check if text is valid
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)
