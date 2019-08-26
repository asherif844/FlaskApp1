from flask import Flask, render_template

app = Flask(__name__)

@app.route('/test')
def index():
    return 'Wolf-PAC Florida'


@app.route('/')
def homepage():
    return render_template("/home.html", title="Home")

def main():
    app.run(debug = True)



if __name__ == '__main__':
    main()