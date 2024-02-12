# Script for my "Thorsten-Voice" step-by-step tutorial on "Running a local Piper TTS server and use it with Python on Linux"
# https://youtu.be/pLR5AsbCMHs

import requests

textToSpeak = "This is a text to be spoken using the locally running Piper TTS server process."
urlPiper = "http://localhost:5000"
outputFilename = "output.wav"

payload = {'text': textToSpeak}

r = requests.get(urlPiper,params=payload)

with open(outputFilename, 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)
