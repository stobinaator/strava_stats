import json
import os


from download_and_save import retrieve_raw_activities, save_raw, save_runs_walks, save_split_run
from structure_raw import structure_activities
from split_acts import split, return_total_runs_walks

cd = os.path.abspath(os.getcwd())
with open(f"{cd}/config_personal.json") as f:
    data = json.load(f)

def main():
    save_raw(retrieve_raw_activities(payload_dict=data))
    activities = structure_activities()
    runs, walks = return_total_runs_walks(activities)
    save_runs_walks(runs, walks)
    
    for year in [2018, 2019, 2020, 2021, 2022, 2023]:
        splitt = split(activities, year)
        save_split_run(splitt, year)

    # activities_lite = clean_up_activities(struct_activities)
    # save_cleaned_activities(activities_lite)

if __name__ == "__main__":
    main()
    print("Done! You can now run 'python3 app.py'")