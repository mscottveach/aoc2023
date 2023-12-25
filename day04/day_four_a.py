

file_path = './input_a.txt'


with open(file_path, 'r') as file:
    lines = [line.strip() for line in file]

total_num_of_cards = len(lines)
print(lines[1])

card_wins = {}
card_count = {}
for idx in range(0,total_num_of_cards):
    card_count[idx] = 1


total_value_of_cards = 0
counter = 0
#for a_line in lines:
for idx in range(0, total_num_of_cards):
    a_line = lines[idx]
    counter += 1
    split_nums = a_line.split('|')
    wins = split_nums[0].split(' ')
    mine = split_nums[1].split(' ')


    wins = [x for x in wins if x != '']
    mine = [x for x in mine if x != '']
    wins = wins[2:]
 
    wins = [int(x) for x in wins]
    mine = [int(x) for x in mine]
    
    print(wins)
    print(mine)   

    num_of_wins = 0
    for my_num in mine:
        if my_num in wins:
            num_of_wins += 1

    card_wins[idx] = num_of_wins
    
    if num_of_wins == 0:
        value = 0
    else:
        value = 2**(num_of_wins-1)

    total_value_of_cards += value


print(total_value_of_cards)

for idx in range(0, total_num_of_cards):
    no_of_wins = card_wins[idx]
    for idy in range(1, no_of_wins+1):
        card_count[idx+idy] += card_count[idx]

print(sum(card_count.values()))
