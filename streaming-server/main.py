
import time
import logging
import os
from threading import Thread
import subprocess
import json

from flask import Flask,Response
from flask import request
from flask import json
# from flask_cors import CORS
import platform
from werkzeug.utils import secure_filename


app = Flask(__name__)
# CORS(app)

def stream_reponse(counter=10,sleep=3):
    for i in range(0, counter):
        print(i)
        yield(str(i)+'\n')
        time.sleep(sleep)
    yield("Good bye!\n")


@app.route('/stream', methods = ['POST'])
def samd_update():
    counter = 10
    waitTime = 1
    if 'counter' in request.args:
        counter = int(request.args.get('counter'))
    if 'wait' in request.args:
        waitTime = int(request.args.get('wait'))
    print(counter, waitTime)
    return Response(stream_reponse(counter,waitTime), mimetype='text/html')


if __name__ == '__main__':
    print("Running webserver")
    port = os.getenv('IOTEDGE_PORT', 8084)
    app.run(debug=True,port=port,host='0.0.0.0')