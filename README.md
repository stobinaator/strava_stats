>![](thumbnails/KA-run.jpg)

# strava_running
Tutorial to follow: </br>
https://towardsdatascience.com/using-the-strava-api-and-pandas-to-explore-your-activity-data-d94901d9bfde </br>
Video walkthrough: </br>
https://www.youtube.com/watch?v=2FPNb1XECGs&list=PLO6KswO64zVvcRyk0G0MAzh5oKMLb6rTW&index=4 </br>

- gets 1 page with 200 activities. </br>
- Dataset is converted to a Pandas DataFrame and columns are renamed and certain values converted. </br>
- after the cleanup process only a certain amount of columns are taken for the next step (this can be easily changed).

# get_all_run_walk_activities
- gets 10 pages each with 200 activities (if so many exists. </br>
- only the `Run` and `Walk` activities are taken where the main information is `activity_id` and `summary_polyline` of the map and saved to a csv file. </br>
- drop some rows that have no meaningful information in them, save the cleaned DFs to new files.

# leaflet_walk.html / leaflet_run.html 
- these 2 files are visualizing the information that is being taken from the csv files with the help of app.py file.

To start the Flask instance just run `python app.py`. </br>
Open your browser http://127.0.0.1:5001/X , X can be runs or walks. </br>