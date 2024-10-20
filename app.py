from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f'Hello, World! Current date and time: {current_time}'
