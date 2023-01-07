import pandas as pd
import os


def structure_activities() -> pd.DataFrame:
    """
    Function get the initial csv with activities
    It changes the column names, drops some columns and renames other.
    Further it converts the data of certain columns.
    """
    cd = os.path.abspath(os.getcwd())
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