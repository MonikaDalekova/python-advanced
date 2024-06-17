def team_lineup(*args):
    team = {}
    for element in args:
        name_player = element[0]
        country = element[1]

        if country not in team.keys():
            team[country] = []
        team[country].append(name_player)
    sorted_team = sorted(team.items(), key=lambda x: (-len(x[1]), x[0]))
    result = ''
    for country, players in sorted_team:
        result += f"{country}:\n"
        for player in players:
            result += f"  -{player}\n"
    return result


print(team_lineup(   ("Harry Kane", "England"),    ("Manuel Neuer", "Germany"),    ("Raheem Sterling", "England"),
                     ("Toni Kroos", "Germany"),   ("Cristiano Ronaldo", "Portugal"),   ("Thomas Muller", "Germany")))
