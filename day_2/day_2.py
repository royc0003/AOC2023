
DAY_2_INPUT = 'day_2.txt'
global_input = []

def text_parser():
    file = open(DAY_2_INPUT, 'r')
    lines = file.readlines()
    for line in lines:
        global_input.append(line)

text_parser()

# sample_input = [
# 'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
# 'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
# 'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
# 'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
# 'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'
# ]
# global_input = sample_input

def extract_game_no(game_input, cur_i):
    game_no = 0
    while game_input[cur_i] != ':':
        if game_input[cur_i].isnumeric():
            game_no *= 10
            game_no += int(game_input[cur_i])
        cur_i += 1
    return [game_no, cur_i]

def is_possible(game_input, cur_i):
    allowable_config = {'red': 12, 'green': 13, 'blue' : 14}
    color = ""
    color_no = 0
    while cur_i < len(game_input):
        if game_input[cur_i] == ";" or game_input[cur_i] == ",":
            color = ""
            color_no = 0
            cur_i += 1
            continue
        if game_input[cur_i].isnumeric():
            color_no *= 10
            color_no += int(game_input[cur_i])
        if game_input[cur_i].isalpha():
            color += game_input[cur_i]
        if color in allowable_config:
            if color_no > allowable_config[color]:
                return False
        cur_i += 1
    return True

total_game_no = 0 
for game_input in global_input:
    i = 0
    cur_game_no, i = extract_game_no(game_input, i)
    # skip ':'
    i += 1
    if is_possible(game_input, i):
        # print(cur_game_no)
        total_game_no += int(cur_game_no)

print(total_game_no)





