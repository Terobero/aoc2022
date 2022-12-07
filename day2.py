# Part 1
lines = open("inputs/day2.txt", "r").read().splitlines()

total = 0
for line in lines:
    if line == "A X":
        total += 4
    elif line == "A Y":
        total += 8
    elif line == "A Z":
        total += 3
    elif line == "B X":
        total += 1
    elif line == "B Y":
        total += 5
    elif line == "B Z":
        total += 9
    elif line == "C X":
        total += 7
    elif line == "C Y":
        total += 2
    elif line == "C Z":
        total += 6

print(f"Part 1 answer: {total}")


# Part 2
total = 0
for line in lines:
    if line == "A X":
        total += 3
    elif line == "A Y":
        total += 4
    elif line == "A Z":
        total += 8
    elif line == "B X":
        total += 1
    elif line == "B Y":
        total += 5
    elif line == "B Z":
        total += 9
    elif line == "C X":
        total += 2
    elif line == "C Y":
        total += 6
    elif line == "C Z":
        total += 7

print(f"Part 2 answer: {total}")
