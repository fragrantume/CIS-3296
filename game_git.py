import csv 

def score(d, i, rate, total = 0):
    # Add current score to total
    total += i

    # Stop recursion when D reaches 1
    if d == 1:
        print(f"Your final score: {total}")
        return round(total)

    return score(d - 1, i * rate, rate, total)

#calculate bu using "score" for round 4 and round 6
def calc_team_score(initial_score, growth_rate, d):
    new_scorelist = []

    #calculate until round 4
    for idx in range(len(initial_score)):
        team_total = score(
            d,
            i = initial_score[idx],
            rate = growth_rate[idx]
        )
        new_scorelist.append(team_total)
        
    return new_scorelist

def main():

    #initialize arrays
    university_name = []
    team_name = []
    initial_score = []
    growth_rate = []

    #open and input data
    with open('hackathon_teams.csv', mode = 'r', encoding = 'utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            university_name.append(row['university'])
            team_name.append(row['team_name'])
            initial_score.append(int(row['initial_score']))
            growth_rate.append(float(row['growth_rate']))

    #calculate scores for each team and store as array
    round4_score = calc_team_score(initial_score, growth_rate, d = 4)
    round6_score = calc_team_score(initial_score, growth_rate, d = 6)

    # Only check qualification if D is at least 4   
    for idx in range (len(round4_score)):
        score_val = round(round4_score[idx])
        if score_val >= 80:
            print("You are qualified.")
        else:
            print("You are NOT qualified.")     

    #sort by the round 6 scores
    newlist = sorted(round4_score)
    print(newlist)   
            
if __name__ == '__main__':
    main()

