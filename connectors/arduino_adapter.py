
class ArduinoAdapter():

    def __init__(self, configs):
        self.configs = configs
        self.base_config = "serial"

    def send_serial_message(self):
        com_port = self.configs.get_config(self.base_config, "com_port")
        baudrate = self.configs.get_config(self.base_config, "baudrate")
        print(f"Enviando mensagem serial na porta {com_port}, Baudrate {baudrate}")