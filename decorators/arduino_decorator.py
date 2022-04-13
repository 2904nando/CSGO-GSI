from utils.config import BaseConfig

from connectors.arduino_adapter import ArduinoAdapter


class Arduino():

    def get_adapter(self):
        config = BaseConfig()
        arduino_adapter = ArduinoAdapter(config)
        return arduino_adapter

    def __call__(self, f):
        
        def run(**kwargs):
            
            arduino_adapter = self.get_adapter()
            
            return f(arduino_adapter=arduino_adapter, **kwargs)
                
        return run