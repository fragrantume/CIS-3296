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

