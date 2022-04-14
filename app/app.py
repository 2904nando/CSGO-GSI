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

@app.route("/", methods=['POST'])
@Arduino()
def main(arduino_adapter: ArduinoAdapter):
    # arduino_adapter.send_serial_message()
    formatted_data = json.loads(request.data)
    # print(formatted_data)
    game_state.update(**formatted_data)
    # global last_action
    # last_action = formatted_data
    # with open(os.path.join(here, 'logs', f'{formatted_data["provider"]["timestamp"]}.json'), mode="w") as json_file:
    #     json.dump(formatted_data, json_file)

    print(f"Updated: {game_state.previous.udpated_topics}")
    if game_state.previous.udpated_topics:
        result = json.dumps(game_state, default=lambda o: getattr(o, '__dict__', str(o)))
        print(result)

    return "OK"

# @app.route("/last", methods=['GET'])
# def mainGET():
#     return last_action

if __name__ == "__main__":
    app.run(port=8080, debug=True)