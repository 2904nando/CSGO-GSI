from flask import Flask

import sys
import os

here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(here, ".."))

from connectors.arduino_adapter import ArduinoAdapter
from decorators.arduino_decorator import Arduino

app = Flask(__name__)

@app.route("/")
@Arduino()
def main(arduino_adapter: ArduinoAdapter):
    arduino_adapter.send_serial_message()
    return "Teste"

if __name__ == "__main__":
    app.run(port=8080, debug=True)