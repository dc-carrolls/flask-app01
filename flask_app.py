
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def hello_world():
    return render_template('main_page.html')

@app.route('/test')
def test_page():
    return '<h1>This is a test</h1>'
