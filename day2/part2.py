games = []

with open("input.txt") as file:
    
    for line in file:
        games.append(line.strip().split(" "))


def game_score(p_game):
    score = 0
    if p_game[1] == "X":
        score += 0
        if p_game[0] == "A":
            score += 3
        elif p_game[0] == "B":
            score += 1
        elif p_game[0] == "C":
            score += 2
    elif p_game[1] == "Y":
        score += 3
        if p_game[0] == "A":
            score += 1
        elif p_game[0] == "B":
            score += 2
        elif p_game[0] == "C":
            score += 3
    elif p_game[1] == "Z":
        score += 6
        if p_game[0] == "A":
            score += 2
        elif p_game[0] == "B":
            score += 3
        elif p_game[0] == "C":
            score += 1
    print(p_game,score)
    return score

total_score = 0
for game in games:
    total_score += game_score(game)

print(total_score)