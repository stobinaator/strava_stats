>![](thumbnails/KA-run.jpg)
>![](thumbnails/KA-walk.jpg)
>![](thumbnails/VT-run.jpg)

>![](thumbnails/avg_speed_dist.jpg)
>![](thumbnails/max_speed_dist.jpg)
>![](thumbnails/countplot_runs.jpg)
>![](thumbnails/barplot_activities.jpg)

## tutorials
Tutorial to follow: </br>
https://towardsdatascience.com/using-the-strava-api-and-pandas-to-explore-your-activity-data-d94901d9bfde </br>
Video walkthrough: </br>
https://www.youtube.com/watch?v=2FPNb1XECGs&list=PLO6KswO64zVvcRyk0G0MAzh5oKMLb6rTW&index=4 </br>

## strava_activities.ipynb
- Tries getting 99 pages each with 200 activities. (if so many exist)</br>
- Original raw DataFrame is saved to a .csv file. </br>
- `Run` & `Walk` are filtered and saved raw. </br>
- Cleanup run/walk and save again. Activities dataset is converted to a Pandas DataFrame and columns are renamed and certain values converted. </br>
- After the cleanup process only a certain amount of columns are taken for the next step.</br>
- The cleaned DataFrame is saved to a .csv file. </br>
- Data is again read and visualized with different graphs (seaborn) </br>

## templates/leaflet_*.html 
- `app.py` reads run/walk.csvs, takes polyline information and forwards it to the 2 template files - one for each activity - to visualize them.

## start
- To start the Flask instance - run in terminal `python app.py`. </br>
- Open your browser http://127.0.0.1:5001/X , X can be runs or walks. </br>

## TODO
1. overlay all run and walk workouts with different colors.
