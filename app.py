from flask import Flask
from flask import render_template
import csv
import json
import os

cd = os.path.abspath(os.getcwd())

app = Flask(__name__)

@app.route('/')
@app.route('/runs')
def my_runs():
    runs = []
    with open(f"{cd}/csvs/clean/runs.csv", "r") as runs_file:
        reader = csv.DictReader(runs_file)

        for row in reader:
            runs.append(row["map.summary_polyline"])

    return render_template("leaflet_run.html", runs = json.dumps(runs))

@app.route('/walks')
def my_walks():
    walks = []
    with open(f"{cd}/csvs/clean/walks.csv", "r") as walks_file:
        reader_walks = csv.DictReader(walks_file)

        for row in reader_walks:
            walks.append(row["map.summary_polyline"])

    return render_template("leaflet_walk.html", walks = json.dumps(walks))

if __name__ == "__main__":
    app.run(port = 5001, debug=True)