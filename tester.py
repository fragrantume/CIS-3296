def add_team():
    return 
def view_teams():
    return
def update_teams():
    return


def user_menu():
    #print menu on screen of commands the user can use + what they do
    menu = {
        "add": add_team(),
        "view": view_teams(),
        "update": update_teams(),
    }

    running = True

    while running:
        print("\nMenu Options (Type command you want to do): \n\tAdd: Register a new team \n\tView: View all current teams and data \n\tUpdate: Make changes to existing team data\n")

        choice = input("\nEnter your choice: ").strip().lower()

        if choice == "exit":
            print("------Exiting Program------")
            running = False
        elif choice == "add":
            add_team()
        elif choice == "view":
            view_teams()
        elif choice == "update":
            update_teams()
        else:
            print("This is not an option. Please try again")
    return 

def main():
    user_menu()

if __name__ == '__main__':
    main()