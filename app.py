
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

    all_teams = ["Hawks", "Celtics", "Nets", "Hornets", "Bulls", "Cavaliers", "Mavericks", "Nuggets", "Pistons", "Warriors", "Rockets", "Pacers", "Clippers", "Lakers", "Grizzlies", "Heat", "Bucks", "Timberwolves", "Pelicans", "Knicks", "Thunder", "Magic", "76ers", "Suns", "Trail Blazers", "Kings", "Spurs", "Raptors", "Jazz", "Wizards", "Supersonics", "Bobcats", "Bullets"]

    team = request.args.get('search-team');
    year = request.args.get('search-year')

    cantheywin = "NO";

    if team == "Warriors" and year == "2016-2017" or team == "Bulls" and year == "1995-1996":
        cantheywin = "YES"
    else:
        cantheywin = "NO"


    return render_template("results.html", team=team, year=year, cantheywin=cantheywin, all_teams=all_teams)

if os.environ.get('ENV') == 'production':
    debug = False
else:
    debug = True

if __name__ == '__main__':
    app.run(debug=debug,port=3000)
