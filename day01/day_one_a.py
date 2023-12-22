import re

file_path = 'day_one_a.txt'

# Open the file and read the lines
with open(file_path, 'r') as file:
    lines = [line.strip() for line in file]

sum_total = 0
for a_line in lines:
    numbers = re.findall(r'\d+', a_line)
    first_and_last = numbers[0] + numbers[-1]
    first_and_last = int(first_and_last[0] + first_and_last[-1])
    print(numbers, first_and_last)
    sum_total += first_and_last

print(sum_total)
