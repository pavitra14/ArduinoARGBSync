import sys
import glob
import serial
import serial.tools.list_ports
import socket
import time
from SerialConsole import SerialConsole
def serial_ports():
    ports = list(serial.tools.list_ports.comports())
    result = {}
    for p in ports:
        result[p.device] = p.description
    return result

def get_computer_name():
    return socket.gethostname()

PRESETS = {
    "MODE_RAINBOW": "1",
    "MODE_RAINBOW_CYCLE": "2",
    "MODE_RAINBOW_THEATRE": "3",
    "MODE_THEATRE_WHITE": "4",
    "MODE_THEATRE_RED": "5",
    "MODE_THEATRE_GREEN": "6",
    "MODE_THEATRE_BLUE": "7",
    "MODE_RED": "8",
    "MODE_GREEN": "9",
    "MODE_BLUE": "10",
    "MODE_WHITE": "CUSTOM#255#255#255",
    "MODE_CUSTOM": "11",
    "MODE_MOVE": "12",
    "CHANGE_WAIT_TIME_1": "WT#1",
    "CHANGE_WAIT_TIME_5": "WT#5",
    "CHANGE_WAIT_TIME_10": "WT#10",
    "CHANGE_WAIT_TIME_20": "WT#20",
    "CHANGE_WAIT_TIME_30": "WT#30",
    "CHANGE_WAIT_TIME_40": "WT#40",
    "CHANGE_WAIT_TIME_50": "WT#50"
}

def handle_change(data):
    selected_com = data['selectedPort']
    argb_mode = data['argbMode']
    argb_value = data['customARGB']
    a = serial.Serial(selected_com, 9600, timeout=.1)
    time.sleep(5)
    instruction = argb_mode if argb_mode != PRESETS['MODE_CUSTOM'] else "CUSTOM#"+argb_value
    a.write(bytearray(instruction, 'utf-8'))
    a.close()


if __name__ == '__main__':
    print(serial_ports())