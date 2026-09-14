from scoring import cumulative, is_qualified

def show_leaderboard(teams, d):
    # Rank teams by cumulative score through round d, highest first.
    scored = [(team, cumulative(team, d)) for team in teams]
    scored.sort(key=lambda pair: pair[1], reverse=True)

    print(f"\n=== Leaderboard through round {d} ===")
    print(f"{'Rank':<6}{'University':<35}{'Team':<20}{'Score':>8}  Status")
    print("-" * 85)

    previous_score = None
    previous_rank = 0

    for position, (team, score) in enumerate(scored, start=1):
        rounded = round(score, 2)
        if rounded == previous_score:
            rank = previous_rank
        else:
            rank = position
            previous_score = rounded
            previous_rank = rank

        status = "QUALIFIED" if is_qualified(team) else "NOT QUALIFIED"
        print(f"{rank:<6}{team['university']:<35}{team['team_name']:<20}{score:>8.2f}  {status}")