from flask import Flask, request

import sys
import os

import json

here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(here, ".."))

from connectors.arduino_adapter import ArduinoAdapter
from decorators.arduino_decorator import Arduino
from lib.models.GameState import GameState

app = Flask(__name__)

game_state = GameState()
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/", methods=['POST'])
@Arduino()
def main(arduino_adapter: ArduinoAdapter):
    # arduino_adapter.send_serial_message()
    formatted_data = json.loads(request.data)
    game_state.update(**formatted_data)

    print(f"Updated: {game_state.previous.udpated_topics}")
    print(f"Added: {game_state.added.added_topics}")
    if game_state.previous.udpated_topics or game_state.added.added_topics:
        result = json.dumps(game_state, default=lambda o: getattr(o, '__dict__', str(o)))
        print(result)

    return "OK"

@app.route("/", methods=['GET'])
def main_get():
    response = app.response_class(
        response=json.dumps(game_state, default=lambda o: getattr(o, '__dict__', str(o))),
        status=200,
        mimetype="application/json"
    )
    return _build_cors_preflight_response(response)

def _build_cors_preflight_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080, debug=True)