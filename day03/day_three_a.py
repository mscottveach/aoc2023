import numpy as np
import matplotlib.pyplot as plt



# Use Matplotlib to display the array
gear_ratio = {}
file_path = './input_a.txt'
np.set_printoptions(threshold=np.inf)
safety_dance = []

def extract_nums_from_row(in_row, row_idx, touchers):
    is_first_dig = True
    is_last_dig = False
    start = 0
    end = 0
    num_str = ''
    for idx in range(0,len(in_row)):
        if in_row[idx].isdigit() and is_first_dig:
            is_first_dig = False
            is_last_dig = True
            num_str = in_row[idx]
            #print(num_str)
            start = idx
         
        elif in_row[idx].isdigit() and not is_first_dig:
            num_str += in_row[idx]
            #print(num_str)
        elif in_row[idx].isdigit() and idx == (len(in_row) - 1):
            num_str += in_row[idx]
            #print(num_str)
            a_num = int(num_str)
            if a_num in safety_dance:
                print ('ERROR! ERROR!')
            else:
                safety_dance.append(a_num)
            #print(a_num)
            end = idx - 1
            touchers.append((a_num,idy,start,end))
        elif not in_row[idx].isdigit() and is_last_dig:
            is_last_dig = False
            is_first_dig = True
            a_num = int(num_str)
            if a_num in safety_dance:
                pass
                #print ('ERROR! ERROR!')
            else:
                safety_dance.append(a_num)
            #print(a_num)
            end = idx - 1
            touchers.append((a_num,idy,start,end))

    return()



def mark_adj_grid(in_y, in_x, in_oray, in_hlp, counter):
    #print(in_x,in_y)

    for idy in range(-1,2):
        for idx in range(-1,2):
         if in_hlp[idy+in_y][idx+in_x] > 0:
                print('PROBLKEM!')

    in_oray[in_y-1][in_x-1] = counter
    in_oray[in_y][in_x-1] = counter
    in_oray[in_y+1][in_x-1] = counter
    in_oray[in_y-1][in_x] = counter
    in_oray[in_y+1][in_x] = counter
    in_oray[in_y-1][in_x+1] = counter
    in_oray[in_y][in_x+1] = counter
    in_oray[in_y+1][in_x+1] = counter
    found = []
    gr = 1
   

    return(gr)

def it_touches(the_num,in_y, in_x_start, in_x_end, in_oray, gear_ratio):
    for idx in range(in_x_start, in_x_end+1):
        if in_oray[idy][idx] > 0:
            #print('hit ',idy,idx)
            val = in_oray[idy][idx]
            gear_ratio[val].append(the_num)
            return True
    return False

def is_a_symbol(in_c):
    if in_c != '.' and not in_c.isdigit():
        #print(in_c)
        return True
    return False

# def adjust_input(in_ray,touchers,ph):
#     for num in touchers:
#         idy = num[1]
#         the_num = num[0]
#         #print(num)
#         # print(in_ray[num[1])])
#         for idx in range(num[2],num[3]+1):
#             ph[idy][idx] = the_num

    

# Open the file and read the lines
with open(file_path, 'r') as file:
    lines = [line.strip() for line in file]


rows = len(lines) + 2
cols = len(lines[0]) + 2
# cols = 50
# rows = 50
pad_input = np.full((rows, cols), '.', dtype='<U1')
pad_oray = np.full((rows, cols), 0, dtype=int)
pad_helper = np.full((rows, cols), 0, dtype=int)

for idy in range(0,rows-2):
    for idx in range(0,cols-2):
        pad_input[idy+1][idx+1] = lines[idy][idx]


#adjust_input(pad_input,touchers,pad_helper)
#print(pad_input)
#print(pad_helper)


#print(touchers)
counter = 0
gr_tot = 0
for idy in range(rows):
    for idx in range(cols):

        if (is_a_symbol(pad_input[idy][idx])):
           # print(idy, idx, pad_input[idy][idx])
            #print(idy,idx, " is a symbol.")
            counter += 1
            gear_ratio[counter] = []
            mark_adj_grid(idy,idx,pad_oray,pad_helper, counter)

# print(pad_oray)
# print(gr_tot)


total_sum = 0
touchers = []
for idy in range(rows):
    idx = 0
    the_nums = extract_nums_from_row(pad_input[idy], idy, touchers)
    # for num in the_nums:
    #     if it_touches(num[0],idy, num[1],num[2],pad_oray,gear_ratio):
    #         total_sum += num[0]
    for num in touchers:
        the_num = num[0]
        startx = num[2]
        endx = num[3]
        y = num[1]
        for idx in range(startx,endx+1):
            if pad_oray[y][idx] > 0:
                sym = pad_oray[y][idx]
                if the_num not in gear_ratio[sym]:
                    gear_ratio[sym].append(the_num)
gr_tot = 0
print(gear_ratio)
for a_key in gear_ratio.keys():
    if len(gear_ratio[a_key]) == 2:
        two_nums = gear_ratio[a_key]
        gr = two_nums[0] * two_nums[1]
        gr_tot += gr

print(gr_tot)