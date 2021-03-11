from flask import Flask, request, jsonify
import time
app = Flask(__name__)

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