# StatLock

StatLock is inspired by 25 years of playing pool for the American Poolplayers Association. If you've played any type of sport involving a handicap, you know the ratings come from somewhere. For the APA, ratings are based on a player's most recent 20 matches. The current APA website/app allows a player to see a current session win/loss record(max 16 weeks) or a lifetime view. There is nowhere to view the most recent 20 matches played without manual tracking. For the last 5 years, my team has tracked each player's performance on an Excel spreadsheet, but I believed there should be a better way.


## Stat Tracker was built to allow a team "captain" to:
  * At a glance see skill ratings at a team level
  * See individual player details showing performance for last 20 matches
  * Track weekly play by each player at a touch and save that data for future use
  * Be able to update player ratings as they change through league play
  * Generate a potential lineup card based on current team skill level ratings.
  
 
 ## Table of Contents
  * [Project Requirements and Features List](#project-requirements-and-features-list)
  * [Technologies Used](#technologies-used)
  * [Installing and Launching StatLock](#instructions-for-installing-statlock)
  * [Entity Relationship Diagram](#entity-relationship-diagram)
  * [Code that grew my abilities](https://github.com/JohnALong/stat_lock/blob/master/statlock/statlockapp/views/lineups/opplineup.py)
  

## Project Requirements and Features List
### Get Started
When a user registers an account they will be directed to the Home page.  There they will be able to choose from two options.
If the user was able to select their team from the available drop down choices on Register, they will select the My Team button.
If New Team was selected during Register, the Add Team button will be selected.  This will enable a user to create a new team.
### Players for a team
If a Team was selected during Register, then that team will be populated by existing players in the League that are on that team.
Creating a new team, will require a user to add their players to the roster.  A user will be on the Team view after completing 
team creation.  From there selecting Add Player will allow the user to fill their roster.  Once the roster is completed, the
user is ready to begin tracking the weekly 8 ball and 9 ball matches of his/her players.
### Creating matches
From the team view, a user will select the Match Entry button to create a match.  All players will be available for selection along with the match type and whether the match was won or lost.
### Tracking/Correcting matches
To see a players last 20 matches, select the player name to be take to a details view of that player.  A user will
be given a listing of up to 20 matches played for both 8 ball and 9 ball along with the players winning percentage.
A user will also be able to edit a match to make corrections in the event of incorrect entry for either the match type or
match won.
### Team Lineup Changes
In the event a player leaves a team, selecting that players personal view will allow a user to delete that player from the 
roster.  Then, a user can add a new player to the roster and begin tracking their performance.
### Possible Lineup Combinations
An APA team consists of a maximum of 8 players of which only 5 play on any given night.  The 5 players combined skill levels
may not go over 23.  To assist a user in determining their lineup, StatLock has a lineup generator available from the team
view.  Selecting this will allow a user to see all possible combinations of 5 players the sum of which are under 24.
From this lineup view, a user can also select to see how their opponent skill levels can be combined to create a lineup,
and compare them to each other.

## Technologies Used
* Python/Django
* HTML
* CSS
* Bootstrap

## Instructions for Installing StatLock
* Clone repo and cd into it
* `cd statlock`

* Create your OSX virtual environment in Terminal:
  * `python -m venv statlockenv`
  * `source ./statlockenv/bin/activate`
  
* or Create your Windows virtual environment in Command Line:
  * `python -m venv statlockenv`
  * `source ./statlockenv/Scripts/activate`
  
* Install the app dependencies:
  * `pip install -r requirements.txt`
  
* Build your database from existing models:
  * `python manage.py makemigrations statlockapp`
  * `python manage.py migrate`
  
* Populate your database with initial data from fixtures (follow order listed)
  * `python manage.py loaddata teams`
  * `python manage.py loaddata players`
  * `python manage.py loaddata matchtypes`
  * `python manage.py loaddata matches`
  
* Upon server start user will be able to register a Captain and select a listed team or select New Team to create their own.
  * `python manage.py runserver`
  * open a browser and and access the application
  * http://localhost:8000
  
### Congratulations!  You are now using StatLock!

## Entity Relationship Diagram
* [StatLock ERD at dbdiagram](https://dbdiagram.io/d/5dc2d032edf08a25543d979d)
  






















