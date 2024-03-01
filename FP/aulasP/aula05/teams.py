def dest_teams(teams):
    games = []
    cnt = 0;
    for t in teams:
        for t2 in teams:
            if t != t2:
                games.append((t, t2))
                cnt += 1
    return games, cnt




def main():
    teams = ['Flamengo', 'Vasco', 'Fluminense', 'Botafogo']

    games , cnt= dest_teams(teams)

    print("Games", games)
    print("Number of games", cnt)

main()