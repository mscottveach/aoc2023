file_path = 'input_a.txt'

# Open the file and read the lines
with open(file_path, 'r') as file:
    lines = [line.strip() for line in file]


#split the line based on j
#print(len(lines))
#
def calc_the_pulls(pull_quants, a_pull):
    print(a_pull)
    the_split = a_pull.split(',')
    for idx, pull in enumerate(the_split):
        if pull[0] == ' ':
            the_split[idx] = pull[1:]    
    #print(the_split)
    for pull in the_split:

        split_pull = pull.split(' ')
        #print(split_pull)
        color_key = split_pull[1]
        #print(the_split)
        quant = int(split_pull[0])
    # print(the_split)
       # print(color_key, quant)
        pull_quants[color_key] = quant


def ret_game_number(in_string):
    a_game = int(in_string[5:])
    return(a_game)

power_sum = 0
iter_count = 0
possible_game_count = 0
master_cubes = {'red':12,'green':13,'blue':14}
pull_quants = {'red':0,'green':0,'blue':0}
min_quants = {'red':-1,'green':-1,'blue':-1}
for row in lines:
    print(row)
    # iter_count += 1
    # if iter_count > 5:
    #     break
    impossible = False
    #print(row)
    num_and_games = row.split(':')
    #print(num_and_games)
    game_num = ret_game_number(num_and_games[0])
   # print(num_and_games[0])
    #print(num_and_games[1])
    games = num_and_games[1]
    #print(games)
    pulls = games.split(';')
    #print(pulls)
    #print(pulls)
    #print(pulls)
    min_quants = {'red':-1,'green':-1,'blue':-1}
    for a_pull in pulls:
        #print(a_pull)
        pull_quants = {'red':0,'green':0,'blue':0}

        #print(a_pull)
       # print(a_pull[1:])
        calc_the_pulls(pull_quants,a_pull[1:])
        #print(game_num, a_pull)
       # print(pull_quants)
       # print()
        for key in master_cubes:
            if pull_quants[key] > master_cubes[key]:
              #  print('impossible')

                impossible = True
            if min_quants[key] < 0:
                min_quants[key] = pull_quants[key]
            elif min_quants[key] < pull_quants[key]:
                min_quants[key] = pull_quants[key]
            
    game_power = 1
    for key in min_quants:
        game_power = game_power * min_quants[key]
    power_sum += game_power 
    print(game_power)
    if not impossible:
        possible_game_count += game_num

print(possible_game_count, power_sum)

