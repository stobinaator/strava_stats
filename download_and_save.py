import requests
import urllib3
import os
import pandas as pd

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Setting some options for pandas
pd.set_option("display.max_columns", 83)
pd.set_option("display.max_colwidth", 25)
pd.set_option("display.max_rows", None)
pd.set_option("display.precision", 2)

AUTH_URL = "https://www.strava.com/oauth/token"
ACTIVITIES_URL = "https://www.strava.com/api/v3/athlete/activities"
ACTIVITIES_PER_PAGE = 200
PAGES_TO_REQUEST = 13

cd = os.path.abspath(os.getcwd())
cd_csvs = f'{cd}/csvs'

def download_raw_activities(payload_dict: dict) -> pd.DataFrame:
    """
    Function queries Strava API for activities. Each request awaits a page with 200.
    """
    print("Downloading data...")
    res = requests.post(AUTH_URL, data=payload_dict["payload"], verify=False)
    header = {"Authorization": "Bearer " + res.json()["access_token"]}

    my_activities = pd.DataFrame()
    for page in range(1, PAGES_TO_REQUEST):
        my_dataset = requests.get(
            ACTIVITIES_URL, headers=header, params={"per_page": ACTIVITIES_PER_PAGE, "page": page}
        ).json()
        my_dataframe = pd.json_normalize(my_dataset)
        my_activities = pd.concat([my_activities, my_dataframe], ignore_index=True)
    print("Data downloaded!")
    return my_activities

def save_initial_activities(my_activities: pd.DataFrame) -> None:
    my_activities.to_csv(f"{cd_csvs}/raw/all_activities_raw.csv")

def save_split_run_based_on_year(run: pd.DataFrame, year:int) -> None:
    run.to_csv(f"{cd_csvs}/clean/runs_{year}.csv")
    print(f"Run for year {year} saved!")

def save_runs_walks(runs:pd.DataFrame, walks:pd.DataFrame) -> None:
    runs.to_csv(f"{cd_csvs}/clean/runs.csv")
    walks.to_csv(f"{cd_csvs}/clean/walks.csv")
    print("Normal runs/walks saved!")

def save_cleaned_activities(my_acts: pd.DataFrame) -> None:
    my_acts.to_csv(f"{cd_csvs}/clean/all_activities.csv")