import os, sys

### Part 1 ###
print("### Part 1 ###")

def shape_values(chosen_shapes):
    # A / X = Rock = 1
    # B / Y = Paper = 2
    # C / Z = Scissors = 3

    shape_dict = {
        "A": 1,
        "B": 2,
        "C": 3,
        "X": 1,
        "Y": 2,
        "Z": 3
    }

    return (shape_dict[chosen_shapes[1]], shape_dict[chosen_shapes[0]])

with open(f"{os.path.dirname(sys.argv[0])}\input", "r") as rps_games:

    total_score = 0
    for game in rps_games:

        round_score = 0
        chosen_shapes = game.strip().split(" ")

        game_values = shape_values(chosen_shapes)

        round_score += game_values[0]

        if game_values[0] == game_values[1]:
            # draw
            round_score += 3
        elif game_values[0] == 2 and game_values[1] == 1 or game_values[0] == 3 and game_values[1] == 2 or game_values[0] == 1 and game_values[1] == 3:
            # win
            round_score += 6

        total_score += round_score

print(total_score)

### Part 2 ###
print("### Part 2 ###")

# Losing games totals
lose_dict = {
    "A": 3,
    "B": 1,
    "C": 2
}

# Drawn game totals (effectively double)
draw_dict = {
    "A": 1,
    "B": 2,
    "C": 3
}

# Winning game totals
win_dict = {
    "A": 2,
    "B": 3,
    "C": 1
}


with open(f"{os.path.dirname(sys.argv[0])}\input", "r") as rps_games:

    total_score = 0
    for game in rps_games:
        round_score = 0

        chosen_result = game.strip().split(" ")

        if chosen_result[1] == "X":
            # Lose
            round_score = lose_dict[chosen_result[0]]
        elif chosen_result[1] == "Y":
            # Draw
            round_score += 3
            round_score += draw_dict[chosen_result[0]]
        elif chosen_result[1] == "Z":
            # Win
            round_score += 6
            round_score += win_dict[chosen_result[0]]
        else:
            print("uh oh")

        total_score += round_score

print(total_score)

# Alternate method

result_offsets = {
    "X": -1,
    "Y": 0,
    "Z": 1
}
result_values = {
    "X": 0,
    "Y": 3,
    "Z": 6
}
shape_values = [1, 2, 3]
shape_index = ["A", "B", "C"]

with open(f"{os.path.dirname(sys.argv[0])}\input", "r") as rps_games:

    total_score = 0
    for game in rps_games:
        round_score = 0

        chosen_result = game.strip().split(" ")

        # Add shape value
        round_score += shape_values[(shape_index.index(chosen_result[0]) + result_offsets[chosen_result[1]]) % 3]

        # Add result value
        round_score += result_values[chosen_result[1]]

        total_score += round_score

print(total_score)