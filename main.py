from data import load_teams, save_teams, view_teams, add_team, update_team

def ask_round():
    while True:
        answer = input(f"Enter the number of rounds ({MIN_ROUNDS}-{MAX_ROUNDS}, blank to cancel): ").strip()

        if answer == "":
            return None

        try:
            rounds = int(answer)
            if MIN_ROUNDS <= rounds <= MAX_ROUNDS:
                return rounds
            else:
                print(f"Please enter a number between {MIN_ROUNDS} and {MAX_ROUNDS}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def show_menu():
    print("\n=== Hackathon Team Manager ===")
    print("1. View teams")
    print("2. Add a team")
    print("3. Update a team")
    print("4. Show leaderboard")
    print("5. Quit")

DATA_FILE = "hackathon_teams.csv"
MIN_ROUNDS = 4
MAX_ROUNDS = 10

def main():
    teams = load_teams(DATA_FILE)

    while True:
        show_menu()
        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            view_teams(teams)  # view_teams(teams) - issue #9

        elif choice == "2":
            add_team(teams)  # add_team(teams) - issue #9
            save_teams(DATA_FILE, teams)

        elif choice == "3":
            update_team(teams)  # update_team(teams) - issue #9
            save_teams(DATA_FILE, teams)

        elif choice == "4":
            d = ask_round()
            if d is not None:
                pass  # show_leaderboard(teams, d) - issue #3

        elif choice == "5":
            print("Bye bye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()