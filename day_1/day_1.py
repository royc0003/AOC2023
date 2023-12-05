import collections

DAY_1_INPUT = 'day_1_input.txt'
global_input = []
def text_parser():
    file = open(DAY_1_INPUT, 'r')
    lines = file.readlines()
    for line in lines:
        global_input.append(line)
        
text_parser()

def numerical_val_in_characters_parser(cur_i, cur_line):
    valid_starting_char = {'o', 't', 'f', 's', 'e', 'n'}
    if(cur_line[cur_i] not in valid_starting_char):
            return [cur_i, -1]
    digit_map = {'one' : 1, 'two' : 2, 'three' : 3, 'four' : 4, 'five': 5, 'six' : 6, 'seven' : 7, 'eight' : 8, 'nine' : 9}
    forward_i = cur_i + 1
    # step 1: run to the next digit or end of line
    while (forward_i < len(cur_line) and not cur_line[forward_i].isnumeric()):
        forward_i += 1
    
    # Step 2: perform sliding window
    # oone
    # 
    l = 0
    first_digit = -1
    second_digit = -1
    tmp_line = cur_line[cur_i: forward_i]
    for r, val in enumerate(tmp_line):
        if(cur_line[l] not in valid_starting_char):
            l += 1
            continue
        if tmp_line[l:r+1] in digit_map:
            if first_digit == -1:
                first_digit = int(digit_map[tmp_line[l:r+1]])
            else:
                second_digit = int(digit_map[tmp_line[l:r+1]])
            l = r + 1
            continue
        while (r-l+1) > 5 :
            l += 1
            
    return [forward_i, first_digit, second_digit]
        
sample_input = ['two1nine',
'eightwothree',
'abcone2threexyz',
'xtwone3four',
'4nineeightseven2',
'zoneight234',
'7pqrstsixteen']
global_input = sample_input

def value_parser_using_first_and_last_digits():
    res = 0 
    for line in global_input:
        cur_val = 0 
        first_digit = -1
        last_digit = -1
        i = 0
        while i < len(line):
            tmp_res = numerical_val_in_characters_parser(i, line)
            i = tmp_res[0]
            if tmp_res[1] != -1:
                if first_digit == -1:
                    first_digit = tmp_res[1]
                    if last_digit == -1 and tmp_res[2] != -1:
                        last_digit = tmp_res[2] 
                else:
                    last_digit = tmp_res[1]
            if i >= len(line):
                break
            if not line[i].isnumeric():
                i += 1
                continue
            if first_digit == -1:
                first_digit = int(line[i])
            last_digit = int(line[i])
            i += 1
        cur_val += first_digit
        cur_val *= 10
        cur_val += last_digit
        print(cur_val)
        res += cur_val

    return res


print("Part 2 Answer:: The total value is: ")
print(value_parser_using_first_and_last_digits())
