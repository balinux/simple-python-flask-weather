from flask import Flask, render_template, request

import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/temperature', methods=['POST'])
def temperature():
    country = request.form['country']
    requesData = requests.get('https://samples.openweathermap.org/data/2.5/weather?q=' +
                              country+'&appid=b6907d289e10d714a6e88b30761fae22')
    json_object = requesData.json()
    temp_k = float(json_object['main']['temp'])
    return render_template('temperature.html', temp=temp_k)

@app.route('/temperatureapi', methods=['POST'])
def temperatureapi():
    country = request.form['country']
    requesData = requests.get('https://samples.openweathermap.org/data/2.5/weather?q=' +
                              country+'&appid=b6907d289e10d714a6e88b30761fae22')
    json_object = requesData.text
    return json_object


if __name__ == '__main__':
    app.run(debug=True)
