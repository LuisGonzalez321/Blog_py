from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/publicaciones')
def publicaciones():
    return render_template('publicaciones.html')