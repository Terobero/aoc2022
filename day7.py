class Folder:
    def __init__(self, parent):
        self.parent = parent
        self.contents = {}

    def size(self):
        size = 0
        for content in self.contents.values():
            if isinstance(content, Folder):
                size += content.size()
            elif isinstance(content, File):
                size += content.size

        return size

    def find_sizes(self):
        sizes = []
        size = 0
        for content in self.contents.values():
            if isinstance(content, Folder):
                size += content.size()
                sizes += content.find_sizes()
            elif isinstance(content, File):
                size += content.size

        return [size] + sizes


class File:
    def __init__(self, size):
        self.size = size


# Part 1
lines = open("inputs/day7.txt", "r").read().splitlines()

filesystem = Folder(None)
current_folder = filesystem

i = 1
while i < len(lines):
    line = lines[i]
    if line == "$ cd ..":
        current_folder = current_folder.parent
    elif line.startswith("$ cd"):
        directory = line[5:]
        current_folder = current_folder.contents.get(directory)
    elif line == "$ ls":
        while i+1 < len(lines) and not lines[i+1].startswith("$"):
            i += 1
            if lines[i].startswith("dir"):
                current_folder.contents[lines[i].split()[1]] = Folder(current_folder)
            else:
                current_folder.contents[lines[i].split()[1]] = File(int(lines[i].split()[0]))
    i += 1

print(f"Part 1 answer: {sum(size for size in filesystem.find_sizes() if size < 100000)}")

# Part 2
space_needed = 30000000 - 70000000 + filesystem.size()
print(f"Part 2 answer: {min(size for size in filesystem.find_sizes() if size >= space_needed)}")
