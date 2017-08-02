from flask import Flask
from flask import render_template
from requests import get
import json

app = Flask(__name__)


@app.route('/')
def index():
    url = 'http://some.host.com:8123/api/states/sensor.garage_door_status'
    headers = {'content-type': 'application/json'}
    response = get(url, headers=headers)
    garage_status = json.loads(response.text)
    return render_template('home.html', garage_status=garage_status)

