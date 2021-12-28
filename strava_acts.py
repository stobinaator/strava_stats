import requests
import urllib3
import json
import os
import pandas as pd
from typing import Tuple

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Setting some options for pandas
pd.set_option("display.max_columns", 83)
pd.set_option("display.max_colwidth", 25)
pd.set_option("display.max_rows", None)
pd.set_option("display.precision", 2)

AUTH_URL = "https://www.strava.com/oauth/token"
ACTIVITIES_URL = "https://www.strava.com/api/v3/athlete/activities"


cd = os.path.abspath(os.getcwd())
with open(f"{cd}/config_personal.json") as f:
    data = json.load(f)

DataFrameTuple = Tuple[pd.DataFrame, pd.DataFrame]


def retrieve_raw_activities(payload_dict: dict) -> pd.DataFrame:
    """
    Function receives a dictionary with payload information like:
    access_token, refresh_token, etc
    It tries to get X pages each with 200 activities from strava
    Saves each page in a DF and concatenates it with the already retrieved activities
    """
    print("Downloading data")
    res = requests.post(AUTH_URL, data=payload_dict["payload"], verify=False)
    header = {"Authorization": "Bearer " + res.json()["access_token"]}

    my_activities = pd.DataFrame()
    for page in range(1, 8):
        my_dataset = requests.get(
            ACTIVITIES_URL, headers=header, params={"per_page": 200, "page": page}
        ).json()
        my_dataframe = pd.json_normalize(my_dataset)
        my_activities = pd.concat([my_activities, my_dataframe], ignore_index=True)
    print("Data downloaded!")
    return my_activities


def save_raw(my_activities: pd.DataFrame) -> None:
    my_activities.to_csv(f"{cd}/csvs/raw/all_activities_raw.csv")


def structure_activities() -> pd.DataFrame:
    """
    Function retrieves the raw activities and does a couple of things
    in order to clean up the data a bit.
    It changes the column names, drops some columns and renames other.
    Further it converts the data of certain columns.
    """
    return (
        pd.read_csv(f"{cd}/csvs/raw/all_activities_raw.csv")
        .rename(columns=str.lower)
        .drop(["unnamed: 0", "resource_state"], axis=1)
        .rename(
            columns={
                "average_speed": "average_speed_mps",
                "max_speed": "max_speed_mps",
                "moving_time": "moving_time_s",
                "elapsed_time": "elapsed_time_s",
            }
        )
        .assign(
            start_date_local=lambda x: pd.to_datetime(x["start_date_local"]),
            start_time=lambda x: x["start_date_local"].dt.time,
        )
        .assign(
            start_date_local=lambda x: x["start_date_local"].dt.strftime("%Y/%m/%d"),
            timezone=lambda x: pd.Categorical(
                x["timezone"].str.split(" ").str[-1],
            ),
        )
        .assign(
            start_date_local=lambda x: pd.to_datetime(x["start_date_local"]),
            start_day_name=lambda x: pd.Categorical(
                x["start_date_local"].dt.strftime("%A")
            ),
            moving_time_min=lambda x: pd.to_datetime(
                x["moving_time_s"], unit="s"
            ).dt.strftime("%H:%M:%S"),
            average_speed_kmh=lambda x: x["average_speed_mps"] * (18 / 5),
            max_speed_kmh=lambda x: x["max_speed_mps"] * (18 / 5),
            distance_km=lambda x: x[(x["type"] == "Run") | (x["type"] == "Walk")][
                "distance"
            ]
            / 1000,
            visibility=lambda x: pd.Categorical(x["visibility"]),
            name=lambda x: pd.Categorical(x["name"]),
            type=lambda x: pd.Categorical(x["type"]),
        )
    )


def split_activities(my_activities: pd.DataFrame) -> DataFrameTuple:
    """
    Functions splits the cleaned up activities in 2 further subcategories:
    run_maps and walk_maps and drops any NaN. The 2 maps will be used
    for visualization with Flask.
    """
    runs_maps = my_activities[my_activities["type"] == "Run"][
        ["id", "map.summary_polyline"]
    ]
    walks_maps = my_activities[my_activities["type"] == "Walk"][
        ["id", "map.summary_polyline"]
    ]
    runs_maps = runs_maps.dropna()
    walks_maps = walks_maps.dropna()
    return runs_maps, walks_maps


def save_runs_walks(runs_maps: pd.DataFrame, walks_maps: pd.DataFrame) -> None:
    runs_maps.to_csv(f"{cd}/csvs/clean/runs.csv")
    walks_maps.to_csv(f"{cd}/csvs/clean/walks.csv")


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


def main() -> None:
    save_raw(retrieve_raw_activities(payload_dict=data))

    struct_activities = structure_activities()
    runs_maps, walks_maps = split_activities(struct_activities)
    save_runs_walks(runs_maps, walks_maps)

    activities_lite = clean_up_activities(struct_activities)
    save_cleaned_activities(activities_lite)


if __name__ == "__main__":
    main()
    print("Done!")
