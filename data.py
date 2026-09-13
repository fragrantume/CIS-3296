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
    for i, team in enumerate(teams, start=1):
        print(f"{i}. University: {team['university']}, Team Name: {team['team_name']}, Initial Score: {team['initial_score']}, Growth Rate: {team['growth_rate']}")

def add_team(teams):
    # Allow user to input data for a new team and append to csv file
    print("\nAdd a New Team------")
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
    print("\nUpdate a Team------")
    view_teams(teams)
    #asks user to select a team to update w/ input checks 
    while True:
        try:
            team_index = int(input("Enter the number of the team to update (or 0 to cancel): ").strip())
            if team_index == 0:
                return
            if 1 <= team_index <= len(teams):
                break
            else:
                print(f"Please enter a number between 1 and {len(teams)}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    #go through each field and ask user to update or keep the same value
    updated_team = teams[team_index - 1]
    print(f"\nUpdating team: {updated_team['team_name']}")
    university = input(f"Enter the university name [{updated_team['university']}]: ").strip()
    team_name = input(f"Enter the team name [{updated_team['team_name']}]: ").strip()

    while True:
        initial_score_input = input(f"Enter the initial score [{updated_team['initial_score']}]: ").strip()
        if initial_score_input == "":
            initial_score = updated_team['initial_score']
            break
        try:
            initial_score = int(initial_score_input)
            break
        except ValueError:
            print("Invalid input. Please enter a number for the initial score.")
    while True:
        growth_rate_input = input(f"Enter the growth rate [{updated_team['growth_rate']}]: ").strip()
        if growth_rate_input == "":
            growth_rate = updated_team['growth_rate']
            break
        try:
            growth_rate = float(growth_rate_input)
            break
        except ValueError:
            print("Invalid input. Please enter a number for the growth rate.")

    #update only the new values, keeps old values if input was blank
    updated_team.update({
        "university": university if university else updated_team['university'],
        "team_name": team_name if team_name else updated_team['team_name'],
        "initial_score": initial_score,
        "growth_rate": growth_rate,
    })
