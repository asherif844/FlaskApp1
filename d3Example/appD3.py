from flask import Flask, render_template, jsonify
import json 


app = Flask(__name__)

@app.route('/weather_data_json')
def main():
    with open('d3Example/data/nyc_weather_data.json') as json_file:
        data = json.load(json_file)
    return jsonify(data)

@app.route('/d3')
def d3main():
    with open('d3Example/data/nyc_weather_data.json') as weather_file:
        weather = json.load(weather_file)
    return render_template('d3template.html', data = weather)


if __name__ == '__main__':
    app.run(debug = True)