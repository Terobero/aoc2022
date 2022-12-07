# Part 1
lines = open("inputs/day3.txt", "r").read().splitlines()

total = 0
for line in lines:
    compartment1 = line[:len(line)//2]
    compartment2 = line[len(line)//2:]
    common = list(set(compartment1).intersection(set(compartment2)))[0]

    if common.islower():
        total += ord(common) - 97 + 1
    else:
        total += ord(common) - 65 + 27

print(f"Part 1 answer: {total}")


# Part 2
total = 0
for i in range(0, len(lines), 3):
    common = list(set(lines[i]).intersection(set(lines[i+1]).intersection(set(lines[i+2]))))[0]

    if common.islower():
        total += ord(common) - 97 + 1
    else:
        total += ord(common) - 65 + 27

print(f"Part 2 answer: {total}")
