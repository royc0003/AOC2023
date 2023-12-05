import collections
import time
start_time = time.time()

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
            return [cur_i, -1, -1]

    digit_map = {'one' : 1, 'two' : 2, 'three' : 3, 'four' : 4, 'five': 5, 'six' : 6, 'seven' : 7, 'eight' : 8, 'nine' : 9}
    forward_i = cur_i + 1

    while (forward_i < len(cur_line) and not cur_line[forward_i].isnumeric()):
        forward_i += 1

    tmp_line = cur_line[cur_i: forward_i]
    first_digit = [-1]
    second_digit = [-1]

    def handle_digit_priority(cur_digit):
        if first_digit[0] == -1:
            first_digit[0] = cur_digit
            return
        second_digit[0] = cur_digit

    i = 0
    while i < len(tmp_line): 
        updated = False      
        for k, v in digit_map.items():
            if (i < len(tmp_line) and tmp_line[i] not in valid_starting_char):
                break
            if(i + len(k)) <= len(tmp_line) and tmp_line[i:i+len(k)] == k:
                handle_digit_priority(v)
                i += 1
                updated = True
                break
        if updated == True:
            continue
        i += 1
            
    return [forward_i, first_digit[0], second_digit[0]]
        

def value_parser_using_first_and_last_digits():
    '''
    O(N*M^2) -- where N refers to length of each line parsed; M^2 due to string comparison
    '''
    line_no = 1
    res = 0 
    for line in global_input:
        cur_val = 0 
        first_digit = -1
        last_digit = -1
        i = 0
        while i < len(line): # O(N)
            tmp_res = numerical_val_in_characters_parser(i, line)
            i, tmp_first_digit, tmp_second_digit = tmp_res[0], tmp_res[1], tmp_res[2]
            if first_digit == -1 and tmp_first_digit != -1:
                first_digit = tmp_first_digit
            if tmp_second_digit != -1:
                last_digit = tmp_second_digit
            else:
                if tmp_first_digit != -1:
                    last_digit = tmp_first_digit
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
        line_no += 1
        res += cur_val
    return res


print("Part 2 Answer:: The total value is: ")
print(value_parser_using_first_and_last_digits())
print("--- %s seconds ---" % (time.time() - start_time))