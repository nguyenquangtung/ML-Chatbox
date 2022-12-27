import os
import subprocess

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT_DIR)
size = os.path.getsize("intents.json")
check = ""

with open('intent_size.txt', 'r') as temp_file:
    check = temp_file.readline()

if str(size) == check:
    print("True")
else:
    open('intent_size.txt', 'w').close()
    with open('intent_size.txt', 'w') as temp_file:
        temp_file.write(str(size))
    subprocess.run(["python training.py"])
