# Part 1
lines = open("inputs/day1.txt", "r").read().splitlines()

max_elf = 0
current_elf = 0
for line in lines:
    if line:
        current_elf += int(line)
    else:
        max_elf = max(max_elf, current_elf)
        current_elf = 0

print(f"Part 1 answer: {max_elf}")


# Part 2
max_elfs = [0, 0, 0]
current_elf = 0
for line in lines:
    if line:
        current_elf += int(line)
    else:
        if current_elf > max_elfs[0]:
            max_elfs = [current_elf, max_elfs[0], max_elfs[1]]
        elif current_elf > max_elfs[1]:
            max_elfs = [max_elfs[0], current_elf, max_elfs[1]]
        elif current_elf > max_elfs[2]:
            max_elfs = [max_elfs[0], max_elfs[1], current_elf]
        current_elf = 0

print(f"Part 2 answer: {sum(max_elfs)}")
