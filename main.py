from data import load_teams

DATA_FILE = "hackathon_teams.csv"


def main():
    teams = load_teams(DATA_FILE)
    print(f"Loaded {len(teams)} teams.")   # menu goes here, issue #4


if __name__ == "__main__":
    main()