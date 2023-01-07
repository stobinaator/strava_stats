import pandas as pd
from datetime import datetime

from download_and_save import save_split_run_based_on_year

def split(my_activities: pd.DataFrame) -> pd.DataFrame:
    
    for year in [2018, 2019, 2020, 2021, 2022, 2023]:
        print(f"Splitting activities for year {year}")
        split_year = split_run_certain_year(my_activities, year=year)
        split_year = split_year.dropna()
        save_split_run_based_on_year(split_year, year)

def split_run_certain_year(my_activities: pd.DataFrame, year: int):
    """
    Converts the start_date to object and checks if the year is equal to year
    """
    runs = pd.DataFrame()
    for _, row in my_activities[my_activities['type'] == 'Run'].iterrows():
        date_time_obj = datetime.strptime(row.start_date.split("T")[0], '%Y-%m-%d')
        if date_time_obj.year == year:
            runs = pd.concat([runs,row], axis=1)
    runs = runs.transpose()
    return runs[['id', 'map.summary_polyline']]

def split_activities_to_runs_and_walks(my_activities: pd.DataFrame) -> pd.DataFrame:
    runs_maps = my_activities[my_activities["type"] == "Run"][
            ["id", "map.summary_polyline"]
    ]
    runs_maps = runs_maps.dropna()
    walks_maps = my_activities[my_activities["type"] == "Walk"][
        ["id", "map.summary_polyline"]
    ]
    walks_maps = walks_maps.dropna()
    return runs_maps, walks_maps

