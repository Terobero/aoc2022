# Part 1
lines = open("inputs/day4.txt", "r").read().splitlines()

total = 0
for line in lines:
    elf1, elf2 = line.split(",")
    elf1 = list(map(int, elf1.split("-")))
    elf2 = list(map(int, elf2.split("-")))

    if (elf1[0] <= elf2[0] and elf1[1] >= elf2[1]) or (elf2[0] <= elf1[0] and elf2[1] >= elf1[1]):
        total += 1

print(f"Part 1 answer: {total}")


# Part 2
total = 0
for line in lines:
    elf1, elf2 = line.split(",")
    elf1 = list(map(int, elf1.split("-")))
    elf2 = list(map(int, elf2.split("-")))

    if not (elf1[0] <= elf1[1] < elf2[0] or elf2[1] < elf1[0] <= elf1[1] or elf2[0] <= elf2[1] < elf1[0] or elf1[1] < elf2[0] <= elf2[1]):
        total += 1

print(f"Part 2 answer: {total}")
