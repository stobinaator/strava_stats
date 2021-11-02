>![](thumbnails/KA-run.jpg)
>![](thumbnails/KA-walk.jpg)
>![](thumbnails/VT-run.jpg)

>![](thumbnails/relplot_run.jpg)
>![](thumbnails/violinplot_run.jpg)
>![](thumbnails/max_speed_dist.jpg)
>![](thumbnails/countplot_runs.jpg)
>![](thumbnails/barplot_activities.jpg)

## tutorials
Tutorial to follow: </br>
https://towardsdatascience.com/using-the-strava-api-and-pandas-to-explore-your-activity-data-d94901d9bfde </br>
Video walkthrough: </br>
https://www.youtube.com/watch?v=2FPNb1XECGs&list=PLO6KswO64zVvcRyk0G0MAzh5oKMLb6rTW&index=4 </br>

## strava_activities.ipynb
- Getting a couple of pages, each with 200 activities.</br>
- Original raw DataFrame is saved to a .csv file. </br>
- `Run` & `Walk` are filtered and saved </br>
- Activities dataset is converted to a Pandas DataFrame and columns are renamed and certain values converted. After that only a certain amount of colums are left for the next steps. Again saved.</br>
- Data now again read and can be visualized with different graphs (seaborn) </br>

## templates/leaflet_*.html 
- `app.py` reads run/walk.csvs, takes polyline information and forwards it to the 2 template files - one for each activity - to visualize them.

## start
- To start the Flask instance - run in terminal `python app.py`. </br>
- Open your browser http://127.0.0.1:5001/X , X can be runs or walks. </br>

## TODO
1. overlay all run and walk workouts with different colors.
