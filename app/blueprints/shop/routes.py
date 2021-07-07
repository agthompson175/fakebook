from flask import render_template, url_for
from .import bp as app


@app.route('/products')
def products():
    return 'THIS products WORKS'


@app.route('/cart')
def cart():
    return 'THIS cart WORKS'


@app.route('/success')
def success():
    return 'THIS success WORKS'


@app.route('/failure')
def failure():
    return 'THIS failure WORKS'
