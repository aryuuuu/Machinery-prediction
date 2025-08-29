import os
# Suppress oneDNN warnings
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

from flask import Flask, request, jsonify, render_template
from md import answer
app = Flask(__name__)
 
 
@app.route("/")
def index():

    return render_template("index.html", failure=None)
 
@app.route('/data', methods=["POST", "GET"])
def login():
    # Get form data
    type_value = request.form.get('type', '').upper()
    air_temp = float(request.form.get('air', 0))
    proc_temp = float(request.form.get('proc', 0))
    rpm = float(request.form.get('rpm', 0))
    torque = float(request.form.get('torque', 0))
    tool_wear = float(request.form.get('tool', 0))
    
    # Convert Type to numerical encoding (L=0, M=1, H=2)
    type_mapping = {'L': 0, 'M': 1, 'H': 2}
    type_encoded = type_mapping.get(type_value, 1)  # Default to M=1 if invalid input
    
    # Create input array in the correct order
    inps = [type_encoded, air_temp, proc_temp, rpm, torque, tool_wear]
    
    failure = answer(inps)
    return render_template("index.html", failure=failure)

if __name__ == '__main__':
    app.run(debug=True, port=8123)
