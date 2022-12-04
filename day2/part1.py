games = []

with open("input.txt") as file:
    
    for line in file:
        games.append(line.strip())


def game_score(p_game: str):
    score = 0
    if p_game[2] == "X":
        score += 1
        if p_game[0] == "A":
            score += 3
        elif p_game[0] == "B":
            score += 0
        elif p_game[0] == "C":
            score += 6
    elif p_game[2] == "Y":
        score += 2
        if p_game[0] == "A":
            score += 6
        elif p_game[0] == "B":
            score += 3
        elif p_game[0] == "C":
            score += 0
    elif p_game[2] == "Z":
        score += 3
        if p_game[0] == "A":
            score += 0
        elif p_game[0] == "B":
            score += 6
        elif p_game[0] == "C":
            score += 3
    print(p_game,score)
    return score

total_score = 0
for game in games:
    total_score += game_score(game)

print(total_score)