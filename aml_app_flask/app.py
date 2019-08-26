from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)


@app.route('/')
def form1():
    return render_template('index.html')


@app.route('/', methods = ['POST'])
def sentiment_value():
    text = request.form['sentiment']
    output = jsonify(text)
    url = 'http://b4bd3ab7-7138-4500-bc07-d733549eb37b.eastus2.azurecontainer.io/score'
    headers = {'Content-Type' : 'application/json'}
    r = requests.post(url, text, headers=headers)
    score = r.text
    
    # output = text
    # return """<p>The content is {}</p>""".format(output)
    return score

# @app.route('/b4bd3ab7-7138-4500-bc07-d733549eb37b.eastus2.azurecontainer.io/score', methods = ['POST'])
# def sentiment_post():
#     text = request.form['sentiment']
#     return {{
#   method: 'post',
#   body: JSON.stringify(data),
#   headers: { 'Content-type': 'application/json' }
# })

# @app.route('/', methods = ['POST'])
# def sentiment_value():
#     text = request.form['sentiment']
#     output = text
#     # text = text.upper()
#     url = 'http://b4bd3ab7-7138-4500-bc07-d733549eb37b.eastus2.azurecontainer.io/score'
#     data = {'body': output, 
#             'link':url}
#     js = json.dumps(data)
#     return 



if __name__ == '__main__':
    app.run(debug=True)
