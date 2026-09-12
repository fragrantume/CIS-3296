QUALIFYING_ROUND = 4
QUALIFYING_SCORE = 80


def score(d, i, rate, total=0):
    # Cumulative score after d rounds, starting with initial score i and growth by rate.
    total += i
    if d == 1:
        return total
    return score(d - 1, i * rate, rate, total)


def cumulative(team, d):
    # Cumulative score for a team after d rounds. 
    return score(d, team["initial_score"], team["growth_rate"])


def is_qualified(team):
    # Qualifies if the cumulative score after QUALIFYING_ROUND is at least QUALIFYING_SCORE.
    return cumulative(team, QUALIFYING_ROUND) >= QUALIFYING_SCORE