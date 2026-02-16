"""
Docstring for 2026.february.2026_winter_games_day_11
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-16
                    2026 Winter Games Day 11: Ice Hockey
Given an array of 6 ice hockey teams and their records after the round robin games, determine the match-ups for the semi-final round.

Each array item will have a team and their record in the format "TEAM: W-OTW-OTL-L". Where:
"W" is the number of wins in regulation, worth 3 points each
"OTW" is the number of overtime wins, worth 2 points each
"OTL" is the number of overtime losses, worth 1 point each
"L" is the number of losses, worth 0 points each
For example, "FIN: 2-2-1-0" would have 11 points after adding up their record.

Find the total number of points for each team and return "The semi-final games will be (1st) vs (4th) and (2nd) vs (3rd).". For example, "The semi-final games will be FIN vs SWE and CAN vs USA."
"""
def get_semifinal_matchups(teams):
    team_scores = []

    for team in teams:
        team_name, team_record = team.split(": ")
        w, otw, otl, l = team_record.split("-")
        team_score = int(w) * 3 + int(otw) * 2 + int(otl) * 1 
        team_scores.append((team_name, team_score))
    
    team_scores.sort(key=lambda x: x[1], reverse=True)

    first = team_scores[0][0]
    second = team_scores[1][0]
    third = team_scores[2][0]
    fourth = team_scores[3][0]

    return f"The semi-final games will be {first} vs {fourth} and {second} vs {third}."

print(get_semifinal_matchups(["CAN: 2-2-0-1", "FIN: 2-2-1-0", "GER: 1-0-1-3", "SUI: 0-1-3-1", "SWE: 1-1-2-1", "USA: 2-1-0-2"])) # should return "The semi-final games will be FIN vs SWE and CAN vs USA.".
print(get_semifinal_matchups(["CAN: 2-1-1-1", "CZE: 1-1-1-2", "FIN: 1-2-1-1", "NOR: 0-1-1-3", "SLO: 1-0-1-3", "USA: 5-0-0-0"])) # should return "The semi-final games will be USA vs CZE and CAN vs FIN.".
print(get_semifinal_matchups(["CAN: 3-2-0-0", "CZE: 2-1-2-0", "LAT: 0-0-1-4", "ITA: 1-1-1-2", "DEN: 1-0-0-4", "USA: 3-1-1-0"])) # should return "The semi-final games will be CAN vs ITA and USA vs CZE.".
print(get_semifinal_matchups(["AUT: 2-2-1-0", "DEN: 1-0-0-4", "ITA: 1-1-1-2", "JPN: 3-2-0-0", "KOR: 2-1-2-0", "LAT: 0-0-1-4"])) # should return "The semi-final games will be JPN vs ITA and AUT vs KOR.".