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

def open_csv_get_polyline(year):
    runs_XXXX = []
    with open(f"{cd}/csvs/clean/runs_{year}.csv", "r") as runs_file:
        reader = csv.DictReader(runs_file)

        for row in reader:
            runs_XXXX.append(row["map.summary_polyline"])
    return runs_XXXX

@app.route('/runs-2018')
def my_runs_2018():
    runs = open_csv_get_polyline(2018)

    return render_template("leaflet_run_2x.html", year = 2018, runs = json.dumps(runs))

@app.route('/runs-2019')
def my_runs_2019():
    runs = open_csv_get_polyline(2019)

    return render_template("leaflet_run_2x.html", year = 2019, runs = json.dumps(runs))
    
@app.route('/runs-2020')
def my_runs_2020():
    runs = open_csv_get_polyline(2020)

    return render_template("leaflet_run_2x.html", year = 2020, runs = json.dumps(runs))

@app.route('/runs-2021')
def my_runs_2021():
    runs = open_csv_get_polyline(2021)
   
    return render_template("leaflet_run_2x.html", year = 2021, runs = json.dumps(runs))

@app.route('/runs-2022')
def my_runs_2022():
    runs = open_csv_get_polyline(2022)

    return render_template("leaflet_run_2x.html", year = 2022, runs = json.dumps(runs))

@app.route('/runs-2023')
def my_runs_2023():
    runs = open_csv_get_polyline(2023)

    return render_template("leaflet_run_2x.html", year = 2023, runs = json.dumps(runs))

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