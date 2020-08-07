import serial
import threading

class SerialConsole(threading.Thread):
    def __init__(self, arduino):
        threading.Thread.__init__(self)
        self.arduino = arduino
    def run(self):
        while True:
            data = self.arduino.readline()[:-2] #the last bit gets rid of the new-line chars
            if data:
                print("SerialConsole:", data)
