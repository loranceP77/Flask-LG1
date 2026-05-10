from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/') 
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/')
def index():
    flowers = load_data()
    return render_template('index.html', flowers=flowers)

import json

@app.route('/')
def index():
    flowers = load_data()
    return render_template('index.html', flowers=flowers)
