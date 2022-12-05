def get_round_score(outcome):
    if outcome == -1:
        return 0
    elif outcome == 0:
        return 3
    elif outcome == 1:
        return 6
    else:
        raise AttributeError

rock = 0
paper = 1 
scissors = 2
round_outcome = {
    rock: {
        rock: 0,
        paper: -1,
        scissors: 1,
    },
    paper: {
        rock: 1,
        paper: 0,
        scissors: -1,
    },
    scissors: {
        rock: -1,
        paper: 1,
        scissors: 0,
    }
}

opp_off = ord("A")
res_off = ord("X")

rounds = []
with open("2.txt") as f:
    for line in f:
        moves = line.split(" ")
        rounds.append((ord(moves[0])-opp_off, ord(moves[1][0])-res_off))

ans = 0
for opp_move, res_move in rounds:
    ans += (res_move + 1) + get_round_score(round_outcome[res_move][opp_move])

print(ans)