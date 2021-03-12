from flask import Flask, request, jsonify
import time
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # enable cors for all origins

@app.route('/time')
def get_current_time():

    response = { }

    # set some values on the response
    response["time"] = time.time()

    # Return the response in json format
    return jsonify(response)

# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)