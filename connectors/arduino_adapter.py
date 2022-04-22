import serial

import sys
import os

here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(here, ".."))

from utils.config import BaseConfig

class ArduinoAdapter():

    def __init__(self, configs):
        self.configs = configs
        self.base_config = "serial"

        self.port = self.configs.get_config(self.base_config, "com_port")
        self.baudrate = self.configs.get_config(self.base_config, "baudrate")

        try:
            self.arduino = serial.Serial(port=self.port, baudrate=self.baudrate, timeout=.1)
        except Exception as e:
            print("Serial error")

    def send_serial_message(self, message):
        # arduino = serial.Serial(port=self.port, baudrate=self.baudrate, timeout=.1)
        print(f"Enviando {message} serial na porta {self.port}, Baudrate {self.baudrate}")
        self.arduino.write(bytes(message, 'utf-8'))

# arduino_adapter = ArduinoAdapter(BaseConfig())

# print("teste")