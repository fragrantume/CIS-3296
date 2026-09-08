import csv 

def score(d, i=10, total=0):
    # Add current score to total
    total += i

    # Print c
    print(i)

    # Stop recursion when D reaches 1
    if d == 1:
        print(f"Your final score: {total}")
        return total

    return score(d - 1, round(i * 1.2), total)

def main():

    teams = []

    with open('hackathon_teams.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            teams.append(row)

    pressed = False

    while not pressed:
        # Ask the user for their D
        print("To exit, enter number less than 2, or press Enter")

        try:
            d = int(input("Enter your D: "))
            i = int(input("Enter your I: "))
        except ValueError:
            break

        if d >= 2:
            final = score(d, i)

            # Only check qualification if D is at least 4   
            if d >= 4:
                if final >= 80:
                    print("You are qualified.")
                else:
                    print("You are NOT qualified.")

        else:
            # Exit if D is less than 2
            pressed = True
            
if __name__ == '__main__':
    main()
