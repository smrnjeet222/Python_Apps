import re

hand = open("regex_sum_829837.txt")
x = list()
for line in hand:
    y = re.findall('[0-9]+', line)
    x = x+y

sum = 0
for z in x:
    sum += int(z)

print(sum)

