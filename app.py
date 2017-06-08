
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_modus import Modus
import sys
import os

app = Flask(__name__)


@app.route('/', methods=[ "GET"])
def search():
    return render_template("index.html")


@app.route('/results', methods=[ "GET"])
def results():
    team = request.args.get('search-team');
    year = request.args.get('search-year')
    return render_template("results.html", team=team, year=year)

if os.environ.get('ENV') == 'production':
    debug = False
else:
    debug = True

if __name__ == '__main__':
    app.run(debug=debug,port=3000)
