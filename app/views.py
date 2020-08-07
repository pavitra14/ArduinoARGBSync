from flask import render_template, request
from app import app
from utils import *

com_ports = serial_ports()
@app.route('/', methods=["GET", "POST"])
def index():
    data_sent = False
    if request.method == "POST":
        data = request.form
        handle_change(data)
        data_sent = True
    return render_template('index.html', title = get_computer_name(), ports = com_ports, modes = PRESETS, signal_sent = data_sent)
