import json

import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    df = pd.read_csv('d3Example/data/data.csv').drop('Open', axis=1)
    chart_data = df.to_dict(orient='records')
    chart_data = json.dumps(chart_data, indent=2)
    data = {'chart_data': chart_data}
    return render_template('raw.html', data=data)

@app.route("/temporary")
def index_temporary():
    df = pd.read_csv('d3Example/data/data.csv').drop('Open', axis=1)
    chart_data = df.to_dict(orient='records')
    chart_data = json.dumps(chart_data, indent=2)
    data = {'chart_data': chart_data}
    return render_template('index.html', data=data)

@app.route("/piproject")
def pi_project():
    df_table = pd.read_csv('d3Example/data/data.csv').drop('Open', axis=1)
    return render_template('index2.html', table = df_table) 

@app.route("/simple")
def simple():
    df_table2 = pd.read_csv('d3Example/data/data.csv').drop('Open', axis=1)
    return render_template('simple.html', data = df_table2)
    # return 'hello world'


if __name__ == "__main__":
    app.run(debug=True)
