import json
import os


from download_and_save import download_raw_activities, save_initial_activities, save_runs_walks, save_cleaned_activities
from structure_and_cleanup import structure_activities, clean_up_activities
from split_acts import split, split_activities_to_runs_and_walks

cd = os.path.abspath(os.getcwd())
with open(f"{cd}/config_personal.json") as f:
    data = json.load(f)

def main():
    save_initial_activities(download_raw_activities(payload_dict=data))
    activities = structure_activities()
    runs, walks = split_activities_to_runs_and_walks(activities)
    save_runs_walks(runs, walks)
    
    split(activities)

    # activities_lite = clean_up_activities(activities)
    # save_cleaned_activities(activities_lite)

if __name__ == "__main__":
    main()
    print("Done! You can now run 'python3 app.py'")