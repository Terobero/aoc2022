# Part 1
lines = open("inputs/day6.txt", "r").read().splitlines()

line = lines[0]
index = 0
for i in range(len(line)):
    if len(line[i:i+4]) == len(set(line[i:i+4])):
        index = i + 4
        break

print(f"Part 1 answer: {index}")


# Part 2
index = 0
for i in range(len(line)):
    if len(line[i:i+14]) == len(set(line[i:i+14])):
        index = i + 14
        break

print(f"Part 2 answer: {index}")
