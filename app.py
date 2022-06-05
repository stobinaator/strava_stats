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

@app.route('/runs-2021')
def my_runs_2021():
    runs_2021 = []
    with open(f"{cd}/csvs/clean/runs_2021.csv", "r") as runs_file:
        reader = csv.DictReader(runs_file)

        for row in reader:
            runs_2021.append(row["map.summary_polyline"])

    return render_template("leaflet_run_2021.html", runs = json.dumps(runs_2021))

@app.route('/runs-2022')
def my_runs_2022():
    runs_2022 = []
    with open(f"{cd}/csvs/clean/runs_2022.csv", "r") as runs_file:
        reader = csv.DictReader(runs_file)

        for row in reader:
            runs_2022.append(row["map.summary_polyline"])

    return render_template("leaflet_run_2022.html", runs = json.dumps(runs_2022))

@app.route('/walks')
def my_walks():
    walks = []
    with open(f"{cd}/csvs/clean/walks.csv", "r") as walks_file:
        reader_walks = csv.DictReader(walks_file)

        for row in reader_walks:
            walks.append(row["map.summary_polyline"])

    return render_template("leaflet_walk.html", walks = json.dumps(walks))

if __name__ == "__main__":
    app.run(port = 5002, debug=True)