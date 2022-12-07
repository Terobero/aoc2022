# Part 1
lines = open("inputs/day5.txt", "r").read().splitlines()

original_grid = []
for line in lines[:lines.index("")-1]:
    for i in range(0, len(line), 4):
        if line[i:i+4].strip():
            while len(original_grid) <= i//4:
                original_grid.append([])
            original_grid[i//4].append(line[i+1])

grid = [i[::-1] for i in original_grid]

for line in lines[lines.index("")+1:]:
    amount, dest, to = map(int, line.split()[1::2])
    dest -= 1
    to -= 1

    for i in range(amount):
        grid[to].append(grid[dest][-1])
        grid[dest] = grid[dest][:-1]

print(f"Part 1 answer: {''.join([i[-1] for i in grid])}")


# Part 2
grid = [i[::-1] for i in original_grid]

for line in lines[lines.index("")+1:]:
    amount, dest, to = map(int, line.split()[1::2])
    dest -= 1
    to -= 1

    grid[to] += grid[dest][-amount:]
    grid[dest] = grid[dest][:-amount]

print(f"Part 2 answer: {''.join([i[-1] for i in grid])}")
