from flask import Flask
from flask import render_template
import csv
import json
import os

cd = os.path.abspath(os.getcwd())

app = Flask(__name__)

@app.route('/runs')
def my_runs():
    runs = []
    with open(f"{cd}/csvs/clean_runs.csv", "r") as runs_file:
        reader = csv.DictReader(runs_file)

        for row in reader:
            runs.append(row["polyline"])

    return render_template("leaflet_run.html", runs = json.dumps(runs))

@app.route('/walks')
def my_walks():
    walks = []
    with open(f"{cd}/csvs/clean_walks.csv", "r") as walks_file:
        #reader_walks = csv.reader(walks_file, delimiter=',')
        reader_walks = csv.DictReader(walks_file)

        for row in reader_walks:
            #walks.append(row[1])
            walks.append(row["polyline"])

    return render_template("leaflet_walk.html", walks = json.dumps(walks))

@app.route('/both')
def my_activities():
    runs = []
    walks = []
    with open(f"{cd}/csvs/clean_runs.csv", "r") as runs_file, open(f"{cd}/csvs/clean_runs.csv", "r") as walks_file:
        r_reader = csv.DictReader(runs_file)
        w_reader = csv.DictReader(walks_file)

        for row in r_reader:
            runs.append(row["polyline"])

        for row in w_reader:
            walks.append(row["polyline"])


    return render_template("leaflet_mix.html", runs = json.dumps(runs), walks = json.dumps(walks))


if __name__ == "__main__":
    app.run(port = 5001)