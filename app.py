
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

    all_teams = ["hawks", "celtics", "nets", "hornets", "bulls", "cavaliers", "mavericks", "nuggets", "pistons", "warriors", "rockets", "pacers", "clippers", "lakers", "grizzlies", "heat", "bucks", "timberwolves", "pelicans", "knicks", "thunder", "magic", "76ers", "suns", "trail blazers", "kings", "spurs", "raptors", "jazz", "wizards", "supersonics", "bobcats", "bullets"]

    team = request.args.get('search-team')
    year = request.args.get('search-year')

    cantheywin = "NO"
    display_image = "hide"
    clap = "hide"
    bullshrug = "hide"
    question = ""

    not_a_team = "That's not a team, but the Warriors could still beat them."

    if team.lower() == "warriors" and year == "2016-2017":
        cantheywin = "YES"
        clap = "show"
    else:
        cantheywin = "NO"


    if team.lower() not in all_teams:
        cantheywin = "That's not a team, but the Warriors could still beat them."

    if team.lower() == "lakers" and year == "1986-1987":
        display_image = "show"
        cantheywin = "NO"


    if team.lower() == "bulls" and year == "1995-1996":
        cantheywin = "maybe"
        bullshrug = "show"

    if cantheywin == "maybe":
        question = "?"


    return render_template("results.html", team=team, year=year, cantheywin=cantheywin, all_teams=all_teams, display_image=display_image, clap=clap, bullshrug=bullshrug, question=question)

if os.environ.get('ENV') == 'production':
    debug = False
else:
    debug = True

if __name__ == '__main__':
    app.run(debug=debug,port=3000)
