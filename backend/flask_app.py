from flask import Flask, jsonify, request, render_template
import numpy as np

app = Flask(__name__, template_folder='./templates', static_folder='./static')

@app.route('/',methods=['GET',])
def home():
    return render_template('index.html')

@app.route('/heartbeat')
def heartbeat():

    return jsonify({"backend_status":"OK"})


if __name__ == '__main__':

    app.run(debug=True)