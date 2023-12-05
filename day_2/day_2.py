
DAY_2_INPUT = 'day_2.txt'
global_input = []

def text_parser():
    file = open(DAY_2_INPUT, 'r')
    lines = file.readlines()
    for line in lines:
        global_input.append(line)

text_parser()


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
    current_config = {'red':0, 'green':0, 'blue':0}
    color = ""
    color_no = 0
    res = True
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
                res = False
            current_config[color] = max(current_config[color], color_no)
        cur_i += 1
    return [res, current_config]

total_game_no = 0 
total_power = 0
for game_input in global_input:
    i = 0
    cur_game_no, i = extract_game_no(game_input, i)
    # skip ':'
    i += 1
    res = is_possible(game_input, i)
    check_possible, current_config = res[0], res[1]
    if check_possible:
        total_game_no += int(cur_game_no)
    tmp_val = 1
    for k,v in current_config.items():
        tmp_val *= v
    total_power += tmp_val

print(total_game_no)
print(total_power)





