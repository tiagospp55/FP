def dest_teams(teams):
    games = []
    cnt = 0
    for t in teams:
        for t2 in teams:
            if t != t2:
                games.append((t, t2))
                cnt += 1
    return games, cnt

def get_results(games, teams, goals, victories, draw):
    results = {}


    for game in games:
        print("Enter the result for the game", game)
        e1 = int(input("Golos da equipa " + game[0] + ":"))
        e2 = int(input("Golos da equipa " + game[1] + ":"))
        results[game] = (e1, e2)

        for t in teams:
            print("Team", t)
            if t == game[0]:
                goals[t].append(e1)
            elif t == game[1]:
                goals[t].append(e2);
        print("Game", game[1])
        if e1 > e2:
            print("The winner is", game[0])
            victories[game[0]] += 1
        elif e2 > e1:
            print("The winner is", game[1])
            victories[game[1]] += 1
        else:
            print("It's a draw")
            print("Goals", goals)
            draw[game[0]] += 1
            draw[game[1]] += 1


    return results, goals, victories, draw


def main():
    goals = {}
    draw = {}
    victories = {}

    num_teams = int(input("Enter the number of teams: "))
    teams = []
    for i in range(num_teams):
        team = input("Enter the team name: ")
        teams.append(team)
        goals[team] = []
        draw[team] = 0
        victories[team] = 0

    games , cnt= dest_teams(teams)
    results, goals, victories, draw = get_results(games,teams, goals, victories, draw)
    print("Results", results)

    print("Goals", goals)
    print("Victories", victories)
    print("Draws", draw)
    print("Games", games)

    points = {}
    for t in teams:
        points[t] = victories[t] * 3 + draw[t]
    mx = 0
    for t in teams:
        if points[t] > mx:
            mx = points[t]
            print("The winner is", t)
    
    # print da tabela classificativa com os pontos, vitorias e empates
            
    for t in teams:
        print(t, "Points", points[t], "Victories", victories[t], "Draws", draw[t])

main()
