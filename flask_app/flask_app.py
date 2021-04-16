from flask import Flask, jsonify, request, render_template
import numpy as np

app = Flask(__name__, template_folder='templates', static_folder='./static')

@app.route('/')
def home():
    message='microservice is running'
    return render_template('index.html', message=message)


if __name__ == '__main__':

    app.run(debug=True)