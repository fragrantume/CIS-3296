# CIS-3296 - Number Game

## Purpose
To run a simulation of an AI hackathon that will display a leaderboard for several university teams. The program reads the provided hackathon_teams.csv and allows the user to manage the participating teams, pick a number of rounds and run a simulation of a game to see what teams qualify and dont qualify. 

* We started with Andrei's version 

## Members
Andrei Ushakov, Devona Thomas-McClurkin, Moe Odaki

## How to run
python3 main.py

## Structure/Organization
Seprate files to keep it tidy:
* main.py - holds the user menu and user input for number of rounds
* data.py - holds the funcs that collect data (ie. load and save)
* leaderboard.py - holds the funcionality to display the team leaderboard
* scoring.py - calculates the scores
* records.py - holds the funcs that can manage teams (ie. add, view, update)

## Further-improvement/Checks + Results
We checked that the program runs with expected results as well as unexpected results. Like improper numbers or numbers where words should be. We checked that the program exited properly as well. The results are that the program runs as we expected it to.