import requests
import urllib3
import json
import os
import pandas as pd
from typing import Tuple
from datetime import datetime
from typing import List

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Setting some options for pandas
pd.set_option("display.max_columns", 83)
pd.set_option("display.max_colwidth", 25)
pd.set_option("display.max_rows", None)
pd.set_option("display.precision", 2)

AUTH_URL = "https://www.strava.com/oauth/token"
ACTIVITIES_URL = "https://www.strava.com/api/v3/athlete/activities"


DataFrameTuple = Tuple[pd.DataFrame, pd.DataFrame]

cd = os.path.abspath(os.getcwd())

def retrieve_raw_activities(payload_dict: dict) -> pd.DataFrame:
    """
    Function receives a dictionary with payload information like:
    access_token, refresh_token, etc
    It tries to get X pages each with 200 activities from strava
    Saves each page in a DF and concatenates it with the already retrieved activities
    """
    print("Downloading data...")
    res = requests.post(AUTH_URL, data=payload_dict["payload"], verify=False)
    header = {"Authorization": "Bearer " + res.json()["access_token"]}

    my_activities = pd.DataFrame()
    for page in range(1, 13):
        my_dataset = requests.get(
            ACTIVITIES_URL, headers=header, params={"per_page": 200, "page": page}
        ).json()
        my_dataframe = pd.json_normalize(my_dataset)
        my_activities = pd.concat([my_activities, my_dataframe], ignore_index=True)
    print("Data downloaded!")
    return my_activities

def save_raw(my_activities: pd.DataFrame) -> None:
    my_activities.to_csv(f"{cd}/csvs/raw/all_activities_raw.csv")

def save_split_run(run: pd.DataFrame, year:int) -> None:
    run.to_csv(f"{cd}/csvs/clean/runs_{year}.csv")
    print(f"Run for year {year} saved!")

def save_runs_walks(runs:pd.DataFrame, walks:pd.DataFrame) -> None:
    runs.to_csv(f"{cd}/csvs/clean/runs.csv")
    walks.to_csv(f"{cd}/csvs/clean/walks.csv")
    print("Normal runs/walks saved!")

def clean_up_activities(my_activities: pd.DataFrame) -> pd.DataFrame:
    """
    Function leaves only columns that matter to the user
    """
    cols = [
        "upload_id",
        "name",
        "type",
        "distance_km",
        "moving_time_min",
        "start_time",
        "start_date_local",
        "start_day_name",
        "timezone",
        "average_speed_kmh",
        "max_speed_kmh",
        "total_elevation_gain",
        "average_heartrate",
        "max_heartrate",
        "achievement_count",
        "kudos_count",
        "visibility",
    ]
    return my_activities[cols]


def save_cleaned_activities(my_acts: pd.DataFrame) -> None:
    my_acts.to_csv(f"{cd}/csvs/clean/all_activities.csv")