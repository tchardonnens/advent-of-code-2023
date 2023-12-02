import re

# 1 star

with open("input.txt", "r") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

sum = 0
for line in lines:
    line = re.sub("[^0-9]", "", line)
    res = line[0] + line[-1]
    sum += int(res)

print(sum)

# 2 stars

with open("input.txt", "r") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

sum = 0
numbers_in_letters = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

for line in lines:
    
    for i in range(len(line)):
        for key in numbers_in_letters.keys():
            if key in line[i:i+5]:
                line = line.replace(key, numbers_in_letters[key])
    
    line = re.sub("[^0-9]", "", line)
    res = line[0] + line[-1]
    sum += int(res)

print(sum)

