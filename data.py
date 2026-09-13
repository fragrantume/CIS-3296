import csv

FIELDS = ["university", "team_name", "initial_score", "growth_rate"]

def load_teams(filename):
    # Load all team records from the CSV into a list of dictionaries.
    teams = []
    with open(filename, mode="r", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            teams.append({
                "university": row["university"],
                "team_name": row["team_name"],
                "initial_score": float(row["initial_score"]),
                "growth_rate": float(row["growth_rate"]),
            })
    return teams

def save_teams(filename, teams):
    # Write all team records back to the CSV, replacing the file.
    with open(filename, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(teams)

def view_teams(teams):
    # Print All teams and team data to screen
    print("\nCurrent Teams:")
    for team in teams:
        print(f"University: {team['university']}, Team Name: {team['team_name']}, Initial Score: {team['initial_score']}, Growth Rate: {team['growth_rate']}")  

def add_team(teams):
    # Allow user to input data for a new team and append to csv file
    university = input("Enter the university name: ").strip()
    team_name = input("Enter the team name: ").strip()
    while True:
        try:
            initial_score = float(input("Enter the initial score: ").strip())
            break
        except ValueError:
            print("Invalid input. Please enter a number for the initial score.")
    while True:
        try:
            growth_rate = float(input("Enter the growth rate: ").strip())
            break
        except ValueError:
            print("Invalid input. Please enter a number for the growth rate.")
    teams.append({
        "university": university,
        "team_name": team_name,
        "initial_score": initial_score,
        "growth_rate": growth_rate,
    })

def update_team(teams):
    # Display teams and allow user to rewrite a teams data
    print("\nThese are the current teams:")
    view_teams(teams)
