from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def homepage():
    # return 'Hello, From Janris Foundation!'
    return render_template("index.html")