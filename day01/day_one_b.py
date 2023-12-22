import re




def reverse_string(s):
    return s[::-1]

def word_to_num(match_str):


    num_dict = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    if match_str not in num_dict.keys():
        return(match_str)
    ret_val = str(num_dict[match_str])
    return(ret_val)


pattern_first = r'one|two|three|four|five|six|seven|eight|nine|zero|1|2|3|4|5|6|7|8|9|0'
pattern2 = r'.*(?:one|two|three|four|five|six|seven|eight|nine|zero)'
pattern3 = r'(?:one|two|three|four|five|six|seven|eight|nine|zero).*'
pattern_last =  r'0|9|8|7|6|5|4|3|2|1|orez|enin|thgie|neves|xis|evif|ruof|eerht|owt|eno'
file_path = 'day_one_a.txt'
digits_pat = r'\d+(\d+)'
digits_pat_last = r'\d+(?=\D*$)'


# Open the file and read the lines
with open(file_path, 'r') as file:
    lines = [line.strip() for line in file]
count = 0
sum_total = 0
for a_line in lines:
    # count += 1
    # if count> 5:
    #     break
    print('1',a_line)
  
    #new_text = re.sub(pattern, word_to_num, a_line)
    first = re.search(pattern_first,a_line)
    if (first):
        print('2',first.group())
        w2n_first = word_to_num(first.group())
        print('4',w2n_first)
        a_line = a_line[0:first.start()] + w2n_first +  a_line[first.start()+1:]
        print('7', a_line)

    rev_line = reverse_string(a_line)
    print('rev1',rev_line)
    last = re.search(pattern_last,rev_line)
    if (last):
        print('3',last.group())
        rev_match = reverse_string(last.group())
        w2n_last = word_to_num(rev_match)
        print('5',w2n_last )
        a_line = rev_line[0:last.start()] + w2n_last +  rev_line[last.start()+1:]
        a_line = reverse_string(a_line)

        print('6',a_line)
        numbers = re.findall(r'\d+', a_line)
    

    #print(numbers[0], numbers[-1])
    first_and_last = numbers[0] + numbers[-1]
    #print(first_and_last)
    first_and_last = int(first_and_last[0] + first_and_last[-1])
    print('9',first_and_last)
    sum_total += first_and_last
   # print(a_line, first_and_last, sum_total)

print(sum_total)


